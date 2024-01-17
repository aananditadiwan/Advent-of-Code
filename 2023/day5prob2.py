def calculationFunction(seedsListInput,seedsToSoilList):
   seedsListInput.sort()
   destRangeList =[]
   srcRangeList = []
   srcDestMapping =[]
   srcDestDictionary = []

   for seedsToSoilListEachElement in seedsToSoilList:                         # seedsToSoilList is list input having destination , source, counter
      # print("each element : ", seedsToSoilListEachElement)
      dest = int(seedsToSoilListEachElement.split(' ')[0])
      src = int(seedsToSoilListEachElement.split(' ')[1])
      counter = int(seedsToSoilListEachElement.split(' ')[2])

      destRangeList.append(dest)
      destRangeList.append(dest+counter-1)
      destRangeList.sort()
      srcRangeList.append(src)
      srcRangeList.append(src+counter-1)
      srcRangeList.sort()

      srcDestDictionary.append((src,src+counter-1,dest,dest+counter-1))
      # srcDestDictionary.append((dest,dest+counter-1))
   # print('destRangeList : ',destRangeList)
   # print('srcRangeList',srcRangeList)
   # print('srcDestDictionary : : : ',srcDestDictionary)

   for src in seedsListInput:
      if src<destRangeList[0] or src>destRangeList[-1]:
         srcDestMapping.append((src,src))
      else :
         for eachRangeInSrcList in srcDestDictionary :
            if src>=eachRangeInSrcList[0] and src<=eachRangeInSrcList[1]:
               difference = src-eachRangeInSrcList[0]
               srcDestMapping.append((src,eachRangeInSrcList[2]+difference))
               break
   
   newSrcArray =[]
   for iterable in srcDestMapping :
      newSrcArray.append( iterable[1])
   return(newSrcArray)
      

file = open('input.txt').read()
contents=file.split('\n\n')

inputArray=[]
for x in contents:
   inputArray.append(x.split('\n'))
seedsListInput=[]
seedsInput = (''.join(inputArray[0])).split(':')[1]
seedsInput = (''.join(seedsInput)).split(' ')
seedsInput = ' '.join(seedsInput).split()
for eachElement in range(0,len(seedsInput)):
   seedsInput[eachElement]=int(seedsInput[eachElement])


for iterable in range(0,len(seedsInput)-1,2):
   for innerIterable in range (seedsInput[iterable],seedsInput[iterable]+seedsInput[iterable+1]):
      seedsListInput.append(innerIterable)

seedsToSoil = inputArray[1][1:] 
SoilToFertilizerList = inputArray[2][1:] 
FertilizerToWaterList = inputArray[3][1:] 
WaterToLightList = inputArray[4][1:] 
LightToTemeratureList = inputArray[5][1:] 
TemeratureToHumidityList = inputArray[6][1:] 
HumidityToLocationList = inputArray[7][1:] 


# print("seeds: ",seedsListInput)
# print("seedsToSoilList: ",seedsToSoil)
newInput = calculationFunction(seedsListInput,seedsToSoil)
# print("SoilToFertilizerList: ",SoilToFertilizerList)
newInput = calculationFunction(newInput,SoilToFertilizerList)
# print("FertilizerToWaterList: ",FertilizerToWaterList)
newInput = calculationFunction(newInput,FertilizerToWaterList)
# print("WaterToLightList: ",WaterToLightList)
newInput = calculationFunction(newInput,WaterToLightList)
# print("LightToTemeratureList: ",LightToTemeratureList)
newInput = calculationFunction(newInput,LightToTemeratureList)
# print("TemeratureToHumidityList: ",TemeratureToHumidityList)
newInput = calculationFunction(newInput,TemeratureToHumidityList)
# print("HumidityToLocationList: ",HumidityToLocationList)
newInput = calculationFunction(newInput,HumidityToLocationList)

print("final answer : ",newInput)
print(min(newInput))
