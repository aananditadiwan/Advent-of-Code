import numpy as np

file = open('input.txt').read()
contents=file.split('\n')

upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower = []
for x in upper :
   lower.append(x.lower())

firstHalf = []
secondHalf = []
intersectArray = []
sum = 0

for x in contents:
   half= len(x)/2
   firstHalf=[]
   secondHalf=[]
   for y in range (0,int(half)) :
      firstHalf.append(x[y])
   for y in range (int(half),int(len(x))) :
      secondHalf.append(x[y])

   intersectArray.append(np.intersect1d(firstHalf, secondHalf)[0])

for x in intersectArray :
   if x in upper :
      sum += upper.index(x)+27
   if x in lower :
      sum += lower.index(x)+1
print(sum)