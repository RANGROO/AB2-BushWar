# Contributing

Start with [AGENTS.md](AGENTS.md), [current state](docs/CURRENT_STATE.md) and [the tool index](tools/README.md). The instructions apply equally to people and coding agents.

## Smallest complete change

1. Identify the faction, role, historical horizon and affected purchase options.

2. Inspect a comparable vanilla unit/formation in your own installed game. Record which fields and structures you reuse.

3. Separate observed evidence, bounded inference and game allocation. A delivery date is not automatically an operational date.

4. Preserve IDs and selector ordinals. Expand companies into their HQ/platoons and check personnel, vehicles and transports.

5. Change only the intended records/assets. Record exact input and output hashes when modelling or deploying.

6. Run the maintained verifier, then native-reference checks if the installed game is available. Check every supported month, including transitions.

7. Inspect actual exported art. Record gameplay testing separately, including game version, map, date, faction pair and actions tested.

8. Describe behaviour, evidence, validation and untested limits in the contribution. Use a draft pull request unless asked otherwise.

## Development environment

The maintained verifier and packager require Python **3.11 or newer** and only the standard library. They resolve this checkout from their own location and accept explicit installation paths. Windows is the target installation platform.

Historical modelling scripts have individual dependencies, external source inputs and local archive paths. They are not a clean-machine build system. Do not install an arbitrary combination of packages or run them to reconstruct the accepted payload without reviewing the relevant workflow and inputs.

## Useful learning

Keep concise case studies under [docs/lessons](docs/lessons/README.md): symptom, evidence, demonstrated correction, prevention check and remaining uncertainty. Do not turn an unverified hypothesis into a general engine rule. Do not paste full chat transcripts, private configuration or machine-specific instructions into the active agent guide.

The [minimal XML example](examples/native_formation_pattern.md) illustrates record relationships. It is documentation, not an installable migration.

## Storage and history

Keep generated archives, caches, rollback copies and account configuration outside Git. The original project preserves the full development history. Only documented maintained tools belong in this candidate.

