file = open('input.txt').read()
contents=file.split('\n')

arr=[]
xyzValues = { "X":1, "Y":2, "Z":3 }
abcValues = { "A":1, "B":2, "C":3 }
roundVales = { "lost":0, "draw":3 , "win":6 }
roundOutcome = ""
grandTotal = 0

for x in contents:
   arr=x.split(" ")
   if ( (arr[1] == "X" and arr[0] == "B") or (arr[1] == "Y" and arr[0] == "C") or (arr[1] == "Z" and arr[0] == "A") ):
      roundOutcome = "lost"
   else :
      if ( (arr[1] =="X" and arr[0] =="A") or (arr[1] =="Y" and arr[0] =="B") or (arr[1] =="Z" and arr[0] =="C") ):
         roundOutcome = "draw"
      else :
         roundOutcome = "win"

   grandTotal += roundVales[roundOutcome]+xyzValues[arr[1]]
print(grandTotal)