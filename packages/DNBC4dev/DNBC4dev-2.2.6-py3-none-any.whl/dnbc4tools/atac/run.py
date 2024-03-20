import os
import argparse
import time
from typing import List, Optional

class Runpipe:
    def __init__(self, args):
        self.name: str = args.name
        self.fastq1: str = args.fastq1 
        self.fastq2: str = args.fastq2
        self.threads: int = args.threads
        self.darkreaction: Optional[str] = args.darkreaction
        self.customize: Optional[str] = args.customize
        self.outdir: str = os.path.abspath(args.outdir)
        self.genomeDir: str = os.path.abspath(args.genomeDir)
        self.forcecells: int = args.forcecells
        self.filter_frags: int = args.frags_cutoff
        self.filter_tss: float = args.tss_cutoff
        self.filter_jaccard: float = args.jaccard_cutoff
        self.merge_frags: int = args.merge_cutoff
        self.skip_barcode_check = args.skip_barcode_check
        self.process: List[str] = args.process.split(",")
        
    def runpipe(self) -> None:
        ### import lib
        from dnbc4tools.tools.utils import str_mkdir, judgeFilexits, change_path, start_print_cmd, read_json
        from dnbc4tools.__init__ import __root_dir__

        ### run
        change_path()
        judgeFilexits(self.fastq1, self.fastq2, self.genomeDir)

        genomeDir = os.path.abspath(self.genomeDir)
        indexConfig = read_json('%s/ref.json'%genomeDir)
        refindex = indexConfig['index']
        genome = indexConfig['genome']
        chrmt: str = indexConfig['chrmt']
        genomesize: str = indexConfig['genomesize']
        tssregion: str = indexConfig['tss']
        species: str = indexConfig['species']
        blacklist: str = indexConfig['blacklist']

        ### data pipeline
        data_cmd: List[str] = [
            f"dnbc4atac data",
            f"--fastq1 {self.fastq1} ",
            f"--fastq2 {self.fastq2} ",
            f"--threads {self.threads} ",
            f"--name {self.name} ",
            f"--darkreaction {self.darkreaction} ",
            f"--outdir {self.outdir} ",
            f"--genome {genome} ",
            f"--index {refindex} ",
            f"--chrmt {chrmt}",
            f"--genomesize {genomesize} ",
            f"--bcerror 1 ",
            ]
        
        if self.customize:
            data_cmd += [
                f'--customize {self.customize}'
                ]
        if self.skip_barcode_check:
            data_cmd += [
                f'--skip-barcode-check'
            ]
        if self.merge_frags:
            data_cmd += [
                f'--minmerge {self.merge_frags}'
            ]
        if self.filter_jaccard:
            data_cmd += [
                f'--minjaccard {self.filter_jaccard}'
            ]
        data_cmd = ' '.join(data_cmd)

        ### decon pipeline
        decon_cmd: List[str] = [
            f"dnbc4atac decon",
            f"--name {self.name} ",
            f"--threads {self.threads}",
            f"--outdir {self.outdir}",
            f"--chrmt {chrmt}",
            f"--tss {tssregion}",
            f"--bl {blacklist}"
        ]
        if self.filter_frags:
            decon_cmd += [
                f'--min_frags_per_cb {self.filter_frags}'
                ]
        if self.filter_tss:
            decon_cmd += [
                f'--min_tss_per_cb {self.filter_tss}'
                ]
        if self.forcecells:
            decon_cmd += [
                f'--forcecells {self.forcecells}'
                ]
        decon_cmd = ' '.join(decon_cmd)

        analysis_cmd: List[str]  = [
            f"dnbc4atac analysis",
            f"--name {self.name}",
            f"--outdir {self.outdir}"
            ]
        analysis_cmd = ' '.join(analysis_cmd)
        
        report_cmd: List[str] = [
            f'dnbc4atac report',
            f"--name {self.name}",
            f"--outdir {self.outdir}",
            f"--species {species}"
        ]
        report_cmd = ' '.join(report_cmd)

        cmdlist: List[str] = []
        if 'data' in self.process:
            cmdlist.append(data_cmd)
        if 'decon' in self.process:
            cmdlist.append(decon_cmd)
        if 'analysis' in self.process:
            cmdlist.append(analysis_cmd)
        if 'report' in self.process:
            cmdlist.append(report_cmd)

        start_time = time.time()
        str_mkdir('%s/log'%os.path.join(self.outdir,self.name))
        for pipecmd in cmdlist:
            start_print_cmd(pipecmd,os.path.join(self.outdir,self.name))
        end_time = time.time()

        analysis_time = end_time - start_time
        analysis_time_minutes, analysis_time_seconds = divmod(analysis_time, 60)
        analysis_time_hours, analysis_time_minutes = divmod(analysis_time_minutes, 60)

        print(f'\nAnalysis Finished')
        print(f'Elapsed Time: {int(analysis_time_hours)} hours {int(analysis_time_minutes)} minutes {int(analysis_time_seconds)} seconds')
            
def run(args):
    Runpipe(args).runpipe()

def helpInfo_run(parser):
    parser.add_argument(
        '--name', 
        metavar='<SAMPLE_ID>',
        help='User-defined sample ID', 
        type=str,
        required=True
        )
    parser.add_argument(
        '--fastq1', 
        metavar='<FQ1FILES>',
        help='The input R1 fastq files.', 
        required=True
        )
    parser.add_argument(
        '--fastq2', 
        metavar='<FQ2FILES>',
        help='The input R2 fastq files.', 
        required=True
        )
    parser.add_argument(
        '--genomeDir',
        type=str, 
        metavar='<DATABASE>',
        help='Path to the directory where genome files are stored.',
        required=True
        )
    parser.add_argument(
        '--outdir', 
        metavar='<OUTDIR>',
        help='Output diretory, [default: current directory].', 
        default=os.getcwd()
        )
    parser.add_argument(
        '--threads',
        type=int, 
        metavar='<CORENUM>',
        default=4,
        help='Number of threads used for analysis, [default: 4].'
        )
    parser.add_argument(
        '--darkreaction',
        metavar='<DARKCYCLE>',
        help='Sequencing dark cycles. Automatic detection is recommended, [default: auto].', 
        default='auto'
        )
    parser.add_argument(
        '--customize',
        metavar='<STRUCTURE>',
        help='Customize readstructure.'
        )
    parser.add_argument(
        '--forcecells', 
        type=int,
        metavar='<CELLNUM>',
        help='Force pipeline to use this number of cells.'
        )
    parser.add_argument(
        '--frags_cutoff', 
        type=int, 
        metavar='<MIN_FRAGMENTS>',
        help='Filter cells with unique fragments number lower than this value, [default: 1000]'
        )
    parser.add_argument(
        '--tss_cutoff', 
        type=float,
        metavar='<MIN_TSS_RATIO>',
        help='Filter cells with tss proportion lower than this value, [default: 0].'
        )
    parser.add_argument(
        '--jaccard_cutoff', 
        type=float,
        metavar='<MIN_JACCARD>',
        help=argparse.SUPPRESS
        )
    parser.add_argument(
        '--merge_cutoff', 
        type=int,
        metavar='<MIN_MERGE>',
        help="The lowest number of fragments when merging beads, [default: 1000]."
        )
    parser.add_argument(
        '--skip-barcode-check',
        action='store_true',
        help=argparse.SUPPRESS
        )
    parser.add_argument(
        '--process', 
        metavar='<ANALYSIS_STEPS>',
        help='Custom analysis steps enable the skipping of unnecessary steps, [default: data,decon,analysis,report].',
        type=str,
        default='data,decon,analysis,report')
    return parser