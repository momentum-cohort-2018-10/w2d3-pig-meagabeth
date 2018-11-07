import random

class Die:

    def __init__(self, side, number_sides):
        """
        This defines the parameters of class Die.
        """
        self.side = side
        self.number_sides = number_sides

    def roll_die(self):  
        """
        Chooses a random integer between 1 & 6 when the die is rolled.
        """
        roll = random.randint(1, 6)
        return roll

    def value_of_side(self):
        """
        This determines the return value of which side is rolled.
        """
        roll = random.randint(1, 6)
        if roll > 1:
            return roll
        else:
            print("You rolled a 1. Your turn is over.")
            return 
        

class Player:

    def __init__(self):
        """
        This defines the parameters of class Player.
        """
        

    def player_rolls_die(self):
        """
        This function acts as the player rolling the die and returns the value of the side of the die that it stopped on.
        """
        
    def roll_or_pass(self):
        """
        This function prompts user to choose if they want to roll again or pass(ending their turn).
        """


class Game:

    def __init__(self):
        self.self = self

    def first_player(self):
        """
        The first player is chosen randomly. (For example, you could flip a coin or both roll a die and pick the higher roll.)
        """
        players = ["human", "computer"]
        goes_first = random.choice(players)
        print(goes_first + " will go first.")
        return 

    def  display_score(self):
        """
        At the end of each player's turn, display each player's current total score.
        """

    def play_again(self):
        """
        When a player wins, the game is over. Prompt the user to play again.
        """