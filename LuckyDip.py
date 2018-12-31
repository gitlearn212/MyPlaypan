#Lotto LuckyDip
import sys
import random
array=[]

# This part of the code will Pick 6 different random numbers between 1-59 

while len(array)!=6:
 temp= random.randrange(1,58)+1
 if temp not in array:
     array.append(temp)
 
#This part of the code will display numbers in Ascending Order (Bubble sort Ascending order)
for y in range(len(array)-1,0,-1):
  for x in range(y):
   if array[x]> array[x+1]:
       array[x],array[x+1]=array[x+1],array[x]
       
## OR USE THE BELOW COMMAND SORT() ==>(array.sort()
# ==> array.sort()          

# This part of the code Displays Random numbers in Ascending order

print ("Your Lucky Numbers are :")
for numbers in array:
  print (numbers)
  ### This is the End of this Lotto LuckyDip Programe ###
     
