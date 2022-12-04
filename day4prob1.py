file = open('input.txt').read()
contents=file.split('\n')

elfOne = []
elfTwo = []
elfOneMatrix = []
elfTwoMatrix = []
count = 0

for x in contents:
   for y in x :
      pairs = x.split(",")  

   elfOne=pairs[0]
   elfTwo=pairs[1]

   elfOneRange = elfOne.split('-')
   elfTwoRange = elfTwo.split('-')

   elfOneMatrix=[]
   for i in range ( int(elfOneRange[0]) ,int (elfOneRange[1])+1 ) :
      elfOneMatrix.append(i)
   elfTwoMatrix=[]
   for i in range ( int(elfTwoRange[0]) ,int (elfTwoRange[-1])+1 ) :
      elfTwoMatrix.append(i)

   check = False
   if set(elfOneMatrix).issubset(elfTwoMatrix) or set(elfTwoMatrix).issubset(elfOneMatrix): 
      check = True

   if(check) :
      count +=1

print(count)