# ex1.py
# tkinter : 파이썬에서 윈도우를 담당하는 모듈

from tkinter import *

window = Tk()  # 클래스
window.title('윈도우 창 연습')
window.geometry('400x100') # 창 크기
# window.resizable(width=False, height=FALSE)

label1 = Label(window, text='COOKBOOK~~Python을')
label2 = Label(window, text='열심히', font=('궁서체', 30), fg='blue')
# anchor : 지정한 위치값(NEWS)
label3 = Label(window, text='공부 중입니다.', bg='magenta', width=20, height=5, anchor=CENTER,)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()