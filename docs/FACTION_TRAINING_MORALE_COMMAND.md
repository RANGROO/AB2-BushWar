# Faction training, morale and command

This policy covers all eight Bush War factions. It uses native faction date sections and formation modifiers. Numbers are conservative game calibration against vanilla formations, not historical percentages or measurements.

Implementation, deployment and in-game acceptance require their own receipts. This document alone is not deployment evidence. The owner performs game testing.

## National baselines

| Faction | Period | Training | Morale |
|---|---|---:|---:|
| South Africa | Existing 1965–1994 coverage | 75 | 75 |
| Cuba | October 1975–May 1991 | 70 | 70 |
| UNITA / FALA | March 1966–December 1975 | 55 | 65 |
| UNITA / FALA | January 1976–December 1984 | 60 | 65 |
| UNITA / FALA | January 1985–December 1994 | 65 | 65 |
| MPLA / FAPLA / FAA | Existing opening–October 1975 | 55 | 65 |
| MPLA / FAPLA / FAA | November 1975–December 1984 | 60 | 65 |
| MPLA / FAPLA / FAA | January 1985–May 1991 | 65 | 65 |
| MPLA / FAPLA / FAA | June 1991–December 1993 | 60 | 60 |
| MPLA / FAPLA / FAA | January–December 1994 | 65 | 65 |
| Rhodesia | January 1965–December 1979 | 75 | 75 |
| ZANLA | April 1966–December 1979 | 60 | 65 |
| ZIPRA / ZAPU | January 1965–December 1979 | 60 | 65 |
| Mozambique / FRELIMO / FPLM / FADM | January 1965–December 1994 | 60 | 65 |

Existing flag, model and identity cuts remain. Quality changes split those intervals where necessary; they do not extend availability or replace national identities. Unit and formation introduction/withdrawal dates remain unchanged. A quality cohort boundary is not an equipment introduction date.

Mid-1980s Angolan improvements are bounded cohort inferences. The government army's 1991–93 reduction represents disrupted organisation and cohesion; January 1994 is a coarse recovery allocation following documented retraining, not an exact universal readiness date. Training and morale are assessed separately.

## Formation modifiers

These are adjustments to the national baseline, using vanilla fields. All formations outside the listed cohorts retain zero modifiers.

| Faction | Existing cohort | Training modifier | Morale modifier |
|---|---|---:|---:|
| South Africa | Parachute infantry, dedicated HQs and companies | +5 | +10 |
| South Africa | Recce Scout Section, ID 3774 | +10 | +10 |
| South Africa | 32 Battalion Scout Section, ID 3775 | +5 | +5 |
| Rhodesia | RLI/RAR operational formations and Grey's Scouts | +5 | +5 |
| Rhodesia | Rhodesia Regiment territorial formations | −5 | 0 |
| Rhodesia | SAS and Selous Scouts selected specialists | +10 | +10 |
| Rhodesia | Guard Force, including mounted Puma formations | −10 | −5 |
| ZIPRA | Late conventional rifle/armour branch, IDs 5240–5242 and 5260–5263 | +5 | 0 |
| Mozambique | Militia rifle platoon/company, IDs 5438–5439 | −5 | 0 |
| Cuba, UNITA, MPLA/FAPLA and ZANLA | All formations | 0 | 0 |

Exact South African and Rhodesian formation membership is recorded in [the cohort research](../research/faction_quality_v1/sadf_rhodesia.json). Generic scouts, sappers, weapon teams and armoured crews receive no automatic elite bonus. UNITA's existing purchase names do not reliably identify its documented regular/semi-regular/local-defence tiers, so no guessed tier modifiers are added.

Stock authoring gives matching modifiers to a cohort company, its platoons and dedicated HQ. This policy follows that pattern. Shared generic HQs remain neutral where their mixed use prevents one cohort assignment. This is verified native authoring practice; no additive engine inheritance formula is claimed. See the [native modifier audit](../research/faction_quality_v1/native_modifier_policy.md).

## Command settings

| Factions | commandDelay | commandDelayMod | Decision |
|---|---:|---:|---|
| South Africa, Rhodesia | 20 | 20 | Retain existing native pair |
| Cuba, UNITA, MPLA/FAPLA, ZANLA, ZIPRA, Mozambique | 30 | 0 | Retain existing native pair |

The installed manual describes faction, HQ, contact and communications effects but does not document an equation for these two fields. The pair is not translated into a seconds formula. Fireforce, independent patrols or Soviet-style organisation cannot establish exact engine values. Artillery delays and every other off-map setting remain unchanged.

## Evidence and uncertainty

