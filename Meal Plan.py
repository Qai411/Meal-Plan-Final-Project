amt_on_card = 50
welcome = print("Welcome to Shef Catering Service.\n==> You have 50gh daily ('~')<==\n Below is a list of items available \nPress the number to order\n 1. Rice -- 10gh\n 2. Banku -- 10gh\n 3. Gobhe -- 15gh\n 4. Fufu -- 20gh\n 5. Drink -- 5gh\nPress 100 to exit")
rice = 10
banku = 10
Gobhe = 15
Fufu = 20
Drink = 5
arrow = print("==> ",end="")
choice = int(input())

while choice != 100:
    if amt_on_card > 0:
        if choice == 1:
            if amt_on_card < 10:
                print("You have insufficient amount on card")
                break
            amt_on_card -= 10
            print("You ordered Rice. Get Seated & Enjoy! :P")
        elif choice == 2:
            if amt_on_card < 10:
                print("You have insufficient amount on card")
                break
            amt_on_card -= 10
            print("You ordered Banku. Get Seated & Enjoy! :P")
        elif choice == 3:
            if amt_on_card < 25:
                print("You have insufficient amount on card")
                break
            amt_on_card -= 25
            print("You ordered Gobhe. Get Seated & Enjoy! :P")
        elif choice == 4:
            if amt_on_card < 20:
                print("You have insufficient amount on card")
                break
            amt_on_card -= 20
            print("You ordered Fufu. Get Seated & Enjoy! :P")
        elif choice == 5:
            if amt_on_card < 5:
                print("You have insufficient amount on card")
                break
            amt_on_card -= 5
            print("You ordered Drink. Take a stand & Enjoy! :P")
        else:
            print("I don't understand. Try again")
            arrow = print("==> ",end="")
            choice = int(input())
    else:
        print("I don't understand. Try again")
        arrow = print("==> ", end="")
    print("You have ", amt_on_card, "gh left")
    notice = print("Order again? Press the number item or press 100 to exit")
    arrow = print("==> ", end="")
    choice = int(input())
else:
    quit()
print("You have ",amt_on_card,"gh still left")

while amt_on_card >= 15:
    print("You can only afford \n1. Rice\n2. Banku\n3. Gobhe\n5.Drinks")
    arrow = print("==> ", end="")
    choice = int(input())
    if choice == 1:
        amt_on_card -= 10
        print("You ordered Rice. Get Seated & Enjoy! :P")
    elif choice == 2:
        amt_on_card -= 10
        print("You ordered Banku. Get Seated & Enjoy! :P")
    elif choice == 3:
        amt_on_card -= 25
        print("You ordered Gobhe. Get Seated & Enjoy! :P")
    elif choice == 5:
        amt_on_card -= 5
        print("You ordered Drink. Take a stand & Enjoy! :P")
    else:
        print("I don't understand")
    arrow = print("==> ", end="")
    choice = int(input())

while amt_on_card >= 10:
    print("You can only afford \n1. Rice\n2. Banku\n5. Drinks")
    if choice == 1:
        amt_on_card -= 10
        print("You ordered Rice. Get Seated & Enjoy! :P")
    elif choice == 2:
        amt_on_card -= 10
        print("You ordered Banku. Get Seated & Enjoy! :P")
    elif choice == 5:
        amt_on_card -= 5
        print("You ordered Drink. Take a stand & Enjoy! :P")
    else:
        print("I don't understand")
    print("You have ", amt_on_card, "gh still left")
    arrow = print("==> ", end="")
    choice = int(input())

while amt_on_card >= 5:
    print("You can only afford \n5. Drinks")
    if choice == 5:
        amt_on_card -= 5
        print("You ordered Drink. Take a stand & Enjoy! :P")
    else:
        print("I don't understand")
    print("You have ", amt_on_card, "gh still left")
    arrow = print("==> ", end="")
    choice = int(input())

print("Thank you for using Shef services")