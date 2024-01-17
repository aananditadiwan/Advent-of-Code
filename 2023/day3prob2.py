from array import *

file = open('input.txt').read()
contents=file.split('\n\n')
for x in contents:
   y = x.split('\n')

input2DArray =[]
totalSum =0
totalRatio =0
for eachElement in y :
   input2DArray.append(list(eachElement))

for r in input2DArray:
   for c in r:
      print(c,end = " ")
   print()

with open('log.txt', 'w') as file:

   for r in range(0,len(input2DArray)):
      for c in range(0,len(input2DArray[r])):
         if input2DArray[r][c]=='*':
            starAdjacentToDigits = 0
            digitsAdjacentToStar =[]
            print(" Special character : ",input2DArray[r][c])
            file.write(f'Special character : {input2DArray[r][c]}\n')

            if c!=0:                                                                                  # if left is number
               if input2DArray[r][c-1].isnumeric() :
                  print("number on left")
                  file.write(f'number on left : ')
                  numberPresentAsList =[]
                  tempCounter = c-1
                  while input2DArray[r][tempCounter].isnumeric()==True:                               # Loop left till numeric is there
                     if tempCounter<0 :
                        break
                     else:
                        numberPresentAsList.insert(0,input2DArray[r][tempCounter])
                        tempCounter -= 1
                  numberPresent = ''.join(numberPresentAsList)
                  totalSum += int(numberPresent)
                  print("NUMBER  : ", numberPresent)
                  file.write(f'{numberPresent} \n')
                  starAdjacentToDigits+=1
                  digitsAdjacentToStar.append(numberPresent)


            if c != len(input2DArray[r])-1:                                                           # if right is number
               if input2DArray[r][c+1].isnumeric() :
                  print("number on right")
                  file.write(f'number on right : ')
                  numberPresentAsList =[]                               
                  tempCounter = c+1
                  while input2DArray[r][tempCounter].isnumeric():                                     # Loop right till numeric is there
                     numberPresentAsList.append(input2DArray[r][tempCounter])
                     tempCounter += 1
                     if tempCounter>len(input2DArray[r])-1:
                        break
                  numberPresent = ''.join(numberPresentAsList)
                  totalSum += int(numberPresent)
                  print("NUMBER  : ", numberPresent)
                  file.write(f'{numberPresent} \n')
                  starAdjacentToDigits+=1
                  digitsAdjacentToStar.append(numberPresent)

            if r != 0 :                                                 
               if input2DArray[r-1][c].isnumeric() :                                                  # if above is number
                  print("number is above")
                  file.write(f'number is above : ')
                  if(input2DArray[r-1][c-1].isnumeric() and input2DArray[r-1][c+1].isnumeric()) :     # number extends both sides
                     tempCounter = c
                     while input2DArray[r-1][tempCounter-1].isnumeric() :                             # going to start of number        
                        if tempCounter == 0 :
                           break
                        else :
                           tempCounter-=1
                        
                     numberPresentAsList =[]                           
                     while input2DArray[r-1][tempCounter].isnumeric():                                # Loop right till numeric is there
                        numberPresentAsList.append(input2DArray[r-1][tempCounter])
                        tempCounter += 1
                        if tempCounter>len(input2DArray[r-1])-1:
                           break
                     numberPresent = ''.join(numberPresentAsList)
                     totalSum += int(numberPresent)
                     print("NUMBER  : ", numberPresent)
                     file.write(f'{numberPresent} \n')
                     starAdjacentToDigits+=1
                     digitsAdjacentToStar.append(numberPresent)

                  else :
                     if (input2DArray[r-1][c-1].isnumeric()) :                                        # if numeric is on left loop left
                        numberPresentAsList =[]
                        tempCounter = c
                        while input2DArray[r-1][tempCounter].isnumeric():                             # Loop left till numeric is there
                           if tempCounter<0 :
                              break
                           else:
                              numberPresentAsList.insert(0,input2DArray[r-1][tempCounter])
                              tempCounter -= 1
                        numberPresent = ''.join(numberPresentAsList)
                        totalSum += int(numberPresent)
                        print("NUMBER  : ", numberPresent)
                        file.write(f'{numberPresent} \n')
                        starAdjacentToDigits+=1
                        digitsAdjacentToStar.append(numberPresent)

                     if (input2DArray[r-1][c+1].isnumeric()) :                                        # if numeric is on right loop left
                        numberPresentAsList =[]                               
                        tempCounter = c
                        while input2DArray[r-1][tempCounter].isnumeric():                             # Loop right till numeric is there
                           if tempCounter>len(input2DArray[r-1]):
                              break
                           else:
                              numberPresentAsList.append(input2DArray[r-1][tempCounter])
                              tempCounter += 1
                        numberPresent = ''.join(numberPresentAsList)
                        totalSum += int(numberPresent)
                        print("NUMBER  : ", numberPresent)
                        file.write(f'{numberPresent} \n')
                        starAdjacentToDigits+=1
                        digitsAdjacentToStar.append(numberPresent)


               else:
                  if c!=0:    
                     if input2DArray[r-1][c-1].isnumeric() :                                          # if top-left(diagonal) is number
                        print("diagionally")
                        file.write(f'above diagonally left: ')
                        if input2DArray[r-1][c-2].isnumeric() :
                           numberPresentAsList =[]
                           tempCounter = c-1
                           while input2DArray[r-1][tempCounter].isnumeric()==True:                    # Loop left till numeric is there
                              if tempCounter<0 :
                                 break
                              else:
                                 numberPresentAsList.insert(0,input2DArray[r-1][tempCounter])
                                 tempCounter -= 1
                           numberPresent = ''.join(numberPresentAsList)
                           totalSum += int(numberPresent)
                           print("NUMBER  : ", numberPresent)
                           file.write(f'{numberPresent} \n')
                           starAdjacentToDigits+=1
                           digitsAdjacentToStar.append(numberPresent)
                        # print(input2DArray[r-1][c-1],end = " ")  

                  if c != len(input2DArray[r])-1:    
                     if input2DArray[r-1][c+1].isnumeric() :                                          # if top-right(diagonal) is number
                        print("diagionally")
                        file.write(f'above diagonally right: ')
                        numberPresentAsList =[]                               
                        tempCounter = c+1

                        while input2DArray[r-1][tempCounter].isnumeric():                             # Loop right till numeric is there
                           numberPresentAsList.append(input2DArray[r-1][tempCounter])
                           tempCounter += 1
                           if tempCounter>len(input2DArray[r-1])-1:
                              break
                        numberPresent = ''.join(numberPresentAsList)
                        totalSum += int(numberPresent)
                        print("NUMBER  : ", numberPresent)
                        file.write(f'{numberPresent} \n')
                        starAdjacentToDigits+=1
                        digitsAdjacentToStar.append(numberPresent)
                        # print(input2DArray[r-1][c+1],end = " ")  

            if r != len(input2DArray)-1 :                               
               if input2DArray[r+1][c].isnumeric() :                                                     # if below is number
                  print("number is below")
                  file.write(f'number is below : ')
                  if(input2DArray[r+1][c-1].isnumeric() and input2DArray[r+1][c+1].isnumeric()) :        # number extends both sides
                     tempCounter = c
                     while input2DArray[r+1][tempCounter-1].isnumeric() :                             # going to start of number        
                        if tempCounter == 0 :
                           break
                        else :
                           tempCounter-=1
                        
                     numberPresentAsList =[]                           
                     while input2DArray[r+1][tempCounter].isnumeric():                                # Loop right till numeric is there
                        numberPresentAsList.append(input2DArray[r+1][tempCounter])
                        tempCounter += 1
                        if tempCounter>len(input2DArray[r+1])-1:
                           break
                     numberPresent = ''.join(numberPresentAsList)
                     totalSum += int(numberPresent)
                     print("NUMBER  : ", numberPresent)
                     file.write(f'{numberPresent} \n')
                     starAdjacentToDigits+=1
                     digitsAdjacentToStar.append(numberPresent)
                  else :
                     if input2DArray[r+1][c-1].isnumeric() :                                                # if number extends to left
                        numberPresentAsListBelow =[]
                        tempCounter = c
                        while input2DArray[r+1][tempCounter].isnumeric():                                   # Loop left till numeric is there
                           if tempCounter<0 :
                              break
                           else:
                              numberPresentAsListBelow.insert(0,input2DArray[r+1][tempCounter])
                              tempCounter -= 1
                        numberPresentBelow = ''.join(numberPresentAsListBelow)
                        totalSum += int(numberPresentBelow)
                        print("NUMBER  below: ", numberPresentBelow)
                        file.write(f'{numberPresentBelow} \n')
                        starAdjacentToDigits+=1
                        digitsAdjacentToStar.append(numberPresentBelow)

                     if input2DArray[r+1][c+1].isnumeric() :                           # if number extends to right
                        numberPresentAsList =[]                               
                        tempCounter = c
                        while input2DArray[r+1][tempCounter].isnumeric()==True:        # Loop right till numeric is there
                           if tempCounter>len(input2DArray[r+1]):
                              break
                           else:
                              numberPresentAsList.append(input2DArray[r+1][tempCounter])
                              tempCounter += 1
                        numberPresent = ''.join(numberPresentAsList)
                        totalSum += int(numberPresent)
                        print("NUMBER  : ", numberPresent)
                        file.write(f'{numberPresent} \n')
                        starAdjacentToDigits+=1
                        digitsAdjacentToStar.append(numberPresent)
                  
               else:
                  if c!=0:    
                     if input2DArray[r+1][c-1].isnumeric() :               # if bottom-left(diagonal) is number
                        file.write(f'below diagonally left: ')
                        if input2DArray[r+1][c-2].isnumeric() :                        # if number extends to left
                           numberPresentAsListBelow =[]
                           tempCounter = c-1
                           while input2DArray[r+1][tempCounter].isnumeric():           # Loop left till numeric is there
                              if tempCounter<0 :
                                 break
                              else:
                                 numberPresentAsListBelow.insert(0,input2DArray[r+1][tempCounter])
                                 tempCounter -= 1
                           numberPresentBelow = ''.join(numberPresentAsListBelow)
                           totalSum += int(numberPresentBelow)
                           print("NUMBER  below: ", numberPresentBelow)
                           file.write(f'{numberPresentBelow} \n')
                           starAdjacentToDigits+=1
                           digitsAdjacentToStar.append(numberPresentBelow)
                        # print(input2DArray[r+1][c-1],end = " ")
                  if c != len(input2DArray[r])-1:
                     if input2DArray[r+1][c+1].isnumeric() :               # if bottom-right(diagonal) is number
                        file.write(f'below diagonally right: ')
                        numberPresentAsListBottomRight =[]                               
                        tempCounter = c+1
                        # print("len ", )
                        while input2DArray[r+1][tempCounter].isnumeric():                 # Loop right till numeric is there
                           numberPresentAsListBottomRight.append(input2DArray[r+1][tempCounter])
                           tempCounter += 1
                           if tempCounter>len(input2DArray[r+1])-1:
                              break
                        numberPresentBottomRight = ''.join(numberPresentAsListBottomRight)
                        totalSum += int(numberPresentBottomRight)
                        print("NUMBER  : ", numberPresentBottomRight)
                        file.write(f'{numberPresentBottomRight} \n')
                        starAdjacentToDigits+=1
                        digitsAdjacentToStar.append(numberPresentBottomRight)
                        # print(input2DArray[r+1][c+1],end = " ")
            print("starAdjacentToDigits : ", starAdjacentToDigits)
            if(starAdjacentToDigits==2):
               print('digitsAdjacentToStar',digitsAdjacentToStar)
               gearRatio = int(digitsAdjacentToStar[0])*int(digitsAdjacentToStar[1])
               totalRatio+=gearRatio
      #    print(c,end = " ")
      file.write(f'\n')
      print()
   
   
   print(totalRatio)