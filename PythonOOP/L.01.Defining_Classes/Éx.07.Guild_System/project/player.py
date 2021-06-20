class Player:

    def __init__(self, player_name, hp, mp):
        self.player_name = player_name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return f'Skill already added'
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.player_name}"

    def player_info(self):
        res = (f"Name: {self.player_name}\n"
               f"Guild: {self.guild}\n"
               f"HP: {self.hp}\n"
               f"MP: {self.mp}\n")
        res += "\n".join(f'==={s} - {m}\n' for s, m in self.skills.items())

        return res
