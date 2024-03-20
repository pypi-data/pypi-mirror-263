#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   filter_barcode.py
@Time    :   2024/02/28
@Author  :   lishuangshuang
@Version :   1.0
@Contact :   lishuangshuang3@mgi-tech.com
'''

import argparse
import pysam
import os
import pandas as pd
import numpy as np

### filter diffuse frac
class BarcodeProcess:
    def __init__(self, barcode_report, annotation, type, outdir, high_abund=50.0, diffuse_frac=0.02):
        self.barcode_report = barcode_report
        self.annotation = annotation
        self.type = type
        self.outdir = outdir
        self.high_abund = float(high_abund)
        self.diffuse_frac = float(diffuse_frac)
        self.barcode_info = {}
        self.high_abund_cdr3_info = {}
        self.assembly = {}
        self.annoDict = {}

    def load_barcode_info(self):
        with open(self.barcode_report) as fp:
            for line in fp:
                if line.startswith('#'):
                    continue

                cols = line.rstrip().split()
                chain1_cols = cols[2].split(',')
                chain2_cols = cols[3].split(',')

                if len(chain1_cols) > 1 and float(chain1_cols[6]) >= self.high_abund:
                    self._update_high_abund_cdr3_info(chain1_cols, cols[0], 0)

                if len(chain2_cols) > 1 and float(chain2_cols[6]) >= self.high_abund:
                    self._update_high_abund_cdr3_info(chain2_cols, cols[0], 1)

                if len(chain1_cols) > 1:
                    self.assembly[chain1_cols[7]] = chain1_cols[4]
                    chain1_cols[6] = float(chain1_cols[6])

                if len(chain2_cols) > 1:
                    self.assembly[chain2_cols[7]] = chain2_cols[4]
                    chain2_cols[6] = float(chain2_cols[6])

                self.barcode_info[cols[0]] = {"chain1": chain1_cols[:], "chain2": chain2_cols[:]}

    def _update_high_abund_cdr3_info(self, chain_cols, barcode, chain_index):
        if chain_cols[4] not in self.high_abund_cdr3_info:
            self.high_abund_cdr3_info[chain_cols[4]] = {}
        self.high_abund_cdr3_info[chain_cols[4]][barcode] = [chain_index, float(chain_cols[6])]

    def load_annotation(self):
        with pysam.FastxFile(self.annotation) as annofa:
            for read in annofa:
                contig_name = read.name
                contig_length = len(read.sequence)
                contig_sequencing = read.sequence
                self.annoDict.setdefault(contig_name,{})['length'] = contig_length
                self.annoDict.setdefault(contig_name,{})['sequencing'] = contig_sequencing

    def _test_against_high_abund_cdr3(self, chain_cols, test_against, chain_index):
        cdr3 = chain_cols[4]
        for barcode in self.high_abund_cdr3_info[cdr3].keys():
            if self.high_abund_cdr3_info[cdr3][barcode][0] == chain_index and \
                    self.high_abund_cdr3_info[cdr3][barcode][1] * self.diffuse_frac > float(chain_cols[6]):
                test_against[barcode] = 1

    def _write_header(self):
        content = 'barcode,is_cell,contig_id,high_confidence,length,chain,v_gene,d_gene,j_gene,c_gene,full_length,productive,cdr3,cdr3_nt,reads,umis,clonotype_id\n'
        return content
    
    def _select_type(self):
        if self.type.lower() == 'tcr':
            return "abT"
        elif self.type.lower() == 'bcr':
            return "B"
        else:
            raise ValueError("Invalid type . Use TCR or BCR")
    
    def filter_barcodes(self):
        allContigSummary = os.path.join(self.outdir, "all_contig_annotations.csv")
        with open(allContigSummary, 'w') as file, open(self.barcode_report) as fp:
            file.write(self._write_header())
            for line in fp:
                if line.startswith('#'):
                    continue

                cols = line.rstrip().split()
                chain1_cols = cols[2].split(',')
                chain2_cols = cols[3].split(',')

                test_against = {}
                if (len(chain1_cols) > 1 and float(chain1_cols[6]) < self.high_abund and chain1_cols[4] in self.high_abund_cdr3_info):
                    self._test_against_high_abund_cdr3(chain1_cols, test_against, 0)
                if (len(chain2_cols) > 1 and float(chain2_cols[6]) < self.high_abund and chain2_cols[4] in self.high_abund_cdr3_info):
                    self._test_against_high_abund_cdr3(chain2_cols, test_against, 1)

                flag_filter = 0
                for bc in test_against:
                    test_chain1 = self.barcode_info[bc]["chain1"]
                    test_chain2 = self.barcode_info[bc]["chain2"]

                    for i, (c1, c2) in enumerate(zip([chain1_cols, chain2_cols], [test_chain1, test_chain2]), 1):
                        if len(c1) > 1 and len(c2) > 1:
                            if c2[6] * self.diffuse_frac > float(c1[6]) and self.assembly[c1[7]] in self.assembly[c2[7]]:
                                flag_filter |= i
                        elif len(c2) > 1:
                            flag_filter |= i

                high_confidence = 'true' if flag_filter != 3 else 'false'
                if cols[1] == self._select_type():
                    for i in range(2, 4):
                        if cols[i] == "*":
                            continue
                        if cols[i].split(',')[7] in self.annoDict:
                            length = self.annoDict[cols[i].split(',')[7]]['length']
                        generate_10x = TrustReportConverter(cols[i])
                        generate_col = generate_10x.convert_10x()
                        generate_col[0] = cols[0]
                        generate_col[3] = high_confidence
                        generate_col[4] = str(length)

                        file.write(','.join(generate_col)+'\n')

### change barcode report to 10x 
class TrustReportConverter:
    def __init__(self, cols):
        self.cols = cols
        self.chain_name = ["IGH", "IGK", "IGL", "TRA", "TRB", "TRG", "TRD", "None"]

    def get_detail_chain_type(self, *genes):
        for g in genes:
            if g.startswith('IGH'):
                return 0
            elif g.startswith('IGK'):
                return 1
            elif g.startswith('IGL'):
                return 2
            elif g.startswith('TRA'):
                return 3
            elif g.startswith('TRB'):
                return 4
            elif g.startswith('TRG'):
                return 5
            elif g.startswith('TRD'):
                return 6
        return 7

    ## Be V-J spanning with a start codon in the leader region.
    ## Have a detectable CDR3 region in frame with the start codon.
    ## Be free of stop codons in the V-J spanning region. 
    def is_productive(self, aa , nt):
        if (not self._has_stop_codon(nt) or not self._start_C(aa) or not self._len_CDR3(aa) or not self._has_CDR3(aa)):
            return 0
        else:
            return 1

    def _has_stop_codon(self,CDR3nt):
        stop_codons = ["TAA", "TAG", "TGA"]
        for i in range(0, len(CDR3nt), 3):
            codon = CDR3nt[i:i+3]
            if codon in stop_codons:
                return False
        return True

    def _start_C(self,CDR3aa):
        return CDR3aa.startswith('C')

    def _len_CDR3(self,CDR3aa):
        return len(CDR3aa) >= 5

    def _has_CDR3(self,CDR3aa):
        return '_' not in CDR3aa and '?' not in CDR3aa

    def convert_10x(self):
        chain_cols = self.cols.split(',')

        chain_type = self.chain_name[self.get_detail_chain_type(chain_cols[0], chain_cols[2], chain_cols[3])]
        if chain_cols[0]!="" and chain_cols[2]!="" and chain_cols[3]!="":
            if chain_type in ["IGH","TRB"] and chain_cols[1]!="":
                chain_full_length = "true"
            elif chain_type not in ["IGH","TRB"]:
                chain_full_length = "true"
            else:
                chain_full_length = "false"
        else:
            chain_full_length = "false"

        output_cols = [
            self.cols[0], "", chain_cols[7], "true", "None",
            chain_type,
            "" if chain_cols[0] == "*" else chain_cols[0],
            "" if chain_cols[1] == "*" else chain_cols[1],
            "" if chain_cols[2] == "*" else chain_cols[2],
            "" if chain_cols[3] == "*" else chain_cols[3],
            #"true" if chain_cols[9] == "1" else "false",
            "true" if chain_full_length =="true" else "false",
            #"true" if self.is_productive(chain_cols[5],chain_cols[4]) and chain_cols[9] == "1" and int(float(chain_cols[6])) >= 3 else "false",
            "true" if self.is_productive(chain_cols[5],chain_cols[4]) and chain_full_length =="true" else "false",
            chain_cols[5], chain_cols[4], chain_cols[6], chain_cols[6], ""
        ]
        return output_cols


### cell calling
class cellCalling:
    def __init__(self,df,expectcells,RNAcell,outdir,annot):
        self.df = df
        self.expectcells = expectcells
        self.threshold = 0
        self.RNAcell = RNAcell
        self.outdir = outdir
        self.annot = annot

    def umi_threshold(self,queen):
        if self.expectcells > len(queen):
            self.expectcells = len(queen)
        sorted_counts = sorted(queen, reverse=True)
        count_cell_percentile = np.percentile(sorted_counts[:self.expectcells], 85)
        self.threshold = int(count_cell_percentile / 3)
        

    def filter_confidence(self):
        self.df = self.df[self.df['high_confidence'] != False]

    def filter_productive(self):
        self.df = self.df.groupby('barcode').filter(lambda group: not all(group['productive'] == False))

    def filter_umi(self):
        umi_sum_df = self.df.groupby('barcode')['umis'].sum().reset_index()
        self.umi_threshold(umi_sum_df['umis'])
        print(self.threshold)
        filtered_barcodes = umi_sum_df.loc[umi_sum_df['umis'] >= self.threshold, 'barcode']
        self.df = self.df[self.df['barcode'].isin(filtered_barcodes)]

    def cell_filter(self):
        column_list = set(self.df['contig_id'].tolist())
        generate_contig(column_list,self.annot,os.path.join(self.outdir,"all_contig.fasta"))
        self.filter_umi()
        self.filter_confidence()
        self.filter_productive()
        
        if self.RNAcell:
            rna_barcodes = pd.read_csv(self.RNAcell, header=None, names=['barcode'])
            self.df = self.df[self.df['barcode'].isin(rna_barcodes['barcode'])]
        
        column_list = set(self.df['contig_id'].tolist())
        generate_contig(column_list,self.annot,os.path.join(self.outdir,"filtered_contig.fasta"))
        df_clonocyte,df_barcode_clonotype = generate_clonotypes(self.df)
        df_clonocyte.to_csv(os.path.join(self.outdir,"clonotypes.csv"),index=False)
        df_merged = pd.merge(df_barcode_clonotype,self.df, on='barcode', how='left')
        df_merged['clonotype_id'] = df_merged.apply(lambda row: row['clonotype_id_x'] if (row['productive']) else row['clonotype_id_y'], axis=1)
        df_merged.drop(["clonotype_id_x","clonotype_id_y"], axis=1, inplace = True)
        df_merged["is_cell"] = "true"
        df_merged.replace({True: 'true', False: 'false'}, inplace=True)
        df_merged.to_csv(os.path.join(self.outdir,"filtered_contig_annotations.csv"),index=False)

### generate clonotypes
def generate_clonotypes(df_new):
    df = df_new.copy()

    df.loc[(df['productive']), 'cdr3s_aa'] = df.apply(lambda row: f"{row['chain']}:{row['cdr3']}", axis=1)
    df.loc[(df['productive']), 'cdr3s_nt'] = df.apply(lambda row: f"{row['chain']}:{row['cdr3_nt']}", axis=1)
    df.loc[df['productive'] == False, 'cdr3s_aa'] = ""
    df.loc[df['productive'] == False, 'cdr3s_nt'] = ""
    
    def join_skipna(series):
        return ';'.join(filter(lambda x: pd.notna(x) and x != '', series))
    df_result = df.groupby('barcode').agg({
        'cdr3s_aa': join_skipna,
        'cdr3s_nt': join_skipna
    }).reset_index()

    df_result['cdr3s_aa'] = df_result['cdr3s_aa'].astype(str)
    df_result['combined'] = df_result['cdr3s_aa'] + ';' + df_result['cdr3s_nt']
    counts = df_result['combined'].value_counts()
    df_result['frequency'] = df_result['combined'].map(counts)
    
    df_drop = df_result.drop('barcode', axis=1)
    df_drop = df_drop.drop_duplicates()
    df_drop['proportion'] = df_drop['frequency'] / df_drop['frequency'].sum()
    df_drop = df_drop.sort_values(by='frequency', ascending=False)
    df_drop['clonotype_id'] = [f'clonotype{i}' for i in range(1, len(df_drop) + 1)]

    df_clonocyte = df_drop.loc[:,["clonotype_id","frequency","proportion","cdr3s_aa","cdr3s_nt"]]
    df_barcode_clonotype = pd.merge(df_drop,df_result,on="combined").loc[:,["barcode","clonotype_id"]]

    return df_clonocyte,df_barcode_clonotype

def generate_contig(contig_id,annot,outfile):
    with open(outfile, 'w') as out, pysam.FastxFile(annot) as file:
        for read in file:
            if read.name in contig_id:
                out.write('>' + read.name + '\n' + read.sequence + '\n')

def main():
    parser = argparse.ArgumentParser(description="Filter TRUST4 barcode report file for noise like diffused mRNAs. Output to stdout")
    parser.add_argument('--barcode', help="barcode_report file", required=True, dest="barcode_report")
    parser.add_argument('--annot', help="annotation file", dest="annot")
    parser.add_argument('--type', help="type of tcr or bcr",
                        dest="type")
    parser.add_argument('--highAbund', help="The minimum abundance to be regarded as potential source of diffusion",
                        default=50.0, dest="high_abund")
    parser.add_argument('--diffuseFrac', help="The maximum fraction of the diffusion source abundance to be regarded as noise",
                        default=0.02, dest="diffuse_frac")
    parser.add_argument('--outdir', help="Out put dir",dest="out_dir")
    parser.add_argument('--RNAcell', help="input 5' rna result barcodes.tsv.gz",dest="RNAcell", default=None)
    

    args = parser.parse_args()

    processor = BarcodeProcess(args.barcode_report, args.annot, args.type, args.out_dir, args.high_abund, args.diffuse_frac)
    processor.load_barcode_info()
    processor.load_annotation()
    processor.filter_barcodes()

    df = pd.read_csv(os.path.join(args.out_dir, "all_contig_annotations.csv"))

    filterprocess = cellCalling(df,3000,args.RNAcell,args.out_dir,args.annot)
    filterprocess.cell_filter()


if __name__ == "__main__":
    main()