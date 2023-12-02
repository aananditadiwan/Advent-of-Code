file = open('input.txt').read()
contents=file.split('\n\n')

totalOfpowerSet = 0

for x in contents:
   y = x.split('\n')
   for eachGame in y :                                               # each game
      perGameInputArray = eachGame.split(':')[1]
      perGameInputList = perGameInputArray.split(';')

      red =0
      blue =0
      green =0
      powerSet =0

      for eachHandful in perGameInputList:
         eachHandfulList = eachHandful.split(',')

         for eachHandfulListElement in eachHandfulList :             # getting the number of balls from string
            eachHandfulListElementNumericPart =''
            for character in eachHandfulListElement:
               if character.isnumeric() :
                  eachHandfulListElementNumericPart += character
            eachHandfulListElementNumericPart = int(eachHandfulListElementNumericPart)

            if eachHandfulListElement.find('red')>-1:                # checking colorof ball
               if red < eachHandfulListElementNumericPart :
                     red = eachHandfulListElementNumericPart
            elif eachHandfulListElement.find('green')>-1:
               if green < eachHandfulListElementNumericPart :
                     green = eachHandfulListElementNumericPart
            elif eachHandfulListElement.find('blue')>-1:
               if blue < eachHandfulListElementNumericPart :
                     blue = eachHandfulListElementNumericPart

      powerSet = red*blue*green                                      # powerset value of each game
      totalOfpowerSet += powerSet

print(' totalOfpowerSet : ', totalOfpowerSet)