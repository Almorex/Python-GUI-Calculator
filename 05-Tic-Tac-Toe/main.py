from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")
w=17
h=4
global i
i=1

status = [-1,-2,-3,-4,-5,-6,-7,-8,-9]

def resetBoard():
	global i
	i=1
	btn1 = Button(root, text="", width=w, height=h, command= lambda: clicked(1))
	btn2 = Button(root, text="", width=w, height=h, command= lambda: clicked(2))
	btn3 = Button(root, text="", width=w, height=h, command= lambda: clicked(3))
	btn4 = Button(root, text="", width=w, height=h, command= lambda: clicked(4))
	btn5 = Button(root, text="", width=w, height=h, command= lambda: clicked(5))
	btn6 = Button(root, text="", width=w, height=h, command= lambda: clicked(6))
	btn7 = Button(root, text="", width=w, height=h, command= lambda: clicked(7))
	btn8 = Button(root, text="", width=w, height=h, command= lambda: clicked(8))
	btn9 = Button(root, text="", width=w, height=h, command= lambda: clicked(9))
	v2=3
	player_1.grid(row=0, column=0, padx=v2, pady=v2)
	player_2.grid(row=1, column=0, padx=v2, pady=v2)
	player_1_name.grid(row=0, column=1, padx=v2, pady=v2)
	player_2_name.grid(row=1, column=1, padx=v2, pady=v2)
	new_game_btn.grid(row=0, column=2, padx=v2, pady=v2)
	ins_game_btn.grid(row=1, column=2, padx=v2, pady=v2)
	btn1.grid(row=2, column=0)
	btn2.grid(row=2, column=1)
	btn3.grid(row=2, column=2)
	btn4.grid(row=3, column=0)
	btn5.grid(row=3, column=1)
	btn6.grid(row=3, column=2)
	btn7.grid(row=4, column=0)
	btn8.grid(row=4, column=1)
	btn9.grid(row=4, column=2)
	j=-1
	for x in range(0,9):
		status[x]=j
		j-=1

def check_win():
	if (status[0]==status[1] and status[1]==status[2]) or (status[3]==status[4] and status[4]==status[5]) or (status[6]==status[7] and status[7]==status[8]) or (status[0]==status[3] and status[3]==status[6]) or (status[1]==status[4] and status[4]==status[7]) or (status[2]==status[5] and status[5]==status[8]) or (status[0]==status[4] and status[4]==status[8]) or (status[2]==status[4] and status[4]==status[6]):
		if int(i)%2==0:
			messagebox.showinfo(" ", "Congratulations!!! " + str(player_1_name.get()) + " won.")
			resetBoard()
		elif int(i)%2==1:
			messagebox.showinfo(" ", "Congratulations!!! " + str(player_2_name.get()) + " won.")
			resetBoard()
	else:
		return

def clicked(n):
	global i
	if n==1:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=2, column=0)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=2, column=0)
			status[n-1]=0
		i+=1
	if n==2:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=2, column=1)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=2, column=1)
			status[n-1]=0
		i+=1
	if n==3:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=2, column=2)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=2, column=2)
			status[n-1]=0
		i+=1
	if n==4:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=3, column=0)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=3, column=0)
			status[n-1]=0
		i+=1
	if n==5:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=3, column=1)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=3, column=1)
			status[n-1]=0
		i+=1
	if n==6:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=3, column=2)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=3, column=2)
			status[n-1]=0
		i+=1
	if n==7:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=4, column=0)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=4, column=0)
			status[n-1]=0
		i+=1
	if n==8:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=4, column=1)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=4, column=1)
			status[n-1]=0
		i+=1
	if n==9:
		if (int(i)%2==1):
			btn1 = Button(root, text="X", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=4, column=2)
			status[n-1]=1
		else:
			btn1 = Button(root, text="O", width=w, height=h, relief=SUNKEN)
			btn1.grid(row=4, column=2)
			status[n-1]=0
		i+=1
	check_win()

def ins():
	messagebox.showinfo("Instructions", "INSTRUCTIONS\n1. The game is played on a grid that's 3 squares by 3 squares.\n2. Player 1 is X, Player 2 is O. Players take turns putting their marks in empty squares.\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")


player_1 = Label(root, text="Player 1", anchor=W, font=("Verdana", 10))
player_2 = Label(root, text="Player 2", anchor=W, font=("Verdana", 10))
player_1_name = Entry(root, text="Name1")
player_2_name = Entry(root, text="Name2")
new_game_btn = Button(root, text="New Game", command=resetBoard)
ins_game_btn = Button(root, text="Instructions", command=ins)
btn1 = Button(root, text="", width=w, height=h, command= lambda: clicked(1))
btn2 = Button(root, text="", width=w, height=h, command= lambda: clicked(2))
btn3 = Button(root, text="", width=w, height=h, command= lambda: clicked(3))
btn4 = Button(root, text="", width=w, height=h, command= lambda: clicked(4))
btn5 = Button(root, text="", width=w, height=h, command= lambda: clicked(5))
btn6 = Button(root, text="", width=w, height=h, command= lambda: clicked(6))
btn7 = Button(root, text="", width=w, height=h, command= lambda: clicked(7))
btn8 = Button(root, text="", width=w, height=h, command= lambda: clicked(8))
btn9 = Button(root, text="", width=w, height=h, command= lambda: clicked(9))

v2=3

player_1.grid(row=0, column=0, padx=v2, pady=v2)
player_2.grid(row=1, column=0, padx=v2, pady=v2)
player_1_name.grid(row=0, column=1, padx=v2, pady=v2)
player_2_name.grid(row=1, column=1, padx=v2, pady=v2)
new_game_btn.grid(row=0, column=2, padx=v2, pady=v2)
ins_game_btn.grid(row=1, column=2, padx=v2, pady=v2)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btn7.grid(row=4, column=0)
btn8.grid(row=4, column=1)
btn9.grid(row=4, column=2)

root.mainloop()