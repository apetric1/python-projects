##A email finder I wrote in highschool. You type in the first and last name of a student, and the code will return their email
##based off how the school wrote email addresses.

###############################

from array import *
import time
sleep=time.sleep
import os

def clear():
    os.system( 'cls' )
    
def displayHistory(history):
  print(" ")
  clear()
  for a in history:
    print a[0]+":",
    print a[1]
  
    
def undo(history):
  ##global history
  history = history[:-1]
  displayHistory(history)
  promptuser(count,history)

  
def reset(history):
  history = []
  displayHistory(history)
  promptuser(count,history)
  
def promptuser(count,history):
  global name
  name = input('Enter a name:')
  ##name = name.replace('\n', ':')
  Commands = {"/r": reset, "/z" : undo}
  if name in Commands:
    history = Commands[name](history)
  elif '\n' in name:
    nameList=name.split('\n')[:-1]
    print(nameList)
    for a in nameList:
      getEmail(history,a)
  else:
    getEmail(history,name)
  displayHistory(history)
  promptuser(count,history)
    
def getEmail(history,name):
  Table = name.split()
  if len(Table)>1:
    Name1 = Table[0]
    Name2 = Table[1]
    email = ''.join([Name2[0:6],Name1[:9-len(Name2)],'@cbhs.edu']).lower()
    ##print 'Here is their email address:', email
    data = []
    data.append(name)
    data.append(email)
    history.append(data)
    ##displayHistory()
    global count
    count+=1

  else:
    clear()
    print'The name you entered is invalid'
    sleep(1)
    displayHistory(history)
    promptuser(count,history)
def start():

  global count
  count = 0
  history=[]
  promptuser(count,history)
start()
