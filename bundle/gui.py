import os, sys, subprocess, threading, customtkinter as ctk

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

    try:
        message = subprocess.run(
            ["python", main_path, template_path, cookie], capture_output=True, text=True
        )
        response.insert(ctk.END, message.stdout)
        response.see(ctk.END)
    except Exception as e:
        response.insert(ctk.END, f"Error: {str(e)}")

    response.configure(state="disabled")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.geometry("750x400")
root.title("Alteryx Advent of Code start file generator")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

label = ctk.CTkLabel(
    master=frame, text="Annual start file generator", font=("Aptos", 26)
)
label.pack(pady=12, padx=5)

enter_cookie = ctk.CTkEntry(
    master=frame,
    placeholder_text="Enter session cookie",
    height=30,
    width=300,
    font=("Aptos", 18),
    show="*",
)
enter_cookie.pack(pady=12, padx=5)

button = ctk.CTkButton(
    master=frame,
    text="Generate",
    height=30,
    width=150,
    font=("Aptos", 18),
    command=init_new_thread,
)
button.pack(pady=12, padx=5)

response = ctk.CTkTextbox(master=frame, state="disabled", height=200, width=500, font=("Aptos", 18))
response.pack(pady=12, padx=5)

root.mainloop()
