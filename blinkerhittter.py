#Joriel Fairbanks
#10/13/2026
#this is a stupid program about hitting the penjamin
import random

#consider making a gui for this game as its fun the way it is but could be better
#maybe add a prestige system or something
#and add an auto hitter? that auto farms pen hits?

money = 0 
#money starts at 0
playing = True

#upgrades
battery_upgrade = 0
money_multiplier = 1
luck_upgrade = 0

while playing:

    hits = 0
    green = random.randint(1,50) + (battery_upgrade * 5) + (luck_upgrade * 10)
    #make the upgrades display
    greenout = 0


    while True:

        choice = input("do you want to hit the penjamin?y/n").lower()

        if choice == "y":
            hits += 1
            if hits >= green:
                greenout = 1
                break

        elif choice == "n":
            break

        else:
            print("please enter y or n")

    if greenout == 1:
        print("you failed to hit the penjamin properly")

    else:
        print(f"You hit the penjamin {hits} times.")
        print("your maximum hits before greening out was", green)
        earned = hits * money_multiplier 
        money += earned 
        print("You earned", earned, "money!") 
        print("You now have", money, "money.")

#the upgrade shop
    while True: 
        check = (battery_upgrade * 5) + (luck_upgrade * 10)
        #sneaky little calculation of the upgrades
        #make it start printing the amount of money
        #added ^
        print("\n--- UPGRADE SHOP ---") 
        print("1. Better Battery - $10") 
        #make the prices scale somehow?
        print(" Adds 5 to your maximum hits.") 
        print("2. Money Multiplier - $25") 
        #im thinking whatever the old cost was x1.1 to then x5
        print(" Doubles your money earned per hit.") 
        #add some more upgrades? maybe make an inverntory sytem to collect differnt kinds of penjamins
        #maybe make penjamins display in the terminal when you hit them with some ascii art
        #make a referance file if i do something like this
        print("3. Lucky Charm - $50") 
        print(" Adds 10 to your maximum hits.") 
        print("4. Leave shop") 
        print("Your money is currently",money)
        shop_choice = input("What would you like to buy? ") 
        if shop_choice == "1": 
            if money >= 10: 
                money -= 10 
                battery_upgrade += 1 
                print("Better Battery purchased!") 
                print("your current base power is",check)
            else: 
                print("Not enough money!") 
        elif shop_choice == "2": 
            if money >= 25: 
                money -= 25 
                money_multiplier *= 2 
                print("Money Multiplier upgraded!") 
                print("Your multiplier is now", money_multiplier, "x") 
            else: 
                print("Not enough money!") 
        elif shop_choice == "3": 
            if money >= 50: 
                money -= 50 
                luck_upgrade += 1 
                print("Lucky Charm purchased!") 
                print("your current base power is",check)

            else: 
                print("Not enough money!") 
        elif shop_choice == "4": 
            break 
        else: 
            print("Please select a valid option.")


    again = input("Play another round? y/n: ").lower()
#main loop of the game asking if you wanna play
    if again == "n":
        playing = False
#dont break the playing loop or the whole thing crumbles
print("Thanks for playing! You ended with", money, "money.")
