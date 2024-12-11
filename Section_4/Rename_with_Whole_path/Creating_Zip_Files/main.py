from pathlib import Path 
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path('archive.zip')

with zipfile.ZipFile(archive_path, 'w') as zf:
  for path in root_dir.rglob("*.txt"):
    zf.write(path)
    path.unlink()

# Note: that when you are trying to create a path for you zip folder you need to create the path for your zip file first. then you use thezipfile object to put the path and write operations. after that you you can use a for loop to find all the text files and have the with statement to open the and close each folder that will by ziped. 
# then we can use the path.unlink() method to delete that file on your computer

# Also Note:
# this is a longer version of with statement for python
# file = open('example.txt', 'r')
# try:
#     content = file.read()
# finally:
#     file.close()  # Must manually close the file
