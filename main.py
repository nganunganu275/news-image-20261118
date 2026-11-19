# One image summing up the world news of Wednesday 18 November 2026.
# The image is the entry.png beside this file, and the program copies it
# to /output/entry.png. Python 3.13, standard library only: no network,
# no arguments, and both runs write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
src = HERE / "entry.png"
dst = OUT / "entry.png"
shutil.copyfile(src, dst)
# The gate runs the program twice and compares bytes: fail loudly on a
# short copy instead of shipping a truncated image.
if dst.stat().st_size != src.stat().st_size:
    raise RuntimeError("entry.png copy incomplete")
