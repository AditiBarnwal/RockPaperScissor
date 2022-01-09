import random
print("Winning rules of rock paper scissor are as follows:\n"
      + "rock vs paper -> paper wins\n"
      + "rock vs scissors -> rock wins\n"
      + "paper vs scissors -> scissors wins\n")
while True:
    print("Enter choice\n 1.Rock\n2.Scissors\n3.Paper\n")
    choice = int(input("User turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("Enter Valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Scissors'
    else:
        choice_name = 'Paper'
    print("User choice is: " + choice_name)
    print("\nNow its computer turn......")
    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Scissors'
    else:
        comp_choice_name = 'Paper'
    print("computer choice is : " + comp_choice_name)
    print(choice_name + "v/s" + comp_choice_name)

    if (choice == 1 and comp_choice == 2 ) or (choice == 2 and comp_choice_name == 1):
        print("rock wins => ", end="")
        result = "Rock"

    elif (choice == 1 and comp_choice == 3 ) or (choice == 3 and comp_choice_name == 1):
        print("paper wins => ", end="")
        result = "Paper"
    else:
        print("scissors wins => ", end="")
        result = "Scissors"
    if result == choice_name:
        print("<==User  wins==>")
    else:
        print("<==Computer Wins==>")
    print("Do you want to play again(Y/N) :  ")
    ans = input()
    if ans == 'n' or ans == 'N':
        break
print("\n Thanks for Playing")
