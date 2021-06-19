import sys
import time

print('Welcome to the Adventure Game')
print('Main Menu')


def main_menu():
    print("You have 3 options: Options, Quit and Play Game.")
    print(" To select option, type option. \
To select Quit, type quit and to select Play Game, type play game:")
    option_selected = input('Type Here: ')
    if option_selected == 'option':
        option()
    elif option_selected == 'quit':
        quit_game()
    elif option_selected == "play game":
        from playgame1 import intro
        time.sleep(0.5)
        intro()
    else:
        print('Wrong Input')
        main_menu()


def quit_game():
    print("Are you sure?")
    exit_game = input("To exit, type yes and to stay type no:").lower()
    if exit_game == "yes":
        print('Thanks for Playing')
        sys.exit()
    elif exit_game == "no":
        print("Welcome Back")
        main_menu()
    else:
        print('Wrong Input')
        quit_game()


def option():
    print('You have 3 options on how to play the game. Easy, Medium or Hard. Please Select one.')
    easy = 'Easy refers to low Damage from enemy'
    medium = 'Medium refers to medium Damage from enemy'
    hard = "High refers to high Damage from enemy"
    print(easy)
    print(medium)
    print(hard)
    difficulty = input("Please select one: ").lower()
    if difficulty == 'easy':
        print('you have selected EASY')
    elif difficulty == 'medium':
        print('you have selected MEDIUM')
    elif difficulty == 'hard':
        print('you have selected HARD')
    else:
        print('Wrong Input')
        option()


main_menu()
