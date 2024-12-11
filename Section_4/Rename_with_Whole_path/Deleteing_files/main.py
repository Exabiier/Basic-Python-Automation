from pathlib import Path

root_dir = Path('destination')

for path in root_dir.glob("*.csv"):
    with open(path, 'w') as file:
        file.write(b'')

# Note: that we need to use the .glob() method because the rglob() method will give you all the files in the directory and all the subdirectories to be effected as well