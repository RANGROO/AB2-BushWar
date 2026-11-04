"""Check installed database structure against native field domains and references."""
from pathlib import Path
import collections, hashlib, json, math, re, xml.etree.ElementTree as E

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / 'package/data/database/Bush War'
STOCK = None  # Supplied by verify_mod.py through the explicit --game-root option.

def parse(path):
    """Accept native bare ampersands for analysis without rewriting source XML."""
    return E.fromstring(re.sub(rb'&(?!amp;|lt;|gt;|quot;|apos;|#)', b'&amp;', path.read_bytes()))

def canonical(key):
    # Weapon slots share value domains; a fourth-slot sample is not a separate enum.
    return re.sub(r'\d+', '#', key)

def audit_licence_requirements(tables):
    """Observe native LF dependency consistency without asserting engine entitlement rules."""
    names = ('units.xml', 'formations.xml', 'aircraft.xml', 'flights.xml', 'factions.xml')
    records, flags, counts = {}, {}, {}
    malformed, unsampled, flagged = [], [], []
    for name in names:
        records[name], flags[name] = {}, {}
        counts[name] = collections.Counter()
        for section in tables.get(name, []):
            ident = section.get('name')
            fields = {x.get('name'): x.get('value', '') for x in section if x.tag == 'string'}
            records[name][ident] = fields
            values = [x.get('value', '') for x in section if x.tag == 'string' and x.get('name') == 'LF']
            raw = values[0] if len(values) == 1 else None
            if not values:
                value = 0
                counts[name]['absent'] += 1
            elif len(values) != 1 or not re.fullmatch(r'[0-9]+', raw):
                malformed.append(dict(table=name, id=ident, values=values))
                value = None
                counts[name]['malformed'] += 1
            else:
                value = int(raw)
                counts[name][str(value)] += 1
                if value not in (0, 4):
                    unsampled.append(dict(table=name, id=ident, value=value))
            flags[name][ident] = value
            if value:
                flagged.append(dict(table=name, id=ident, name=fields.get('name'), value=value))
    edges, mismatches, selectors, disabled, invalid_selectors = [], [], [], [], []
    for name, pattern, target in (
        ('formations.xml', r'unit\d+Type', 'units.xml'),
        ('formations.xml', r'formation\d+Type', 'formations.xml'),
        ('flights.xml', r'aircraft\d+Type', 'aircraft.xml'),
    ):
        for ident, fields in records[name].items():
            for key, child in fields.items():
                if not re.fullmatch(pattern, key) or child == '0' or child not in flags[target]:
                    continue
                parent_lf, child_lf = flags[name][ident], flags[target][child]
                uncovered = None if parent_lf is None or child_lf is None else child_lf & ~parent_lf
                edge = dict(table=name, id=ident, field=key, target_table=target, target_id=child,
                            parent_lf=parent_lf, child_lf=child_lf, uncovered_bits=uncovered)
                edges.append(edge)
                if uncovered:
                    mismatches.append(edge)
    for ident, fields in records['factions.xml'].items():
        for key, raw in fields.items():
            match = re.fullmatch(r'(formation|flight)\d+', key)
            if not match:
                continue
            parts = [p.strip() for p in raw.split(',')]
            try:
                if len(parts) != 6:
                    raise ValueError('invalid selector tuple')
                weight = float(parts[5])
                if not math.isfinite(weight) or weight < 0:
                    raise ValueError('invalid selector weight')
            except ValueError:
                invalid_selectors.append(dict(faction=ident, field=key, value=raw))
                continue
            target = 'formations.xml' if match[1] == 'formation' else 'flights.xml'
            child = parts[0]
            parent_lf = flags['factions.xml'][ident]
            child_lf = flags[target].get(child)
            uncovered = None if parent_lf is None or child_lf is None else child_lf & ~parent_lf
            selector = dict(faction=ident, field=key, value=raw, target_table=target, target_id=child,
                            weight=weight, parent_lf=parent_lf, child_lf=child_lf, uncovered_bits=uncovered)
            (disabled if weight == 0 else selectors).append(selector)
    active_mismatches = [x for x in selectors if x['uncovered_bits']]
    return dict(report_only=True, flag_counts=counts, flagged_records=flagged, malformed_flags=malformed,
                unsampled_flags=unsampled, dependency_edges=edges, dependency_mismatches=mismatches,
                positive_weight_selectors=selectors, positive_weight_selector_mismatches=active_mismatches,
                disabled_weight_zero_selectors=disabled, malformed_selectors=invalid_selectors,
                limits='LF=4 is observed on the installed Scandinavia records; absent LF is treated as zero. '
                       'Requirement subset arithmetic is inferred from stock patterns, not a documented engine '
                       'or ownership API. Other flag values are unsampled. This report changes neither audit '
                       'errors/warnings nor passed status, and does not authorize stripping genuine DLC requirements.')

