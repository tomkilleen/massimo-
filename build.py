#!/usr/bin/env python3
"""Copy the shared core into every skill so each skill is self-contained. Run after editing core/."""
import shutil, pathlib
root = pathlib.Path(__file__).parent
core = root / "core"
for skill in sorted((root / "skills").iterdir()):
    if not skill.is_dir(): continue
    ref = skill / "references"; scr = skill / "scripts"
    ref.mkdir(exist_ok=True); scr.mkdir(exist_ok=True)
    for f in ("DESIGN.md", "canon.md", "reference-works.md", "tokens.css"):
        shutil.copy(core / f, ref / f)
    shutil.copy(core / "massimo_check.py", scr / "massimo_check.py")
    print("built", skill.name)
shutil.copy(core / "DESIGN.md", root / "DESIGN.md")
