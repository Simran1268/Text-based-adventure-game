import time
import gamestart

inventory = []


def intro():
    time.sleep(0.5)
    intro1 = ("Welcome to the Magical World known as Asylum. You will see various kinds of people and monsters.\n \
Your main Objective is to collect information and SURVIVE. Good luck\n")
    print(intro1)
    time.sleep(0.5)
    print('Character Creation is Opened. Create a character of your liking. ')
    time.sleep(0.5)

    def character_create():
        print(' You have 4 options in front of you: Gender, Classes, Hair Type and Name.\n')
        time.sleep(0.5)
        character_characteristics = []
        gender = ['Male', 'Female']
        classes = ['Warrior', 'Rouge', 'Mage']
        hair_type = ['Brown', 'Black', 'Blonde']

        def gender_function():
            print("This is your Gender window.\n ")
            time.sleep(0.5)
            print(gender)
            selected_gender = input('Please type male or female:\n ').lower()
            if selected_gender == 'male' or selected_gender == "female":
                character_characteristics.append(selected_gender)

            else:
                print("Invalid Input")
                gender_function()
            return ""

        def classes_function():
            print("This is your class window.\n")
            time.sleep(0.5)
            print(classes)
            selected_class = input('Please select any one of them:\n ').lower()
            if selected_class == 'warrior' or selected_class == 'mage' or selected_class == 'rouge':
                character_characteristics.append(selected_class)
            else:
                print('Invalid Entry')
                classes_function()
            return ""

        def hair_type_function():
            print("This is your Hair Type window.\n")
            time.sleep(0.5)
            print(hair_type)
            select_hair_type = input("Please select any one of the hair types:\n ").lower()
            if select_hair_type == 'black' or select_hair_type == "brown" or select_hair_type == "blonde":
                character_characteristics.append(select_hair_type)
            else:
                print('Invalid Entry')
                hair_type_function()
            return ""

        def name_function():
            name = input("Please Write a name for your character:\n ")
            time.sleep(0.5)
            character_characteristics.append(name)
            return ""

        print(gender_function(), classes_function(), hair_type_function(), name_function())
        time.sleep(0.5)
        print("Welcome " + character_characteristics[3] + ", your Character is a " + character_characteristics[0] +
              ", with " + character_characteristics[2] + " hair and your class is " +
              character_characteristics[1] + ' \n')

    print(character_create())
    time.sleep(0.5)
    invalid = 'Invalid option'

    def game_start_point():
        print("You're randomly transported into a medieval town with no memories of what had happened in your \
past")
        time.sleep(0.5)

    def first_choice():
        print("You have two choices. There is a town in right of you. It is a small town as you can see it from \
far away and in front of you, there is a tavern")
        time.sleep(0.5)
        movement = input('If you want to go to town, type RIGHT or if you want to go tavern, type \
TAVERN:\n ').lower()
        time.sleep(0.5)

        if movement == 'right':
            def in_center_of_town():
                print("You are now in the center of the town now. Town's center is empty. ")
                time.sleep(0.5)
                in_town = input('If you want to go back to first choices, type BACK: \n').lower()
                time.sleep(0.5)
                if in_town == 'back':
                    first_choice()
                else:
                    print(invalid)
                    in_center_of_town()

            print(in_center_of_town())

        elif movement == "tavern":
            def way_to_tavern():
                print("While going to tavern, you see a gold coin on the road.")
                time.sleep(0.5)
                choice = input("If you want to pick up the coin, type PICK or if you don't want to pick it up type \
LEAVE: \n").lower()
                time.sleep(0.5)

                if choice == "pick":

                    def beggars_place():
                        print("\nYou are lured into a beggar's trap and killed by him. Game Over. Remember, Don't \
be greedy ")
                        time.sleep(0.5)
                        play_again = input("If you want go back to previous checkpoint, type CHECKPOINT,\
if you want to Play Again from starting, type PLAY AGAIN or if you want to quit type \
QUIT: \n").lower()

                        if play_again == 'play again':
                            print(game_start_point())
                        elif play_again == "checkpoint":
                            first_choice()
                        elif play_again == 'quit':
                            gamestart.quit_game()
                        else:
                            print(invalid)
                            beggars_place()

                    print(beggars_place())

                elif choice == "leave":
                    def in_tavern():
                        time.sleep(0.5)
                        print('You got lucky, beggar had set up a trap. ')
                        time.sleep(0.5)
                        print("Now, you have reached inside of tavern. It is completely destroyed, while exploring,\
you see a board with a description of town on your LEFT,\n there is a of the town and on your RIGHT there is a guy at \
the bar with torn up armor and there is a sweet roll on the bar")
                        time.sleep(0.5)
                        tavern_choice = input("If you want to go to see the board, type LEFT, if you want to go to the guy,\
type RIGHT or if you want to pick up and eat sweet roll, type PICK \n").lower()
                        if tavern_choice == "left":
                            def tavern_board():
                                print("Town of Asvile is one of the luxurious town in the in the kingdom of\
Asylum. It is well known for its wine and silk. It was established by the great king Alvador II and prosper under \
his reign")
                                time.sleep(0.5)
                                at_tavern_board = input("If you want to go back, type BACK.\n").lower()
                                if at_tavern_board == "back":
                                    in_tavern()
                                else:
                                    print(invalid)
                                    tavern_board()
                            print(tavern_board())

                        elif tavern_choice == "pick":
                            def sweet_roll():
                                print("Guy picked up his sword and cut your arm, you died instantly.\
Game Over. That's why never eat someones food without permission")
                                time.sleep(0.5)
                                play_again = input("If you want go back to previous checkpoint, type CHECKPOINT,\
if you want to Play Again from starting, type PLAY AGAIN or if you want to quit type \
QUIT: \n").lower()
                                time.sleep(0.5)
                                if play_again == 'play again':
                                    print(game_start_point())
                                elif play_again == "checkpoint":
                                    in_tavern()
                                elif play_again == 'quit':
                                    gamestart.quit_game()
                                else:
                                    print(invalid)
                                    sweet_roll()
                            print(sweet_roll())

                        elif tavern_choice == "right":
                            def by_tavern_guy():
                                print("He says, You are someone I never saw. Guy starts talking about his\
backstory.He told that all the solider and people \
of the town were killed by \nthe goblins. He barely escaped from their attack. The great mage of the Asvile, told that \
a deity from another world is required to kill those goblins as they are too powerful. \nSo, he gave me a magical spoon \
, in order to call the deity. After I used it, nothing happens and everyone who survived \nlost all hope. In order to \
calm my mind, I came here. \n")
                                time.sleep(0.5)
                                print("He added, if by any chance you are our hope, head toward the north through \
Dragon Valley and take a left from Highway Hell, there you will see a cave.\n There I had thrown the spoon out of \
frustration")
                                time.sleep(0.5)
                                print("Player thought, if that spoon can bring him here so it is also possible to \
to go back home with it.")
                                time.sleep(0.5)

                                def outside_tavern_function():
                                    print("Now you are outside of the tavern. ")
                                    time.sleep(0.5)
                                    print("Attention: You just saw a white rabbit.")
                                    time.sleep(0.5)
                                    outside_tavern = input("If you want to talk to the guy again, type BACK, If you\
follow the rabbit, type rabbit or If you want to go north, type NORTH\n").lower()
                                    if outside_tavern == "back":
                                        print("Congratulation, You just received a sword from the \
guy to kill goblins.")
                                        time.sleep(0.5)
                                        inventory.append("Sword")
                                        outside_tavern_function()

                                    elif outside_tavern == "rabbit":
                                        def rabbit():
                                            print("You have fallen into an old fashion trap. Game Over. \
Beware, next time don't follow stupid things ")
                                            time.sleep(0.5)

                                            play_again = input("If you want go back to previous checkpoint, \
type CHECKPOINT, if you want to Play Again from starting, type PLAY AGAIN or if you want to quit type QUIT: \n").lower()

                                            if play_again == 'play again':
                                                print(game_start_point())
                                            elif play_again == "checkpoint":
                                                outside_tavern_function()
                                            elif play_again == 'quit':
                                                gamestart.quit_game()
                                            else:
                                                print(invalid)
                                                rabbit()
                                        print(rabbit())

                                    elif outside_tavern == "north":
                                        def north():
                                            print("You are now in Dragon Valley. Upon exploring, you have Two \
routes in front of you. There is a small alley on your LEFT and Highway Hell on your RIGHT")
                                            time.sleep(0.5)
                                            north_choices = input("If you want to go to alley, Type LEFT or if \
you want to go on bridge, Type RIGHT.\n").lower()
                                            if north_choices == "left":
                                                def alley():
                                                    print("You saw a bunch of Dead Bodies. End of route")
                                                    time.sleep(0.5)
                                                    alley_choices = input("To go back to dragon valley, \
type BACK\n").lower()
                                                    if alley_choices == "back":
                                                        north()
                                                    else:
                                                        print(invalid)
                                                        alley()

                                                print(alley())
                                            elif north_choices == "right":
                                                def highway():
                                                    print("You are now on Highway Hell.")
                                                    time.sleep(0.5)
                                                    print("Cave is in the site. \n Attention: You sense some danger\
in the cave.")
                                                    highway_choices = input("If you want to check your inventory, \
type INVENTORY \n").lower()
                                                    if highway_choices == "inventory":
                                                        print(inventory)
                                                        if len(inventory) == 1:
                                                            def have_sword():
                                                                print("You have a Sword in it and player equip it.")
                                                                time.sleep(0.5)
                                                                cave = input("Now you can go to into cave,\
to go inside type CAVE\n").lower()
                                                                if cave == "cave":
                                                                    print("You are inside the cave now.\
You see 5 goblins inside.")
                                                                    time.sleep(0.5)
                                                                    print("Since you have the sword you killed \
them without any problem. You have retrieved the the magical spoon.")
                                                                    time.sleep(0.5)
                                                                    print("Congratulation, with the use \
of spoon you are able to go home. Game Over")


                                                                else:
                                                                    print(invalid)
                                                                    have_sword()

                                                            print(have_sword())

                                                        elif len(inventory) == 0:
                                                            def inventory_empty():
                                                                print("Inventory is empty. You have nothing to \
fight with. Hint: Talk to the guy again, maybe he knows where it is")
                                                                time.sleep(0.5)
                                                                print("If you want to go back, you have Following \
choices: Starting point, Tavern, Outside of tavern, Dragon Valley, Highway Hell ")
                                                                time.sleep(0.5)
                                                                print("If you don't want to go back, move Forward")
                                                                time.sleep(0.5)
                                                                empty = input(" Type STARTING POINT or TAVERN or \
OUTSIDE TAVERN or DRAGON VALLEY or HIGHWAY HELL or FORWARD\n").lower()
                                                                if empty == "starting point":
                                                                    first_choice()
                                                                elif empty == "tavern":
                                                                    way_to_tavern()
                                                                elif empty == "outside tavern":
                                                                    outside_tavern_function()
                                                                elif empty == "highway hell":
                                                                    highway()
                                                                elif empty == "forward":
                                                                    cave = input("Now you can go to into cave,\
to go inside type CAVE").lower()
                                                                    if cave == "cave":

                                                                        print("You are inside the cave now.\
You see 5 goblins inside.")
                                                                        time.sleep(0.5)
                                                                        print("Since you don not have the sword, \
Those goblins ripped you apart and killed you.")
                                                                        time.sleep(0.5)
                                                                        print("Congratulation, You died \
successfully. Game Over")
                                                                        time.sleep(0.5)

                                                                        def play_again_function():
                                                                            play_again = input("If you want go \
back to previous checkpoint, type CHECKPOINT, if you want to Play Again from starting, type PLAY AGAIN or \
if you want to quit type QUIT: \n").lower()
                                                                            time.sleep(0.5)

                                                                            if play_again == 'play again':
                                                                                print(game_start_point())
                                                                            elif play_again == "checkpoint":
                                                                                inventory_empty()
                                                                            elif play_again == 'quit':
                                                                                gamestart.quit_game()
                                                                            else:
                                                                                print(invalid)
                                                                                play_again_function()
                                                                            return ""

                                                                        print(play_again_function())
                                                                else:
                                                                    print(invalid)
                                                                    inventory_empty()
                                                                return ""

                                                            print(inventory_empty())
                                                        else:
                                                            print(invalid)
                                                            highway()
                                                        return ""

                                                    else:
                                                        print(invalid)
                                                        highway()
                                                    return ""

                                                print(highway())
                                            else:
                                                print(invalid)
                                                north()
                                            return ""

                                        print(north())

                                    else:
                                        print(invalid)
                                        outside_tavern_function()
                                    return ""

                                print(outside_tavern_function())

                            print(by_tavern_guy())

                        else:
                            print(invalid)
                            in_tavern()
                        return ""

                    print(in_tavern())
                else:
                    print(invalid)
                    way_to_tavern()
                return ""

            print(way_to_tavern())
        else:
            print(invalid)
            first_choice()
        return ""

    print(game_start_point(), first_choice())

    return ""
print(intro())

