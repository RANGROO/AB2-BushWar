# Install, update and remove the unit mod

This candidate contains the eight-faction **Bush War 1965–1994** unit database. Custom maps and scenery are not installed. The full Armored Brigade II game is required; this is not a standalone game.

## Locate the two destinations

| Destination | Contents |
|---|---|
| AB2 user-data folder, normally `Documents/My Games/Armored Brigade 2` | The archive's `data/` tree |
| Your actual AB2 game installation | Only the namespaced aircraft files listed in `deployment/aircraft-overlay-manifest.json` |

Documents may be redirected or inside OneDrive. Use the folder your game actually uses. Do not guess the game directory from another contributor's workstation paths.

## Before installing or updating

1. Close AB2. Extract the candidate ZIP into an empty temporary folder; do not extract it directly over your game.
2. Keep the ZIP's checksum. The portable payload manifest records every owned user-data file and hash.
3. Back up existing destination files that the payload/overlay would change, plus the prior ownership manifests. Keep those backups outside the game and repository. Do not replace unknown files without reviewing the collision.
4. For aircraft, each manifest row names a `source` relative to the extracted archive and a `target_relative_to_game` relative to your game installation. If an existing target differs and you cannot establish that it belongs to your previous Bush War installation, stop and investigate. Do not overwrite stock/other-mod files.

## Install

1. Copy the extracted `data/` tree into the AB2 user-data folder, preserving its relative paths. Do not replace or delete the entire existing `data` directory.
2. Copy each selected aircraft manifest source to its exact game-relative target. These are namespaced additions; no executable or stock model replacement is required. The current manifest contains 341 files, but use its actual entries rather than hard-coding this count.
3. Retain `deployment/payload-manifest.json` and `deployment/aircraft-overlay-manifest.json` with your installation backup for future updates/removal.
4. If using the source checkout, verify installed ownership with:

   ```powershell
   python -B tools/verify_mod.py --runtime-root "<AB2 user-data folder>" --game-root "<AB2 game installation>"
   ```

5. Start AB2 yourself and select **Bush War 1965–1994**. Choose a date inside the selected faction's supported horizon. Rhodesia ends December 1979; Cuba covers October 1975–May 1991.

The game launch is an owner test, not an action performed by the verification tools.

## Update or uninstall

Compare the old and new manifests before updating. Remove retired files only when they are positively owned by the previous mod and their current hashes match the old manifest. Preserve unknown or locally changed files. This update does not authorize deleting files omitted from an old, incomplete manifest.

To uninstall, close the game, restore backed-up pre-mod files, and remove only unchanged mod-owned additions listed in your saved manifests. Apply the same rule to the namespaced game aircraft overlay. Do not delete the user's whole database, graphics, maps or scenario directories.

## Troubleshooting

- Missing faction: check the selected database and date first.
- Missing purchases: report faction/date, purchase category and expected formation.
- Crash: retain the latest game error log and any crash dump; report map, date, both factions and whether it failed before or after Start.
- Missing model/texture: check the actual referenced file and installed hash, including the game-directory aircraft overlay.
- Read [known limitations](KNOWN_LIMITATIONS.md). Do not run old builders/installers as a repair shortcut.
