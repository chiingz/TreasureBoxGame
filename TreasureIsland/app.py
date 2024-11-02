import random
treasure = """
       __________
      /_________/|
     |         | |
     |  $$$$$  | |
     |  $$$$$  | |
     |_________|/
       Treasure Box
"""
print("Welcome to Treasure Island")
print("Your mission is to find the Lost treasure")
choice1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'?\n ").lower()


if choice1 == "left":
    choice2 = input("You have come to a lake, "
                    "there is an island in the middle of the lake, "
                    "type 'wait' to wait for boat, "
                    "type 'swim' to swim across\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed."
                        " There is house with 3 doors.one red, "
                        "one yellow, and one blue. "
                        "what colour do you choose?\n")
        if choice3 == "red":
            print("it is a room full of fire. Game over")
        elif choice3 == "yellow":
            print("You open the door and found 3 Boxes label 1, 2, 3."
                  "open any of the cone you will find the treasure")
            secret_cone = random.randint(1, 3)
            your_choice = int(input("Make your choice? "))
            if your_choice == secret_cone:
                print("Congratulation found the Treasure",
                      f"{treasure}")
            else:
                print(f"Sorry you lose, the Treasure is in Box {secret_cone}")
        elif choice3 == "blue":
            print("You enter a room of beasts.Game over.")
        else:
            print("You chose a door that doesnt exist. Game over.")
    else:
        print("You were eaten by a shark, sorry Game over")
else:
    print("You chose right, sorry Game over.")