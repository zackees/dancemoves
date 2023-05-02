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
    # rename file
    os.rename(f, f'{i}.jpg')
