"""Lightweight port of electroscopy/Statistics.ipynb — computes simple summary stats and plots."""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--npy', help='input .npy file for signal', default=None)
    p.add_argument('--outdir', help='output directory', default=None)
    args = p.parse_args()

    base = os.path.dirname(__file__)
    outdir = args.outdir or os.path.abspath(os.path.join(base, '../../figures'))
    os.makedirs(outdir, exist_ok=True)

    if args.npy and os.path.isfile(args.npy):
        data = np.load(args.npy)
    else:
        np.random.seed(0)
        data = np.random.randn(1000)

    stats = dict(mean=float(np.mean(data)), std=float(np.std(data)), median=float(np.median(data)))
    print('Summary stats:', stats)

    plt.figure(figsize=(6,4))
    plt.hist(data, bins=30, alpha=0.7)
    plt.title('Data distribution')
    plt.xlabel('Value')
    plt.ylabel('Count')
    out = os.path.join(outdir, 'electroscopy_statistics_hist.png')
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    print('Saved', out)


if __name__ == '__main__':
    main()
