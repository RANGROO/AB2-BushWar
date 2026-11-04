# AB2 stats, availability and formations guide

Originally consolidated 12 October 2026; current Bush War scope is 1965–1994 with individual faction horizons. Use current stock XML and the relevant unit evidence when implementing changes. This process does not certify every existing record as historically exact.

## Complete data chain

Trace faction/date selector → formation or flight → unit or aircraft → weapon → ammunition → resource bindings/files. A model in the encyclopedia does not establish a selectable formation, campaign aircraft or working weapon.

Compare several stock nations with similar roles and dates. Reuse native fields and behaviours. A field name, unique ID or successful XML parse does not prove a new mechanic exists.

## Evidence classifications

| Classification | Required explanation |
|---|---|
| Historical fact | Source, page/date and exact variant or establishment covered |
| Presence bound | Equipment documented by a date; not necessarily first introduction |
| Inference | Reasoning and unresolved alternatives |
| Gameplay proxy | Native donor, changed values and practical limitation |
| Test fixture | Diagnostic date/configuration, separate from service history |
| Unresolved | Missing evidence or engine behaviour; hold or document the provisional choice |

Availability, establishment and performance need separate evidence. Captured stocks do not prove a launcher in every section. Deliveries do not prove immediate nationwide replacement. Modern performance does not authenticate an original-period round. Tabletop figure ratios are not vehicle counts, and Red Dragon balance values are not historical statistics.

## Stats and weapon loads

- Choose a stock peer in the same class. Compare armour faces, dimensions, handling, visibility, survivability, weapon slots and loads as applicable.

- Change values supported by the intended variant. Label donor-derived armour/handling/crew values as proxies. Conventional plate thickness does not automatically simulate mine protection.

- Inspect weapon **and** ammunition: burst/timing/reload behaviour, loads, ranges, accuracy, penetration, effects, guidance and target categories must agree.

- Keep kinetic, HEAT, tandem and guided behaviour distinct. Do not grant modern effects merely to improve an older weapon's balance.

- Compare practical engagement ranges with native gameplay. Brochure maximum range is not automatically the correct on-map range.

- Explain accuracy, reload and ammunition values that are native gameplay allocations rather than measurements.

- Avoid double counting aggregate multi-barrel weapons. Aircraft ammunition is per aircraft, not per flight. For ground units, inspect `weaponNNum` and `AmmoNNumPerWeapon` together before calculating total loads.

- Preserve valid slot and muzzle relationships. A weapon entry does not prove its visual firing pose is selected correctly.

- Do not invent unverified passenger-capacity, resupply, engineering, mine-blast or packing mechanics from a flag or model accessory.

## Purchases and formations

Current policy: vanilla-style combat companies, platoons, support sections and proper HQs; no standalone training/logistics/noncombat purchases. The older ban on company-level purchases is superseded. Necessary transports and tractors inside combat formations can remain. Prefer multi-vehicle troops/sections. A ten-man infantry section is a tactical element, not a singleton soldier.

Use native category, icon, HQ/radio flags and dependency patterns. A platoon containing a command team is not itself necessarily an HQ formation. Expand nested formations to check total soldiers, vehicles and transports.

Use familiar purchase names, with **[R4]** following Britain's **[SA80]** convention. Keep weapon stats generic while the suffix identifies the rifle version. Avoid draft, late-crew and development-process labels. Use **Prototype**, not Experimental. Inferred prototype group sizes remain gameplay allocations, not authenticated establishments.

Hide dated equipment upgrades behind existing purchase names instead of multiplying nearly identical options. Preserve record IDs where practical. Scenarios use **faction selector ordinals**, not global formation/flight IDs; reindexing requires scenario migration.

### Verified stock examples

