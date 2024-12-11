from pathib import Path
import zipfile

root_dir = Path('.')
destination_dir = Path('destination')

for path in root_dir.rglob("*.zip"):
    with zipfile.ZipFile(path) as zf:
        final_path = destination_dir / path.name
        zf.extractall(path=final_path)

# Note: that we are making a new directory to put the unzipped files in. and we al putting all those files in there.
