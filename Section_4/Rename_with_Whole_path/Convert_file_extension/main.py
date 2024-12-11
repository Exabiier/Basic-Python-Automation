from pathlib import Path

root_dir = Path('files')

for path in root_dir.rglob("*.csv"):
  if path.is_file():
    new_filepath = path.with_suffix(".txt")
    path.rename(new_filepath)

# NOTE: that the rglob() method will give you all the files in the directory and all the subdirectories so any .csv file will be renamed to .txt. We this with path.with_suffix() method this method will replace the old file extension with the new file extension

