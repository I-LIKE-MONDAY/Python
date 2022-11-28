# ex2.py
from tkinter import *

window = Tk()

photo1 = PhotoImage(file='GIF/dog2.gif') # 클래스. 대문자로 시작되는것은 모두 클래스
photo2 = PhotoImage(file='GIF/dog3.gif')

label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)

label1.pack()
label2.pack()

window.mainloop()