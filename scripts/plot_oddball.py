"""Plot example traces from .mat files in a directory (oddball experiment style).
Usage: python plot_oddball.py --matdir path/to/matfiles --outdir ../figures
"""
import argparse
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from scipy import io as sio


def load_first_mat(matdir):
    mats = glob.glob(os.path.join(matdir, '*.mat')) if matdir and os.path.isdir(matdir) else []
    if not mats:
        return None
    try:
        data = sio.loadmat(mats[0])
        return data
    except Exception:
        return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--matdir', help='directory with .mat files', default=None)
    p.add_argument('--outdir', help='output directory', default='../figures')
    args = p.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    matdata = load_first_mat(args.matdir)
    if matdata is not None:
        # heuristics: find the first 1D numeric array in matdict
        arrays = [v for k,v in matdata.items() if isinstance(v, (np.ndarray,))]
        arr = None
        for a in arrays:
            if a.ndim == 1 or (a.ndim == 2 and (1 in a.shape)):
                arr = a.squeeze()
                break
        if arr is None:
            print('No 1D arrays in first .mat file; falling back to demo signal')

    else:
        arr = None

    if arr is None:
        # generate demo oddball-like epochs
        fs = 1000
        t = np.linspace(0,1,fs,endpoint=False)
        n_trials = 8
        arr = np.sin(2*np.pi*10*t)
        trials = np.array([arr * (1 + 0.2*np.random.randn()) + 0.05*np.random.randn(fs) for _ in range(n_trials)])
    else:
        # if arr is long, chop into trials
        if arr.size > 10000:
            trials = arr.reshape(-1, int(arr.size//10))[:8]
        else:
            trials = np.tile(arr, (8,1))

    plt.figure(figsize=(8,4))
    for i in range(min(8, trials.shape[0])):
        plt.plot(trials[i] + i*0.5, color='C0')
    plt.title('Oddball-like example traces (stacked)')
    plt.xlabel('Time (samples)')
    outpath = os.path.join(args.outdir, 'oddball_traces.png')
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    print('Saved', outpath)


if __name__ == '__main__':
    main()
