file = open('input.txt').read()
contents=file.split('\n\n')

totalSum =0
copyFrequencyDict = {}
for x in contents:
   y = x.split('\n')
   for counter in range(1,len(y)+1):
      copyFrequencyDict[counter] = 1

for x in contents:
   y = x.split('\n')
   for eachElement in y:
      
      gameNumberArray = eachElement.split(':')[0]
      gameNumber = gameNumberArray.split(' ')[-1]
      inputArray = eachElement.split(':')[1]
      print('gameNumber',gameNumber)

      winningSide = inputArray.split('|')[0]
      winningSide = winningSide.split(' ')
      winningSide = ' '.join(winningSide).split()
      print("winningSide : ",winningSide)

      ourSide = inputArray.split('|')[1]
      ourSide = ourSide.split(' ')
      ourSide = ' '.join(ourSide).split()
      print("ourSide : ",ourSide)

      matchesFound = 0
      for eachOurSideElement in ourSide :
         if eachOurSideElement in winningSide :
            matchesFound += 1
      print("matchesFound OfThisGame", matchesFound)  

      for copyOfCard in range(int(gameNumber)+1,matchesFound+int(gameNumber)+1):
         copyFrequencyDict[copyOfCard] += 1
         if(copyFrequencyDict[int(gameNumber)]>1):
            for iterable in range (0, copyFrequencyDict[int(gameNumber)]-1):
               copyFrequencyDict[copyOfCard] += 1
      print('copyFrequencyDict',copyFrequencyDict)
      print('\n')
   for iterable in copyFrequencyDict :
      totalSum += int(copyFrequencyDict[iterable])
print('totalSum', totalSum)