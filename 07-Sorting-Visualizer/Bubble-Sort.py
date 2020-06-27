from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Bubble-Sort-Visualizer")
root.maxsize(900, 600)
root.configure(bg='black')

#Variables
alg = StringVar()


def drawData():
	pass


def gen():
	pass


opt = Frame(root, width=600, height=200, bg='grey')
opt.grid(row=0, column=0, padx=10, pady=5)

C = Canvas(root, width=600, bg='white', height=380)
C.grid(row=1, column=0, pady=5, padx=10)


Label(opt, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(opt, textvariable=alg, values=['Bubble Sort','Selection Sort','Merge Sort','Quick Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)
Button(opt, text="Generate Array", command=gen, bg='#c20000', fg='white').grid(row=0, column=2, padx=5, pady=5)

Label(opt, text="Size: ", bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(opt)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(opt, text="Min Value: ", bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(opt)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(opt, text="Max Value: ", bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(opt)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)



root.mainloop()