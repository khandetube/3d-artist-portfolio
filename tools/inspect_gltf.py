#!/usr/bin/env python3
"""Inspect basic structure of a .gltf file without third-party packages."""
import argparse, json
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description="Inspect basic glTF structure")
    p.add_argument("file", type=Path)
    a=p.parse_args()
    if not a.file.is_file():
        print("ERROR: file not found:", a.file); return 1
    try: data=json.loads(a.file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print("ERROR: invalid JSON:", e); return 1
    asset=data.get("asset", {})
    print("glTF inspection")
    print("version:", asset.get("version", "missing"))
    print("generator:", asset.get("generator", "not specified"))
    for key in ("scenes","nodes","meshes","materials","textures","images","animations"):
        print(key + ":", len(data.get(key, [])))
    return 0 if asset.get("version")=="2.0" else 1

if __name__=="__main__": raise SystemExit(main())