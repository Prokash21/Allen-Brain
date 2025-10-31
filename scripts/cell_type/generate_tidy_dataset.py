"""Port of cell_type/generate_tidy_dataset.ipynb — demonstrates assembling a tidy table (synthetic)."""
import os
import numpy as np
import pandas as pd


def main():
    base = os.path.dirname(__file__)
    outdir = os.path.abspath(os.path.join(base, '../../figures'))
    datadir = os.path.abspath(os.path.join(base, '../../data'))
    os.makedirs(outdir, exist_ok=True)
    os.makedirs(datadir, exist_ok=True)

    # synthesize a tidy table similar to what the notebook builds
    np.random.seed(1)
    df = pd.DataFrame({
        'cell_id': np.arange(1,201),
        'area': np.random.choice(['VISp','VISl','AUDp'], size=200),
        'spk_rate': np.abs(np.random.randn(200))*5,
        'gene_count': np.random.poisson(50, size=200)
    })

    outcsv = os.path.join(datadir, 'tidy_cell_table.csv')
    df.to_csv(outcsv, index=False)
    print('Wrote', outcsv)

    # small summary
    summary = df.groupby('area')['spk_rate'].median()
    print('Median spk_rate per area:\n', summary)


if __name__ == '__main__':
    main()
