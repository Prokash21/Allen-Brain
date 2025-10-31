"""Run all scripts under scripts/ in a headless, time-limited fashion.
This runner uses subprocess with MPLBACKEND='Agg' to avoid GUI backends
and enforces a per-script timeout so a hung plotting call won't block the whole run.
"""
import subprocess
import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / 'scripts'
LOG_DIR = ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)

PY = sys.executable
TIMEOUT = 60  # seconds per script

def run_script(path: Path):
    print('RUNNING', path)
    env = os.environ.copy()
    env['MPLBACKEND'] = 'Agg'
    try:
        proc = subprocess.run([PY, str(path)], capture_output=True, text=True, timeout=TIMEOUT, env=env)
        out = proc.stdout
        err = proc.stderr
        rc = proc.returncode
    except subprocess.TimeoutExpired as e:
        out = e.stdout or ''
        err = (e.stderr or '') + f'\nTimeout after {TIMEOUT}s'
        rc = -1

    logf = LOG_DIR / (path.name + '.log')
    with open(logf, 'w', encoding='utf8') as f:
        f.write('--- STDOUT ---\n')
        f.write(out or '')
        f.write('\n--- STDERR ---\n')
        f.write(err or '')
        f.write('\n--- RETURN CODE ---\n')
        f.write(str(rc))

    print(f'Finished {path.name} (rc={rc}), log -> {logf}')
    return rc

def main():
    py_files = sorted(p for p in SCRIPTS_DIR.rglob('*.py') if p.name != Path(__file__).name)
    results = {}
    for p in py_files:
        rc = run_script(p)
        results[p.name] = rc

    print('\nRun summary:')
    for name, rc in results.items():
        print(name, '->', rc)

if __name__ == '__main__':
    main()
