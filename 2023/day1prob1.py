file = open('input.txt').read()
contents=file.split('\n\n')

# print(contents)

totalCalibrationValue =0

for x in contents:
   y = x.split('\n')
   # print(y)
   # print('@@@@@@@@@@@@@@@@@@@\n\n')
   for word in y :
      arrayOfNumbers = []
      calibrationValue = 0 
      print(word)
      for letter in word:
         if letter.isnumeric():
            arrayOfNumbers.append(letter)
      if len(arrayOfNumbers)>1:
         calibrationValue = arrayOfNumbers[0] + arrayOfNumbers[-1]
      else:
         calibrationValue = arrayOfNumbers[0] + arrayOfNumbers[0]
      print(arrayOfNumbers)
      print(calibrationValue)
      totalCalibrationValue = totalCalibrationValue + int(calibrationValue)
   print('totalCalibrationValue',totalCalibrationValue)
   

   