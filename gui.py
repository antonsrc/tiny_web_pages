from tkinter import *
from tkinter import ttk, filedialog
from datetime import date
import os

def clear_all():
    entry_title.delete(0, END)
    entry_date.delete(0, END)
    main_text.delete(1.0, END)

def save_as():
    f = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=(("Text files", "*.txt"),("All files", "*.*")),
        initialdir=str(os.getcwd()) + '\source')
    if f == '':
        return
    f = open(str(f), 'w', encoding='utf-8')
    f.write('header: ' + str(entry_title.get()))
    f.write('\n' + 'date: ' + str(entry_date.get()))
    f.write('\n' + 'content: ' + str(main_text.get(1.0, END)))
    f.close()

def set_DPI_for(root_):
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    root.tk.call('tk', 'scaling', 2)

TODAY = str(date.today())

root = Tk()
root.title('GUI Py')
set_DPI_for(root)
mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=3, pady=3)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# title
ttk.Label(mainframe, text='Title:').grid(column=1, row=1, sticky=W)
entry_title = ttk.Entry(mainframe, textvariable=StringVar())
entry_title.grid(column=1, row=2, sticky=(E, W))
entry_title.focus()

# date
ttk.Label(mainframe, text='Date (YYYY-MM-DD):').grid(column=1, row=3, sticky=W)
entry_date = ttk.Entry(mainframe, textvariable=StringVar())
entry_date.insert(0, TODAY)
entry_date.grid(column=1, row=4, sticky=(E, W))

# tags
ttk.Label(mainframe, text='Tags:').grid(column=1, row=5, sticky=W)
# в папку data закинуть файл с тегами
entry_tag = ttk.Entry(mainframe, textvariable=StringVar())
entry_tag.grid(column=1, row=6, sticky=(E, W))

lbl_title_show_var = StringVar()
lbl_title_show_var.set('dfsdfasf')
lbl_title_show = ttk.Label(mainframe, textvariable=lbl_title_show_var)
lbl_title_show.grid(column=3, row=6, sticky=(E, W))

i = 0
def f(*args):
    global i
    i += 1
    print('Enter passed', i)

gg = root.bind("<Return>", f)


# content
ttk.Label(mainframe, text='Main content:').grid(column=1, row=7, sticky=W)
main_text = Text(mainframe, width=40, height=10)
main_text.grid(column=1, row=8, sticky=(W, N, E))
scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=main_text.yview)
scrollbar.grid(column=2, row=8, sticky=(N, S, W))
main_text['yscrollcommand'] = scrollbar.set

btn_clear = ttk.Button(mainframe, text='Clear', command=clear_all)
btn_clear.grid(column=1, row=9, sticky=W)

btn_save = ttk.Button(mainframe, text='Save as...', command=save_as)
btn_save.grid(column=1, row=10, sticky=W)

root.mainloop()

# TODO
# как файлы хранятся в source, так и будут в html

# для каждого тега составляется страница с ссылками на материалы
# навигация по тегам

