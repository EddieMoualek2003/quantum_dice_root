from __future__ import annotations
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PKG = "quantum_dice_game"     # your package folder name
GAME_ID = "quantum-dice"
GAME_NAME = "Quantum Dice"
MANIFEST = ROOT / "paiqm_game.yaml"

def read_pyproject():
    pp = ROOT / "pyproject.toml"
    if not pp.exists():
        return GAME_NAME, "0.0.0", []
    data = tomllib.loads(pp.read_text(encoding="utf-8"))
    proj = data.get("project", {})
    name = proj.get("name") or GAME_NAME
    ver = proj.get("version") or "0.0.0"
    deps = proj.get("dependencies", [])
    return name, ver, deps

def read_requirements() -> list[str]:
    r = ROOT / "requirements.txt"
    if not r.exists():
        return []
    lines = [ln.strip() for ln in r.read_text(encoding="utf-8").splitlines()]
    return [ln for ln in lines if ln and not ln.startswith("#")]

def write_manifest():
    name, version, deps_from_pyproject = read_pyproject()
    reqs = read_requirements() or deps_from_pyproject or ["qiskit"]
    req_block = "".join(f"    - {p}\n" for p in reqs)

    manifest = f"""\
schema_version: 1
id: {GAME_ID}
name: "{name}"
version: "{version}"
description: "Learn randomness and measurement with a simple quantum dice."
author: "Eddie Moualek"
license: "MIT"

requirements:
  python: ">=3.11,<3.13"
  pip:
{req_block}runtime:
  type: "python"
  entry:
    module: "{PKG}"   # runs: python -m {PKG}
    args: []
ui:
  icon: ""
  categories: ["education","beginner"]

compatibility:
  raspi_models: ["Pi 4","Pi 5"]
  min_ram_mb: 2048

hooks:
  post_clone: []
"""
    MANIFEST.write_text(manifest, encoding="utf-8")
    print(f"Wrote {MANIFEST}")

if __name__ == "__main__":
    write_manifest()
