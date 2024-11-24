# Install packages
import os, sys, datetime as dt, shutil as sh

if getattr(sys, "frozen", False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.abspath(".")

def get_relative_path(relative_path):
    return os.path.join(bundle_dir, relative_path)

try:
    # Set constants
    year = dt.date.today().year
    template_file = sys.argv[1]
    year_dir = get_relative_path(f"./{year}")

    # 1. Take user input for session cookie value
    cookie = sys.argv[2]

    # Simple check for cookie length & existing directories
    if len(cookie) != 128:
        print("Invalid session cookie - expecting 128 characters.")
        exit()

    if os.path.exists(f"{year_dir}"):
        print("Error: You already have start files for this year.")
        exit()

    # 2. Generate year subdir at root
    os.mkdir(f"{year_dir}")
    print(f"Successfully created {year} directory!")
    print("Creating days 1 to 25...")

    # 3. Generate subdirs within year for days 1-25
    for i in range (1, 26):
        dir_name = f"{year_dir}\\Day {i}"
        file_name = f"{dir_name}\\Day {i}.yxmd"

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
    print("Done!")
except Exception as e:
    print(f"Error: {str(e)}\n")
