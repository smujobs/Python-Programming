import tkinter as tk
from tkinter import ttk

genders = ['male', 'female', 'other']
colors = ['red', 'yellow', 'blue']

def build_GUI():
    text_label = ttk.Label(window, text='Choose Your Gender:')
    text_label.pack()

    global gender
    gender = tk.IntVar()
    for i in range(3):
        radio_btn = ttk.Radiobutton(window, text=genders[i], value=i, variable=gender, command=change_gender)
        radio_btn.pack()

    gender.set(-1) # Reset Button Choice

def change_gender():
    user_choice = gender.get()
    window.configure(background=colors[user_choice])

window = tk.Tk()
window.title('radio btn example')
build_GUI()
window.mainloop()
