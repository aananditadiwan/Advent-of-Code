file = open('input.txt').read()
contents=file.split('\n\n')

largest = 0
secondLargest =0
thirdLargest=0
sortedCalories = []

for x in contents:
   y = x.split('\n')
   sum =0
   for z in y :
      sum += int(z)     
   sortedCalories.append(sum) 

sortedCalories.sort(reverse = True)
print(sortedCalories[0]+sortedCalories[1]+sortedCalories[2])