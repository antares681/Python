from Ex05_Shop.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if not player.guild == self.name and not player.guild == 'Unaffiliated':
            return f'Player {player.player_name} is in another guild.'
        filtered_player = [p for p in self.players if p == player.player_name]
        if filtered_player:
            return f'Player {player.player_name} is already in the guild.'
        self.players.append(player.player_name)
        player.guild = self.name
        return f'Welcome player {player.player_name} to the guild {self.name}'

    def kick_player(self, pl_name):
        filtered_player = [p for p in self.players if p == pl_name]
        if not filtered_player:
            return f"Player {pl_name} is not in the guild."
        pl = filtered_player[0]
        self.players.remove(pl)
        player.player_info = 'Unaffiliated'
        return f"Player {pl_name} has been removed from the guild."

    def guild_info(self):
        to_return = f'Guild: {self.name}\n'
        for p in self.players:
            to_return += player.player_info()
        return to_return


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())