# Build your own AB2 unit mod

This workflow records project experience, not an official engine specification. Start with one unit and a current vanilla peer from your own installed game.

1. Define the faction, role and date window. Separate equipment delivery, operational use, establishment and inference.

2. Trace faction selector -> formation -> unit -> weapon -> ammunition -> resource file. Reserve non-colliding IDs in your own database; same IDs can mean different things across game versions.

3. Copy the relevant native field structure, then make supported variant changes. Compare weapon and ammunition together. Do not invent mechanics or small-arms performance to match a model.

4. Inspect scale, markers, UVs, hierarchy and complete visible assembly. Use the art guide. Decode final textures and verify referenced filenames; offline import is not a gameplay test.

5. Add a tactical platoon with appropriate HQ, sections and transports. Create a company with HQ and nested platoons where supported. Expand it to verify total personnel and vehicles. See the [formation pattern](../examples/native_formation_pattern.md).

6. Add positive faction purchase selectors at supported dates. Check every month and transition, not just unit dates. Preserve selector ordinals when updating a mod because scenarios reference them.

7. Compare quality modifiers and DLC flags with current vanilla peers. Shared national/date infantry visuals are distinct from per-unit weapons and stats.

8. Maintain an ownership manifest for your mod. The included verifier is tied to Bush War paths, hashes and protected scope. Adapt it deliberately for a new mod; its pass does not certify unrelated content.

9. Stage a reversible install with drift checks and backups. Aircraft may require namespaced game-folder files in addition to user data. Preserve unknown and stock files.

10. Record game version, artifact hash, factions, date and actual load/movement/firing/transport/articulation results. Keep offline checks, installed bytes and owner gameplay evidence separate.

## Working with coding agents

Use [AGENTS.md](../AGENTS.md) as a project-specific example. Give an agent the intended unit/date, comparable vanilla record, allowed files, preservation requirements and checks. Require inspection of current files, explicit uncertainty and an actual diff. Deployment and publication need their own authority. See [lessons](lessons/README.md) for failures and corrections.

## Limits

A separate moving uniform for every infantry unit and supported mod-scoped scenery loading were not demonstrated. Shared national/date appearances were accepted; custom maps and scenery are excluded. These findings do not establish universal engine impossibility. Artwork regeneration from original source inputs is not a reproducible clean-machine build; the shipped payload can be verified and packaged.


Start the file-level work with [database layout and resources](MOD_LAYOUT_AND_RESOURCES.md) and the [extracted Ratel chain](../examples/ratel_reference_chain.md).
