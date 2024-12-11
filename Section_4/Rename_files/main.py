from pathlib import Path

root_dir = Path('Files')

file_paths = root_dir.iterdir()

# print(list(file_paths))

for path in file_paths:
    # Nate that the path.stem and path.suffix give the name and what the file is in pices
    new_filename = "new-" + path.stem + path.suffix
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)
