# ZANLA, ZIPRA and Mozambique crash investigation

The owner reported crashes when playing these three factions on 4 November 2026, with no crash logs available. The owner does not recall the mission date or crash phase and requested a file-based investigation. Those details are not a prerequisite for this audit.

All five flags selected by these factions had image-only sprite definitions. The other packaged faction flags also define translation and rotation origins. The correction adds those same `top_left` origins, preserving image paths, identities, dates, formations, statistics and models. The payload ownership hash is updated. The maintained verifier now rejects image sprites with missing transform origins.

This is a confirmed difference from the established resource pattern and a candidate crash correction, not a proven root cause. The earlier database audit accepted these incomplete definitions. Full native database checks passed with zero errors and 1,501 inherited warnings; monthly availability passed. All 1,258 subscribed PNGs decoded successfully.

No game was launched. No Workshop update or manual installation was performed for this correction. Owner loading and mission-start tests remain required before claiming the crashes resolved. If a crash persists, investigate the exact selected date, force and crash phase instead of treating this correction as acceptance.

## Expanded checks

- The actual Steam subscription matches all 2,273 files in the uploaded native manifest. This is not a stale ZIP installation.
- Tracing every dated selector for factions 16–18 reached 108 formations and 54 units. The maintained audit found no broken references or recursive formation cycles.
- All 44 shared `fa_1979` infantry poses passed the installed x86 `assimp-vc140-mt.dll` importer with flags 3 and required finite position, normal, tangent, bitangent and UV arrays.
- All 10 distinct directly referenced static vehicle/crew models in that unit closure passed the same import check. This does not certify every indirectly bound weapon or aircraft assembly.
- The three factions have zero `artyGunNum` throughout their profiles, unlike stock profiles. This remains an unconfirmed compatibility risk. No demonstrated faulting arithmetic or supported alternative way to disable faction artillery was found. It is retained rather than granting unsupported artillery or substituting another speculative zero-valued setting.
- No Windows Application Error/WER entry or local crash dump for AB2 was found in the inspected recent window. Absence of such an entry does not prove the game did not crash.

The flag patch is deliberately narrow. Import, reference and image checks do not establish mission-start acceptance or prove that zero artillery is safe.
