'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
'''

'''
Samantha Bennefield
11/17/16
Mr. Davis
Pig
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

root = Tk()
root.title("Pig")
root.minsize(300, 300)
mainframe = ttk.Frame(root, borderwidth=5, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=3)
mainframe.columnconfigure(1, weight=3)
mainframe.columnconfigure(2, weight=3)
mainframe.columnconfigure(3, weight=3)
mainframe.columnconfigure(4, weight=3)
mainframe.columnconfigure(5, weight=3)

mainframe.rowconfigure(0, weight=3)
mainframe.rowconfigure(1, weight=3)
mainframe.rowconfigure(2, weight=3)
mainframe.rowconfigure(3, weight=3)
mainframe.rowconfigure(4, weight=3)
mainframe.rowconfigure(5, weight=3)
mainframe.rowconfigure(6, weight=3)
mainframe.rowconfigure(7, weight=3)
mainframe.rowconfigure(8, weight=3)
mainframe.rowconfigure(9, weight=3)

global turn #<---Keeps track of who's turn it is
turn=1 #<---Defaults to 1

global p1 #<---Player 1's overall points
p1=0

global p2 #<---Player 2's overall points
p2=0

score = [] #<---List of points earned during the turn

#=====Hold Function=====
def hold():
    global turn
    global p1
    global p2
    
    if turn==1:
        pts=sum(i for i in score) #<---Adds all the gathered points
        p1=p1+pts #<---Adds new points to existing
        p1_score.set(p1)
        p1_turnTotal.set(0)
        player_label.set("Player 2 it's your turn!")
        label.configure(foreground="blue")
        del score[:] #<---Clears the list (score) for the next turn
        turn=2
    elif turn==2:
        pts=sum(i for i in score) #<---Adds all the gathered points
        p2=p2+pts #<---Adds new points to existing
        p2_score.set(p2)
        p2_turnTotal.set(0)
        player_label.set("Player 1 it's your turn!")
        label.configure(foreground="red")
        del score[:] #<---Clears the list (score) for the next turn
        turn=1


#=====Roll Function=====
def roll():
    roll = random.randint(1, 6) #<---The 'dice'

    rolled.set(roll)#<---Change the rolled number
    
    if roll==1: #<---Turn total = 0 and turn changes
        p1_turnTotal.set(0)
        p2_turnTotal.set(0)
        del score[:]
        hold() #<---No points are added. Runs hold just to change the turn.      
    else:
        score.append(roll) #<---Appends all the gathered points unless 1 is rolled
        pts=sum(i for i in score)
    
        if turn==1: #<---Updates the turn total for the current turn
            p1_turnTotal.set(pts)
        elif turn==2:
            p2_turnTotal.set(pts)


#=====Check (before Roll) Function=====
def rollCheck(): #<---Checking to see if either player has hit 100 points
    if p1>=100 or p2>=100:
        player_label.set("Game over!")
        label.configure(foreground="black")
        roll_btn.configure(state='disabled')
        hold_btn.configure(state='disabled')
    else:
        roll()


#=====Check (before Hold) Function=====
def holdCheck(): #<---Checking to see if either player has hit 100 points
    if p1>=100 or p2>=100:
        player_label.set("Game over!")
        roll_btn.configure(state='disabled')
        hold_btn.configure(state='disabled')
    else:
        hold()
    

#=====About Function for Toolbar=====
def about():
    messagebox.showinfo(title="About", message='''Pig (Version  1.0)

Instructions:
Each player repeatedly rolls a die until a 1 is rolled or the player holds.

If the player rolls a 1, the player's turn total is set back to 0 and it becomes the next player's turn.

If the player rolls any number other than 1 it is added to their turn total.

If a player chooses to 'hold', their turn total is added to their score.

First player to score 100 or more points wins.''')   

#=====Toolbar=====
root.option_add('*tearOff', FALSE)

topMenu = Menu(root)
root.config(menu=topMenu)

subMenu = Menu(topMenu)
topMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=quit)

secondMenu = Menu(topMenu)
topMenu.add_cascade(label="Help", menu=secondMenu)
secondMenu.add_cascade(label="About", command=about)


#=====Labels=====
player_label = StringVar()
player_label.set("Player 1 it's your turn!")
label = ttk.Label(mainframe, textvariable=player_label)
label.grid(column=2, row=0, padx=4, pady=4, rowspan=2)
label.configure(foreground="red")

rolled = StringVar() #<---Display the number 'rolled' on the dice
rolled.set(0)
ttk.Label(mainframe, text="Rolled:").grid(column=2, row=4, padx=4, pady=4)
ttk.Label(mainframe, textvariable=rolled).grid(column=2, row=5, padx=4, pady=4)

p1_turnTotal = StringVar() #<---How much is earned until 1 is rolled or hold is pressed
p1_turnTotal.set(0)
p1_score = StringVar() #<---All points earned
p1_score.set(0)

player1 = ttk.Label(mainframe, text="Player 1")
player1.grid(column=0, row=2, padx=4, pady=4)
player1.configure(foreground="red")
ttk.Label(mainframe, text="Turn Total").grid(column=0, row=4, padx=4, pady=4)
ttk.Label(mainframe, textvariable=p1_turnTotal).grid(column=0, row=5, padx=4, pady=4)
ttk.Label(mainframe, text="Score").grid(column=0, row=6, padx=4, pady=4)
ttk.Label(mainframe, textvariable=p1_score).grid(column=0, row=7, padx=4, pady=4)


p2_turnTotal = StringVar() #<---How much is earned until 1 is rolled or hold is pressed
p2_turnTotal.set(0)
p2_score = StringVar() #<---All points earned
p2_score.set(0)

player2 = ttk.Label(mainframe, text="Player 2")
player2.grid(column=4, row=2, padx=4, pady=4)
player2.configure(foreground="blue")
ttk.Label(mainframe, text="Turn Total").grid(column=4, row=4, padx=4, pady=4)
ttk.Label(mainframe, textvariable=p2_turnTotal).grid(column=4, row=5, padx=4, pady=4)
ttk.Label(mainframe, text="Score").grid(column=4, row=6, padx=4, pady=4)
ttk.Label(mainframe, textvariable=p2_score).grid(column=4, row=7, padx=4, pady=4)


#=====Buttons=====
roll_btn = Button(mainframe, text="Roll", command=rollCheck)
roll_btn.grid(column=2, row=8, padx=4, pady=4)

hold_btn = Button(mainframe, text="Hold", command=holdCheck)
hold_btn.grid(column=2, row=9, padx=4, pady=4)



root.mainloop()
