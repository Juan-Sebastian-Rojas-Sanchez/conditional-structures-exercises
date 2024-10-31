import math
height=float(input("Enter your heigth"))
weight=float(input("Enter your weigth"))
age=float(input("Enter your age"))

Imc =weight/math.pow(height,2)
if(age<45):
  if(Imc>22):
      print("your low_risk status")
  else: 
       print("your low_risk status")
else:
    if(Imc<22):
        print("medium risk condition")
    else:
        print("high risk condition")