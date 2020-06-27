from tkinter import *
from PIL import ImageTk, Image

global i
i = 0#to iterate over images

root = Tk()
root.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("Images/01.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/02.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/03.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/05.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("Images/07.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("Images/08.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img5, my_img7, my_img8]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image = my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forw():
	global my_label
	global i
	my_label.grid_forget()
	i+=1
	if i>5:
		i=0
	my_label = Label(image = image_list[i])
	my_label.grid(row=0, column=0, columnspan=3)
	status = Label(root, text="Image "+str(i+1)+" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def bac():
	global my_label
	global i
	my_label.grid_forget()
	i-=1
	if i<0:
		i=5
	my_label = Label(image = image_list[i])
	my_label.grid(row=0, column=0, columnspan=3)
	status = Label(root, text="Image "+str(i+1)+" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=2, column=0, columnspan=3, sticky=W+E)


btn_for = Button(root, text="→", command=forw)
btn_exit = Button(root, text="Exit Program", command=root.quit)
btn_back = Button(root, text="←", command=bac)

btn_back.grid(row=1, column=0)
btn_exit.grid(row=1, column=1)
btn_for.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=E+W)

root.mainloop()