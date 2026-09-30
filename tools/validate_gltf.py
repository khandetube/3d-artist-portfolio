#!/usr/bin/env python3
"""Small, dependency-free checks for a GLB file.

This script intentionally performs only checks that can be made safely
without pretending to be a complete glTF validator.
"""

from __future__ import annotations

import argparse
import struct
from pathlib import Path


def validate_glb(path: Path) -> list[str]:
    errors: list[str] = []

    if not path.is_file():
        return [f"File not found: {path}"]

    if path.stat().st_size < 20:
        return ["File is too small to be a valid GLB container."]

    with path.open("rb") as f:
        header = f.read(12)
        magic, version, length = struct.unpack("<4sII", header)

        if magic != b"glTF":
            errors.append("Invalid GLB magic; expected b'glTF'.")
        if version != 2:
            errors.append(f"Unsupported GLB version: {version}.")
        if length != path.stat().st_size:
            errors.append(
                f"Header length ({length}) does not match file size "
                f"({path.stat().st_size})."
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Basic GLB container validation")
    parser.add_argument("file", type=Path, help="Path to a .glb file")
    args = parser.parse_args()

    errors = validate_glb(args.file)

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALID: GLB container header and file length checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
