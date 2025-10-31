"""Plot a BYB recording (multi-channel) from a numpy file or demo data.
Usage: python plot_byb_recording.py --input path/to/recording.npy --outdir ../figures
"""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', help='npy file with shape (n_channels, n_samples) or (n_samples,)', default=None)
    p.add_argument('--outdir', help='output directory', default='../figures')
    p.add_argument('--channels', help='number of channels to plot (defaults 4)', type=int, default=4)
    args = p.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    if args.input and os.path.exists(args.input):
        data = np.load(args.input)
        if data.ndim == 1:
            data = np.expand_dims(data, 0)
    else:
        # demo multichannel
        fs = 1000
        dur = 5.0
        t = np.linspace(0, dur, int(fs*dur), endpoint=False)
        ch = args.channels
        data = np.array([np.sin(2*np.pi*(5 + i*5)*t) + 0.1*np.random.randn(t.size) for i in range(ch)])

    ch_to_plot = min(args.channels, data.shape[0])
    plt.figure(figsize=(10, 2*ch_to_plot))
    for i in range(ch_to_plot):
        plt.subplot(ch_to_plot, 1, i+1)
        plt.plot(data[i], color='k', linewidth=0.6)
        plt.ylabel(f'ch{i}')
        if i < ch_to_plot-1:
            plt.xticks([])
    plt.xlabel('Samples')
    outpath = os.path.join(args.outdir, 'byb_recording.png')
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    print('Saved', outpath)


if __name__ == '__main__':
    main()
