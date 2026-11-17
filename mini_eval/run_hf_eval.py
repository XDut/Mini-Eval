"""Backwards-compatible entry point for the ORIGINAL local Mini-Eval script.

The old --backend hf-api mode is intentionally removed: this edition does not
use hosted inference or require a token. See run_local.py --help.
"""
from run_local import main
if __name__ == '__main__':
    main()
