from tkinter import *
from tkinter import ttk
from ctypes import windll

def show_text(*args):
    lbl_title_show_var.set('header: ' + str(entry_title.get()))
    lbl_maintxt_show_var.set('content: ' + str(main_text.get(1.0, END)))

def clear_all():
    entry_title.delete(0, END)
    lbl_title_show_var.set('')
    lbl_maintxt_show_var.set('')
    main_text.delete(1.0, END)

root = Tk()
root.title('GUI Py')
root.geometry('500x450+400+400')
windll.shcore.SetProcessDpiAwareness(1)
root.tk.call('tk', 'scaling', 2)
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=3, pady=3)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Title:').grid(column=1, row=1, sticky=W)

entry_title = ttk.Entry(mainframe, textvariable=StringVar())
entry_title.grid(column=1, row=2, sticky=(E, W))
entry_title.focus()

lf_title = ttk.Labelframe(mainframe, text='header:')
lf_title.grid(column=3, row=2, sticky=(W, N))
lbl_title_show_var = StringVar()
lbl_title_show_var.set('')
lbl_title_show = ttk.Label(lf_title, textvariable=lbl_title_show_var)
lbl_title_show.grid(sticky=(W, N, S, E))

ttk.Label(mainframe, text='Main content:').grid(column=1, row=1, sticky=W)

main_text = Text(mainframe, width=40, height=10)
main_text.grid(column=1, row=4, sticky=(W, N, E))
scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=main_text.yview)
scrollbar.grid(column=2, row=4, sticky=(N, S, W))
main_text['yscrollcommand'] = scrollbar.set

lf_maintxt = ttk.Labelframe(mainframe, text='content:')
lf_maintxt.grid(column=3, row=4, sticky=(W, N, E), rowspan=5)
lbl_maintxt_show_var = StringVar()
lbl_maintxt_show_var.set('')
lbl_maintxt_show = ttk.Label(lf_maintxt, textvariable=lbl_maintxt_show_var)
lbl_maintxt_show.grid(sticky=(W, N, S, E))

btn_show_text = ttk.Button(mainframe, text='Show text', command=show_text)
btn_show_text.grid(column=1, row=5, sticky=W)

btn_clear = ttk.Button(mainframe, text='Clear', command=clear_all)
btn_clear.grid(column=1, row=6, sticky=W)
# temp2
root.mainloop()