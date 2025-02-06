ride = int(input("Which type of ride do you want?"+ "\n"+ "1 = Bike"+ "\n"+ "2 = Car"+ "\n"))

if ride == 1:
    color = input("Which color do you want the bike?"+ "\n"+ "White"+ "\n"+ "Black"+ "\n"+ "Blue"+ "\n"+ "Blue"+ "\n"+ "Red"+ "\n")
    print("You have selected a bike ride with color "+ color)
elif ride == 2:
    color = input("Which color do you want the Car?"+ "\n"+ "White"+ "\n"+ "Black"+ "\n"+ "Blue"+ "\n"+ "Blue"+ "\n"+ "Red"+ "\n")
    print("You have selected a Car ride with color "+ color)
else:
    print("Invalid Input")