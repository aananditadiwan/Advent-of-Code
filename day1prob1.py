file = open('input.txt').read()
contents=file.split('\n\n')

largest = 0

for x in contents:
   y = x.split('\n')
   sum =0
   for z in y :
      sum += int(z)
   if (sum > largest) :
      largest = sum
print(largest)

   