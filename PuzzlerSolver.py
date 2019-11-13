##designed to solve a riddle involving animals parts being in a country name

from array import * 
import time 
import random 
import os 


countryList = open('countries.txt','r').read().lower().splitlines() 
animalList = open('animalparts.txt','r').read().lower().splitlines() 
humanList = open('humanparts.txt','r').read().lower().splitlines() ##[:-1]

results = [];
finalResults = [];


def findOccurrences(s, ch):
  ls = [i for i, letter in enumerate(s) if letter == ch]
  ls.insert(0, ch)
  return ls
  
def searchDupList(dup,char): ##only for indexing Duplicates List
  for set in dup:
    if char in set:
      return True;
  return False;
def remove_char(str, n):
  first_part = str[:n] 
  last_part = str[n+1:]
  return first_part + last_part

for country in (countryList):## for every country 
  print "--------------------------"
  print "COUNTRY: " + country 
  print "--------------------------"
  for human in (humanList): ## for every animal part' 
    ##print "---human Part: " + human 
    wordCheck = ''
    humanLetterSpot = 0
    countryLetterSpot = 0
  
    for countryLetter in country:
      if humanLetterSpot < len(human):
        if human[humanLetterSpot] == countryLetter:
          wordCheck = wordCheck + human[humanLetterSpot]
          humanLetterSpot +=1;
    #### Start analysing ####
    if len(wordCheck)>0:
      
      ###########check repeats##########
      ##duplicateCharacters = []
      ##for humanLetter in human:
        ##if ((country.count(humanLetter)>1) and searchDupList(duplicateCharacters, humanLetter)==False):
          ##duplicateCharacters.append(findOccurrences(country, humanLetter))
          
        
      ##print human + ' ' + str(duplicateCharacters)
      ###################################
      ##for i in range (len(duplicateCharacters)+1):
      humanLetterSpot = 0
      if wordCheck==human:
        newName = '' 
        for countryLetter in country:
          removeLetter = False
          if humanLetterSpot < len(human):
              if human[humanLetterSpot] == countryLetter:
                removeLetter = True
                humanLetterSpot +=1;
              if removeLetter == False:
                newName = newName + countryLetter
              
      results.append(newName)
        
print(results)

for animal in animalList:
  for result in results:
    print animal + ' : ' + result
    if animal == result:
      finalResults.append(result)
      
print"FINAL RESULTS: " + str(finalResults)

      ##print "---human Part: " + human 
      ##print("------"+ wordCheck)
          
        
      
