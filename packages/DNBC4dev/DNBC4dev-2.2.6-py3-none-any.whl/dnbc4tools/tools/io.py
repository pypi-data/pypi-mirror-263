#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   io.py
@Time    :   2024/03/07
@Author  :   lishuangshuang
@Version :   1.0
@Contact :   lishuangshuang3@mgi-tech.com
'''

### import lib
import os
import scipy.io
from scipy.sparse import csr_matrix
import anndata
import pandas as pd

import scipy.io
import scipy.sparse
import shutil
import gzip
import polars as pl
pl.enable_string_cache()


def read_anndata(path):
    
    mat = scipy.io.mmread(path+"/"+"matrix.mtx.gz").astype("float32")
    mat = mat.transpose()
    mat = csr_matrix(mat)
    adata = anndata.AnnData(mat,dtype="float32")
    genes = pd.read_csv(path+'/'+'features.tsv.gz', header=None, sep='\t')
    var_names = genes[0].values
    var_names = anndata.utils.make_index_unique(pd.Index(var_names))
    adata.var_names = var_names
    adata.var['gene_symbols'] = genes[0].values
    adata.obs_names = pd.read_csv(path+'/'+'barcodes.tsv.gz', header=None)[0].values
    adata.var_names_make_unique()
    return adata

def read_data_atac(path): 
    file_list=os.listdir(path)
    for file in file_list:
        if file =="barcodes.tsv.gz":
            file=path+file          
            obs = pd.read_csv(file, header=None, index_col=0, sep="\t")
            obs.index.name = ""
        if file =="peaks.bed.gz":
            file=path+file                      
            var = pd.read_csv(file, header=None, index_col=None, sep="\t")
            new_index = var[0].astype(str) + ':' + var[1].astype(str) + '-' + var[2].astype(str)
            var.index = new_index
            var.drop(columns=[0, 1, 2], inplace=True)
            var.index.name = ""
        if file =="matrix.mtx.gz":   
            file=path+file  
            mtx = csr_matrix(scipy.io.mmread(file).T)
    adata=anndata.AnnData(mtx,obs=obs,var=var)
    adata.var_names_make_unique()
    return adata

def write_matrix(adata,outdir):
    adata.X = csr_matrix(adata.X.astype('int32'))
    scipy.io.mmwrite(
        "%s/matrix.mtx"%outdir, 
        adata.X.transpose()
        )
    adata.var.to_csv(
        '%s/features.tsv.gz'%outdir, 
        sep='\t', index=True, header=False,
        compression='gzip'
        )
    adata.obs.to_csv(
        '%s/barcodes.tsv.gz'%outdir, 
        sep='\t', index=True, header=False,
        compression='gzip'
        )
    with open("%s/matrix.mtx"%outdir,'rb') as mtx_in:
        with gzip.open("%s/matrix.mtx"%outdir + '.gz','wb') as mtx_gz:
            shutil.copyfileobj(mtx_in, mtx_gz)
    os.remove("%s/matrix.mtx"%outdir)


### polars read fragment
def read_bc_and_counts_from_fragments_file(fragments_bed_filename: str, cellbc=None):
    open_fn = gzip.open if fragments_bed_filename.endswith(".gz") else open
    skip_rows = 0
    nbr_columns = 0
    with open_fn(fragments_bed_filename, "rt") as fragments_bed_fh:
        for line in fragments_bed_fh:
            line = line.strip()

            if not line or line.startswith("#"):
                skip_rows += 1
            else:
                nbr_columns = len(line.split("\t"))
                break
    if nbr_columns < 5:
        raise ValueError(
            "Fragments BED file needs to have at least 5 columns. "
            f'"{fragments_bed_filename}" contains only {nbr_columns} columns.'
        )

    fragments_df = pl.read_csv(
        fragments_bed_filename,
        has_header=False,
        skip_rows=skip_rows,
        separator="\t",
        use_pyarrow=False,
        infer_schema_length=0,
        columns=["column_1", "column_2", "column_3", "column_4", "column_5"],
        new_columns=["Chromosome", "Start", "End", "CellBarcode", "FragmentCount"],

    ).with_columns(
            pl.col("Chromosome").cast(pl.Categorical),
            pl.col("Start").cast(pl.UInt32),
            pl.col("End").cast(pl.UInt32),
            pl.col("CellBarcode").cast(pl.Categorical),
            pl.col("FragmentCount").cast(pl.UInt32),
        )

    if cellbc:
        selected_cbs_df = pl.read_csv(
            cellbc,
            has_header=False,
            columns=["column_1"],
            new_columns=["CellBarcode"],
            dtypes=[pl.Categorical],
        )
        fragments_df = selected_cbs_df.join(
            fragments_df,
            on="CellBarcode",
            how="left",
        )

    return fragments_df