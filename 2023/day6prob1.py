file = open('input.txt').read()
contents=file.split('\n\n')

for x in contents:
   y = x.split('\n')
tempTime = y[0].split(':')[1].split(' ')
times = ' '.join(tempTime).split()
tempDistance = y[1].split(':')[1].split(' ')
distances = ' '.join(tempDistance).split()

finalProduct =1
for iterator in range(0, len(times)):
   numberOfWaysOfWinning =0

   for seconds in range(0,int(times[iterator])+1):
      distanceTravelled = 0
      timeTravelled = 0
      if seconds==0 or seconds== int(times[iterator]):
         distanceTravelled = 0
      else:
         timeTravelled = int(times[iterator])-seconds
         distanceTravelled = seconds*timeTravelled
      if(distanceTravelled>int(distances[iterator])):
         numberOfWaysOfWinning +=1
   finalProduct *=numberOfWaysOfWinning
print('numberOfWaysOfWinning: ',finalProduct)