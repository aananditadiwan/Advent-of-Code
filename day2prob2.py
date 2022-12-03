file = open('input.txt').read()
contents=file.split('\n')

arr=[]
roundVales = { "lost":0, "draw":3 , "win":6 }
roundOutcome = ""
grandTotal = 0


for x in contents:

   arr=x.split(" ")

   if(arr[1]=="Y") :
      roundOutcome = "draw"
      if( arr[0] == "A") :
         xyz = 1
      if( arr[0] == "B") :
         xyz = 2
      if( arr[0] == "C") :
         xyz = 3

   if(arr[1]=="X") :
      roundOutcome = "lost"
      if( arr[0] == "A") :
         xyz = 3
      if( arr[0] == "B") :
         xyz = 1
      if( arr[0] == "C") :
         xyz = 2
   
   if(arr[1]=="Z") :
      roundOutcome = "win"
      if( arr[0] == "A") :
         xyz = 2
      if( arr[0] == "B") :
         xyz = 3
      if( arr[0] == "C") :
         xyz = 1

   grandTotal += roundVales[roundOutcome]+xyz

print(grandTotal)