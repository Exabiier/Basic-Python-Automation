from pathlib import Path

root_dir = Path('files')

for path in root_dir.glob("**/*"):
  if path.is_file():
    parent_folder = path.parts
    subfolders = path.parts[1:-1]

    new_filename = "-".join(subfolders) + '-' + path.name
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)

    # Note: In this example we can see that the parts[1: -1] will give you ('file', '2021', 'November, 'd.txt') what this does is allow you take ('2021', 'November) and join them together with a "-".join() method what this do is make the list of 2 into "2021-November"then we also add the path.name at the end. then we use the .with_name() method to replace the old file name with the new file name