# Minimal native record relationships

This is a schematic XML example, not a complete loadable database. IDs are placeholders; allocate real unused IDs and verify every required field against your installed vanilla database before implementing it.

```xml
<!-- factions.xml: selector ordinal is distinct from the referenced formation ID. -->
<string name="formationN" value="PLATOON_ID,1976,1,1979,12,100" />

<!-- formations.xml: a company references its dedicated HQ and platoons. -->
<section name="COMPANY_ID">
  <string name="name" value="Rifle Company" />
  <string name="trainingMod" value="0" />
  <string name="moraleMod" value="0" />
  <string name="isParentFormation" value="TRUE" />
  <string name="formation1Type" value="HQ_ID" />
  <string name="formation2Type" value="PLATOON_ID" />
  <string name="formation3Type" value="PLATOON_ID" />
  <string name="formation4Type" value="PLATOON_ID" />
</section>
```

The six selector values are formation ID, start year/month, end year/month and chance. Preserve selector ordinals used by existing scenarios. Complete formations require additional native fields; direct-unit platoons reference units using their own slot fields rather than these nested-formation links.

Verify the company is actually selected by a faction, all nested records exist, the national date sections cover the selector interval, and every unit/transport is appropriate for that period. Inspect a matching vanilla company for required HQ flags, counts and structure.

For an actual implemented quality example, inspect [the reviewed policy](../research/faction_quality_v1/implementation_policy.json) and its [native modifier audit](../research/faction_quality_v1/native_modifier_policy.md). Do not apply all parent/child modifiers as a hand-calculated stacking formula.
