from tkinter import *
from tkinter import ttk
from ctypes import windll

def show_text(*args):
    lbl_title_show_var.set('header: ' + str(entry_title.get()))

def clear_all():
    entry_title.delete(0, END)
    lbl_title_show_var.set('header: ')
    main_text.delete(1.0, END)

root = Tk()
root.title('GUI Py')
root.geometry('500x450+400+400')
windll.shcore.SetProcessDpiAwareness(1)
root.tk.call('tk', 'scaling', 2)
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



ttk.Label(mainframe, text='Title:').grid(column=1, row=1, sticky=W)

entry_title = ttk.Entry(mainframe, width=15, textvariable=StringVar())
entry_title.grid(column=1, row=2, sticky=W)
entry_title.focus()

lbl_title_show_var = StringVar()
lbl_title_show_var.set('')
lbl_title_show = ttk.Label(mainframe, textvariable=lbl_title_show_var)
lbl_title_show.grid(column=1, row=3, sticky=W)

main_text = Text(mainframe, width=25, height=10)
main_text.grid(column=1, row=4, sticky=W)
scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=main_text.yview)
scrollbar.grid(column=2, row=4, sticky=(N,S))
main_text['yscrollcommand'] = scrollbar.set


ttk.Button(mainframe, text='Show text', command=show_text).grid(column=1, row=5, sticky=W)
root.bind("<Return>", show_text)

ttk.Button(mainframe, text='Clear', command=clear_all).grid(column=1, row=6, sticky=W)

root.mainloop()