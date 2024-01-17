file = open('input.txt').read()
contents=file.split('\n\n')
for x in contents:
   y = x.split('\n')

leftHandMappings =[]
rightHandMappings =[]
for eachElement in y :
   leftHandMappings.append(eachElement.split(' = ')[0])
   rightHandMappings.append(eachElement.split(' = ')[1])

instructionSet =list('LLRRLRRRLLRLRRLLLLRLRRLRRRLRLRRRLLRRLRRRLLRRLRRLRRLLRRRLRRLRRLRRRLRRLRLRLRRLRRLRRRLLRRLLLRRLRRRLRRRLRRRLRRLRRRLRLLRLRRRLRLRRLLRLRRRLRRRLRLRRRLRRRLRLRLRRLRRLRLRRLLRRRLRRRLRRRLLRRRLRLRLRLRLLRRRLRRRLRRLRRRLLRLRRLRRLRRRLRRRLRRLRLRLRRRLRRLRRLRRRLLRRLRLRLRRRLRLRLRRLRRLLRRLRRRLLRLLRLRLRRRR')
iterator =0
count = 0

currentStep = 'AAA'
# indexOfCurrentStep = 0
indexOfCurrentStep = leftHandMappings.index(currentStep)


with open('log.txt', 'w') as file:
   while currentStep!= 'ZZZ':
      indexOfCurrentStep = leftHandMappings.index(currentStep)
      file.write(f'{currentStep} : {rightHandMappings[indexOfCurrentStep]} \n')
      file.write(f'{instructionSet[iterator]}\n')
      print(currentStep , ' : ', rightHandMappings[indexOfCurrentStep])
      print(instructionSet[iterator])

      if( instructionSet[iterator] == 'L') :
         currentStep = rightHandMappings[indexOfCurrentStep].split(',')[0].replace('(','')

      elif( instructionSet[iterator] == 'R') :
         currentStep = rightHandMappings[indexOfCurrentStep].split(', ')[1].replace(')','')
      if(iterator < len(instructionSet) -1) :
         iterator+=1
      else:
         iterator = 0
      print(currentStep , '\n')
      file.write(f'{currentStep}\n\n')

      count+=1

   print(count)