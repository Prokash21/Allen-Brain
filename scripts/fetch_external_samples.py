"""Download small sample data files referenced by the notebooks into ./data.

This script downloads a curated set of small CSV/JSON files used in several notebooks
so you can run the analysis scripts without the original notebooks.
"""
import os
import urllib.request

FILES = {
    'SpecimenMetadata.csv': 'https://raw.githubusercontent.com/nuoxuxu/gene-ephys-tutorial/main/data/SpecimenMetadata.csv',
    'lib_size.csv': 'https://raw.githubusercontent.com/nuoxuxu/gene-ephys-tutorial/main/data/lib_size.csv',
    'IC_list.json': 'https://raw.githubusercontent.com/nuoxuxu/gene-ephys-tutorial/main/data/IC_list.json',
}


def download(dest_dir='data'):
    os.makedirs(dest_dir, exist_ok=True)
    saved = []
    for name, url in FILES.items():
        dest = os.path.join(dest_dir, name)
        try:
            print(f'Downloading {name}...')
            urllib.request.urlretrieve(url, dest)
            print('Saved to', dest)
            saved.append(dest)
        except Exception as e:
            print('Failed to download', url, '->', e)
    return saved


if __name__ == '__main__':
    files = download()
    if not files:
        print('No files downloaded.')
    else:
        print('\nDownloaded files:')
        for f in files:
            print(' -', f)
