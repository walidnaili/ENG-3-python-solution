name = input("Please enter your name :")
if not(name == "VIP"):
    nb =  input("How many tickets would you like to buy ? ")
    nb = int(nb)
    print("The total cost is :" + str(nb * 15.50) )
    print("Enjoy your tickets!")
else :
    print("Enjoy the show for free!")

