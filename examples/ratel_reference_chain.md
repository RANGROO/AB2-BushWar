# Ratel reference chain

Real excerpts from the shipped snapshot. These IDs belong to Bush War; allocate new IDs for another mod. Excerpts omit required fields and are not a complete loadable skeleton.

## Ground unit 1730
```xml
<string name="name" value="Ratel 20 IFV" />
<string name="vehicle3DModel" value="za_ratel_nutria_test" />
<string name="vehicle3DComm" value="za_ratel_nutria_test_crew" />
<string name="weapon1Type" value="89" />
<string name="weapon1Num" value="1" />
<string name="weapon1Ammo1Type" value="177" />
<string name="weapon1Ammo1NumPerWeapon" value="900" />
<string name="weapon1Ammo2Type" value="178" />
<string name="weapon1Ammo2NumPerWeapon" value="300" />
<string name="weapon2Type" value="19" />
<string name="weapon2Num" value="1" />
<string name="weapon2Ammo1Type" value="17" />
<string name="weapon2Ammo1NumPerWeapon" value="4000" />
```

## Formation 3037
```xml
<section name="3037">
    <string name="name" value="Ratel Infantry Platoon [R4]" />
    <string name="sprite" value="mechgroup1" />
    <string name="type" value="GROUPTYPE_INF_MECH" />
    <string name="isCompany" value="FALSE" />
    <string name="isInfantryHQ" value="FALSE" />
    <string name="isVehicleHQ" value="FALSE" />
    <string name="moraleMod" value="0" />
    <string name="trainingMod" value="0" />
    <string name="comment" value="ZA. Additive weapon-identity gameplay option. Overlapping date windows deliberately avoid instantaneous nationwide R1/R4 replacement. Start/end are selection approximations, not unit issue orders; R1/Bren end1994 retains a reserve option, not proven continued frontline establishment. Eight-man mounted / ten-man foot establishment and three-section foot platoon are proxies. No assigned AT launcher; specialist teams separately available. Proper period SADF uniforms/webgear and manual engine acceptance pending." />
    <string name="unit1Type" value="1730" />
    <string name="unit1Radio" value="TRUE" />
    <string name="unit2Type" value="1730" />
    <string name="unit2Radio" value="TRUE" />
    <string name="unit3Type" value="1730" />
    <string name="unit3Radio" value="TRUE" />
    <string name="unit4Type" value="1730" />
    <string name="unit4Radio" value="TRUE" />
    <string name="unit5Type" value="2003" />
    <string name="unit5Radio" value="FALSE" />
    <string name="unit6Type" value="2003" />
    <string name="unit6Radio" value="FALSE" />
    <string name="unit7Type" value="2003" />
    <string name="unit7Radio" value="FALSE" />
    <string name="unit8Type" value="2003" />
    <string name="unit8Radio" value="FALSE" />
  </section>
```

Nested parent 3025:
```xml
<section name="3025">
    <string name="name" value="Ratel Rifle Company" />
    <string name="sprite" value="mechgroup1" />
    <string name="type" value="GROUPTYPE_INF_MECH" />
    <string name="isParentFormation" value="TRUE" />
    <string name="isCompany" value="TRUE" />
    <string name="isInfantryHQ" value="FALSE" />
    <string name="isVehicleHQ" value="FALSE" />
    <string name="moraleMod" value="0" />
    <string name="trainingMod" value="0" />
    <string name="comment" value="ZA. Formation purchase rework. Group counts not explicitly sourced in docs/SADF_FORMATIONS_REWORK.md remain gameplay approximations, not authenticated period establishments. Existing availability is retained, including June1994-only fixtures; these are not proven service dates. Personnel art, transport assignment and engine acceptance remain pending. No supply/repair/medical mechanics inferred." />
    <string name="formation1Type" value="3010" />
    <string name="formation2Type" value="3037" />
    <string name="formation3Type" value="3037" />
    <string name="formation4Type" value="3037" />
  </section>
```

## Weapon 89
```xml
<string name="name" value="20mm GI-2 Autocannon" />
```

## Weapon 19
```xml
<string name="name" value="7.62mm Coax MG" />
```

Ammunition 177: HEI.
Ammunition 178: APCR.
Ammunition 17: Ball.

## Resource bindings
```xml
<string name="za_ratel_nutria_test_m" value="3d\vehicle\za\ratel_nutria_test.dae" />
<texture name="za_ratel_nutria_test_ds" file="3d\vehicle\za\ratel_nutria_test_ds.png" />
<texture name="za_ratel_nutria_test_dw" file="3d\vehicle\za\ratel_nutria_test_ds.png" />
<texture name="za_ratel_nutria_test_dd" file="3d\vehicle\za\ratel_nutria_test_ds.png" />
<texture name="za_ratel_nutria_test_ns" file="3d\vehicle\za\ratel_nutria_test_n.png" />
<texture name="za_ratel_nutria_test_nw" file="3d\vehicle\za\ratel_nutria_test_n.png" />
<texture name="za_ratel_nutria_test_nd" file="3d\vehicle\za\ratel_nutria_test_n.png" />
<texture name="za_ratel_nutria_test_ss" file="3d\vehicle\za\ratel_nutria_test_s.png" />
<texture name="za_ratel_nutria_test_sw" file="3d\vehicle\za\ratel_nutria_test_s.png" />
<texture name="za_ratel_nutria_test_sd" file="3d\vehicle\za\ratel_nutria_test_s.png" />
```

Inspect complete records and date selectors before adapting these excerpts. See [layout and resources](../docs/MOD_LAYOUT_AND_RESOURCES.md).