#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   cut_fastq_cbub.py
@Time    :   2024/02/27
@Author  :   lishuangshuang
@Version :   1.0
@Contact :   lishuangshuang3@mgi-tech.com
'''

import pysam

G_BASES = "G"

class extract_crur_fastq:

    @staticmethod
    def extract_cr_ur_fqpaired_pysam(indir, outdir, n_reads):
        with pysam.FastqFile(f'{indir}/clean_R1.fastq') as fastq_in_1, \
            pysam.FastqFile(f'{indir}/clean_R2.fastq') as fastq_in_2, \
            open(f'{outdir}/cb_cut.fastq', 'w') as cr_out, \
            open(f'{outdir}/ub_cut.fastq', 'w') as ur_out, \
            open(f'{outdir}/fq1_cut.fastq', 'w') as fq1_out, \
            open(f'{outdir}/fq2_cut.fastq', 'w') as fq2_out:
            for read_1, read_2 in zip(fastq_in_1, fastq_in_2):
                description = read_1.name
                parts = description.split('|||')
                read_id = parts[0]

                cr_data = None
                ur_data = None

                for part in parts:
                    if part.startswith('CB:Z:'):
                        cr_data = part[5:]
                    elif part.startswith('UR:Z:'):
                        ur_data = part[5:]

                if cr_data:
                    cr_out.write(f'@{read_id}\n{cr_data}\n+\n{G_BASES * len(cr_data)}\n')
                if ur_data:
                    ur_out.write(f'@{read_id}\n{ur_data}\n+\n{G_BASES * len(ur_data)}\n')
                fq1_out.write(f'@{read_id}\n{read_1.sequence}\n+\n{read_1.quality}\n')
                fq2_out.write(f'@{read_id}\n{read_2.sequence}\n+\n{read_2.quality}\n')

                if n_reads != None:
                    n_reads -= 1
                    if n_reads == 0:
                        break
    
    @staticmethod                    
    def extract_cr_ur_fqsingle_pysam(indir, outdir, n_reads):
        with pysam.FastqFile(f'{indir}/clean.fastq') as fastq_in, \
            open(f'{outdir}/cb_cut.fastq', 'w') as cr_out, \
            open(f'{outdir}/ub_cut.fastq', 'w') as ur_out, \
            open(f'{outdir}/fq_cut.fastq', 'w') as fq_out:
            for read in fastq_in:
                description = read.name
                parts = description.split('|||')
                read_id = parts[0]

                cr_data = None
                ur_data = None

                for part in parts:
                    if part.startswith('CB:Z:'):
                        cr_data = part[5:]
                    elif part.startswith('UR:Z:'):
                        ur_data = part[5:]

                if cr_data:
                    cr_out.write(f'@{read_id}\n{cr_data}\n+\n{G_BASES * len(cr_data)}\n')
                if ur_data:
                    ur_out.write(f'@{read_id}\n{ur_data}\n+\n{G_BASES * len(ur_data)}\n')
                fq_out.write(f'@{read_id}\n{read.sequence}\n+\n{read.quality}\n')

                if n_reads != None:
                    n_reads -= 1
                    if n_reads == 0:
                        break

