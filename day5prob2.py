import re 

one = ['C','S','G','B']
two = ['G','V','N','J','H','W','M','T']
three = ['S','Q','M']
four = ['M','N','W','T','L','S','B']
five = ['P','W','G','V','T','F','Z','J']
six = ['S','H','Q','G','B','T','C']
seven = ['W','B','P','J','T']
eight = ['M','Q','T','F','Z','C','D','G']
nine = ['F','P','B','H','S','N']

containers = [one,two,three,four,five,six,seven,eight,nine]

sub_list = ["move","from","to"]

file = open('input.txt').read()
contents=file.split('\n')

for x in contents:

    for sub in sub_list:
        x = x.replace( sub , '')
    x = re.findall(r'\d+', x)

    fromStack = int(x[1])
    movingContainer = int(x[0])
    toStack = int(x[2])

    if(movingContainer<2) :
        containers[toStack-1].insert(0, containers[fromStack-1][movingContainer-1])
        del containers[fromStack-1][0]

    else :
        for counter in range (movingContainer,0,-1):
            containers[toStack-1].insert(0, containers[fromStack-1][counter-1])
            del containers[fromStack-1][counter-1] 
        
for counter in containers:
    print(counter[0])      