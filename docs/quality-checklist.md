# Real-Time 3D Asset Quality Checklist

## Geometry
Check normals, unintended overlapping geometry, smoothing, hard/soft edges and unnecessary geometry.

## UVs
Confirm required UV attributes exist, inspect accidental overlaps and verify texture scale/consistency.

## PBR materials
Verify Base Color, Metallic, Roughness, Normal and Emissive inputs when required. Confirm texture references remain valid after export.

## Transforms and anchors
Review location, rotation, scale, origin/pivot, orientation, attachment-point names and parent/child hierarchy.

## Runtime delivery
Test the final GLB/glTF in the intended runtime or a representative viewer. Blender-only inspection is not sufficient evidence of runtime correctness.

## Automation
Automated checks are a repeatable first validation layer; they do not replace visual and runtime inspection.