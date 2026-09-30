# Real-Time GLB / glTF Workflow

This document describes the intended technical workflow demonstrated by this portfolio.

## 1. Geometry

Before export, inspect:

- flipped or inconsistent normals
- overlapping faces where they are not intentional
- duplicate or unnecessary geometry
- non-manifold/problematic topology where relevant
- smoothing and shading consistency

## 2. Materials

For PBR assets, verify that material inputs are mapped consistently and that texture references are valid. Typical inputs include base color, metallic, roughness and normal information.

## 3. UVs

Check that required meshes have usable UV coordinates and that UV layouts do not contain accidental overlaps or missing islands when the asset requires unique texture placement.

## 4. Transforms and anchors

Check object transforms, origins/pivots, scale and orientation before delivery. When an asset uses attachment points, naming and placement should be explicit and consistent.

## 5. Export

The target delivery format for the web-focused examples is glTF/GLB. The exported file should preserve the intended scene hierarchy, materials and transforms while remaining practical for real-time use.

## 6. Validation

Run the repository validation script after export. Automated checks are intended to catch structural delivery issues before the asset reaches a web or real-time application.

## Important

This is a self-initiated portfolio workflow. It should not be interpreted as a claim of previous paid client work.