def audit(package_graphics=None,report_path=None,database_graphics_fallback=None):
    """Report hard format/reference defects separately from unproven engine extensions."""
    errors, warnings, hashes, tables = [], [], {}, {}
    for path in DB.glob('*.xml'):
        hashes[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
        tree = parse(path)
        tables[path.name] = tree
        for parent in tree.iter():
            names = [x.get('name') for x in parent if x.get('name') is not None]
            for key, count in collections.Counter(names).items():
                if count > 1:
                    matches = [E.tostring(x) for x in parent if x.get('name') == key]
                    target = warnings if len({v.strip() for v in matches}) == 1 else errors
                    target.append([path.name, parent.get('name'), key, 'duplicate'])
        if not (STOCK / path.name).exists() or path.name.startswith('resources'):
            continue
        native = parse(STOCK / path.name)
        domains = collections.defaultdict(set)
        for x in native.iter('string'):
            domains[canonical(x.get('name', ''))].add(x.get('value', ''))
        sections = native.findall('section')
        required = set.intersection(*[{x.get('name') for x in s} for s in sections]) if sections else set()
        required = {k for k in required if not re.search(r'\d', k)}
        for section in tree.iter('section'):
            fields = {x.get('name'): x.get('value', '') for x in section if x.tag == 'string'}
            # Each populated native formation unit slot requires its own radio boolean.
            if path.name == 'formations.xml':
                for slot, unit in fields.items():
                    match = re.fullmatch(r'unit(\d+)Type', slot)
                    if match and unit != '0':
                        radio = 'unit' + match.group(1) + 'Radio'
                        if radio not in fields:
                            errors.append([path.name, section.get('name'), radio, 'missing radio field for populated unit slot'])
            for key in (required - fields.keys()) if section in list(tree) else []:
                errors.append([path.name, section.get('name'), key, 'missing universal native field'])
            for key, value in fields.items():
                domain = domains.get(canonical(key), set())
                if not domain:
                    warnings.append([path.name, section.get('name'), key, 'field not sampled in stock'])
                elif domain <= {'TRUE', 'FALSE'}:
                    if value not in domain:
                        errors.append([path.name, section.get('name'), key, 'invalid native boolean domain', value])
                elif all(re.fullmatch(r'[A-Z][A-Z0-9_]*', v) for v in domain):
                    if value not in domain:
                        errors.append([path.name, section.get('name'), key, 'invalid native enum', value])
                else:
                    try:
                        numbers = [float(v) for v in domain]
                    except ValueError:
                        numbers = None
                    if numbers is not None:
                        try:
                            assert math.isfinite(float(value))
                        except (ValueError, AssertionError):
                            errors.append([path.name, section.get('name'), key, 'invalid finite number', value])
                if key in ['topArmor', 'hullFrontArmor', 'hullSideArmor', 'hullRearArmor', 'turretFrontArmor', 'turretSideArmor', 'turretRearArmor']:
                    parts = value.split(',')
                    try:
                        assert len(parts) == 4 and parts[3] in {'ARMOR_FACETYPE_NONE', 'ARMOR_FACETYPE_SIMPLE', 'ARMOR_FACETYPE_COMPLEX'}
                        assert all(math.isfinite(float(v)) for v in parts[:3])
                    except (AssertionError, ValueError):
                        errors.append([path.name, section.get('name'), key, 'invalid armour tuple', value])
    ids = {name: {x.get('name') for x in tree.findall('section')} for name, tree in tables.items()}
    resources = set()
    for base in [STOCK, DB]:
        resources.update(x.get('name') for x in parse(base / 'resources_custom_3d.xml'))
    for name, tree in tables.items():
        for section in tree.iter('section'):
            for x in section:
                key, value = x.get('name', ''), x.get('value', '')
                target = None
                if name == 'units.xml' and re.fullmatch(r'weapon\d+Type', key): target = 'weapons.xml'
                if name == 'units.xml' and re.fullmatch(r'weapon\d+Ammo\d+Type', key): target = 'ammunition.xml'
                if name == 'formations.xml' and re.fullmatch(r'unit\d+Type', key): target = 'units.xml'
                if name == 'formations.xml' and re.fullmatch(r'formation\d+Type', key): target = 'formations.xml'
                if name == 'flights.xml' and re.fullmatch(r'aircraft\d+Type', key): target = 'aircraft.xml'
                if name == 'factions.xml' and re.fullmatch(r'formation\d+', key):
                    target, value = 'formations.xml', value.split(',')[0]
                if name == 'factions.xml' and re.fullmatch(r'flight\d+', key):
                    target, value = 'flights.xml', value.split(',')[0]
                if target and value not in ids[target] and value != '0': errors.append([name, section.get('name'), key, 'broken reference', value])
                if name == 'units.xml' and key.startswith('vehicle3D') and value and value not in resources and value + '_m' not in resources:
                    errors.append([name, section.get('name'), key, 'missing 3D binding', value])
                if name == 'aircraft.xml' and key == 'aircraft3DModel' and value and value + '_m' not in resources:
                    errors.append([name, section.get('name'), key, 'missing aircraft binding', value])
    graph = {s.get('name'): [x.get('value') for x in s if re.fullmatch(r'formation\d+Type', x.get('name', ''))]
             for s in tables['formations.xml']}
    visited = set()
    def visit(ident, active):
        """Reject recursive formation cycles while retaining shared child formations."""
        if ident in active:
            errors.append(['formations.xml', ident, 'children', 'recursive formation cycle'])
            return
        if ident in visited:
            return
        for child in graph.get(ident, []):
            visit(child, active | {ident})
        visited.add(ident)
    for ident in graph:
        visit(ident, set())
    native_assets = {x.get('name'): (x.tag, x.get('value'), x.get('file'))
                     for x in parse(STOCK / 'resources_custom_3d.xml')}
    asset_count = 0
    for x in tables['resources_custom_3d.xml']:
        value = x.get('file') if x.tag == 'texture' else x.get('value')
        if not value:
            continue
        asset_count += 1
        if value.lower().endswith(('.png', '.dds', '.jpg', '.jpeg')) and x.tag != 'texture':
            errors.append(['resources_custom_3d.xml', None, x.get('name'), 'image resource must be texture/file, not string/value', value])
        if '\\\\' in value:
            errors.append(['resources_custom_3d.xml', None, x.get('name'), 'noncanonical doubled path separator', value])
        relative = Path(value.replace('\\', '/'))
        roots = [DB / 'graphics', Path(package_graphics) if package_graphics is not None else ROOT / 'package/data/graphics', STOCK.parents[1] / 'graphics']
        # A changed-files candidate can reuse unchanged owned art without a full staging copy.
        if database_graphics_fallback is not None:
            roots.insert(1,Path(database_graphics_fallback))
        is_directory_binding = value.endswith(('\\', '/'))
        if not any((base / relative).is_dir() if is_directory_binding else (base / relative).is_file() for base in roots):
            unchanged_native = native_assets.get(x.get('name')) == (x.tag, x.get('value'), x.get('file'))
            target = warnings if unchanged_native else errors
            target.append(['resources_custom_3d.xml', None, x.get('name'),
                           'unmodified native missing asset' if unchanged_native else 'missing custom asset', value])
    result = dict(passed=not errors, checked_tables=len(tables), three_d_assets_checked=asset_count, source_hashes=hashes,
                  errors=errors, warnings=warnings, engine_load_verified=False,
                  licence_requirements=audit_licence_requirements(tables),
                  database_graphics_fallback=str(database_graphics_fallback) if database_graphics_fallback is not None else None,
                  limits='Native-derived static checks, not an exhaustive engine schema or live database load. Unknown optional fields require engine testing.')
    output=Path(report_path) if report_path is not None else ROOT/'evidence/database-loading-audit.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(passed=not errors, error_count=len(errors), errors=errors[:60], warning_count=len(warnings)), indent=2))
    return result

if __name__ == '__main__':
    raise SystemExit('Use verify_mod.py --game-root <AB2 installation>; this module is a library.')
