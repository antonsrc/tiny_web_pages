from tkinter import *
from ctypes import windll

from setuptools import Command

CLICKS = 0

def click_button():
    global CLICKS
    CLICKS += 1
    root.title('Clicks {}'.format(CLICKS))
    buttonText.set('Clicks {}'.format(CLICKS))
    btn3.config(bg = '#ff0')

def say_hi_and_show_text():
    print('Hi!')
    labelText.set('Если допустить, что жизнь человеческая\n'
                  ' может управляться разумом, – то уничтожится\n'
                  ' возможность жизни. «Война и мир»')

root = Tk()
root.title('GUI Py')
root.geometry('500x450+400+400')

windll.shcore.SetProcessDpiAwareness(1)
root.tk.call('tk', 'scaling', 2)

btn = Button(text = 'Save',
             activebackground = '#001',
             activeforeground = '#f0f',
             bd = 1,
             command = click_button)
btn.pack()

btn2 = Button(text = 'Say Hi in cmd', command = say_hi_and_show_text)
btn2.pack()

buttonText = StringVar()
buttonText.set('Изначальный текст')
btn3 = Button(textvariable = buttonText, command = click_button)
btn3.pack(side = RIGHT)

label1 = Label(text = 'Если искать совершенства,\nто никогда не будешь доволен.\n«Анна Каренина»',
               fg = '#00f')
label1.pack()

labelText = StringVar()
labelText.set('')
label2 = Label(textvariable = labelText)
label2.pack()

root.mainloop()