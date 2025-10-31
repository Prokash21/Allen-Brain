"""Lightweight port of key plotting steps from allen_25/PatchSeq.ipynb

This script is defensive: it uses small sample downloads if the original large count
matrices are not present. It produces a small figure (library size histogram) so you
can validate the pipeline without downloading huge files.
"""
import argparse
import os
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt


SAMPLE_LIB_SIZE_URL = 'https://raw.githubusercontent.com/nuoxuxu/gene-ephys-tutorial/main/data/lib_size.csv'


def ensure_lib_size(path='data/lib_size.csv'):
    if os.path.exists(path):
        return path
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    try:
        print('Downloading small sample lib_size.csv...')
        urllib.request.urlretrieve(SAMPLE_LIB_SIZE_URL, path)
        return path
    except Exception as e:
        print('Failed to download sample lib_size.csv:', e)
        return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--outdir', default='../../figures', help='output directory')
    p.add_argument('--libsize', default='data/lib_size.csv', help='path to lib_size.csv')
    args = p.parse_args()

    outdir = os.path.abspath(os.path.join(os.path.dirname(__file__), args.outdir))
    os.makedirs(outdir, exist_ok=True)

    lib_path = args.libsize if os.path.exists(args.libsize) else ensure_lib_size(args.libsize)
    if not lib_path:
        print('No library size CSV available. Exiting.')
        return

    df = pd.read_csv(lib_path, sep='\t', index_col=0)
    # expect a single column of sizes; choose the first numeric column
    numcols = df.select_dtypes('number').columns.tolist()
    if not numcols:
        # try first column
        col = df.columns[0]
    else:
        col = numcols[0]

    plt.figure(figsize=(6,4))
    df[col].hist(bins=40)
    plt.xlabel('Library size')
    plt.ylabel('Count')
    plt.title('Library size distribution (sample)')
    outpath = os.path.join(outdir, 'patchseq_lib_size_hist.png')
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    print('Saved', outpath)


if __name__ == '__main__':
    main()
