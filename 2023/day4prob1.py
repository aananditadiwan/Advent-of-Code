file = open('input.txt').read()
contents=file.split('\n\n')

totalSum =0
for x in contents:
   y = x.split('\n')
   for eachElement in y:
      
      gameNumber = eachElement.split(':')[0]
      inputArray = eachElement.split(':')[1]
      print(gameNumber)

      winningSide = inputArray.split('|')[0]
      winningSide = winningSide.split(' ')
      winningSide = ' '.join(winningSide).split()
      print("winningSide : ",winningSide)

      ourSide = inputArray.split('|')[1]
      ourSide = ourSide.split(' ')
      ourSide = ' '.join(ourSide).split()
      print("ourSide : ",ourSide)

      firstEncounter = False
      iterationProduct = 0
      for eachOurSideElement in ourSide :
         if eachOurSideElement in winningSide :
            if not firstEncounter:
               firstEncounter = True
               iterationProduct = 1
            else :
               iterationProduct *= 2
      print("sumOfThisGame", iterationProduct)  
      totalSum += iterationProduct
      print('\n')
print("total = ", totalSum)