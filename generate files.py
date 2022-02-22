# Create list of all files in the current directory
import os

files = os.listdir()
# print(files)

# Add files to Files.md

with open('Files.md', 'w') as f:
    for file in files:
        f.write(file + '\n')

# alt - markdown tree
