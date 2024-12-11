import os
from pathlib import Path

# What you can do is use the read_text() method to read the text from a file. and the file from path before
# current_dir = os.path.dirname(__file__)

p1 = Path(__file__).parent / 'abc.txt' 
# print(p1.read_text())

if p1.exists():
    # Read and print the file contents
    print(p1.read_text())
else:
    print("File not found")