- **South Africa and Rhodesia:** participant accounts support selected reconnaissance personnel and uneven Guard Force training. Service duration alone does not establish combat proficiency. Territorial, parachute and specialist adjustments use restrained vanilla comparisons. [Participant lecture account](https://samilitaryhistory.org/13/c13febne.html), [Guard Force history](https://sites.google.com/site/rhodesianguardforce/home/historic-overview), [national-service chronology archive](https://www.saha.org.za/ecc25/timeline.htm).

- **Cuba:** contemporary US assessments identify an independently operating Cuban combat force and counterinsurgency preparation. This supports a trained regular baseline, without making every unit elite. [1975 assessment](https://history.state.gov/historicaldocuments/frus1969-76v28/d132), [1976 assessment](https://history.state.gov/historicaldocuments/frus1969-76ve11p1/d309).

- **Angolan forces:** the Library of Congress country study distinguishes training institutions and FALA force tiers. Human Rights Watch fieldwork documents demobilisation disruption and subsequent government retraining. Morale accounts conflict; no universal UNITA motivation bonus is inferred. [Country study](https://www.loc.gov/item/90003244/), [1994 field investigation](https://www.hrw.org/reports/archives/africa/ANGOLA94N.htm).

- **ZANLA and ZIPRA:** a contemporary intelligence assessment distinguishes ZIPRA conventional training from ZANLA training/discipline limitations. It remains a foreign intelligence judgement, not a census of individual fighters. The ZIPRA bonus represents trained conventional cohorts, not proven elite combined-arms experience. [September 1977 assessment](https://history.state.gov/historicaldocuments/frus1977-80v16/d168).

- **Mozambique:** the 1965 assessment distinguishes trained cadres from rapidly trained recruits; it cannot describe every fighter across three decades. UN reporting establishes that the 1994 integrated army was still forming and training. The coarse baseline avoids inventing universal improvements. [1965 assessment](https://history.state.gov/historicaldocuments/frus1964-68v24/d432), [UN formation chronology](https://peacekeeping.un.org/sites/default/files/past/onumozFT.htm).

The proposed ZANLA cadre bonus is held: the existing labels alone do not qualify a selected personnel cohort. The proposed Mozambique 1985 reduction is also held: indexed CIA passages suggest problems, but direct source retrieval did not provide adequate full-document qualification. Mozambique therefore retains 60/65 throughout; militia training −5 is explicitly a modest role-based game calibration, not a historical measurement. Its morale remains unchanged.

Research recommendations are inputs, not the final policy. In particular, this policy supersedes the research draft's July 1993 MPLA recovery, optional ZANLA cadre bonus and proposed Mozambique 1985 step. See [Angola/Cuba research](../research/faction_quality_v1/angola_cuba.md), [South Africa/Rhodesia research](../research/faction_quality_v1/sadf_rhodesia.md) and [ZANLA/ZIPRA/Mozambique research](../research/faction_quality_v1/zanla_zipra_mozambique.md).

## Test limits

Offline XML, topology and date checks can prove the intended fields and unchanged availability. Deployment parity can prove installed bytes. Neither establishes actual morale, command response, purchase-cost effects or company/platoon behaviour in a running mission. Owner testing remains pending; use the same date, mission settings and comparable vanilla formations when assessing results.

## Owner check after deployment

1. Compare standalone platoon and company purchases for a listed cohort, using the same date and scenario quality settings.

2. Check Rhodesian RLI/RAR, territorial and Guard Force quality differences in 1979.

3. Check Cuba versus FAPLA in 1979, and the documented Angolan quality cohorts in later dates.

4. Confirm HQ orders, suppression and recovery behave normally. Scenario overrides and battle randomisation can alter displayed values; the database numbers are baselines.

National fields are faction-wide, rather than an infantry-only override. Aircraft quality remains subject to the native faction/scenario system; no separate flight modifier was added.

## Local deployment

Stage `all_faction_quality_v1` is installed locally. Independent parity verified all 2,289 package/ZIP files, 2,286 owned runtime files, changed-file backups and the sole Fort Irwin scenario. Database loading reports zero errors and the same 1,501 warnings as before. All 341 selected national aircraft overlay hashes, 12 stock map definitions and 10 stock database XML files are unchanged. Custom maps remain withdrawn.

Receipts: installation (archived reference: `../evidence/all_faction_quality_v1-installation.json`), full parity (archived reference: `../evidence/all_faction_quality_v1-post-install-parity.json`), protected assets (archived reference: `../evidence/all_faction_quality_v1-protected-parity.json`), independent review (archived reference: `../evidence/all_faction_quality_v1-independent-review.json`), monthly proof (archived reference: `../evidence/all_faction_quality_v1-monthly-proof.json`), [final policy](../research/faction_quality_v1/implementation_policy.json).

No game/editor was launched. Engine behaviour and owner acceptance remain unverified.

