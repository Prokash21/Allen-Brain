"""Port of cell_type/compare_cell_features.ipynb — pairwise feature comparison demo."""
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    base = os.path.dirname(__file__)
    outdir = os.path.abspath(os.path.join(base, '../../figures'))
    os.makedirs(outdir, exist_ok=True)

    # try to find a CSV in data/, otherwise synthesize
    csv_path = os.path.abspath(os.path.join(base, '../../data/compare_features.csv'))
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        np.random.seed(0)
        df = pd.DataFrame({
            'feature_A': np.random.randn(200) + 1,
            'feature_B': np.random.randn(200) * 0.5,
            'feature_C': np.random.rand(200) * 3
        })

    sns.set(style='whitegrid')
    g = sns.pairplot(df.sample(min(200, len(df))), kind='reg', diag_kind='kde')
    out = os.path.join(outdir, 'celltype_compare_pairplot.png')
    g.fig.suptitle('Cell-type feature pairplot', y=1.02)
    plt.tight_layout()
    g.fig.savefig(out, dpi=150)
    print('Saved', out)


if __name__ == '__main__':
    main()
