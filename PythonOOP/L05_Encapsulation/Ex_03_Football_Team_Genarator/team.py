from Ex_03_Football_Team_Genarator.player import Player

class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        for plr in self.__players:
            if player.name == plr.name:
                return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player):
        for plr in range(len(self.__players)):
            if self.__players[plr].name == player:
                return self.__players.pop(plr)
        return (f"Player {player} not found")