from modules.team import Team

players = ["Derice Bannock", "Sanka Coffie", "Junior Bevil", "Yul Brenner"]
team = Team("Cool Runnings", players, "Irv Blitzer") #this contains a class

team.add_player("Mary Earps")
print(team.__dict__)


print(team.has_player("Junior Bevil"))  # True
print(team.has_player("Usain Bolt"))  # False

team.add_player("Roger")
print(team.has_player("Roger"))  # True

# team.play_game(True)
# print(team.points)  # 3

# team.play_game(False)
# print(team.points)  # 3
