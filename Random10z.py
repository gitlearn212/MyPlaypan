import sys
import random
array=[]
# This part of programme will Pick 6 different random numbers between 1-59 
while len(array)!=6:
 temp= random.randrange(1,58)+1
 if temp not in array:
     array.append(temp)
 
#Bubble sort(Ascending order)
for y in range(len(array)-1,0,-1):
  for x in range(y):
   if array[x]> array[x+1]:
       array[x],array[x+1]=array[x+1],array[x]
          
 # Displaying Random numbers in order (working)
print ("Your Lucky Numbers are :")
for v in array:
  print ('(', v,')')
     
