"""Port of allen_25/CompareCellFeatures.ipynb focusing on downloading a small CSV and plotting.
"""
import argparse
import os
import urllib.request
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

CSV_URL = 'https://raw.githubusercontent.com/nuoxuxu/gene-ephys-tutorial/main/data/SpecimenMetadata.csv'


def ensure_csv(path='data/human_cell_metrics.csv'):
    if os.path.exists(path):
        return path
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    try:
        print('Downloading sample CSV...')
        urllib.request.urlretrieve(CSV_URL, path)
        return path
    except Exception as e:
        print('Failed to download sample CSV:', e)
        return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--csv', default='data/human_cell_metrics.csv')
    p.add_argument('--outdir', default='..\..\figures')
    args = p.parse_args()

    csvpath = args.csv if os.path.exists(args.csv) else ensure_csv(args.csv)
    if not csvpath:
        print('No CSV available. Exiting.')
        return

    df = pd.read_csv(csvpath)
    num = df.select_dtypes('number').iloc[:, :6]
    sns.pairplot(num.sample(n=min(300, len(num)), random_state=0))
    outdir = os.path.abspath(os.path.join(os.path.dirname(__file__), args.outdir))
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, 'allen25_compare_pairplot.png')
    plt.savefig(outpath, dpi=150)
    print('Saved', outpath)


if __name__ == '__main__':
    main()
