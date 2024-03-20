from collections import defaultdict
import pysam
import pandas as pd

class BarcodeProcessor:
    def __init__(self, barcode_fa, umi_fa, barcode_translation, newbc, report1, report2):
        self.barcode_fa = barcode_fa
        self.umi_fa = umi_fa
        self.barcode_translation = barcode_translation
        self.newbc = newbc
        self.report1 = report1
        self.report2 = report2
        self.read_count_dict = defaultdict(int)
        self.umi_dict = defaultdict(set)
        self.combine_dict = {}

    def process_barcodes(self):
        with pysam.FastxFile(self.barcode_fa) as f1, \
            pysam.FastqFile(self.umi_fa) as f2:

            for read_1, read_2 in zip(f1, f2):
                cb = read_1.sequence
                umi = read_2.sequence
                self.read_count_dict[cb] += 1
                self.umi_dict[cb].add(umi)

        barcode_list = list(self.read_count_dict.keys())
        df_count = pd.DataFrame({'barcode': barcode_list,
                                 'read_count': [self.read_count_dict[i] for i in barcode_list],
                                 'UMI': [len(self.umi_dict[i]) for i in barcode_list]})
        df_count.sort_values(by='UMI', ascending=False, inplace=True)

        combine_list = pd.read_table(self.barcode_translation, header=None)
        combine_list.columns = ['barcode', 'cell']
        df_cell = pd.merge(df_count, combine_list, how='left', on='barcode')
        df_cell['cell'].fillna(df_cell['barcode'], inplace=True)

        df_cell.to_csv(self.report1, sep=',', index=None)

        self.combine_dict = dict(zip(df_cell['barcode'], df_cell['cell']))

        df_cellcombine = self.gene_combineSummary()
        df_cellcombine.to_csv(self.report2, sep=',', index=None)


    def gene_combineSummary(self):
        result_dict1 = defaultdict(int)
        for old_key, new_key in self.combine_dict.items():
            dict1_value = self.read_count_dict.get(old_key, 0)
            result_dict1[new_key] += dict1_value

        result_dict2 = defaultdict(list)
        for old_key, new_key in self.combine_dict.items():
            dict2_value = self.umi_dict.get(old_key, "")
            result_dict2[new_key].extend(dict2_value)

        barcode_list = list(result_dict1.keys())
        df_cellcombine = pd.DataFrame({
            'cell': barcode_list, 
            'read_count': [result_dict1[i] for i in barcode_list], 
            'UMI': [len(set(result_dict2[i])) for i in barcode_list]
            })
        df_cellcombine_sorted = df_cellcombine.sort_values(by='UMI', ascending=False)
        return df_cellcombine_sorted



    def extract_combine_with_pysam(self):
        with pysam.FastqFile(self.barcode_fa) as fastq_in, \
            open(self.newbc, 'w') as fq_out:

            for read in fastq_in:
                new_cellid = self.combine_dict[read.sequence]
                fq_out.write(f'>{read.name}\n{new_cellid}\n')