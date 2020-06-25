from tkinter import *
import math

root = Tk()
root.configure(bg="#141414")

e = Entry(root, width=23, borderwidth=1, font=("Helvetica",24), bg="#d9d9d9")
e.grid(row=0, column=0, columnspan=4, padx=0, pady=2)

def btn_click(num):
	cur = e.get()
	e.delete(0, END)
	e.insert(0, str(cur)+str(num))

def btnadd():
	global fnum
	fnum=e.get()
	e.delete(0, END)
	global math
	math="add"

def btnsub():
	global fnum
	fnum=e.get()
	e.delete(0, END)
	global math
	math="sub"

def btnmul():
	global fnum
	fnum=e.get()
	e.delete(0, END)
	global math
	math="mul"

def btndiv():
	global fnum
	fnum=e.get()
	e.delete(0, END)
	global math
	math="div"

def btnsqrt():
	global fnum
	fnum = int(e.get())
	e.delete(0, END)
	e.insert(0, math.sqrt(int(fnum)))

def btnbck():
	st = str(e.get())
	st = st[:-1]
	e.delete(0, END)
	e.insert(0, st)

def btneql():
	s_num=e.get()
	e.delete(0, END)
	if (math=="add"):
		e.insert(0, int(fnum)+int(s_num))
	if math=="sub":
		e.insert(0, int(fnum)-int(s_num))
	if math=="mul":
		e.insert(0, int(fnum)*int(s_num))
	if math=="div":
		e.insert(0, int(fnum)/int(s_num))

def btnclr():
	e.delete(0, END)

def btndot():
	pass

btn1 = Button(root, text="1", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(1))
btn2 = Button(root, text="2", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(2))
btn3 = Button(root, text="3", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(3))
btn4 = Button(root, text="4", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(4))
btn5 = Button(root, text="5", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(5))
btn6 = Button(root, text="6", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(6))
btn7 = Button(root, text="7", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(7))
btn8 = Button(root, text="8", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(8))
btn9 = Button(root, text="9", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(9))
btn0 = Button(root, text="0", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=lambda: btn_click(0))
btn_add = Button(root, text="+", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=btnadd)
btn_sub = Button(root, text="-", bg="#000000", fg="#ffffff", padx=42, pady=10, font=("Helvetica", 12), command=btnsub)
btn_mul = Button(root, text="*", bg="#000000", fg="#ffffff", padx=42, pady=10, font=("Helvetica", 12), command=btnmul)
btn_div = Button(root, text="/", bg="#000000", fg="#ffffff", padx=42, pady=10, font=("Helvetica", 12), command=btndiv)
btn_eql = Button(root, text="=", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=btneql)
btn_sqrt = Button(root, text="√", bg="#000000", fg="#ffffff", padx=40, pady=10, font=("Helvetica", 12), command=btnsqrt)
btn_bck = Button(root, text="←", bg="#000000", fg="#ffffff", padx=36, pady=10, font=("Helvetica", 12), command=btnbck)
btn_dot = Button(root, text=".", bg="#000000", fg="#ffffff", padx=42, pady=10, font=("Helvetica", 12), command=btndot)
btn_clr = Button(root, text="Clear", bg="#000000", fg="#ffffff", padx=80, pady=10, font=("Helvetica", 12), command=btnclr)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn_add.grid(row=1, column=3)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn_sub.grid(row=2, column=3)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn_mul.grid(row=3, column=3)

btn0.grid(row=4, column=0, columnspan=1)
btn_div.grid(row=4, column=1, columnspan=1)
btn_sqrt.grid(row=4, column=2, columnspan=1)
btn_bck.grid(row=4, column=3, columnspan=1)

btn_dot.grid(row=5, column=0)
btn_eql.grid(row=5, column=1)
btn_clr.grid(row=5, column=2, columnspan=2)

root.mainloop()