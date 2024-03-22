import tkinter as tk
from tkinter import ttk

def main():
    app = tk.Tk()
    app.title("Pip")
    
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 24))
    
    label = ttk.Label(app, text="Thanks for installing!", style="TLabel")
    label.pack(padx=20, pady=20)
    
    app.mainloop()

if __name__ == "__main__":
    main()
