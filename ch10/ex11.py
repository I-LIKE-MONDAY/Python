from tkinter import *
from tkinter import messagebox

def clickLeft(event):
  messagebox.showinfo('마우스', '마우스 왼쪽 버튼이 클릭됨')

def clickRight(event):
  messagebox.showinfo('마우스', '마우스 오른쪽 버튼이 클릭됨')

def clickMiddle(event):
  messagebox.showinfo('마우스', '마우스 가운데 버튼이 클릭됨')

window = Tk()

window.bind('<Button-1>', clickLeft)  # Button-1 : 마우스 왼쪽 버튼
window.bind('<Button-2>', clickMiddle)  # Button-2 : 마우스 가운데 버튼
window.bind('<Button-3>', clickRight) # Button-3 : 마우스 오른쪽 버튼

window.mainloop()

