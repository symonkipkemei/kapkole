
from parameters import *
import webbrowser

def main():
    """The search for the princess begins, Would you rescue her? or will you be part of the statistics of the fallen soldiers?
    """

     # welcome the user to the game on first time only
    player = player_name()

    play_again = True
    while play_again:
        # objects placed here to allow for resetting
        #________________________________________________________________________

        #Hero
        warrior = Hero(player)
    
        #opponents
        black_panther = Opponent("Black Panther",0)
        gorilla =Opponent("Gorilla",0)
        prey_mantis =Opponent("Prey Mantis",0)
        cheetah =Opponent("Cheetah",0)

        #opponent pool
        opponent_pool = [black_panther,gorilla,prey_mantis,cheetah]
        #_________________________________________________________________________

        # Game begins, no way out unless you rescue the girl or you are defeated
        return_previous_room = True
        while return_previous_room:

            # state the state of the inventory
            print("\nYOUR STATE OF INVENTORY")
            print("_________________________________________________________________")
            print(f"collections : {warrior.arsenal}" )
            print(f"opponents pool: {[opp.name for opp in opponent_pool]}")
            print(f"opponents beheaded: {warrior.head_count}")
            print(f"Keys : {warrior.key}")
            print("_________________________________________________________________")
            print("all the best in search for the princess")

            # select an opponent randomly from the pool
            opp = random.choice(opponent_pool)

            # display the door choices
            doors = {1:"Opponents cave", 2:"Jungle cave", 3:"locked cave", 4:"exit cave"}
            selection = door_choices(doors)
            if selection == doors[1]:
                # fight if hero wins collect the opponents head, if he loses all items are retrieved
                print("You found an Opponent!\n")

                win = warrior.attack(opp)
                if win:
                    print(f"{opp.name} has been beheaded and elimninated from the pool")
                    opponent_pool.remove(opp)
                    if len(opponent_pool) == 0:
                        print("You have found a key")
                        warrior.key += 1

                    warrior.head_count += 1

                else:
                    #check the status of the collection ,if any item is 0, the game ends.
                    collection_status = [status for status in warrior.arsenal.values()]
                    if 0 in collection_status:
                        print(f"The fight was exhausting and your energy pack (collection) was empty.\n{warrior.name}, it is sad to see you die😥😥😥")
                        return_previous_room = False
                    else:
                        #if defeated the opponents empties the heros collection
                        warrior.decollect()
                        print(f"\nYour collections(energy pack) has been emptied by {opp.name}.\nYou need collections to survive the next round of fight if defeated")
                        

            if selection == doors[2]:
                # enters a room collect random item
                warrior.collect()

            elif selection == doors[3]:
                # the cave is locked 
                #what custodian needs
                multiplier = 1
                custodian_fruits= [fruits for fruits in warrior.arsenal.keys()]
                custodian_needs ={}
                
                custodian_needs[custodian_fruits[0]] = 1 * multiplier
                custodian_needs[custodian_fruits[1]] = 2 * multiplier
                custodian_needs[custodian_fruits[2]] = 3 * multiplier
                beheaded = 2 * multiplier
                custodian_keys = 1 * multiplier

                print("LOCKED CAVE")
                print("__________________________________________________________________________________")
                print(f"Hi {player}\n\nI am a baboon 🐒🐒🐒 ,custodian of the locked cave.\nTo enter this cave,you need:\n")
                print("**********************************************************")
                print(f"collections🍓 : {custodian_needs}")
                print(f"opponents_beheaded 💀: {beheaded}")
                print("**********************************************************")
                print("OR")
                print("**********************************************************")
                print(f"keys 🔑 : {custodian_keys}")
                print("__________________________________________________________________________________")

                print("\n***********************")
                print("1. Proceed anyway \n2. Run away")
                print("***********************")
                choice = int(input("Insert option:"))

                if choice == 1:
                    #check if warrior has met the set requirements
                    #if player wins, open youtube and play superhero by the script
                    winnerurl = "https://www.youtube.com/watch?v=WIm1GgfRz6M"
                    loserurl = "https://www.youtube.com/watch?v=RgKAFK5djSk"
                    if warrior.head_count >= beheaded and warrior.arsenal[custodian_fruits[0]] >= custodian_needs[custodian_fruits[0]]   and warrior.arsenal[custodian_fruits[1]] >= custodian_needs[custodian_fruits[1]] and warrior.arsenal[custodian_fruits[2]] >= custodian_needs[custodian_fruits[2]]:
                        print("You have found the daughter of the king . congratulations!")
                        webbrowser.open(winnerurl)
                        return_previous_room = False
                    elif warrior.key == custodian_keys:
                        print("You have found the daughter of the king . congratulations!")
                        webbrowser.open(loserurl)
                        return_previous_room = False

                    else:
                        print("\n👏👏👏👏👏")
                        time.sleep(2)
                        print("👏👏👏👏👏✨✨✨")
                        time.sleep(3)
                        print("👏👏👏👏👏✨✨✨")
                        print(f"You died as a result of injuries from the baboon")
                        webbrowser.open(loserurl)
                        return_previous_room = False



            elif selection == doors[4]:
                #exit the game
                print("\n“There is no failure except in no longer trying.”― Elbert Hubbard.")
                return_previous_room = False


        #play again option
        user_choice = input("\nDo you want to play again? (y/n):")
        user_choice =str.lower(user_choice)
        if user_choice == "y":
            play_again = True
        elif user_choice == "n":
            print("""\n“Maybe there are times when one should welcome defeat, tell it to come right in and sit down.”
― Iris Murdoch,""")
            play_again = False
                

if __name__ == "__main__":
    main()
    

