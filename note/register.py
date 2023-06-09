import tkinter as tk
from tkinter import ttk

win = tk.Tk()

name = tk.StringVar()
grade = tk.IntVar()
grades = ['1학년', '2학년', '3학년', '4학년']
hobbies = ['영화시청', '음악감상', '사진찍기', '운동']

ifUserWatchMovie = tk.IntVar()
ifUserListenMusic = tk.IntVar()
ifUserTakePhoto = tk.IntVar()
ifUserExercise = tk.IntVar()

userGrade = 0

def buildGUI():

    firstFrame = ttk.Frame(win)
    nameLabel = ttk.Label(firstFrame, text='이름:')
    nameInput = ttk.Entry(firstFrame, textvariable=name)
    nameLabel.grid()
    nameInput.grid(row=0, column=1)
    firstFrame.grid(row=0, column=0, sticky='w')

    secondFrame = ttk.Frame(win)
    gradeLabel = ttk.Label(secondFrame, text='학년:')
    gradeLabel.grid()
    for i in range(4):
        radioBtn = ttk.Radiobutton(secondFrame, text=grades[i], value=i, variable=grade)
        radioBtn.grid(row=0, column=i+1)
    secondFrame.grid(row=1, column=0, sticky='w')

    thirdFrame = ttk.Frame(win)
    hobbyLabel = ttk.Label(thirdFrame, text='취미:')
    hobbyLabel.grid()
    movieCheckBtn = ttk.Checkbutton(thirdFrame, text=hobbies[0], variable=ifUserWatchMovie)
    musicCheckBtn = ttk.Checkbutton(thirdFrame, text=hobbies[1], variable=ifUserListenMusic)
    photoCheckBtn = ttk.Checkbutton(thirdFrame, text=hobbies[2], variable=ifUserTakePhoto)
    exerciseCheckBtn = ttk.Checkbutton(thirdFrame, text=hobbies[3], variable=ifUserExercise)
    movieCheckBtn.grid(row=0, column=1)
    musicCheckBtn.grid(row=0, column=2)
    photoCheckBtn.grid(row=0, column=3)
    exerciseCheckBtn.grid(row=0, column=4)
    thirdFrame.grid(row=2, column=0, sticky='w')

    fourthFrame = ttk.Frame(win)
    printBtn = ttk.Button(fourthFrame, text='입력', command=printInfo)
    exitBtn = ttk.Button(fourthFrame, text='종료', command=win.destroy)
    printBtn.grid()
    exitBtn.grid(row=0, column=1)
    fourthFrame.grid(row=3, column=0, sticky='e')
    

def printInfo():
    print(name.get())
    userGrade = grade.get()
    print(userGrade + 1)
    if ifUserWatchMovie.get() == 1:
        print(hobbies[0])
    if ifUserListenMusic.get() == 1:
        print(hobbies[1])
    if ifUserTakePhoto.get() == 1:
        print(hobbies[2])
    if ifUserExercise.get() == 1:
        print(hobbies[3])
    
    
win.title('회원가입 서비스')
buildGUI()
win.mainloop()
