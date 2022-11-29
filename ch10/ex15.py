# ex15

from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry('400x100')

label1 = Label(window, text='입력된 값 : ')
label1.pack()

value = askinteger('숫자놀이', '주사위 숫자(1 ~ 6를 입력하세요', minvalue=1, maxvalue=6)

label1.configure(text=value)

window.mainloop()











window.mainloop()

