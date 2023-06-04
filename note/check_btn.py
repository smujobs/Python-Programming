import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def build_GUI():
    global check
    check = tk.IntVar()
    checkBtn = ttk.Checkbutton(window, text='choose option:', variable=check, command=open_msgbox)

    checkBtn.pack()

def open_msgbox():
    if check.get() == 1:
        messagebox.showinfo('Alert', 'Checked')
    else:
        messagebox.showinfo('Alert', 'Unchecked')

window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry('300x300+30+30')
build_GUI()
window.mainloop()