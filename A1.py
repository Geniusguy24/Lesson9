import time

medical_cause = input("Do you have a medical cause?")
time.sleep(2)

if medical_cause == "yes" or medical_cause == "Yes":
    print("You are eligible for the examination!")
    time.sleep(2)
elif medical_cause  == "No" or medical_cause == "no":
    attendence = int(input("Please Enter your attendence:"))
    if attendence > 75:
        print("You are eligible for the examination!")
    else:
        print("You are not eligible for the examination!")
else:
    print("Invalid Input!")