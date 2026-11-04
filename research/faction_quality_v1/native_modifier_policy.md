# Native modifier placement audit

Read-only stock inspection; no game/editor/control or modifications.

|Formation ID|Name|Training modifier|Morale modifier|Children|
|---:|---|---:|---:|---|
|861|Parachute Rifle Platoon|+5|+10|direct units|
|862|Parachute Rifle Company|+5|+10|871, 861, 861, 861|
|871|Parachute Rifle SHQ|+5|+10|direct units|
|839|Territorial Infantry Platoon|-10|-10|direct units|
|840|Territorial Infantry Company|-10|-10|847, 839, 839, 839|
|847|Territorial Infantry HQ|-10|-10|direct units|
|288|Airborne Infantry Platoon|+20|+10|direct units|
|289|Airborne Infantry Company|+20|+10|300, 288, 288, 288|
|300|Airborne Infantry HQ|+20|+10|direct units|

British862 references HQ871 and platoon861 three times. All five nodes have the same+5/+10 authoring. Territorial840 references847 and839x3, all-10/-10. Soviet289 references300 and288x3, all+20/+10.

## Implementation policy

Use the same cohort modifier on selectable company, its platoons and dedicated cohort HQ, following those native examples. Do not invent an additive stacking calculation or claim engine inheritance is proven. Leave shared generic HQ neutral where mixed cohort ownership prevents a unique modifier. Retain historical selector/date intersections and all existing structures. The same annotation appearing on parent and child is native practice, not grounds to strip the parent bonus.

## Command semantics

Installed manual printed pages52-54 explains faction/HQ/contact/communications effects and the longer delay of individual orders. It does not document the two database fields separately or provide their equation. Installed game guide content_en.xml sections on HQ/formations confirms the same qualitative behaviour. Retain current native command pairs pending evidence; do not translate Fireforce or autonomy into invented seconds.

Stock source: C:\Program Files (x86)\Steam\steamapps\common\Armored Brigade 2\data\database\default\formations.xml

SHA256: cc6a21bcf831ff44f831978154133f75ce17a4318258ca63eb881b8bd21fe4dc

Parsing note: stock bare TO&E ampersands were escaped only in memory; no source repair was performed.

