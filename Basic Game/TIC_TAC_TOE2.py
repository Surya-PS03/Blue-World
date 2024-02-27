#board display code
import numpy as np
board=np.array([["-","-","-"],["-","-","-"],["-","-","-"]])
def display_board(b):
  c=1
  for row in board:
    r="|".join(row)
    print(r)
    if(c<3):
      print("-"*5)
      c=c+1
display_board(board)

#Win condition for the game
def win(Board2):
  for i in range(0,3):
    if(Board2[i][0]==Board2[i][1]==Board2[i][2]=="X"):
      return True
    elif(Board2[i][0]==Board2[i][1]==Board2[i][2]=="O"):
      return True
  for j in range(0,3):
    if(Board2[0][j]==Board2[1][j]==Board2[2][j]=="X"):
      return True
    elif(Board2[0][j]==Board2[1][j]==Board2[2][j]=="O"):
      return True
  if(Board2[0][0]==Board2[1][1]==Board2[2][2]=="X" or Board2[0][0]==Board2[1][1]==Board2[2][2]=="O"):
    return True
  elif(Board2[0][2]==Board2[1][1]==Board2[2][0]=="X" or Board2[0][2]==Board2[1][1]==Board2[2][0]=="O"):
    return True

#In case of draw
def draw(Board1):
  c=0
  if(win(Board1)):
    return False
  for row in Board1:
    for column in row:
      if(column!="-"):
        c+=1
        if(column=="-"):
          return False
  if(c==9):
    print("The game was draw!!!")
    return True

#Player defining and entries
# r denotes row number and c denotes column number
def entry1(R1,C1):
  board[R1-1][C1-1]="X"
def entry2(R2,C2):
  board[R2-1][C2-1]="O"

def game(Board):
  while (win(Board)!= True and draw(Board)!=True):      
    r1=0
    c1=0
    c2=0
    r2=0
    while True:
      r1=int(input("Enter the row no. player1: "))
      c1=int(input("Enter the column no player1: "))
      if(c1<0 and r1<0 and c1>3 and r1>3 and Board[r1][c1]=="0"):
        continue
      else:
        entry1(r1,c1)
        display_board(board)
        if(win(Board)==True):
          print("PLAYER 1 WON!!!")
        break
    if(win(Board)==True):
      break
    if(draw(Board)==True):
      break
    while True:
      r2=int(input("Enter the row no player2: "))
      c2=int(input("Enter the coloumn no player2: "))
      if(c2<0 and r2<0 and c2>3 and r2>3 and Board[r2][c2]):
        continue
      else:
        entry2(r2,c2)
        display_board(board)
        if(win(Board)==True):
          print("PLAYER 2 WON!!!")
        break
    if(draw(Board)==True):
      break
game(board)      

