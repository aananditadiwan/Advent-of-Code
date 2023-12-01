file = open('input.txt').read()
contents=file.split('\n\n')

subStringArray = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine","1","2","3","4","5","6","7","8","9"]
mapWordToNumericValue = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
totalCalibrationValue =0

with open('log.txt', 'w') as file:
   for x in contents:
      y = x.split('\n')

      for word in y :
         calibrationValue=''
         numbersInInputString = {}
         print(word)
         file.write(f'{word} ==> ')

         for subStringCandidate in subStringArray:
            if (word.count(subStringCandidate))>0 :
               print(subStringCandidate)
               if (word.find(subStringCandidate)) >-1 :
                  numbersInInputString[word.find(subStringCandidate)]=subStringCandidate
               if (word.count(subStringCandidate))>1 :
                  numbersInInputString[word.rfind(subStringCandidate)]=subStringCandidate

         wordAtMinimumIndex = min(numbersInInputString)
         wordAtMaximumIndex = max(numbersInInputString)

         if numbersInInputString[wordAtMinimumIndex] in mapWordToNumericValue:
            minimumvalue = mapWordToNumericValue.index(numbersInInputString[wordAtMinimumIndex])
         else :
            minimumvalue = numbersInInputString[wordAtMinimumIndex]

         if numbersInInputString[wordAtMaximumIndex] in mapWordToNumericValue:
            maximumvalue = mapWordToNumericValue.index(numbersInInputString[wordAtMaximumIndex])
         else :
            maximumvalue = numbersInInputString[wordAtMaximumIndex]
         
         calibrationValue = str(minimumvalue) + str(maximumvalue)
         print(calibrationValue)
         file.write(f'{calibrationValue}\n')

         totalCalibrationValue = totalCalibrationValue + int(calibrationValue)
      print('totalCalibrationValue',totalCalibrationValue)
      file.write(f'{str(totalCalibrationValue)}\n')

