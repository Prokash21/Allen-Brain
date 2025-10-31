"""Port of cell_epyhs/tutorial_1_checkpoint.ipynb — small demo plot for course checkpoint."""
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    base = os.path.dirname(__file__)
    outdir = os.path.abspath(os.path.join(base, '../../figures'))
    os.makedirs(outdir, exist_ok=True)

    t = np.linspace(0, 1, 500)
    signal = np.sin(2 * np.pi * 7 * t) + 0.3 * np.random.randn(t.size)

    plt.figure(figsize=(6,3))
    plt.plot(t, signal)
    plt.title('Checkpoint signal demo')
    plt.xlabel('Time (s)')
    out = os.path.join(outdir, 'tutorial_checkpoint_signal.png')
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    print('Saved', out)


if __name__ == '__main__':
    main()
