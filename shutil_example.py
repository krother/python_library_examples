"""
we have some JSON files in a folder. We want to ...
  OK - check the number of lines in each file
  OK - move the files to a different folder
  OK - copy the files to a third folder
  - delete a file
  - check their size
"""
import json
import os
import random
import shutil

print(f"\nI am in the folder {os.getcwd()}\n")

for name in ["deployment", "manifest", "application", "configuration"]:
    filename = name + "_config.json"
    content = {
        "software_version": random.randint(1, 100),
        "client_id": random.choice(["AAA", "BBB", "CCC"]),
        "container_id": str(random.random()),
        "module_list": [
            random.choice(list("abcdefghijk")) for i in range(10)
        ]
    }
    with open(filename, "w") as file:
        json.dump(content, file)


# create a directory
if not os.path.exists("backup"):
    os.mkdir("backup")

if not os.path.exists("storage"):
    os.mkdir("storage")

# loop through all files in a folder
filenames = os.listdir(".")
filenames = [fn for fn in filenames if ".json" in fn]
for fn in filenames:
    # read the file
    # check the number of lines in each file
    with open(fn, "r") as file:
        lines = file.readlines()
        print(f"{fn} has {len(lines)} lines.")

    # copy the files to backup
    shutil.copy(fn, "backup")

    if os.path.exists(f"storage/{fn}"):
        os.remove(f"storage/{fn}")

    # move files away
    shutil.move(fn, "storage")
