# AB2 unit art and export guide

Consolidated 12 October 2026 from local stock-asset inspection and Bush War build records. Project choices below are not universal engine requirements. See the [documentation index](README.md) for the maintained guides. Original detailed investigations remain archived in the old project.

## Native baselines and style

Use an existing AB2 asset when a suitable baseline exists. Inspect its geometry, textures, physical scale, nodes and markers before editing. Preserve the accepted source and record its hash. Choose a peer with comparable construction and role, rather than copying an unrelated asset's triangle count.

Red Dragon references are a fallback for missing families, not the default pipeline. Record provenance and sharing rights separately: access to installed files does not establish redistribution permission.

- Compare actual exports at equal scale, camera and light, including close-ups and tactical distance. Matching paint colour or polygon count alone does not establish style parity.

- The project ceiling is **2,500 visible triangles per complete assembly**, excluding markers. It is not a universal engine limit or a minimum. Include visible operators and separate weapons.

- Preserve silhouette, wheels, turret seating and ground contact before small fittings. Remove unsupported clutter and floating accessories rather than obscuring them with texture detail.

- Keep armour deliberately planar, with hard edges where appropriate. Use smooth normals on tyres, rounded shells and barrels. Blanket flat shading and aggressive decimation caused unwanted facets.

- Wheels need readable sidewalls, a restrained bevel, recessed rim/hub, circular face UVs and tread strips. Single-colour UV points produced poor results despite acceptable triangle counts.

- Check the complete assembly: hull, turret ring, cupola, mantlet, gun, crew and wheel wells. Individually valid parts can still intersect or hover when attached.

- Antenna removal is a project art choice where appropriate, not proof that all stock vehicles omit antennas.

## Textures and shader appearance

The inspected model shaders use diffuse, tangent-space normal and specular maps, with ambient/diffuse lighting and specular highlights. The normal-map green channel is flipped in the inspected shader. Shadowing and ambient occlusion affect the result. Recheck shaders if the game changes; runtime settings were not fully verified by the offline audit.

Most inspected stock vehicle atlases were 512×512. Start there, but preserve justified donor texture sizes. Neutral normal RGB(128,128,255) and restrained specular RGB(51,51,51) match several native peers; other stock maps differ.

Use readable recesses, restrained edge highlights and subtle paint variation. Avoid photographic noise and completely featureless fill. Vehicle brown **#8A6B4D** is the agreed SADF art approximation, not an authenticated paint specification. Uniform nutria is a separate material choice.

Preserve UV charts and texel density through topology changes. Inspect seams, stretching, zero-area UVs and atlas bleeding. Whole-atlas average colour is misleading when much of the image is unused. Check a new free atlas tile against **all** models sharing the texture, or expand the atlas while preserving original texels and density. Flat-colour surfaces still need valid UVs and tangent vectors.

Archived rendering investigation: `ab2-render-style-audit.json` (not included); shader sources are under the installed game's `data/graphics/3d/shader/`. `softrender` previews omit game normal/specular lighting, fog and ambient occlusion.

## Safe COLLADA export

The demonstrated working combination is material-free COLLADA, resource-bound textures, geometry IDs/names distinct from scene-node IDs/names, finite normals/tangents and valid UVs on **every triangle, including markers**.

1. Triangulate every mesh: hull, accessories, operators, wrecks and markers. The Casspir face-not-triangulated crash was not a reason to inspect only the main hull.

2. Preserve the unprefixed default COLLADA namespace. An earlier `ns0:COLLADA` export failed the installed importer with “File came out empty.”

3. Preserve measured axes, parenting, pivots and transforms. An up-axis label alone does not describe another exporter's actual coordinate convention.

4. Preserve native turret, elevation, recoil, muzzle, commander and exhaust contracts. Inspect a peer before inventing nodes or rotating markers.

5. A matching native32-bit import check is required when qualifying new artwork. The original Assimp probe is not included or reproducible here; see [the import limitations](MOD_LAYOUT_AND_RESOURCES.md). Do not substitute a generic import success for native or in-game acceptance.

The Ratel began loading after marker UVs and geometry names changed together. Their individual contributions were not isolated. Tangent-only and material-only changes did not fix that case. Preserve the demonstrated combination without asserting an unproven single cause.

## Infantry and crew lessons

The verified stock pattern selects moving infantry families by **faction and date**. No supported per-unit moving-family override has been established. Different simultaneous moving uniforms for rifle, mechanised and parachute units require further engine evidence. Static support operators can use explicit crew bindings.

South Africa's current broad art convention is early webbing and M63-style helmets before 1983, then Pattern83 assault vests and M83-style helmets from 1983. M87 was omitted by owner direction. Dedicated MG operators use field hats. These are broad era choices, not universal historical issue claims; early nutria, exact webgear and some weapon identities remain approximations.

Use role-appropriate vehicle crew kit rather than automatically fitting full infantry equipment. Removing foreign binding names or recolouring a soldier does not authenticate clothing, headgear or weapons.

Fit headgear from unambiguous UV/position correspondence on the **actual packaged upper skull**. Exporters may reorder triangles; incorrect vertex pairing can produce a deceptively low fit error. Including lower-neck landmarks corrupted previous head fits.

Review all running, crawling, firing, binocular, launcher and casualty poses. Check headgear against hands and weapons as well as the head: head-only checks missed binocular and RPG-hand contacts. Preserve grips and wrist seams when adjusting poses. Do not switch headgear between frames to fake role diversity.

Projected early webbing meshes produced floating kit and intersections. The accepted cleanup instead bakes simplified webbing into garment UVs; it has no extruded pouch silhouette. Do not install the rejected projected-kit candidate. Exact R4 rifle shape, SA7 mark and full uniform authenticity remain separate checks.

## Aircraft, articulation and animation

The examined stock aircraft bake stores into the fuselage mesh. Dedicated loadout models follow that pattern while preserving airframe geometry, normals and texture density. Match visible pod count × tubes per pod to the rocket load; distinguish six-tube F2-type pods from 18-tube pods. Internal bombs need not be visible through a closed bay.

Fit pylons to the wing underside and inspect both sides. Move existing rocket markers to representative pod mouths while preserving orientation. Do not invent a bomb-release marker without a verified native contract. Static baked stores do not establish store detachment or opening-bay animation.

Aircraft have previously required **game-global graphics paths**; user-data presence alone was insufficient in that crash case. Verify actual resource lookup and the separately owned overlay, using existing installer/manifest patterns where applicable. An old installer may not discover newly allocated aircraft IDs. Do not replace stock files.

No wheel nodes, clips or verified scrolling contract were found in the examined stock vehicle assets. That is a scoped observation, not a universal engine claim. Do not invent wheel clips or call a camera-orbit GIF a movement/flight animation.

## Acceptance checklist

1. Record source/final hashes, provenance, dimensions and complete triangle count.

2. Check topology, winding, UVs, normal/tangent finiteness, resources, hierarchy and marker transforms.

3. Check assembly clearances and the relevant motion/pose envelope. Intersection probes exclude some coplanar overlap and containment; zero crossings does not mean bug-free.

4. Inspect final exports from several sides and at tactical scale. Label synthetic stills/GIFs **offline**.

5. Back up owned files, install within scope, and verify runtime hashes and any aircraft overlay.

6. Record actual load, movement, firing, articulation, passengers and shader appearance separately for the exact tested artifact. Record the actual tester and actions.

