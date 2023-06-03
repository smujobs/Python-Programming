"""
Dictionary Maker. by Jiwon Jeong. Sun Jun 4.
Using Class architecture and Class Inheritance.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle as pkl
import os

class file_management:
    
    def check_file_existence(self) -> bool:
        is_file_exists: bool = os.path.isfile(self.filename)
        return is_file_exists
    
    def write_file(self) -> None:
        with open(self.filename, 'wb') as file:
            pkl.dump(self.container, file)
    
    def read_file(self) -> None:
        with open(self.filename, 'rb') as file:
            self.container = pkl.load(file)

class my_dictionary(file_management):

    def __init__(self, filename : str) -> None:
        self.window = tk.Tk()

        self.filename = filename

        if self.check_file_existence():
            self.read_file()
            messagebox.showinfo('단어장 불러옴', f'단어장 파일 {self.filename}.bin이 존재해 불러왔습니다.')
        else:
            self.container = {}
            messagebox.showinfo('단어장 새로 작성', f'단어장 파일 {self.filename}.bin이 존재하지 않아 종료 시 새로운 파일로 저장됩니다.')
            
        self.word = tk.StringVar()
        self.meaning = tk.StringVar()

        self.window.title('단어장')
        self.__buildGUI()

    def __buildGUI(self):
        self.__create_top_inputs().pack()
        self.__create_middle_inputs().pack()
        self.__create_bottom_btns().pack()
    
    def __create_top_inputs(self):
        top_frame = ttk.Frame(self.window)

        txt_label = ttk.Label(top_frame, text='단어:')
        word_input = ttk.Entry(top_frame, textvariable=self.word)
        search_btn = ttk.Button(top_frame, text='검색', command=self.__search_word)
        append_btn = ttk.Button(top_frame, text='추가', command=self.__append_word)

        txt_label.grid()
        word_input.grid(row=0, column=1)
        search_btn.grid(row=0, column=2)
        append_btn.grid(row=0, column=3)

        return top_frame

    def __create_middle_inputs(self):
        middle_frame = ttk.Frame(self.window)

        txt_label = ttk.Label(middle_frame, text='뜻:')
        meaning_input = ttk.Entry(middle_frame, textvariable=self.meaning)

        txt_label.grid()
        meaning_input.grid(row=0, column=1, columnspan=3)
        
        return middle_frame
    
    def __create_bottom_btns(self):
        bottom_frame = ttk.Frame(self.window)

        reset_btn = ttk.Button(bottom_frame, text='초기화', command=self.__reset_dict)
        exit_btn = ttk.Button(bottom_frame, text='종료', command=self.__exit_program)

        reset_btn.grid()
        exit_btn.grid(row=0, column=1)

        return bottom_frame
    
    def __check_word_existence(self):
        return True if self.word.get() in self.container else False
    
    def __search_word(self):
        if self.__check_word_existence():
            self.meaning.set(self.container[self.word.get()])
        else:
            messagebox.showinfo('경고', f'"{self.word.get()}"라는 단어는 단어장에 없습니다!')
            
    
    def __append_word(self):
        if self.__check_word_existence():
            messagebox.showinfo('경고', f'단어 "{self.word.get()}"가 이미 존재합니다.')
        elif not self.__check_word_existence() and self.meaning.get() == '':
            messagebox.showinfo('경고', '뜻을 입력하지 않았습니다.')
        else:
            self.container[self.word.get()] = self.meaning.get()
            messagebox.showinfo('추가 확인', f'단어 "{self.word.get()}"가 추가되었습니다.')
            self.word.set('')
            self.meaning.set('')

    def __reset_dict(self):
        self.container = {}
        messagebox.showinfo('초기화 완료', '단어장이 초기화 되었습니다.')
        self.word.set('')
        self.meaning.set('')

    def __exit_program(self):
        self.write_file()
        messagebox.showinfo('단어장 종료', f'단어장을 종료합니다.\n단어장은 {self.filename}.bin에 저장되었습니다.')
        self.window.destroy()
            
        
    
new_dict = my_dictionary('My dictionary file')
new_dict.window.mainloop()