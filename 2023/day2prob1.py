file = open('input.txt').read()
contents=file.split('\n\n')

totalOfGameId = 0
for x in contents:
   y = x.split('\n')

   for eachGame in y :                                                  # each game

      gamePossible = True
      gameIDnumericPart = ''                                            # getting game ID - game number
      gameID = eachGame.split(':')[0]
      for character in gameID:
         if character.isnumeric() :
            gameIDnumericPart += character

      perGameInputArray = eachGame.split(':')[1]
      perGameInputList = perGameInputArray.split(';')

      for eachHandful in perGameInputList:                              # each handful per game
         eachHandfulList = eachHandful.split(',')

         for eachHandfulListElement in eachHandfulList :                # getting number part of string
            eachHandfulListElementNumericPart =''
            for character in eachHandfulListElement:
               if character.isnumeric() :
                  eachHandfulListElementNumericPart += character
            eachHandfulListElementNumericPart = int(eachHandfulListElementNumericPart)

            if eachHandfulListElement.find('red')>-1:                   # checking color
               if eachHandfulListElementNumericPart>12 :
                  gamePossible = False
            elif eachHandfulListElement.find('green')>-1:
               if eachHandfulListElementNumericPart>13 :
                  gamePossible = False
            elif eachHandfulListElement.find('blue')>-1:
               if eachHandfulListElementNumericPart>14 :
                  gamePossible = False

      if(gamePossible):
         totalOfGameId += int(gameIDnumericPart)

print('game is : ', totalOfGameId)