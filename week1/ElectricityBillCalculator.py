name=input("Enter Name: ")
units=int(input("Enter Units Conusumed"))
if units<=100:
    total=units*5
    print("$5/unit")
elif(units>100):
    total=units*8
    print("8/unit")
else:
    print("Enter Valid Units")    
print("Total Bill:",total)
