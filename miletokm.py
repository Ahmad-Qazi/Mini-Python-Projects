print("Welocome !")
print("here you can find a value of kilo metres in miles and miles to kilometres.")



# kilometre = 1.69344
# mile = 1

k_or_m = None


while k_or_m != "e" or "E":
    print("Enter K for kilometre to mile.")
    print("Enter M for mile to kilometre.")
    print("Enter E for exit")



    k_or_m = input("Enter the function you want: ")
    user = float(input("Enter the value: "))


    if k_or_m == "K" or "k":
        ans = user * 1.69344
        print(ans)
    elif k_or_m == "M" or "m":
        ans = 1.69344 / user
        print(ans)
    else:
        print("Check the charcter you want.")

print("Allah hafiz")