import tkinter as tk
from tkinter import ttk

class TempApp():
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('온도변환기-1단계')

        self.cTempText = tk.StringVar()
        self.fTempText = tk.StringVar()

    def buildGUI(self):
        fTempLabel = ttk.Label(self.window, text='화씨')
        fTempLabel.pack()

        fTempEntry = ttk.Entry(self.window, textvariable=self.fTempText)
        fTempEntry.pack()

        cTempLabel = ttk.Label(self.window, text='섭씨')
        cTempLabel.pack()

        cTempEntry = ttk.Entry(self.window, textvariable=self.cTempText)
        cTempEntry.pack()

        fToCBtn = ttk.Button(self.window, text='화 -> 섭', command=self.convertFToC) # make
        fToCBtn.pack()

        cToFBtn = ttk.Button(self.window, text='섭 -> 화', command=self.convertCToF) # make
        cToFBtn.pack()

        resetBtn = ttk.Button(self.window, text='초기화', command=self.resetAll) # make
        resetBtn.pack()

        exitBtn = ttk.Button(self.window, text='종료', command=self.window.destroy)
        exitBtn.pack()

    def convertFToC(self):
        self.cTempText.set(str((float(self.fTempText.get()) - 32 ) / 1.8))
        #(화씨온도 - 32) ÷ 1.8 = 섭씨온도
    
    def convertCToF(self):
        self.fTempText.set(str((float(self.cTempText.get()) * 1.8) + 32))
        # (섭씨온도 × 1.8) + 32 = 화씨온도
    
    def resetAll(self):
        self.cTempText.set('')
        self.fTempText.set('')
    
    def start(self):
        self.buildGUI()
        self.window.mainloop()


# main

newWindow = TempApp()
newWindow.start()
