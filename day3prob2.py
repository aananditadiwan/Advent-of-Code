file = open('input.txt').read()
contents=file.split('\n')
 
upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower = []
for x in upper :
   lower.append(x.lower())

firstElf = []
secondElf = []
thirdElf = []
intersectArray = []
sum = 0

totalElements = len(contents)

for x in range (0,totalElements,3) :
   firstElf = contents[x]
   secondElf = contents[x+1]
   thirdElf = contents[x+2]
      
   intersectArray.append( ( set( set(firstElf).intersection(secondElf) ).intersection(thirdElf)) ) 


for x in intersectArray :
   for y in x :                     #Extract string from set
      if y in upper :
         sum += upper.index(y)+27
      if y in lower :
         sum += lower.index(y)+1
print(sum)