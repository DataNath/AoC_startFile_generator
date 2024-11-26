import os, sys, threading, webbrowser, customtkinter as ctk, datetime as dt, shutil as sh

def init_new_thread():
    cookie = enter_cookie.get()
    threading.Thread(target=run_main, args=(cookie,)).start()

if getattr(sys, "frozen", False):
    bundle_dir = sys._MEIPASS
    exe_dir = os.path.dirname(sys.executable)
else:
    bundle_dir = os.path.abspath(".")
    exe_dir = os.path.abspath(".")

def get_relative_path(relative_path):
    return os.path.join(bundle_dir, relative_path)

def return_output(message):
    response.configure(state="normal")
    response.insert(ctk.END, message)
    response.see(ctk.END)
    response.configure(state="disabled")

def run_main(cookie):
    template_path = get_relative_path("template.yxmd")

    if not os.path.exists(template_path):
        return_output("template.yxmd not found\n")

    try:
        # Set constants
        year = str(dt.date.today().year)
        year_dir = os.path.join(exe_dir, year)

        # Simple check for cookie length & existing directories
        if len(cookie) != 128:
            return_output("Invalid session cookie - expecting 128 characters.\n")
            sys.exit()

        if os.path.exists(year_dir):
            return_output("Error: You already have start files for this year.\n")
            sys.exit()

        # 2. Generate year subdir at root
        os.mkdir(year_dir)
        return_output(f"Successfully created {year} directory!\n")
        return_output("Creating days 1 to 25...\n")

        # 3. Generate subdirs within year for days 1-25
        for i in range (1, 26):
            dir_name = f"{year_dir}\\Day {i}"
            file_name = f"{dir_name}\\Day {i}.yxmd"

            os.mkdir(dir_name)
            sh.copy(template_path, file_name)

            with open(file_name, "r+") as file:
                contents = file.read()

                contents = contents.replace("{session_cookie}", f"{cookie}")
                contents = contents.replace("{year}", year)
                contents = contents.replace("{day}", str(i))

                file.seek(0)
                file.write(contents)
                file.truncate()

            return_output(f"Created directory and start file for day {i}.\n")
        return_output("Done!\n")

    except Exception as e:
        response.insert(ctk.END, f"Error: {str(e)}")

def launch_alteryx():
    webbrowser.open_new_tab("https://community.alteryx.com/t5/Alter-Nation/Advent-of-Code-2024/ba-p/1342296")

def launch_github():
    webbrowser.open_new_tab("https://github.com/DataNath/AoC_startFile_generator")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("650x600")
root.resizable(False, False)
root.title("Alteryx Advent of Code start file generator")

bg_colour = "#2b2b2b"

frame = ctk.CTkFrame(master=root, fg_color=bg_colour)
frame.pack(pady=10, padx=10, fill="both", expand=True)

main_label = ctk.CTkLabel(
    master=frame, text="Annual start file generator", font=("Aptos", 30)
)
main_label.pack(pady=12, padx=5)

info_label = ctk.CTkLabel(
    master=frame,
    text="Thanks for checking out this tool!\n\n"
    "If you'd like to look over more information on the Alteryx\n"
    "website, or explore the source code for this app,\n"
    "please use the buttons below. Happy solving!\n\n"
    "- DataNath",
    font=("Aptos", 18),
)
info_label.pack(pady=12, padx=10)

button_frame = ctk.CTkFrame(master=frame, height=30, width=320, fg_color=bg_colour)
button_frame.pack(
    pady=10,
    padx=10,
    anchor="center")

alteryx_button = ctk.CTkButton(
    master=button_frame,
    text="Additional info",
    height=30,
    width=150,
    font=("Aptos", 18),
    command=launch_alteryx
)
alteryx_button.pack(side="left", padx=5)

github_button = ctk.CTkButton(
    master=button_frame,
    text="GitHub repo",
    height=30,
    width=150,
    font=("Aptos", 18),
    command=launch_github
)
github_button.pack(side="right", padx=5)

enter_cookie = ctk.CTkEntry(
    master=frame,
    placeholder_text="Enter session cookie",
    height=30,
    width=310,
    justify="center",
    font=("Aptos", 18),
    show="*",
)
enter_cookie.pack(pady=12, padx=10)

button = ctk.CTkButton(
    master=frame,
    text="Generate",
    height=30,
    width=150,
    font=("Aptos", 18),
    command=init_new_thread,
)
button.pack(pady=12, padx=5)

response = ctk.CTkTextbox(
    master=frame, state="disabled", height=300, width=500, font=("Aptos", 18)
)
response.pack(pady=12, padx=5)

root.mainloop()
