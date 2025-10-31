"""Use AllenSDK to download Cell Types data and export convenient CSVs.

This script is a helper: it will try to import allensdk and, if available, initialize
the CellTypesCache and export a small metadata table into ./data/allen_celltypes_metadata.csv.

Warning: AllenSDK downloads can be large. Use --cache-dir to control where files are stored.
"""
import os
import argparse


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--cache-dir', help='Allen cache directory', default='allen_cache')
    p.add_argument('--outcsv', help='Output CSV path', default='data/allen_celltypes_metadata.csv')
    args = p.parse_args()

    try:
        import allensdk
        from allensdk.core.cell_types_cache import CellTypesCache
        from allensdk.api.queries.cell_types_api import CellTypesApi
    except Exception as e:
        print('AllenSDK not available or failed to import:', e)
        print('Install it with: pip install allensdk')
        return

    os.makedirs(args.cache_dir, exist_ok=True)
    os.makedirs(os.path.dirname(args.outcsv) or '.', exist_ok=True)

    print('Initializing CellTypesCache (this may download files)...')
    ctc = CellTypesCache(manifest_file=os.path.join(args.cache_dir, 'cell_types_manifest.json'))

    print('Fetching specimen metadata via CellTypesApi...')
    api = CellTypesApi()
    specimens = api.list_specimens()

    # specimens is a list of dicts; write to CSV
    try:
        import pandas as pd
        df = pd.DataFrame(specimens)
        df.to_csv(args.outcsv, index=False)
        print('Wrote specimen metadata to', args.outcsv)
    except Exception as e:
        print('Failed to write CSV:', e)


if __name__ == '__main__':
    main()
