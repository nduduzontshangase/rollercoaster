print("Welcome to the roller coaster")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    age = int(input("What is you age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("You're going through a lot ride for free!")

    else:
        bill = 12
        print("Adults pay $12")

    wants_photo = input("Do you want to take a photo? Y or N.\n")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("Sorry you need to grow taller before you can ride.")
