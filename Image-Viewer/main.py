from tkinter import *
from PIL import ImageTk, Image

global i
i = 1#to iterate over images

root = Tk()
root.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("Images/01.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/02.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/03.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/05.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("Images/07.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("Images/08.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img5, my_img7, my_img8]

my_label = Label(image = my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forw():
	global my_label
	global i
	my_label.grid_forget()
	my_label = Label(image = image_list[i])
	my_label.grid(row=0, column=0, columnspan=3)
	i+=1
	if i>5:
		i=0

global flg
flg=True

def bac():
	global my_label
	global i
	global flg
	if i==1 and flg==True:
		i=5
		flg=False
	my_label.grid_forget()
	my_label = Label(image = image_list[i])
	my_label.grid(row=0, column=0, columnspan=3)
	i-=1
	if i<0:
		i=5


btn_for = Button(root, text="→", command=forw)
btn_exit = Button(root, text="Exit Program", command=root.quit)
btn_back = Button(root, text="←", command=bac)

btn_back.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_for.grid(row=1, column=2)

root.mainloop()