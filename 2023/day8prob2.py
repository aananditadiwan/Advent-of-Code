def my_function():
   areAllLastStepZ = False
   for i in range(0,len(laststepMappings)):
         if (laststepMappings[i][2]!='Z'):
             areAllLastStepZ =  True
             break
         
   return areAllLastStepZ

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

listOfCurrentSteps = ['GCA','AAA','CMA','QNA','FTA','CBA']
laststepMappings = ['aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa']
# laststepMappings = ['FCZ', 'ZZZ', 'LDZ', 'GKZ', 'SVZ', 'TVZ'] 

# listOfCurrentSteps = ['11A','22A']
# laststepMappings = ['aaa','aaa']


with open('log.txt', 'w') as file:
   while  (my_function() ):
      laststepMappings = []
      # file.write(f'{instructionSet[iterator]}\n')
      # print(instructionSet[iterator])
      for eachElement in listOfCurrentSteps :

         indexOfCurrentStep = leftHandMappings.index(eachElement)
         # file.write(f'{eachElement} : {rightHandMappings[indexOfCurrentStep]} \n')
         # print(eachElement , ' : ', rightHandMappings[indexOfCurrentStep])

         
         if( instructionSet[iterator] == 'L') :
            currentStep = rightHandMappings[indexOfCurrentStep].split(',')[0].replace('(','')
            laststepMappings.append(currentStep)
         elif( instructionSet[iterator] == 'R') :
            currentStep = rightHandMappings[indexOfCurrentStep].split(', ')[1].replace(')','')
            laststepMappings.append(currentStep)
      if(iterator < len(instructionSet) -1) :
         iterator+=1
      else:
         iterator = 0
      listOfCurrentSteps = laststepMappings
      count+=1

      print(laststepMappings, '\n\n')
      file.write(f'{laststepMappings}\n\n')

   print(count)
   file.write(f'{count}\n\n')
