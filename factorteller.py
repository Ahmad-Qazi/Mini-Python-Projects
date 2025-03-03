print("Welcome to Factors teller.")




while True:
    user = int(input("Enter The number:"))
    loop = 1
    while loop <= user:
        y = user % loop

        
        if y == 0:
            print(f"{loop} is a factor of {user}.")

        loop += 1
    exi = str(input("Enter E for exit and A for continue: "))
    if exi == "e":
        break


print("Allah Hafis")