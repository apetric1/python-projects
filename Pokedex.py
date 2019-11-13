##A command line pokedex I created to sort and store 500+ pokemon my friend from highschool made

from array import *
import time
import random
sleep = time.sleep
import os


print"-----------POKEDEX-----------"
print"Commands: /all, /type, /home, /guess"
print" "

rawList = open('rawList.txt','r').read()

##typeList = ['Grass', 'Fire', 'Water', 'Electric', 'Normal', 'Bug', 'Rock', 'Poison', 'Ghost', 'Steel', 'Undetermined', 'Fighting', 'Ground', 'Psychic', 'Ice', 'Flying', 'Dark', 'Dragon', 'Candy']
pokeList =[]




##The raw list is a text file. We will split it into lists that we can sort through

def clear():
  os.system( 'cls' )
  print"-----------POKEDEX-----------"
  print"Commands: /all, /type, /home, /guess"
  print" "
def reset():
  ##userinput = input("test")
  global pokeList
  pokeList = rawList.split()
  nameList = (pokeList[::2]) ##Get the odd ones in the list, which are the names
  global typeList
  typeList = (pokeList[1::2])##Get the even ones in the list, which are the types

  for i in range(len(typeList)):  ##Remove the parantheses
    typeList[i] = typeList[i].strip('()')
    
  pokeList=[] ##Reset pokelist
  for i in range(len(nameList)):
    table = [] ##Create a temporary list
    table.append(nameList[i])
    table.append(typeList[i])
    
    pokeList.append(table)
  for a in pokeList:
    a[1] = a[1].split("/")
    
  typeList = [x for x in typeList if "/" not in x]
  typeList = list(set(typeList))

  global newTypeList
  newTypeList=[]
  
  for a in typeList: 
    tempList = [a]
    newTypeList.append(tempList)
    
  for a in pokeList:
    for b in newTypeList:
      if b[0] in a[1]:  ##if the type is with the pokemon
        b.append(a[0])
        
  promptuser() 
          

def full():
  clear()
  print" "
  print"loading..."
  count = 0
  sleep(0.001)
  clear()
  for a in pokeList:
    count+=1
    print(str(count)+ ": " + a[0] + ": " + str(a[1]))
    ##print "%s: %s: %s" % (str(count),a[0],str(a[1])) ##Alternative way for future reference
      
      
####GUESSING GAME####      
def guessType():
  clear()
  Selection = random.choice(pokeList)
  
  print" "
  for a in (typeList): ##print choices
    print("["+a+"]"),
    
  print" "
  print" "
  print"(Type /home to go back)"
  print" "
  
  userinput = input("What type do you think "+ (Selection[0]) +" is?")
  if checkCommand(userinput)!=True: ##If it wasn't a command then continue
    if len(Selection[1]) == 2:
      if userinput.lower() == Selection[1][1].lower():
        print "2 types"
        clear()
        print" "
        print"Correct!"
        sleep(1)
        guessType()
        return
    if userinput.lower() == Selection[1][0].lower() :
      clear()
      print" "
      print"Correct!"
      sleep(1)
      guessType()
    else:
      clear()
      print("Incorrect, the answer was "+(Selection[1][0]) +".")
      sleep(1.5)
      clear()
      print" "
      print("Next question")
      sleep(1)
      guessType()
  
  
###Check for a Command###
def checkCommand(string):
  Commands = {"/home": reset, "/type" : type, "/all": full,  "/abc":abc, "/guess":guessType}
  if string in Commands:
    Commands[string]()
    promptuser()
    return(True)
    
def promptuser():
  print" "
  userinput = input("Type a command:")
  if checkCommand(userinput)!=True:
    print"--Not a command."
    promptuser()
    
def abc(): ##Doesn't work right now
  print (pokeList.sort())

###Display Types####
def type():
  ##print"/abc, /type"
  print" "
  for a in (typeList): ##print choices
    print("["+a+"]"),
  print" "
  print" "
  print"(Type '/home' to go back)"
  print" "
  userinput = input("What type would you like to sort by? ")
  
  clear()
  if checkCommand(userinput)!=True: ##If it wasn't a command
    for a in newTypeList:
      if userinput.lower() == a[0].lower():
        print"-----"+str(a[0])+"------"
        for i in range(len(a)):
          if i!=0: ##If it's not the first in the list
            ##sleep(.005)
            print(a[i])
        print"---------------"
        
  type()

def sortType():
  types = []
  for a in pokeList:
    types.append(str(a[1]))
  
def start():
  reset()
  
start()
