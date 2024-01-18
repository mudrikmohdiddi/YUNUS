#let flnum=flet intn=integer number
#let frctn=fraction number
flnum=float(input("enter the float number: "))
intn=str(flnum)
frctn,_,frc=intn.partition('.')
print("float number: ",flnum)
print("integer number: ",frctn)
print("fraction number: ",frc)
