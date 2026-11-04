# Database layout and resource bindings

This describes the shipped Bush War snapshot. It is an inspected example, not a guarantee for another engine version. Use the matching current vanilla database to supply complete required fields; do not create empty tables and call the result a working mod.

## Database folder

The user-data payload is `data/database/Bush War/`. The shipped folder contains these ten XML files plus its graphics tree:

| File | Role |
|---|---|
| eras.xml | Database display identifier, default date/factions and era settings |
| factions.xml | National definitions, dated settings, purchase selectors |
| units.xml | Ground unit records and resource/weapon references |
| formations.xml | HQs, sections, platoons and nested companies |
| weapons.xml | Weapon behaviour and ammunition references |
| ammunition.xml | Ammunition definitions |
| aircraft.xml | Aircraft variants, loads and model references |
| flights.xml | Selectable aircraft groupings |
| resources_custom.xml | Additional non-3D resource bindings |
| resources_custom_3d.xml | Models and texture resource bindings |

`eras.xml` names this database using `<string name="databaseID" value="Bush War 1965-1994" />`. Its default date is `1979,12`. Those are this mod's settings, not universal defaults. Preserve the native folder/table structure in a new mod, choose a distinct folder and databaseID, then confirm it actually appears in AB2's database selector. Folder presence alone is not engine acceptance.

## Model and texture forms

These are real native-shaped entries from the shipped database:

```xml
<string name="us_crew_bino_m" value="3d\vehicle\us\crew_bino.dae" />
<texture name="us_crew_bino_ds" file="3d\vehicle\us\crew_ds.png" />
```

Model entries use `string` with `value`; images use `texture` with `file`. The model resource convention uses `_m`. The verifier accepts ground `vehicle3D*` references that resolve directly or with `_m`, and checks aircraft `aircraft3DModel` with the `_m` suffix. This is a verified project convention, not permission to rename arbitrary nodes. Copy the complete matching peer's seasonal diffuse/normal/specular bindings and inspect COLLADA texture symbols rather than guessing from one example.

Resource paths resolve against database graphics, packaged graphics and stock graphics as checked by the native audit. Aircraft additionally have selected game-folder overlay destinations in the manifest. Do not flatten these paths.

## Art import and export

The archived project used an x86 Assimp probe for native-loader comparisons; that helper is not available here. No maintained tool in this candidate claims to perform that check. A generic Blender/Assimp import is only an offline check. For a new asset, record the exporter and version, triangulate the final assembly, preserve demonstrated markers/UVs/material symbols/hierarchy, inspect reimport and compare with the installed peer. Do not invent a universal Blender preset or claim native32-bit compatibility without a real matching loader check. Finish with owner engine loading, texture and articulation tests.

Animated infantry use national/date directories, for example `graphics/3d/infantry/animated/cu_1978`, selected through faction/date bindings. Keep the existing animation structure and complete referenced set. A scout or sapper record does not demonstrate a separate per-unit moving uniform binding.

See [the extracted Ratel reference chain](../examples/ratel_reference_chain.md), [formation example](../examples/native_formation_pattern.md) and [art guide](AB2_UNIT_ART_GUIDE.md).
