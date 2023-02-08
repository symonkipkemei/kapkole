import time
import random
import requests



class Opponent:
    """Generate a game play for the opponent
    """

    def __init__(self,name, strength) -> None:
        """create instance variables
        """
        self.name = name
        self.strength = strength
        

class Hero:
    "Generates a gameplay of the hero"

    def __init__(self,name) -> None:
        self.name = name
        self.arsenal = {"banana":1, "apple" : 1, "mangoes":1}
        self.key = 0
        self.head_count = 0

    def collect(self):
        """Allow the player to randomly select an item from the possible arsenals
        """
        # abstract collection from Hero's possible arsenals into a list
        collections = [arsenal for arsenal in self.arsenal.keys()]
        #randomly select an item from the dictionary
        choice = random.choice(collections)


        #display to the user
        print(f"\nYou have found a {choice}!")
        print("****************")
        print("(1).Take it\n(2).Leave it")
        print("****************")
        user_option = int(input("Your choice: "))
        if user_option == 1:
                self.arsenal[choice] += 1

    def decollect(self):
        "decollect all the arsenal whenever the player is defeated"
        for key in self.arsenal.keys():
            self.arsenal[key] = 0

    def attack(self, other) -> bool:
        """Hero attacks the opponent. Winning is based on the strength of the opponent and the dice outcome 

        Args:
            other (_type_): Opponent Object

        Returns:
            bool: True if Hero wins
        """
        # roll dice to detrmine the winner between self and other opponent
        try_again = True
        while try_again:
            
            #possible outcomes
            ansA = random.randint(1,6)
            ansB = random.randint(1,6)

            #it becomes harder to defeat opponents with more strength, the dice is rigged 😊, your win is based on pure luck.
            ansB = ansB + other.strength
            if ansB > 6:
                ansB = 6
    

            print(f"{self.name} rolls dice; outcome: {ansA}")
            print(f"{other.name} rolls dice; outcome: {ansB }")

            #build anxiety
            time.sleep(5)


            if ansA  > ansB:
                winner = self.name
                loser = other.name
                try_again = False
                # the hero indeed becomes an hero
                hero = True
            elif  ansB == ansA:
                print(f"\n{self.name} tied with {other.name}, redoing the roll\n")
                time.sleep(3)
                print("....................")
                try_again = True
            else:
                winner = other.name
                loser = self.name
                try_again = False
                # the hero is defeated
                hero = False

        print(f"\nCongratulations {winner},you defeated {loser}🤕🤕🥵🤕🤕🤕 !")

        return hero

 
# display door options available
def door_choices(doors:dict) -> str:
    """Allows the player to make a choice between the available doors:
    Returns:
        str: the value pair of the chosen door
    """
    #easily retrieve door names using dictionaries keys
    print(f"\nThere are {len(doors.items())} caves")
    for index, x in doors.items():
        print(f"{index}. {x}")
    door_choice = input("\nMake your choice:")
    print("\n")
    if door_choice.isdigit():
            door_choice = int(door_choice)
    else:
        print("the option is not available,try again")
    return doors[door_choice]

# welcoming the user
def player_name() -> str:
    """Collect user_name and welcome him/her to the game, assign the player a random name from the api

    Returns:
        str: name from the api
    """

    # The name of the player
    player = input("What's your name ? : ")
    player = str.capitalize(player)

    # give the player a new name from API
    max_len = 10
    min_len = 5
    base_url = f"https://uzby.com/api.php?min={min_len}&max={max_len}"

    response = requests.get(base_url)
    response = response.text

    print( f"Hello {player},\nyour warrior name is {response}\n")

    #The welcome message
    print("________________________________")
    print("(◕‿◕)THE CAVES OF KAPKOLE(◕‿◕)")
    print("________________________________")
    print(f"""Hi {response},
The princess of Kapkole Kingdom is stuck in
the caves with dungeons and dragons (~_~).
Fortunately, she is still alive.
You've been entrusted to find and 
bring her home.
________________________________
      """)


    time.sleep(5)

    return response



if __name__ == "__main__":
    pass