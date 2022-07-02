from tkinter import *

CLICKS = 0

def click_button():
    global CLICKS
    CLICKS += 1
    root.title('Clicks {}'.format(CLICKS))
    buttonText.set('Clicks {}'.format(CLICKS))
    btn3.config(bg = '#ff0')

def say_hi():
    print('Hi!')

root = Tk()
root.title('GUI Py')
root.geometry('300x250+400+400')

btn = Button(text = 'Save',
             activebackground = '#001',
             activeforeground = '#f0f',
             bd = 1,
             command = click_button)
btn.pack()

btn2 = Button(text = 'Say Hi in cmd', command = say_hi)
btn2.pack()

buttonText = StringVar()
buttonText.set('Изначальный текст')
btn3 = Button(textvariable = buttonText, command = click_button)
btn3.pack(side = RIGHT)

root.mainloop()