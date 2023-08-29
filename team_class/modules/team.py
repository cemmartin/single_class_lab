# Create a class called Team that has the properties properties name (str), players (list of strs) and a coach (str).
# Create an __init__ method that takes in a name (str), a list of player names (as strs) and a coach(str) to initialise the properties when a new team is created.

# Create a method add_player that takes in a string of a new 
# players's name and adds that new player to the players list.

# Add a method has_player that takes in a string of a player's 
# name and checks to see if they are in the players list. It 
# should return True if the player's name is in the list and 
# False otherwise.

class Team:
    def __init__(self, input_name, input_list_of_players, input_coach): #it's a list, so when we add new players, just need to append
        self.name = input_name
        self.players = input_list_of_players
        self.coach = input_coach

    def add_player(self, new_players):
        self.players.append(new_players)

    def has_player(self, existing_player):
        for players in self.players: #why is this self & not team
            if existing_player == players:
                return True
        return False #needs to be outside the function














