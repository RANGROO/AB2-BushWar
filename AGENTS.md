# Bush War contributor and agent instructions

## Scope and current truth

- This repository maintains the eight-faction Armored Brigade II Bush War unit mod, overall 1965–1994. Read `docs/CURRENT_STATE.md` and `deployment/payload-manifest.json` first.

- Preserve faction-specific horizons. Cuba represents Cuban-operated forces in Angola/southern Africa, October 1975–May 1991. Rhodesia ends December 1979; independent Zimbabwe is excluded. Other national and organisational phases remain bounded by the current XML.

- Custom maps and scenery are excluded. Do not install or enable them while working on units.

- Current receipts override old counts and status reports. A filename containing “current”, “latest”, “final” or “passed” does not establish present acceptance.

## Work safely

- Confirm repository, branch and dirty state before editing. Preserve unrelated work. Never run all tools as a batch.

- Use `tools/README.md` to identify maintained commands. Only documented maintained tools are included. Do not import or run old one-shot migrations.

- Preserve native IDs, purchase-selector ordinals, names, dates, HQs and nested topology unless the task explicitly changes them. Scenarios reference selector ordinals.

- Use native vanilla fields and comparable formations. Research equipment, operation, dates and organisation separately; document inference instead of inventing precision.

- Use companies, platoons, support sections and HQs where appropriate. Generic small-arms statistics follow vanilla categories; historical models can differ.

- Keep full visible model assemblies within the project ceiling of 2,500 triangles, including visible crew and separate weapons. This is a project budget, not a universal engine specification.

- Preserve demonstrated COLLADA conventions: valid UVs/vectors, native hierarchy/markers and resource-bound textures. Read `docs/AB2_UNIT_ART_GUIDE.md` before art work.

## Validation and delivery

- Run `python -B tools/verify_mod.py` for payload hashes, dated selectors, overlay sources and protected scenario/map scope.

- For native database checks, supply an installed game explicitly: `python -B tools/verify_mod.py --game-root "<AB2 installation>"`.

- Build a local candidate with `python -B tools/build_private_snapshot.py`. Generated archives stay in ignored `dist/`; never commit them.

- Offline checks, deployment parity and owner gameplay acceptance are separate. Never describe a native import or checksum as an in-game test.

- Do not launch/control the game, deploy, push, publish, create releases, change repository visibility, merge or rewrite history without the user's relevant authorization.

- Deployment requires ownership/drift checks, backups and exact payload/overlay verification. Preserve unknown files and stock assets. Aircraft use a namespaced game-directory overlay; do not run obsolete fixed-count installers.

- Keep new maintained tools independent of a developer's username, archive drive or private runtime. Require explicit local paths; do not substitute historical receipts for missing inputs.

- Update current documentation and focused evidence. Keep experimental results labelled and preserve useful failure lessons in `docs/lessons/`.

## Reading order

1. `README.md`, `CONTRIBUTING.md`, `docs/CURRENT_STATE.md`.

2. `docs/AB2_STATS_AND_FORMATIONS_GUIDE.md` or `docs/AB2_UNIT_ART_GUIDE.md`.

3. `docs/lessons/README.md` and the relevant exact artifact receipts.

These instructions are tool-independent. Historical mentions of particular assistants or local runtimes do not require contributors to use them.

