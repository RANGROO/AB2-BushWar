# Maintained tools

Use Python 3.11+, standard library only, from the repository root.

| Entry point | Purpose |
|---|---|
| `python -B tools/verify_mod.py` | Verify all shipped hashes, aircraft sources, date windows and protected scope |
| `python -B tools/verify_mod.py --game-root "<game>"` | Also audit against your installed vanilla database |
| `python -B tools/verify_mod.py --runtime-root "<user data>" --game-root "<game>"` | Also compare the existing owned runtime files |
| `python -B tools/build_private_snapshot.py` | Verify and build an unpublished ZIP in ignored dist/ |

`audit_database_loading.py` and `audit_historical_availability.py` are library dependencies, not standalone migration/install commands. Native checks require the explicit game-root supplied by the wrapper. Generated reports and archives stay in dist/. No tool installs, uploads, launches AB2 or changes Steam files.

