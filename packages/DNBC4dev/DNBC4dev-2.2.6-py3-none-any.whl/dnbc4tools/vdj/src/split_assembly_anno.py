import pysam
import random
import numpy as np
import pandas as pd
import subprocess
from multiprocessing import Pool
from dnbc4tools.tools.utils import logfunc, logging_call
import math
from typing import List
from dnbc4tools.tools.utils import bin_path

N_CHUNKS = 10

class SplitBarcode:
    def __init__(self, indir, pairedreads, N_chunk=N_CHUNKS):
        self.indir = indir
        self.pairedreads = pairedreads
        self.N_chunk = N_chunk
    
    def split(self):
        cell_df = pd.read_csv(f"{self.indir}/01.data/cell.sequcencing.tsv")
        celllist = cell_df['cell'].to_list()
        random.shuffle(celllist)
        split_barcodes = np.array_split(celllist, self.N_chunk)
        split_barcodes = [set(i) for i in split_barcodes]

        if self.pairedreads:
            fq1_list = [open(f'{self.indir}/02.assembly/temp/temp_{i+1}_R1.fq','w') for i in range(self.N_chunk)]
            fq2_list = [open(f'{self.indir}/02.assembly/temp/temp_{i+1}_R2.fq','w') for i in range(self.N_chunk)]
            bc_list = [open(f'{self.indir}/02.assembly/temp/temp_{i+1}_bc.fa','w') for i in range(self.N_chunk)]
            umi_list = [open(f'{self.indir}/02.assembly/temp/temp_{i+1}_umi.fa','w') for i in range(self.N_chunk)]

            with pysam.FastqFile(f'{self.indir}/01.data/tcrbcr_cut_1.fq') as fastq_in_1, \
                pysam.FastqFile(f'{self.indir}/01.data/tcrbcr_cut_2.fq') as fastq_in_2 , \
                pysam.FastqFile(f"{self.indir}/01.data/tcrbcr_newbc.fa") as newbc, \
                pysam.FastqFile(f"{self.indir}/01.data/tcrbcr_umi.fa") as umi:
                for read_1, read_2, read_3, read_4 in zip(fastq_in_1, fastq_in_2, newbc, umi):
                    cellbarcode = read_3.sequence
                    for i in range(self.N_chunk):
                        if cellbarcode in split_barcodes[i]:
                            fq1_list[i].write(str(read_1)+"\n")
                            fq2_list[i].write(str(read_2)+"\n")
                            bc_list[i].write(str(read_3)+"\n")
                            umi_list[i].write(str(read_4)+"\n")
                            break
                for i in range(self.N_chunk):
                    fq1_list[i].close()
                    fq2_list[i].close()
                    bc_list[i].close()
                    umi_list[i].close()

        else:
            fq1_list = [open(f'{self.indir}/02.assembly/temp/temp_{i+1}_R1.fq','w') for i in range(self.N_chunk)]
            bc_list = [open(f'{self.indir}/02.assembly/temp/temp_{i+1}_bc.fa','w') for i in range(self.N_chunk)]
            umi_list = [open(f'{self.indir}/02.assembly/temp/temp_{i+1}_umi.fa','w') for i in range(self.N_chunk)]
            with pysam.FastqFile(f'{self.indir}/01.data/tcrbcr_cut_1.fq') as fastq_in_1, \
                pysam.FastqFile(f"{self.indir}/01.data/tcrbcr_newbc.fa") as newbc, \
                pysam.FastqFile(f"{self.indir}/01.data/tcrbcr_umi.fa") as umi:
                for read_1, read_3, read_4 in zip(fastq_in_1, newbc, umi):
                    cellbarcode = read_3.sequence
                    for i in range(self.N_chunk):
                        if cellbarcode in split_barcodes[i]:
                            fq1_list[i].write(str(read_1)+"\n")
                            bc_list[i].write(str(read_3)+"\n")
                            umi_list[i].write(str(read_4)+"\n")
                            break
                for i in range(self.N_chunk):
                    fq1_list[i].close()
                    bc_list[i].close()
                    umi_list[i].close()

