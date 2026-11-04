# Demonstrated lessons for similar mods

Use these alongside the [art guide](../AB2_UNIT_ART_GUIDE.md) and [stats/formation guide](../AB2_STATS_AND_FORMATIONS_GUIDE.md). These are project observations, not an official engine specification.

| Case | Evidence and correction | Prevention and limit |
|---|---|---|
| Missing Generate Mission purchases | Unit definitions alone did not provide complete selectable rosters. Positive faction selectors, nested formations and dated national settings were audited and corrected. | Expand the purchase graph and check every supported month. Basic infantry/HQ coverage is not full combined-arms acceptance. |
| Companies and HQ quality | Stock British parachute/territorial examples use matching company, platoon and dedicated-HQ modifiers. The mod follows that pattern; shared generic HQs remain neutral. | Inspect comparable vanilla records. Do not invent a stacking formula or treat a bonus as evidence of elite historical status. See [modifier audit](../../research/faction_quality_v1/native_modifier_policy.md). |
| Invalid PNG crashes | Owner-reported gun/tank texture failures motivated checking actual referenced textures rather than relying on filenames or successful model imports. | Decode final PNGs, verify resource paths and compare deployed hashes. A valid PNG still does not prove shader/appearance acceptance. |
| Unintended DLC requirements | Inherited expansion requirements and model dependencies were found in custom records; reviewed replacements restored the intended base-game setup. | Review dependency flags and actual resource donors together. Do not remove all flags as a generic crash fix. See historical fix (archived reference: `../LICENCE_COMPATIBILITY_FIX.md`). |
| Aircraft lookup location | Some aircraft required namespaced assets under the game graphics directory, beyond the user database. | Use the current portable overlay manifest; never an obsolete fixed asset count. Do not overwrite different existing files. |
| COLLADA loading | The Ratel loading correction changed marker UVs and geometry names together. Offline imports alone had not predicted the crash. | Preserve the demonstrated hierarchy/UV/naming combination. Do not claim either change alone was the proven cause. |
| Per-unit uniforms and scenery | A unit-specific moving-uniform binding and a supported mod-scoped custom-scenery loading contract were not demonstrated. Shared national/date infantry sets were accepted; scenery/maps remain unused. | Preserve explicit capability limits. Vehicle loading does not prove scenery loading. Avoid unsupported units or global replacements as workarounds. |
| Map crash isolation | The owner reported stock Fort Irwin and a dry-land Cuito area loading while a river/crossroad area crashed after Start. | Record the exact battle box, settings and terrain. This comparison narrows the cause; it does not establish that later river corrections passed. Maps remain withdrawn. |

## Recording a new lesson

Write the symptom, exact artifact/version, observed evidence, correction, validation and unresolved uncertainty. Preserve negative results when they prevent repeated work. Keep the active agent instructions concise; link to the case study instead of copying a session log.
