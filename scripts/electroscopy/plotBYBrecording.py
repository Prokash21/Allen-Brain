"""Port of electroscopy/plotBYBrecording.ipynb — plot multichannel recording or demo data."""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    import pathlib
    p = argparse.ArgumentParser()
    p.add_argument('--npy', help='input .npy multichannel file (channels x samples)', default=None)
    p.add_argument('--outdir', help='output directory', default=None)
    p.add_argument('--channels', type=int, default=4)
    args = p.parse_args()

    base = pathlib.Path(__file__).parent
    outdir = args.outdir or (base.parent.parent / 'figures')
    outdir = pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    if args.npy and pathlib.Path(args.npy).is_file():
        data = np.load(args.npy)
        if data.ndim == 1:
            # assume interleaved - reshape
            samples = data.size // args.channels
            data = data[:samples*args.channels].reshape(args.channels, samples)
    else:
        # synthetic
        samples = 2000
        t = np.linspace(0,1,samples)
        data = np.array([np.sin(2*np.pi*(5+i)*t) + 0.05*np.random.randn(samples) for i in range(args.channels)])

    fig, axs = plt.subplots(data.shape[0], 1, figsize=(8, 2*data.shape[0]), sharex=True)
    if data.shape[0] == 1:
        axs = [axs]
    for i, ax in enumerate(axs):
        ax.plot(data[i], color=f'C{i}')
        ax.set_ylabel(f'Ch {i}')
    axs[-1].set_xlabel('Samples')
    plt.tight_layout()
    out = outdir / 'electroscopy_byb_recording.png'
    plt.savefig(out, dpi=150)
    print('Saved', out)


if __name__ == '__main__':
    main()
