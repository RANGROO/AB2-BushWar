# SADF and Rhodesia quality recommendation

Research only. No database/runtime edits. Numerical values are game-design judgements calibrated to native vanilla units, not historical measurements.

## Baselines

|Faction|Training|Morale|Command|
|---|---:|---:|---|
|South Africa|75|75|retain20/20|
|Rhodesia|75|75|retain20/20|

Keep every existing historical boundary; no automatic improvement curve, political-outcome morale penalty, or Fireforce artillery bonus. Generic SADF formations do not identify Citizen Force versus Permanent Force, so do not relabel them or assign an undocumented reserve penalty.

## Formation modifiers

Apply once per resulting unit. Company/platoon inheritance must be verified independently before authoring parent and child values. Shared generic HQ3402 must remain neutral unless cloned (cloning outside this task).

### 11 parachute: training+5, morale+10

SF; native British parachute calibration

|ID|Current reachable formation|
|---:|---|
|3650|Parachute Infantry Platoon|
|3652|Parachute Infantry HQ|
|3653|Parachute Infantry HQ [R4]|
|3685|Parachute Infantry Platoon|
|3686|Parachute Infantry Platoon [R4]|
|3713|Parachute Infantry Platoon|
|3714|Parachute Infantry Platoon [R4]|
|3731|Parachute Infantry Platoon|
|3732|Parachute Infantry Platoon [R4]|
|3799|Parachute Infantry Company|
|3800|Parachute Infantry Company [R4]|
|3810|Parachute Infantry Company|
|3811|Parachute Infantry Company [R4]|
|3815|Parachute Infantry Company|
|3825|Parachute Infantry Company|
|3826|Parachute Infantry Company [R4]|

### 11 recce: training+10, morale+10

SF; small selected reconnaissance cadre, no extra spotting/mechanics

|ID|Current reachable formation|
|---:|---|
|3774|Recce Scout Section|

### 11 32_battalion_recce: training+5, morale+5

SF; bounded reconnaissance-wing proxy rather than all32Battalion elite

|ID|Current reachable formation|
|---:|---|
|3775|32 Battalion Scout Section|

### 15 operational_regulars: training+5, morale+5

Standing operational cadre; Fireforce is not an extra stacking bonus; Greys moderate-low generic reconnaissance cadre inference

|ID|Current reachable formation|
|---:|---|
|3401|RLI Fire Force Troop|
|3405|RAR Fire Force Platoon|
|3406|RAR HQ|
|3431|RLI Rifle Platoon|
|3433|RAR Rifle Platoon|
|3443|RLI 60mm Mortar Section|
|3447|RLI Assault Pioneer Troop|
|3449|RLI 88mm Rocket Launcher Team|
|3457|RLI RPG-7 Team|
|3471|Grey's Scouts Dismounted Reconnaissance Group|
|3477|MAP75 RLI Tactical Patrol|
|3478|MAP75 RLI Mounted HQ|
|3480|MAP45 RLI Tactical Patrol|
|3481|MAP45 RLI Mounted HQ|
|3483|RLI 81mm Short-Barrel Mortar Section|
|3484|RLI 81mm Long-Barrel Mortar Section|
|3485|RLI 81mm Long-Barrel Mortar Section|
|4200|RLI Rifle Company|
|4201|RAR Rifle Company|
|4204|RLI Scout Section|
|4205|RAR Rifle Section [mot.]|
|4206|RAR HQ [mot.]|
|4207|RAR Rifle Platoon [mot.]|
|4208|RAR Rifle Company [mot.]|

### 15 territorial: training-5, morale+0

Reserve availability and shorter recurrent training; not every reservist inexperienced; modest vanilla Territorial analogue

|ID|Current reachable formation|
|---:|---|
|3409|RR Patrol Platoon|
|3410|RR HQ|
|3435|RR Rifle Platoon|
|4202|RR Rifle Company|

### 15 selected_specialists: training+10, morale+10

SF; SAS label/selection analogy moderate-low, Selous directly participant supported

|ID|Current reachable formation|
|---:|---|
|3450|SAS RPG-7 Team|
|3451|SAS RPD Team|
|3452|SAS HQ|
|3453|SAS LMG Section|
|3462|Selous Scouts Reconnaissance Group|

### 15 guard_force: training-10, morale-5

GF; limited field training, professional cadre prevents blanket militia rating

|ID|Current reachable formation|
|---:|---|
|3454|Guard Force HQ|
|3455|Guard Force Stick|
|3456|Guard Force Rifle Group|
|3467|Guard Force Puma HQ|
|3469|Guard Force Puma Patrol|

## Evidence and counterevidence

- [GF](https://sites.google.com/site/rhodesianguardforce/home/historic-overview): participant compilation; sections explicitly credit Horst Schobesberger and former personnel. Inspected=True. Professional HQ/depot core thinly spread in field; initially quantity over quality; recruit course extended to three months, no exact year stated. Limitation: Partisan retrospective; unfinished date placeholders; not numerical morale measurement.

- [SF](https://samilitaryhistory.org/13/c13febne.html): published account of Stephan Fourie participant lecture. Inspected=True. Selective Selous reconnaissance training, sustained independent small teams; identifies32 Battalion recce wing and SA Recces as analogous. Limitation: Retrospective recollection; reject casualty-share claims as training calibration; contradictory17-week/17-day selection descriptions do not support exact duration.

- [NS](https://www.saha.org.za/ecc25/timeline.htm): archive of participant End Conscription Campaign history. Inspected=True. 1972 nine-to-twelve month national service;1977 two-year service;December1989 reduction to one year;1993 conscription abolition. Limitation: Duration is not combat proficiency; nonreporting is not every deployed soldier morale; retain75 rather than invent step changes.

- [RAR](https://www.armyupress.army.mil/Portals/7/combat-studies-institute/csi-books/ArtOfWar_RhodesianAfricanRifles.pdf): US Army published historical study. Inspected=False. Search identification only Limitation: 403 on direct retrieval; do not cite unseen pages as verified evidence.

Exact regular/SAS/Greys numeric distinctions are moderate-low confidence and should be kept small. Guard Force training distinction and selected Selous/Recce differentiation have direct accessible participant support. No source establishes morale as a numerical percentage. No national collapse or racial attribution is inferred. Root may reduce weakly supported distinctions to zero rather than invent dates or authority.

