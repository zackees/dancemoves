import os

files = os.listdir()
# sort files
files.sort()
# filter out all non jpg
files = [f for f in files if f.endswith('.jpg')]

# print out all files
for f in files:
    print(f)

for i, f in enumerate(files):
    # split file name without extension
    name = f.split('.')[0]
    # cast to a number
    name = int(name)
    # write out file with leading zeros
    # rename file
    os.rename(f, f'{name:03d}.jpg')
