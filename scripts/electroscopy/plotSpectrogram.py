"""Lightweight port of electroscopy/plotSpectrogram.ipynb
Generates a spectrogram from a .npy signal or creates a demo chirp if missing.
"""
import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', help='npy file with 1D signal', default=None)
    p.add_argument('--outdir', help='output directory', default=None)
    args = p.parse_args()

    base = os.path.dirname(__file__)
    outdir = args.outdir or os.path.abspath(os.path.join(base, '../../figures'))
    os.makedirs(outdir, exist_ok=True)

    if args.input and os.path.exists(args.input):
        sig = np.load(args.input)
        fs = 1000.0
    else:
        fs = 1000.0
        t = np.linspace(0, 5.0, int(5.0 * fs), endpoint=False)
        sig = signal.chirp(t, f0=20, f1=200, t1=5.0, method='linear') * np.hanning(t.size)

    f, t_spec, Sxx = signal.spectrogram(sig, fs=fs, nperseg=256, noverlap=200)

    plt.figure(figsize=(8,4))
    plt.pcolormesh(t_spec, f, 10*np.log10(Sxx+1e-12), shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.colorbar(label='Power (dB)')
    outpath = os.path.join(outdir, 'electroscopy_spectrogram.png')
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    print('Saved', outpath)


if __name__ == '__main__':
    main()
