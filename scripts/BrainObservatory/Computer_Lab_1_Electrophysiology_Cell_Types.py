"""Port of BrainObservatory/Computer_Lab_1_Electrophysiology_Cell_Types.ipynb
Creates a simple demo figure and attempts to call AllenSDK minimally if present.
"""
import os
import numpy as np
import matplotlib.pyplot as plt


def try_allensdk_small(out_csv):
    try:
        import allensdk
        # Keep it tiny: write a small CSV marker if import succeeded
        with open(out_csv, 'w') as f:
            f.write('specimen_id,marker\n1,ok\n')
        return True
    except Exception:
        return False


def main():
    base = os.path.dirname(__file__)
    outdir = os.path.abspath(os.path.join(base, '../../figures'))
    datadir = os.path.abspath(os.path.join(base, '../../data'))
    os.makedirs(outdir, exist_ok=True)
    os.makedirs(datadir, exist_ok=True)

    csv_marker = os.path.join(datadir, 'brainobs_marker.csv')
    ok = try_allensdk_small(csv_marker)

    t = np.linspace(0, 1, 500)
    sig = np.sin(2*np.pi*5*t) + 0.2*np.random.randn(t.size)
    plt.figure(figsize=(6,3))
    plt.plot(t, sig)
    plt.title('BrainObservatory demo trace')
    out = os.path.join(outdir, 'brainobservatory_demo_trace.png')
    plt.tight_layout()
    plt.savefig(out, dpi=150)
    print('Saved', out, 'AllenSDK marker created:', ok)


if __name__ == '__main__':
    main()