| Example | Pattern |
|---|---|
| Britain formation 806 | Three sections with ENERGA; one also has Carl Gustav/four rounds |
| USSR formation 269 | Three squads, each with RPG-7/five rounds |
| US formation 568 | Rifle squads with disposable launchers and a weapons squad |
| Finland formation 1332 | Rifle squads and a separate light recoilless-rifle team |
| Norway formation 2539 | Rifle, support and antitank squads in one platoon |
| US formation 641 / unit 347 | Engineer HQ plus three squads; engineer flag and satchel charges |

These are valid alternatives, not a requirement to give every nation identical equipment. South Africa's broad RPG/FT5 section allocation is a documented gameplay choice; see antitank parity (archived reference: `INFANTRY_ANTITANK_PARITY.md`).

Paratroopers can use normal dated infantry formations. Airborne identity does not implement an airdrop. Helicopter transport requires native editor AIRTRANSPORT assignments and scenario setup/save; an XML transport flight alone does not embark infantry.

## Dates, categories and campaign availability

Check **every month**, including transition boundaries. December 1994 is the mod horizon, not necessarily a withdrawal date. January can represent a year-only source at declared annual granularity; do not present it as a known month.

Separate prototype trials from operational introduction. Do not convert old June 1994 test fixtures into service history. The established 1995 quarantine sentinel is outside mod coverage and preserves retired ordinals; it is not a historical date.

Check selector continuity, settings coverage, weights and category fields against stock. Diagnose the actual screen, faction and month/year when a unit is missing. An aircraft resource, encyclopedia entry or faction flight list alone does not prove regular-campaign availability.

## Aircraft and artillery

Stock CAS uses guns, rockets, bombs and sometimes air-to-air missiles, with separate payload/attack variants. Keep loads physically compatible rather than combining every maximum capacity. Match visible stores with ammo and qualify munition integration separately from airframe service dates.

Use the native attack mode matching the bomb contract. Do not silently assign loft ammunition to level attack. Confirm guidance/effects and dates before implementing AS30, glide-bomb or cluster proxies. A compatible-aircraft list does not date first integration. See payload build (archived reference: `AIRCRAFT_PAYLOAD_BUILD.md`) for the active aircraft work.

Vanilla supports on-map artillery; the earlier blanket exclusion was too broad. Compare appropriate native gun sections, ranges, crews, towing/packing behaviour and formation scale. Keep long-range off-map support distinct from on-map assets. This guide does not authorize an artillery change.

## Validation and troubleshooting

1. Check unused IDs and existing reservations. Ground unit IDs below 5000 and formation IDs below 7500 are conservative project conventions, not proven engine maxima.

2. Validate duplicate fields, references, native domains, contiguous selectors and monthly coverage. Preserve unrelated factions and stock records.

3. Expand purchase dependencies; check HQs, transports, troop counts, loads and support flags. Test expected purchases on both sides of date transitions.

4. Validate every model/texture and any required game-global aircraft overlay. Triangulate and native-import final exports.

5. Verify map ID, terrain, setup bounds, objectives and scenario ordinals. Reuse the single Fort Irwin desert mission (`fort_irwin_ntc`, terrain4); keep diagnostic cases small when isolating crashes.

6. Back up owned files, ZIP and manifests; refuse unexpected drift and preserve unknown files. Verify runtime/overlay hashes and archive bytes after final changes.

7. Record live selection, campaign, loading and firing separately. Check fresh logs/dumps and a stock/minimal-custom comparison before assigning crash causes. Do not strip all licence fields or rewrite unrelated data solely because an error mentions licensing.

Use `python -B tools/verify_mod.py` and its optional explicit game/runtime paths. Reports go to ignored `dist/`. The two audit modules are dependencies, not migration entry points. These checks do not replace game tests or historical research.

## Repeatability and sharing

Retain sources and limitations, stock donors, IDs, dated purchase graph, final mesh/texture hashes, checks, installation/rollback receipts and specific owner acceptance. Keep rejected candidates separate from accepted inputs. Record local prerequisites rather than claiming a verified clean-machine build.

Historical authenticity, local installation, packaging, game acceptance and publication are independent statuses. Static checks alone do not establish “complete,” “bug-free” or “released.”

