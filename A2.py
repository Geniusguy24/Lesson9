import time

units = int(input("Please Enter the number of units:"))
time.sleep(2)

if units<50:
    total_bill = (units*2.6) + 25
    print("Your total Electricity bill is:", "\n", total_bill)
elif units<=100:
    total_bill = (50*2.6)+((units - 50)*3.25)+35
    print("Your total Electricity bill is:", "\n", total_bill)
elif units<=200:
    total_bill = (50*2.6)+(50*3.25)+((units - 100)*5.26)+45
    print("Your total Electricity bill is:", "\n", total_bill)
else:
    total_bill = (50*2.6)+(50*3.25)+(100*5.26)+((units - 200)*8.45)+ 75
    print("Your total Electricity bill is:", "\n", total_bill)