class Assemble:
    def __init__(self, root, coordinate, single_thread, pairedreads, N_chunk=N_CHUNKS):
        self.root = root
        self.coordinate = coordinate
        self.single_thread = single_thread
        self.pairedreads = pairedreads
        self.N_chunk = N_chunk
    
    def run(self, params):
        cmd: List[str] = [
            f'{self.root}/software/TRUST4/trust4 '
            f'-t {self.single_thread} '
            f'-f {self.coordinate} '
            f'-o {params["indir"]}/02.assembly/temp/{params["name"]} '
            f'--barcode {params["indir"]}/02.assembly/temp/{params["name"]}_bc.fa '
            f'--UMI {params["indir"]}/02.assembly/temp/{params["name"]}_umi.fa'
        ]
        if self.pairedreads:
            cmd += [
                f'-1 {params["indir"]}/02.assembly/temp/{params["name"]}_R1.fq '
                f'-2 {params["indir"]}/02.assembly/temp/{params["name"]}_R2.fq '
            ]
        else:
            cmd += [
                f'-u {params["indir"]}/02.assembly/temp/{params["name"]}_R1.fq '
            ]
        cmd = ' '.join(cmd)
        logging_call(cmd, 'assembly', params["indir"])

    def run_assemble(self, indir):
        params_list = []
        for i in range(self.N_chunk):
            params = {
                "name": f'temp_{i+1}',
                "indir": indir,
            }
            params_list.append(params)

        with Pool(self.N_chunk) as pool:
            pool.map(self.run, params_list)

class Annotate:
    def __init__(self, root, IMGT, single_thread, N_chunk=N_CHUNKS):
        self.root = root
        self.IMGT = IMGT
        self.single_thread = single_thread
        self.N_chunk = N_chunk
    
    def annotate(self, params):
        cmd = (
            f'{self.root}/software/TRUST4/annotator '
            f'-f {self.IMGT} '
            f'-a {params["indir"]}/02.assembly/temp/{params["name"]}_final.out '
            f'-t {self.single_thread} '
            f'-o {params["indir"]}/02.assembly/temp/{params["name"]} '
            f'--readAssignment {params["indir"]}/02.assembly/temp/{params["name"]}_assign.out '
            f'-r {params["indir"]}/02.assembly/temp/{params["name"]}_assembled_reads.fa '
            f'--barcode --UMI --airrAlignment --noImpute '
            f'> {params["indir"]}/02.assembly/temp/{params["name"]}_annot.fa'
        )
        logging_call(cmd, 'assembly', params["indir"])

    def run_annotate(self, indir):
        params_list = []

        for i in range(self.N_chunk):
            params = {
                "name": f'temp_{i+1}',
                "indir": indir,
            }
            params_list.append(params)

        with Pool(self.N_chunk) as pool:
            pool.map(self.annotate, params_list)

def merge_file(indir, N_chunk=N_CHUNKS):
    file_suffixes = [
        'annot.fa',
        'assembled_reads.fa',
        'assign.out',
        'cdr3.out',
        'final.out',
        'raw.out'
    ]

    for file_suffix in file_suffixes:
        file_path = [f'{indir}/02.assembly/temp/temp_{i+1}_{file_suffix}' for i in range(N_chunk)]
        file_path_str = ' '.join(file_path)
        cmd = f'cat {file_path_str} > {indir}/02.assembly/tcrbcr_{file_suffix}'
        subprocess.check_call(cmd, shell=True)

def analysis_step(root, indir):
    cmd_barcoderep = (
        f'{bin_path()}/perl  {root}/vdj/src/trust-barcoderep.pl '
        f'{indir}/02.assembly/tcrbcr_cdr3.out '
        f'-a {indir}/02.assembly/tcrbcr_annot.fa '
        f'--chainsInBarcode 2 '
        f'> {indir}/02.assembly/tcrbcr_barcode_report.tsv '
    )

    cmd_simplerep = (
        f'{bin_path()}/perl  {root}/vdj/src/trust-simplerep.pl '
        f'{indir}/02.assembly/tcrbcr_cdr3.out '
        f'--barcodeCnt '
        f'--filterBarcoderep {indir}/02.assembly/tcrbcr_barcode_report.tsv '
        f'> {indir}/02.assembly/tcrbcr_report.tsv '
    )

    cmd_barcode_airr = (
        f'{bin_path()}/perl {root}/vdj/src/trust-airr.pl '
        f'{indir}/02.assembly/tcrbcr_barcode_report.tsv '
        f'{indir}/02.assembly/tcrbcr_annot.fa '
        f'--format barcoderep '
        f'> {indir}/02.assembly/tcrbcr_barcode_airr.tsv '
    )

    subprocess.check_call(cmd_barcoderep, shell=True)
    subprocess.check_call(cmd_simplerep, shell=True)
    subprocess.check_call(cmd_barcode_airr, shell=True)

@logfunc
def trust4_pipe(
        indir,
        threads,
        coordinate,
        IMGT,
        root,
        split,
        pairedreads = None
        ):
    single_thread = math.ceil(threads / split)
    split_barcode = SplitBarcode(indir, pairedreads, split)
    split_barcode.split()
    assemble = Assemble(root, coordinate, single_thread, pairedreads, split)
    assemble.run_assemble(indir)
    annotate = Annotate(root, IMGT, single_thread, split)
    annotate.run_annotate(indir)
    merge_file(indir, split)
    analysis_step(root, indir)