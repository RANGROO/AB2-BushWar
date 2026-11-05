"""Verify the portable payload without installing files or launching the game."""
from pathlib import Path
import argparse
import contextlib
import hashlib
import io
import json
import re
import xml.etree.ElementTree as E

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def safe_relative(value):
    """Reject manifest paths that escape their declared source/destination root."""
    assert isinstance(value, str) and value and '\\' not in value and ':' not in value
    path = Path(value)
    assert not path.is_absolute() and path.as_posix() == value
    assert all(part not in ('', '.', '..') and part == part.rstrip(' .') for part in value.split('/'))
    return path


def verify_payload(runtime_root=None, game_root=None):
    """Check owned bytes, native date coverage and optional installed destinations."""
    package = ROOT / 'package'
    manifest = json.loads((ROOT / 'deployment/payload-manifest.json').read_text())
    expected = manifest['files']
    assert manifest['payload_files'] == len(expected)
    for relative, value in expected.items():
        safe_relative(relative)
        assert relative.startswith('data/') and re.fullmatch(r'[0-9a-f]{64}', value)
    actual = {p.relative_to(package).as_posix(): digest(p) for p in package.rglob('*') if p.is_file()}
    assert actual == expected, 'Payload differs from the committed ownership manifest'
    factions = E.parse(package / 'data/database/Bush War/factions.xml')
    for guns in factions.findall(".//string[@name='artyGunNum']"):
        assert int(guns.attrib['value']) > 0, 'Artillery points calculation requires a positive gun count'
    sprites = E.parse(package / 'data/database/Bush War/resources_custom.xml').getroot()
    for sprite in sprites.findall('sprite'):
        if sprite.find('image') is not None:
            for transform in ('translation', 'rotation'):
                node = sprite.find(transform)
                assert node is not None and node.get('origin'), ('Incomplete sprite transform', sprite.get('name'), transform)
    assert not any(n.startswith('data/map/') for n in actual), 'Custom maps must remain withdrawn'
    scenarios = [n for n in actual if n.startswith('data/scenario/') and n.endswith('/scenario.xml')]
    assert scenarios == ['data/scenario/user/sadf_1966_1994_all_vehicles/scenario.xml']
    assert actual[scenarios[0]] == '5e7174aa01f00c66290a9c46f402fc99ab5dfd8537130de66ac4575ae9b3dae6'
    if runtime_root is not None:
        assert runtime_root.is_dir(), 'Missing user-data directory'
        for relative, value in expected.items():
            assert digest(runtime_root / relative) == value, ('Runtime mismatch', relative)
    overlay = json.loads((ROOT / 'deployment/aircraft-overlay-manifest.json').read_text())
    assert overlay['count'] == len(overlay['files'])
    targets = set()
    for row in overlay['files']:
        source = safe_relative(row['source'])
        target = safe_relative(row['target_relative_to_game'])
        assert target.as_posix().startswith(('data/graphics/3d/plane/', 'data/graphics/3d/helicopter/'))
        assert target.as_posix() not in targets, 'Duplicate overlay destination'
        targets.add(target.as_posix())
        assert expected.get(source.as_posix()) == row['sha256'] == digest(package / source)
        if runtime_root is not None and game_root is not None:
            assert digest(game_root / target) == row['sha256'], ('Aircraft overlay mismatch', str(target))
    from audit_historical_availability import audit as audit_dates
    dates = audit_dates(package / 'data/database/Bush War/factions.xml')
    assert dates['passed'], dates['errors']
    result = dict(passed=True, payload_files=len(actual), selected_aircraft_files=len(targets),
                  monthly_availability_passed=True, runtime_checked=runtime_root is not None,
                  installed_overlay_checked=runtime_root is not None and game_root is not None,
                  engine_tested=False)
    if game_root is not None:
        import audit_database_loading as native
        native.STOCK = game_root / 'data/database/default'
        assert native.STOCK.is_dir(), 'Game root must contain data/database/default'
        (ROOT / 'dist').mkdir(exist_ok=True)
        with contextlib.redirect_stdout(io.StringIO()):
            report = native.audit(report_path=ROOT / 'dist/database-audit.json')
        assert report['passed'], report['errors'][:10]
        result['database_errors'] = len(report['errors'])
        result['database_warnings'] = len(report['warnings'])
    return result


def main():
    """Write fresh validation output outside the preserved historical receipts."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game-root', type=Path, help='Installed AB2 game; enables native-reference checks')
    parser.add_argument('--runtime-root', type=Path, help='Existing AB2 user-data folder; compare owned files only')
    args = parser.parse_args()
    try:
        result = verify_payload(args.runtime_root, args.game_root)
    except (AssertionError, OSError, ValueError, KeyError) as error:
        parser.exit(1, 'Verification failed: ' + str(error) + '\n')
    (ROOT / 'dist').mkdir(exist_ok=True)
    (ROOT / 'dist/verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
