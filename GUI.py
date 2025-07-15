
import tkinter as tk
from tkinter import messagebox
import threading
import sys
import os

# path set for importing from parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import start_assistant

def run_assistant():
    try:
        start_assistant()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_start():
    t = threading.Thread(target=run_assistant)
    t.start()

# GUI window
root = tk.Tk()
root.title("Jarvis AI - Desktop Assistant")
root.geometry("400x300")
root.configure(bg="black")

title = tk.Label(root, text="AI Assistant", font=("Helvetica", 24), bg="black", fg="cyan")
title.pack(pady=20)

start_btn = tk.Button(root, text="Start", font=("Helvetica", 16), command=on_start)
start_btn.pack(pady=20)

exit_btn = tk.Button(root, text="Exit", font=("Helvetica", 14), command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()
