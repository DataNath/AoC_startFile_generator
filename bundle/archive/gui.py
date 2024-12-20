import os, sys, subprocess, threading, webbrowser, customtkinter as ctk

def init_new_thread():
    cookie = enter_cookie.get()
    threading.Thread(target=run_main, args=(cookie,)).start()

if getattr(sys, "frozen", False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.abspath(".")

def get_relative_path(relative_path):
    return os.path.join(bundle_dir, relative_path)

def run_main(cookie):
    response.configure(state="normal")
    main_path = get_relative_path("main.py")
    template_path = get_relative_path("template.yxmd")

    if not os.path.exists(main_path):
        print("main.py not found")
    if not os.path.exists(template_path):
        print("template.yxmd not found")

    print(f"Main path: {main_path}")
    print(f"Template path: {template_path}")
    print(f"Cookie: {cookie}")

    try:
        message = subprocess.run(
            ["python", main_path, template_path, cookie],
            cwd=bundle_dir,
            capture_output=True,
            text=True,
            #creationflags=subprocess.CREATE_NO_WINDOW,
        )

        print(f"Subprocess STDOUT: {message.stdout}")
        print(f"Subprocess STDERR: {message.stderr}")
        response.insert(ctk.END, message.stdout)
        response.insert(ctk.END, message.stderr)
        response.see(ctk.END)

    except Exception as e:
        response.insert(ctk.END, f"Error: {str(e)}")

    response.configure(state="disabled")

def launch_alteryx():
    webbrowser.open_new_tab("https://community.alteryx.com/t5/Alter-Nation/Advent-of-Code-2024/ba-p/1342296")

def launch_github():
    webbrowser.open_new_tab("https://github.com/DataNath/AoC_startFile_generator")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("650x700")
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
    "If you want to look at the information page on the Alteryx\n"
    "website, or check out the source code for this app,\n"
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
    master=frame, state="disabled", height=400, width=500, font=("Aptos", 18)
)
response.pack(pady=12, padx=5)

root.mainloop()
