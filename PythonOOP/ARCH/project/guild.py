from player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if not player.guild == self.name and not player.guild == 'Unaffiliated':
            return f"Player {self.name} is in another guild."
        player.guild = self.name
        current_player = [p for p in self.players if p == player]

        if current_player:
            return f"Player {player.name} is already in the guild."
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name in self.players:
            self.players.remove(player_name)
            Player.guild = 'Unaffiliated'
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        res = f"Guild: {self.name}\n"
        # res += f"{Player.player_info()}"
        return res
player_1 = Player("George", 50, 100)
print(player_1.add_skill("Shield Break", 20))
print(player_1.player_info())
guild = Guild("UGT")
print(guild.assign_player(player_1))
print(guild.guild_info())
# print('***********************************************************************')
# player_2 = player.Player("Pepo", 50, 100)
# print(player_2.add_skill("Shield Break", 20))
# print(player_2.player_info())
# guild = Guild("BBB")
# print(guild.assign_player(player_2))
# print(guild.guild_info())
# print('***********************************************************************')
# player_3 = player.Player("GePO", 50, 100)
# print(player_3.add_skill("Shield Break", 20))
# print(player_3.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player_3))
# print(guild.guild_info())
# import unittest
#
#
# class PlayerTest(unittest.TestCase):
#
#     def test_player_init(self):
#         player = Player("Pesho", 90, 90)
#         expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n"
#         self.assertEqual(player.player_info(), expected)
#
#     def test_adding_skill_should_work(self):
#         player = Player("Pesho", 90, 90)
#         message = player.add_skill("A", 3)
#         expected = "Skill A added to the collection of the player Pesho"
#         self.assertEqual(message, expected)
#
#     def test_adding_existing_skill_should_not_work(self):
#         player = Player("Pesho", 90, 90)
#         player.add_skill("A", 3)
#         message = player.add_skill("A", 3)
#         expected = "Skill already added"
#         self.assertEqual(message, expected)
#
#     def test_info(self):
#         player = Player("Pesho", 90, 90)
#         player.add_skill("A", 3)
#         message = player.player_info()
#         expected = "Name: Pesho\nGuild: Unaffiliated\nHP: 90\nMP: 90\n===A - 3\n"
#         self.assertEqual(message, expected)
#
#     def test_guild_init(self):
#         guild = Guild("GGXrd")
#         message = guild.guild_info()
#         expected = "Guild: GGXrd\n"
#         self.assertEqual(message, expected)
#
#     def test_assign_working(self):
#         guild = Guild("GGXrd")
#         player = Player("Pesho", 90, 90)
#         message = guild.assign_player(player)
#         expected = "Welcome player Pesho to the guild GGXrd"
#         self.assertEqual(message, expected)
#
#     def test_assigning_player_in_the_same_guild(self):
#         guild = Guild("GGXrd")
#         player = Player("Pesho", 90, 90)
#         guild.assign_player(player)
#         message = guild.assign_player(player)
#         expected = "Player Pesho is already in the guild."
#         self.assertEqual(message, expected)
#
#
# if __name__ == '__main__':
#     unittest.main()
#



