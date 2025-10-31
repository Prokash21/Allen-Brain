"""Port of 02_CellTypes.ipynb; demonstrates safe AllenSDK usage to list cell types.
If AllenSDK isn't present, prints installation hint.
"""
import argparse
import os


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--outcsv', default='..\..\data\allen_celltypes_specimens.csv')
    args = p.parse_args()

    try:
        import pandas as pd
        from allensdk.core.cell_types_cache import CellTypesCache
        from allensdk.api.queries.cell_types_api import CellTypesApi
    except Exception as e:
        print('AllenSDK not installed or import failed:', e)
        print('Install with: pip install allensdk')
        return

    # initialize cache (may download files)
    ctc = CellTypesCache()
    api = CellTypesApi()
    specimens = api.list_specimens()

    df = pd.DataFrame(specimens)
    os.makedirs(os.path.dirname(args.outcsv) or '.', exist_ok=True)
    df.to_csv(args.outcsv, index=False)
    print('Wrote specimen metadata to', args.outcsv)


if __name__ == '__main__':
    main()
