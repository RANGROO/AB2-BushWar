# Bush War 1965–1994 for Armored Brigade II

A unit mod covering the conflicts of southern Africa, with a focus on Angola and the Rhodesian Bush War. It adds eight factions, historically dated equipment, national uniforms, adapted vehicles and aircraft, and selectable platoons and companies.

This repository also includes practical guides, examples and agent instructions for people who want to build their own AB2 mods.

## Factions

- South Africa
- Cuba
- UNITA / FALA
- MPLA / FAPLA / FAA
- Rhodesia
- ZANLA
- ZIPRA / ZAPU
- Mozambique / FRELIMO

The overall timeline is 1965–1994. Each faction has its own dates: Cuban-operated forces in southern Africa run from October 1975 to May 1991, and Rhodesia ends in December 1979. Some South African prototype vehicles are included. Do not expect even balance against the vanilla factions.

## Install and play

You need **Armored Brigade II**. This is a unit mod; custom maps and battle missions are not included. The repository retains one Fort Irwin diagnostic scenario for development.

1. Get the mod files from this repository, or the [Steam Workshop item](https://steamcommunity.com/sharedfiles/filedetails/?id=3823850809) if you have access. The Workshop download currently contains a manual-install ZIP.
2. Follow [the installation guide](docs/INSTALLATION.md). The `package/data/` files go in AB2's user-data folder. Selected aircraft also need namespaced files in the game folder; the guide and overlay manifest give their exact destinations.
3. Back up files before replacing them. Preserve stock files and other mods.
4. Start AB2, select **Bush War 1965–1994**, and choose a date supported by your factions.

Subscribing alone is not a verified complete installation. Read the guide before copying files.

See [all selectable units](docs/ALL_FACTION_SELECTABLE_ROSTERS.md), [training and morale](docs/FACTION_TRAINING_MORALE_COMMAND.md) and [known limitations](docs/KNOWN_LIMITATIONS.md). Models and historical details remain a work in progress; offline validation is not a claim that every unit has passed gameplay testing.

## Make your own AB2 mod

Start with these guides:

| Guide | What it teaches |
|---|---|
| [Build your own mod](docs/BUILD_YOUR_OWN_MOD.md) | The workflow from a vanilla reference to a selectable force |
| [Database layout and resources](docs/MOD_LAYOUT_AND_RESOURCES.md) | XML files, model bindings and texture paths |
| [Stats and formations](docs/AB2_STATS_AND_FORMATIONS_GUIDE.md) | Weapons, dates, HQs, platoons and companies |
| [Art and export](docs/AB2_UNIT_ART_GUIDE.md) | Models, textures, hierarchy and export limitations |
| [Examples](examples/native_formation_pattern.md) | Formation relationships and a [real Ratel reference chain](examples/ratel_reference_chain.md) |
| [Lessons learned](docs/lessons/README.md) | Problems we encountered, fixes and remaining uncertainty |
| [Agent instructions](AGENTS.md) | How to give coding agents bounded tasks and verify their work |

These are project findings, not an official engine specification. The examples are annotated excerpts, not a tested standalone starter mod. The shipped assets can be verified and packaged; rebuilding all artwork from original inputs is not a supported clean-machine workflow.

## Verify or build a ZIP

Use **Python 3.11 or newer**. No extra Python packages are required. From the repository folder:

```powershell
python -B tools/verify_mod.py
python -B tools/build_private_snapshot.py
```

The first command checks payload hashes, references to aircraft sources and monthly faction availability. The second creates a verified local ZIP under `dist/`.

For additional checks against your installed vanilla database:

```powershell
python -B tools/verify_mod.py --game-root "<your AB2 installation>"
```

These tools do not install files, launch the game or upload anything. See [the tool guide](tools/README.md) for runtime comparison options.

## Contribute or report a problem

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing the mod. For a bug report, include the game version, factions, date, map, unit or formation and what happened. Historical accuracy suggestions are welcome; include a source where possible.

## Repository contents

- `package/`: installable unit payload.
- `deployment/`: file ownership and aircraft overlay manifests.
- `docs/`, `examples/`: guides, current rosters and reusable learning.
- `tools/`: four maintained verification and packaging modules.
- `research/`: selected historical and vanilla comparisons.
- `workshop/`: description, screenshot inventory and original gallery images.

Old migrations, caches, unfinished queues and unused scenery experiments are excluded. Generated ZIPs stay outside Git.

## License

Project-owned code, documentation and original contributions are licensed under **GNU GPL v3.0**. See [LICENSE](LICENSE). Third-party material retains its original rights; this license does not relicense Armored Brigade II or other third-party assets.
