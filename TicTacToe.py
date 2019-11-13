
   ##Tick Tac Toe##

from collections import Counter
from time import sleep
import random
import os

openSpaces=[]

Grid = [
  0,0,0,
  0,0,0,
  0,0,0
  ]
  
winScenario = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9],
  [1, 5, 9],
  [3, 5, 7],
  ]
    
##RESET##
def reset():
  clear()
  print"reseting..."
  sleep(1)
  count=0
  for a in Grid:
    Grid[count]=0
    count+=1
  clear()
  gameStart()
  
def clear():
    os.system( 'cls' )

def checkWin():
  for a in winScenario:
    if Grid[a[0]-1]==Grid[a[1]-1]==Grid[a[2]-1]==1:
      print(" ")
      print("Player one wins!")
      sleep(3)
      reset()
    elif  Grid[a[0]-1]==Grid[a[1]-1]==Grid[a[2]-1]==2:
      print(" ")
      print("Player two wins!")
      sleep(3)
      reset()
  count=0
  for a in Grid:
    if a > 0:
      count+=1
  if count==9:
    print"Nobody won!  Ha!"
    sleep(3)
    reset()

def displayGrid():  ##Update the Grid
  clear()
  count = 0
  print" "
  print"TIC TAC TOE  "
  print("-------------")
  for spot in (Grid):
    count+=1
    Display = [(count),"X","O"]
    num = spot
    if count == 3 or count == 6 or count == 9: ##If it's the last in a row, start new line
      print("|"  + " " + str((Display[num])) +" " + "| ")
      print("-------------")
    else: 
      print("| "  + str((Display[num])) ),
  checkWin()
    
def getOpenSpaces():
  count=0
  openSpaces=[]
  for a in Grid:
    count+=1
    if a==0:
      openSpaces.append(count)
  return openSpaces
    
def compTurn():  ##Computer players turn
  count = 0
  sleep(.5)
  for a in winScenario:
    count+=1
    
    ####Check if computer can win####
    if Grid[a[0]-1]==Grid[a[1]-1]==2 and Grid[a[2]-1]==0:
      placement = a[2]
      print (placement)
      compPlace(placement)
    
    elif Grid[a[0]-1]==Grid[a[2]-1]==2 and Grid[a[1]-1]==0:
      placement = a[1]
      print (placement)
      compPlace(placement)
    elif Grid[a[1]-1]==Grid[a[2]-1]==2 and Grid[a[0]-1]==0:
      placement = a[0]
      print (placement)
      compPlace(placement)
    
    ####Check if enemy is about to win####
    elif Grid[a[0]-1]==Grid[a[1]-1]==1 and Grid[a[2]-1]==0:
      placement = a[2]
      print (placement)
      compPlace(placement)
      
    elif Grid[a[0]-1]==Grid[a[2]-1]==1 and Grid[a[1]-1]==0:
      placement = a[1]
      print (placement)
      compPlace(placement)
      
    elif Grid[a[1]-1]==Grid[a[2]-1]==1 and Grid[a[0]-1]==0:
      placement = a[0]
      print (placement)
      compPlace(placement)
    
  ##otherwise, choose a random space## 
  ##openSpaces = list(filter(lambda x: x == 0, Grid))
  ##openSpaces = [i for i, x in enumerate(Grid) if x == 0]
  openSpaces = getOpenSpaces()
  placement = random.choice(openSpaces)
  sleep(.5)
  compPlace(placement)


def compPlace(placement):
  Grid[int(placement)-1]=2
  displayGrid()
  print" "
  print("Computer placed circle at " + (str(placement)))
  sleep(1)
  displayGrid()
  turnStart(True,1)
    

def playerturn(player):
  print" "
  print ("It is player "+(str(player)) + "'s turn")
  sleep(0.5)
  placement = input("Where do you want to place a marker?")
  try:
    placementSpot = Grid[int(placement)-1]
    if Grid[int(placement)-1]>0:
      displayGrid()
      print" "
      print"You cannot place there! Pick again"
      sleep(1.5)
      displayGrid()
      playerturn(player)
    else: 
      Grid[int(placement)-1]=int(player)
      displayGrid()
      print" "
      print("Player "+ str(player) + " placed at " + (str(placement)))
      print" "
      sleep(1)
      displayGrid()
  except:
    checkResponse(placement)
    playerturn(player)
  
def turnStart(computerbol, playerStart): ##computerbol is a boolean value that determines if you are playing with a cpu or not
  if playerStart==1 and computerbol==False:
    playerturn(1)
    playerturn(2)
    turnStart(computerbol, playerStart)
    
  elif playerStart==2 and computerbol==False:
    playerturn(2)
    playerturn(1)
    turnStart(computerbol, playerStart)
   
  if computerbol == True:  ##If computer player is selected
    if playerStart==2:
      print" "
      print("It is the computer's turn")
      print" "
      compTurn()
      playerturn(1)
    elif playerStart==1:
      playerturn(1)
      print" "
      print("It is the computer's turn")
      print" "
      compTurn()
      turnStart(computerbol, playerStart)
  
def checkResponse(answer):
  Commands = {"r" : reset,  }
  ##Easter egg respones##
  Responses = {"hello" : "hi", "hi" : "hello"}
  if answer.lower() in Commands:
    Commands[answer]()
  elif answer.lower() in Responses:
    print(Responses[answer])
    sleep(3)
    displayGrid()
  else:
    displayGrid()
    print" "
    print"Invalid input.  Nice try."
    sleep(1.5)
    displayGrid()
    
def gameStart():
  print" "
  print"Tic Tac Toe"
  print" "
  print"In game, type r to reset"
  print" "
  answer = input("Do you want to play with a computer player? Answer Y/N")
  playerStart = random.randint(1,2)  ##Deterine who will start the game
  if answer.lower() in ("y","yes"):
    if playerStart == 2:  
      print("The Computer will start.")
      sleep(1)
    else:
      print("Player 1 will start.")
      sleep(1)
    displayGrid()
    turnStart(True, playerStart)
  elif answer.lower() in ("n","no"):
    clear()
    print("Player "+str(playerStart)+" will start.")
    sleep(1)
    displayGrid()
    turnStart(False, playerStart)
  else:
    clear()
    gameStart()
gameStart()
