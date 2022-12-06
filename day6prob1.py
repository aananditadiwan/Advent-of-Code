inputArray = open('input.txt').read()
length =len(inputArray)

count =0
for x in range (0, length):
    if(count <3) :
        count +=1
    else :
        subString = ""
        subString += inputArray[x-3]
        subString += inputArray[x-2]
        subString += inputArray[x-1]

        if inputArray[x] in subString  or  len(set(subString)) != len(subString):
            count += 1
        else :
            break
print(count+1)


