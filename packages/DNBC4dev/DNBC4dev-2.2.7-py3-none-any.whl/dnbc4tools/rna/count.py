import os

class Count:
    def __init__(self,args):
        self.name = args.name
        self.threads = args.threads
        self.calling_method = args.calling_method
        self.expectcells = args.expectcells
        self.forcecells = args.forcecells
        self.minumi = args.minumi
        self.outdir = os.path.abspath(os.path.join(args.outdir,args.name))
    
    def run(self):
        ### import lib
        from dnbc4tools.tools.utils import str_mkdir,logging_call,judgeFilexits,change_path, get_formatted_time,rm_temp
        from dnbc4tools.rna.src.singlecell_summary import cut_umi,generateCellSummary
        from dnbc4tools.tools.cal_saturation import sub_sample_cDNA_rna
        from dnbc4tools.tools.cell_calling import cell_calling
        from dnbc4tools.tools.plot_draw import merge_graph
        from dnbc4tools.tools.combineBeads import similarity_droplet_file,barcodeTranslatefile
        from dnbc4tools.__init__ import __root_dir__

        ### run
        judgeFilexits(
            '%s/01.data/final_sorted.bam'%self.outdir,
            '%s/01.data/cDNA.sequencing.report.csv'%self.outdir,
            '%s/01.data/CB_UB_count.txt'%self.outdir,
            '%s/01.data/beads_stat.txt'%self.outdir
            )
        
        str_mkdir('%s/02.count'%self.outdir)
        str_mkdir('%s/log'%self.outdir)
        str_mkdir('%s/log/.temp'%self.outdir)
        os.environ[ 'MPLCONFIGDIR' ] = '%s/log/.temp'%self.outdir
        os.environ[ 'NUMBA_CACHE_DIR' ] = '%s/log/.temp'%self.outdir
        change_path()

        ## filter oligo
        print(f'\n{get_formatted_time()}\n'
            f'Calculating bead similarity and merging beads.')
        
        cut_umi(
            f"{self.outdir}/01.data/beads_stat.txt",100,
            '%s/02.count'%self.outdir
            )

        similiarBeads_cmd = [
            f"{__root_dir__}/software/similarity",
            f"-n {self.threads}",
            f"{self.name}",
            f"{self.outdir}/01.data/CB_UB_count.txt",
            f"{self.outdir}/02.count/beads.barcodes.umi100.txt",
            f"{__root_dir__}/config/cellbarcode/oligo_type.txt",
            f"{self.outdir}/02.count/similarity.all.csv",
            f"{self.outdir}/02.count/similarity.droplet.csv",
            f"{self.outdir}/02.count/similarity.dropletfiltered.csv"
        ]
        similiarBeads_cmd_str = " ".join(similiarBeads_cmd)  
        logging_call(similiarBeads_cmd_str,'count',self.outdir)

        ### merge beads list
        similarity_droplet_file('%s/02.count/similarity.droplet.csv'%self.outdir,
                                '%s/02.count/beads.barcodes.umi100.txt'%self.outdir,
                                '%s/02.count/combined.list.tsv'%self.outdir,
                                0.4,1)

        barcodeTranslatefile(
            f"{self.outdir}/02.count/combined.list.tsv", 
            f"{self.outdir}/01.data/beads_stat.txt", 
            f"{self.outdir}/02.count/barcodeTranslate.txt",
            f"{self.outdir}/02.count/cell.id",
            f"{self.outdir}/02.count/barcodeTranslate.hex.txt"
            )
    
        ### add DB tag for bam
        # print(f'\n{get_formatted_time()}\t'
        #     f'Generating anno decon sorted bam.')
        tagAdd_cmd = [
            f"{__root_dir__}/software/tagAdd",
            f"-n {self.threads}",
            f"-bam {self.outdir}/01.data/final_sorted.bam",
            f"-file {self.outdir}/02.count/barcodeTranslate.hex.txt",
            f"-out {self.outdir}/02.count/anno_decon_sorted.bam",
            "-tag_check CB:Z:",
            "-tag_add DB:Z:"
        ]
        tagAdd_cmd_str = " ".join(tagAdd_cmd)
        logging_call(tagAdd_cmd_str,'count',self.outdir)

        ### get bam index
        def create_index(threads,bam):
            try:
                bam_index_cmd = '%s/software/samtools index -@ %s %s'%(__root_dir__,threads,bam)
                logging_call(bam_index_cmd,'count',self.outdir)
            except Exception as e:
                print('build csi index for bam')
                bam_index_cmd = '%s/software/samtools index -c -@ %s %s'%(__root_dir__,threads,bam)
                logging_call(bam_index_cmd,'count',self.outdir)
        create_index(self.threads,'%s/02.count/anno_decon_sorted.bam'%self.outdir)

        print(f'\n{get_formatted_time()}\n'
            f'Generating the raw expression matrix.')
        str_mkdir('%s/02.count/raw_matrix'%self.outdir)
        PISA_countRaw_cmd = [
            f"{__root_dir__}/software/PISA",
            "count",
            "-one-hit",
            f"-@ {self.threads}",
            "-cb DB",
            "-anno-tag GN",
            "-umi UB",
            f"-list {self.outdir}/02.count/cell.id",
            f"-outdir {self.outdir}/02.count/raw_matrix",
            f"{self.outdir}/02.count/anno_decon_sorted.bam"
        ]
        PISA_countRaw_cmd_str = " ".join(PISA_countRaw_cmd)
        logging_call(PISA_countRaw_cmd_str,'count',self.outdir)


        ## cell calling using DropletUtils
        if self.forcecells:
            cell_bc, initial_num = cell_calling(
                f"{self.outdir}/02.count/raw_matrix/", 
                force_cell_num = self.forcecells, 
                type = "rna")

        else:
            ### using high min_umi to only get higher umi solution
            cell_bc, initial_num = cell_calling(
                f"{self.outdir}/02.count/raw_matrix/", 
                expected_cell_num = 3000,
                method = "emptydrops",
                min_umi = 1000,
                type = "rna")

        generateCellSummary(
            f"{self.outdir}/01.data/beads_stat.txt", 
            f"{self.outdir}/02.count/barcodeTranslate.txt",
            f"{self.outdir}/02.count/raw_matrix",
            cell_bc,
            f"{self.outdir}/02.count"
        )    
        
        print(f'\n{get_formatted_time()}\n'
            f'Generating the filtered expression matrix.')
        str_mkdir('%s/02.count/filter_matrix'%self.outdir)
        PISA_countFilter_cmd = [
            f"{__root_dir__}/software/PISA",
            "count",
            "-one-hit",
            f"-@ {self.threads}",
            "-cb DB",
            "-anno-tag GN",
            "-umi UB",
            f"-list {self.outdir}/02.count/beads_barcodes.txt",
            f"-outdir {self.outdir}/02.count/filter_matrix",
            f"{self.outdir}/02.count/anno_decon_sorted.bam"
        ]
        PISA_countFilter_cmd_str = " ".join(PISA_countFilter_cmd)
        logging_call(PISA_countFilter_cmd_str,'count',self.outdir)  

        merge_graph(
            f"{self.outdir}/02.count/beads_barcodes.txt", 
            f"{self.outdir}/02.count"
            )     
        
        # print(f'\n{get_formatted_time()}\t'
        #     f'Calculate saturation.')
        sub_sample_cDNA_rna(
            '%s/02.count/anno_decon_sorted.bam'%self.outdir,
            '%s/02.count/beads_barcodes.txt'%self.outdir,
            '%s/02.count'%self.outdir,
            threads = self.threads,
            quality=20
            )

        rm_temp(
            f'{self.outdir}/02.count/cell.id',
            f"{self.outdir}/02.count/cell_count_detail.xls",
            f"{self.outdir}/02.count/similarity.dropletfiltered.csv",
            f"{self.outdir}/02.count/beads_barcodes_umi100.txt",
            f"{self.outdir}/02.count/combined.list.tsv",
        )

def count(args):
    Count(args).run()

def helpInfo_count(parser):
    parser.add_argument(
        '--name',
        metavar='NAME',
        help='sample name.'
        )
    parser.add_argument(
        '--threads',
        metavar='INT',
        help='Analysis threads. [default: 4].',
        type=int,default=4
        )
    parser.add_argument(
        '--outdir',
        metavar='DIR',
        help='output dir, [default: current directory].',
        default=os.getcwd()
        )
    parser.add_argument(
        '--calling_method',
        metavar='STR',
        help='Cell calling method, Choose from barcoderanks and emptydrops, [default: emptydrops].', 
        default='emptydrops'
        )
    parser.add_argument(
        '--expectcells',
        metavar='INT',
        help='Expected number of recovered beads, used as input to cell calling algorithm, [default: 3000].', 
        default=3000
        )
    parser.add_argument(
        '--forcecells',
        help='Force pipeline to use this number of beads, bypassing cell calling algorithm.',
        metavar='INT',
        )
    parser.add_argument(
        '--minumi',
        metavar='INT',
        help='The min umi for use emptydrops, [default: 1000].', 
        default=1000
        )
    return parser
