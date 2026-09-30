# 3D Artist Portfolio

Real-time 3D asset preparation and technical art portfolio.

> **Portfolio note:** The examples in this repository are self-initiated technical demonstrations created to show the workflow and quality checks relevant to real-time 3D asset delivery. They are not presented as previous client work.

## Focus

- Blender-based 3D asset preparation
- glTF / GLB delivery for real-time and web workflows
- PBR material setup and consistency
- UV inspection and cleanup
- Geometry and shading validation
- Transform, origin, pivot and orientation checks
- Asset hierarchy and naming
- Lightweight Python automation for repeatable validation
- Web-ready asset preparation for Three.js, Babylon.js and model-viewer workflows

## Technical workflow

```text
Blender source
   ↓
Geometry / normals / shading checks
   ↓
UV and PBR material checks
   ↓
Transforms / origins / hierarchy
   ↓
glTF / GLB export
   ↓
Automated validation
   ↓
Web / real-time delivery
```

## Repository structure

```text
.
├── README.md
├── docs/
│   └── workflow.md
└── tools/
    └── validate_gltf.py
```

## Validation philosophy

The goal is not only to produce a visually correct model, but to make the delivered asset predictable in a real-time pipeline. Validation therefore focuses on structural issues that can cause problems after export: invalid files, unexpected transforms, missing metadata, inconsistent materials, and other delivery-side issues.

## Demonstration status

This repository is being built as a focused technical portfolio. Additional sample assets, screenshots, Blender source files and automation examples will be added as they are prepared and verified.

## Contact

GitHub: https://github.com/khandetube
