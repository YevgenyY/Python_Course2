class Character:
    def __init__(self):
        self.name="Nagibator"
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()

def add_quest_speak(char):
    quest_name = "Talk to farmer"
    xp = 100
    if quest_name not in (char.passed_quests | char.taken_quests):
        print("Quest has been taken: {}".format(quest_name))

        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print("Quest has been passed through: {}".format(quest_name))
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp

def add_quest_hunt(char):
    quest_name = "Rat hunting"
    xp = 300
    if quest_name not in (char.passed_quests | char.taken_quests):
        print("Quest has been taken: {}".format(quest_name))

        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print("Quest has been passed through: {}".format(quest_name))
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp

def add_quest_carry(char):
    quest_name = "Bring logs"
    xp = 200
    if quest_name not in (char.passed_quests | char.taken_quests):
        print("Quest has been taken: {}".format(quest_name))

        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print("Quest has been passed through: {}".format(quest_name))
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp

class QuestGiver:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def handle_quests(self, character):
        for quest in self.quests:
            quest(character) 
                
    def remove_quest(self, quest):
        self.quests.remove(quest)

all_quests = [add_quest_carry, add_quest_hunt, add_quest_speak]
quest_giver = QuestGiver()

for quest in all_quests:
    quest_giver.add_quest(quest)

player = Character()

quest_giver.handle_quests(player)

player.taken_quests = {"Rat hunting", "Bring logs"}
quest_giver.handle_quests(player)
print("-----------")
quest_giver.handle_quests(player)
