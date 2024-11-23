# Install packages
import os
import sys
import datetime as dt
import shutil as sh

# Set constants
year = dt.date.today().year
template_file = 'template.yxmd'

# 1. Take user input for session cookie value
cookie = sys.argv[1]

# Simple check for cookie length
if len(cookie) != 128:
    print("Invalid session cookie - expecting 128 characters.\n")
    exit()

# 2. Generate year subdir at root
os.mkdir(f"{year}")
print(f"Successfully created {year} directory!")
print("Creating days 1 to 25...")

# 3. Generate subdirs within year for days 1-25
for i in range (1, 26):
    dir_name = f"{year}/Day {i}"
    file_name = f"{dir_name}/Day {i}.yxmd"

    os.mkdir(dir_name)
    sh.copy(template_file, file_name)

    with open(file_name, "r+") as file:
        contents = file.read()

        contents = contents.replace("{session_cookie}", f"{cookie}")
        contents = contents.replace("{year}", f"{year}")
        contents = contents.replace("{day}", str(i))

        file.seek(0)
        file.write(contents)
        file.truncate()

    print(f"Created directory and start file for day {i}.")