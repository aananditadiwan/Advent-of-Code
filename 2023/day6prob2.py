file = open('input.txt').read()
contents=file.split('\n\n')
emptyStr=''
for x in contents:
   y = x.split('\n')

tempTime = list(y[0].split(':')[1])
tempTime = ''.join(tempTime).split()
times = int(emptyStr.join(tempTime))

tempDistance = y[1].split(':')[1]
tempDistance = ''.join(tempDistance).split()
distances = int(emptyStr.join(tempDistance))

finalProduct =1
numberOfWaysOfWinning =0

for seconds in range(0,times+1):
   distanceTravelled = 0
   timeTravelled = 0
   if seconds==0 or seconds== times:
      distanceTravelled = 0
   else:
      timeTravelled = times-seconds
      distanceTravelled = seconds*timeTravelled
   if(distanceTravelled>distances):
      numberOfWaysOfWinning +=1
finalProduct *=numberOfWaysOfWinning
print('numberOfWaysOfWinning: ',finalProduct)