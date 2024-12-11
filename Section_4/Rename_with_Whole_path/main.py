from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.glob("**/*")

for path in file_paths:
  if path.is_file():
    parent_folder = path.parts[-2]
    new_filename = parent_folder + '-' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)


# Note: the path.parts gets the part of the path name you want. I makes you file path into a list data type so we are going back two indexs. the path.with_name allows you to take the file name and replace the old file name. but to fully replace it we have to use the rename() method