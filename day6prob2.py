inputArray = open('input.txt').read()
length =len(inputArray)

count =0
for x in range (0, length):
    if(count <13) :
        count +=1
    else :
        subString = ""
        for i in range (13,0,-1) :
            subString += inputArray[x-i]

        if (len(set(subString)) != len(subString)) or (inputArray[x] in subString):
            count += 1
        else :
            break

print(count+1)