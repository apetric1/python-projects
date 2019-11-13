##The birthday paradox, also known as the birthday problem, states that in a random group of 23 people, 
##there is about a 50 percent chance that two people have the same birthday
##this code attempts to prove that

from collections import Counter
from time import sleep
import random
import os

sleep(.25)
babyNum = 23
testResults = []
testRuns = 1000


def runTest():
  babies = []
  for i in range(babyNum):
    baby = random.randint(1,365)
    babies.append(baby)
  
  BabyCount=(Counter(babies))
  
  for key, value in BabyCount.items():
    if (value>1):
      testResults.append(1)
      break
      

for i in range(testRuns):
  runTest()
  
##os.system( 'cls' )
percentResult = ((len(testResults)/testRuns)*100)
print("Of the "+str(testRuns)+" test runs made, "+str(percentResult)+"% had at least 2 people with the same birthday")
