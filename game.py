# tkinter is a framework used to create GUI elements
from tkinter import *       

#create a window
root = Tk()                 
root.geometry("350x550")        #size of the window
root.title("Tic-Tac-Toe")       #title of the window

#frame1 to create the title
frame1=Frame(root)
frame1.pack()
titleLabel=Label(frame1, text="Tic Tac Toe",font=("Arial",30),bg="violet")
titleLabel.pack()
#frame2 to create 9 grids
frame2=Frame(root)
frame2.pack()

#dictionary to compare one square with another
board={1:" ",2:" ",3:" ",
      4:" ",5:" ",6:" ",
      7:" ",8:" ",9:" "}

# to check if any player has won or not
def checkForWin(player):
  #rows
  if board[1]==board[2]==board[3] and board[3]==player :
    return True
  elif board[4]==board[5]==board[6] and board[6]==player :
    return True
  elif board[7]==board[8]==board[9] and board[9]==player :
    return True
  
  #columns
  elif board[1]==board[4]==board[7] and board[7]==player :
    return True
  elif board[2]==board[5]==board[8] and board[8]==player :
    return True
  elif board[3]==board[6]==board[9] and board[9]==player :
    return True
  
  #diagnols
  elif board[1]==board[5]==board[9] and board[9]==player :
    return True
  elif board[3]==board[5]==board[7] and board[7]==player :
    return True
  
  return False

# to check if the game is draw
def checkForDraw():
  for i in board.keys():
    if board[i] ==" " :
      return False
  return True

# to restart the game
def restartGame() :
  winningLabel = Label(frame2,text="                              ",font=("Arial",25))
  winningLabel.grid(row=3,column=0, columnspan=3)
  global end_game
  end_game=False
  for button in buttons :
    button['text'] = " "
  
  for i in board.keys() :
    board[i]=" " 

#function to play the game
turn = "X" 
end_game=False

def play(event):
  global turn
  global end_game
  if end_game:
    return
  button = event.widget
  buttonText=str(button)
  clicked=buttonText[-1]
  if clicked == "n" :
    clicked = 1
  else :
    clicked = int(clicked)
    
  if button["text"]==" ":
    if turn == "X":
      button["text"] = "X"
      board[clicked]=turn
      # to check after every move    
      if checkForWin(turn) :
        winningLabel = Label(frame2,text=f"{turn} wins the game",bg="orange",font=("Arial",25))
        winningLabel.grid(row=3,column=0, columnspan=3)
        end_game=True
      turn = "O"

    else:
      button["text"] = "O"
      board[clicked]=turn
      # to check after every move    
      if checkForWin(turn) :
        winningLabel = Label(frame2,text=f"{turn} wins the game",bg="orange",font=("Arial",25))
        winningLabel.grid(row=3,column=0, columnspan=3)
        end_game=True
      turn = "X"
      
    if checkForDraw() :
      drawLabel = Label(frame2,text="    Game Draw    ",bg="orange",font=("Arial",25))
      drawLabel.grid(row=3,column=0, columnspan=3)
  
 
  

#buttons for each grid
b1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b1.grid(row=0,column=0)
b1.bind("<Button-1>",play)

b2=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b2.grid(row=0,column=1)
b2.bind("<Button-1>",play)

b3=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b3.grid(row=0,column=2)
b3.bind("<Button-1>",play)

b4=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b4.grid(row=1,column=0)
b4.bind("<Button-1>",play)
                                      
b5=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b5.grid(row=1,column=1)
b5.bind("<Button-1>",play)
                                      
b6=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b6.grid(row=1,column=2)
b6.bind("<Button-1>",play)
                                      
b7=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b7.grid(row=2,column=0)
b7.bind("<Button-1>",play)
                                      
b8=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b8.grid(row=2,column=1)
b8.bind("<Button-1>",play)
                                      
b9=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="blue",relief=RAISED,borderwidth=4)
b9.grid(row=2,column=2)
b9.bind("<Button-1>",play)
           
# buttons that are eeded to be cleared
buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

# button to restart the game
restartButton = Button(frame2,text="Restart Game",width=12,height=1,font=("Arial",20),bg="green",relief=RAISED,borderwidth=4,command=restartGame)
restartButton.grid(row=4,column=0,columnspan=3)                                    



root.mainloop()                 #inorder to stay on the screen  
