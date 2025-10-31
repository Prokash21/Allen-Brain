"""Compare cell features: reads CSV of cell metrics and plots comparisons.
If local CSV is not found, attempts to download a small sample CSV from a public URL.
Usage: python compare_cell_features.py --csv path/to/mouse_cell_metrics.csv --outdir ../figures
"""
import argparse
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request


SAMPLE_URL = 'https://raw.githubusercontent.com/nuoxuxu/gene-ephys-tutorial/main/data/SpecimenMetadata.csv'


def download_sample(dest):
    try:
        print('Downloading sample CSV...')
        urllib.request.urlretrieve(SAMPLE_URL, dest)
        return True
    except Exception as e:
        print('Failed to download sample CSV:', e)
        return False


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--csv', help='CSV file with cell metrics', default='utilities/mouse_cell_metrics.csv')
    p.add_argument('--outdir', help='output directory', default='../figures')
    args = p.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    csvpath = args.csv
    if not os.path.exists(csvpath):
        os.makedirs(os.path.dirname(csvpath) or '.', exist_ok=True)
        if not download_sample(csvpath):
            print('No CSV available locally and sample download failed. Exiting.')
            return

    df = pd.read_csv(csvpath)

    # pick numeric columns for pairplot; limit to 6 columns to keep output readable
    num = df.select_dtypes('number')
    if num.shape[1] > 6:
        num = num.iloc[:, :6]

    if num.shape[1] < 2:
        print('Not enough numeric columns to plot.')
        return

    sns.set(style='whitegrid')
    pairplot = sns.pairplot(num.sample(n=min(500, len(num)), random_state=0))
    outpath = os.path.join(args.outdir, 'compare_cell_features_pairplot.png')
    pairplot.fig.suptitle('Pairplot of cell features', y=1.02)
    pairplot.fig.tight_layout()
    pairplot.fig.savefig(outpath, dpi=150)
    print('Saved', outpath)


if __name__ == '__main__':
    main()
