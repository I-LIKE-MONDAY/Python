from tkinter import *

window = Tk()
window.geometry('400x400') # 창 크기
button1 = Button(window, text='파이썬 종료', fg='red', command=quit)

button1.pack()

window.mainloop()