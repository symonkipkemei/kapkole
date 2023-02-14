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
            anshero = random.randint(1,6)
            ansopp = random.randint(1,6)

            #it becomes harder to defeat opponents with more strength, the dice is rigged 😊, your win is based on pure luck.
            ansopp = ansopp + self.strength
            if ansopp > 6:
                ansopp = 6
            elif ansopp < 1:
                ansopp = 1
    

            print(f"{self.name} rolls dice; outcome: {ansopp}")
            print(f"{other.name} rolls dice; outcome: {anshero }")

            #build anxiety
            time.sleep(5)


            if anshero  > ansopp:
                winner = other.name
                loser = self.name
                try_again = False
                # the hero indeed becomes an hero
                hero = True
            elif  ansopp == anshero:
                print(f"\n{self.name} tied with {other.name}, redoing the roll\n")
                time.sleep(3)
                print("....................")
                try_again = True
            else:
                winner = self.name
                loser = other.name
                try_again = False
                # the hero is defeated
                hero = False

        print(f"\nCongratulations {winner},you defeated {loser}🤕🤕🥵🤕🤕🤕 !")

        return hero

    def decollect(self,other):
        "decollect all the arsenal whenever the player is defeated"
        for key in other.arsenal.keys():
            other.arsenal[key] = 0


class Boss(Opponent):
    "Mega opponent"
    def __init__(self, name:str, strength:int,arsenal:dict,keys:int,heads:int) -> None:
        super().__init__(name, strength)
        self.arsenal = arsenal
        self.key = keys
        self.heads =heads

    def welcome_hero(self,other):
        custodian_fruits= [fruits for fruits in self.arsenal.keys()]
        # arsenal needed by custodian
        custodian_needs ={}
        for fruit in custodian_fruits:
            custodian_needs[fruit] = random.randint(1,3)

        print("LOCKED CAVE")
        print("__________________________________________________________________________________")
        print(f"Hi {other.name}\n\nI am a {self.name} 🐒🐒🐒 ,custodian of the locked cave.\nTo enter this cave,you need:\n")
        print("**********************************************************")
        print(f"collections🍓 : {custodian_needs}")
        print(f"opponents_beheaded 💀: {self.heads}")
        print("**********************************************************")
        print("OR")
        print("**********************************************************")
        print(f"keys 🔑 : {self.key}")
        print("__________________________________________________________________________________")

    def attack(self,other):
        print("\n👏👏👏👏👏")
        time.sleep(2)
        print("👏👏👏👏👏✨✨✨")
        time.sleep(3)
        print("✨✨✨")
        print(f"You died as a result of injuries from the baboon {other.name}")

class WeakOpponent(Opponent):
    def attack(self, other) -> bool:


        return super().attack(other)

class Hero:
    "Generates a gameplay of the hero"

    def __init__(self,name:str,arsenal:dict) -> None:
        self.name = name
        self.arsenal = arsenal
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