"""Port of cell_epyhs/Tutorial.ipynb — tutorial demo script."""
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    base = os.path.dirname(__file__)
    outdir = os.path.abspath(os.path.join(base, '../../figures'))
    os.makedirs(outdir, exist_ok=True)

    # simple demo: plot three sine waves
    t = np.linspace(0, 1, 400)
    plt.figure(figsize=(6,4))
    for i, f in enumerate([3, 6, 12]):
        plt.plot(t, np.sin(2*np.pi*f*t) + 0.1*i, label=f'{f} Hz')
    plt.legend()
    plt.title('Tutorial demo waves')
    out = os.path.join(outdir, 'tutorial_three_waves.png')
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    print('Saved', out)


if __name__ == '__main__':
    main()
