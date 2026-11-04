"""Verify the preserved payload and build a local, unpublished installation ZIP."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile
from verify_mod import verify_payload

ROOT = Path(__file__).resolve().parents[1]


def main():
    """Reject payload drift, then verify every generated archive member against its manifest."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist/Bush_War_AB2.zip', help='Local candidate ZIP; never uploaded')
    args = parser.parse_args()
    verify_payload()
    package = ROOT / 'package'
    manifest = json.loads((ROOT / 'deployment/payload-manifest.json').read_text())
    expected = manifest['files']
    actual = {}
    for path in package.rglob('*'):
        if path.is_file():
            with path.open('rb') as stream:
                actual[path.relative_to(package).as_posix()] = hashlib.file_digest(stream, 'sha256').hexdigest()
    assert actual == expected, 'Payload differs from the preserved deployed manifest'
    extras = ['README.md', 'docs/INSTALLATION.md', 'docs/KNOWN_LIMITATIONS.md',
              'deployment/payload-manifest.json', 'deployment/aircraft-overlay-manifest.json']
    sources = {relative: package / relative for relative in expected}
    sources.update({relative: ROOT / relative for relative in extras})
    archive_hashes = dict(expected)
    for relative in extras:
        archive_hashes[relative] = hashlib.sha256(sources[relative].read_bytes()).hexdigest()
    output = args.output.resolve()
    assert output.suffix.lower() == '.zip', 'Output must be a ZIP'
    assert not output.is_relative_to(package.resolve()), 'Output cannot be inside the payload'
    assert not output.is_relative_to((ROOT / 'art').resolve()), 'Output cannot overwrite art sources'
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix('.zip.tmp')
    assert not temporary.exists(), 'Unfinished build exists; inspect it before rebuilding'
    try:
        with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as archive:
            for relative in sorted(sources):
                archive.write(sources[relative], relative)
        with zipfile.ZipFile(temporary) as archive:
            assert archive.testzip() is None
            assert len(archive.namelist()) == len(archive_hashes)
            assert set(archive.namelist()) == set(archive_hashes)
            for relative, digest in archive_hashes.items():
                with archive.open(relative) as stream:
                    assert hashlib.file_digest(stream, 'sha256').hexdigest() == digest, relative
        temporary.replace(output)
    except BaseException:
        if temporary.exists():
            temporary.unlink()
        raise
    with output.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    output.with_suffix('.zip.sha256').write_text(digest + '  ' + output.name + '\n')
    print(json.dumps({'passed': True, 'payload_files': len(expected), 'documentation_and_manifests': len(extras),
                      'archive_members': len(archive_hashes), 'zip': str(output), 'sha256': digest, 'published': False}))


if __name__ == '__main__':
    main()
