"""Lightweight port of cell_type/CellTypesNotebook_CodingLight.ipynb
Simple figure generation and CSV fallback.
"""
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    base = os.path.dirname(__file__)
    outdir = os.path.abspath(os.path.join(base, '../../figures'))
    os.makedirs(outdir, exist_ok=True)

    # In the notebook this would compute some metrics across cells. We'll simulate.
    rates = np.abs(np.random.randn(150)) * 5

    plt.figure(figsize=(6,4))
    plt.scatter(np.arange(rates.size), np.sort(rates))
    plt.ylabel('Firing-rate-like metric (a.u.)')
    plt.xlabel('Sorted cell index')
    plt.title('CellTypes - demo rate metric')
    out = os.path.join(outdir, 'celltypes_demo_rate_scatter.png')
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    print('Saved', out)


if __name__ == '__main__':
    main()
