class Character:
    def __init__(self):
        self.name="Nagibator"
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()

QUEST_SPEAK, QUEST_HUNT, QUEST_CARRY = "QSPEAK", "QHUNT", "QCARRY"

class Event:
    def __init__(self, kind):
        self.kind = kind

class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor
        
    def handle(self, char, event):
        if self.__successor is not None:
            self.__successor.handle(char, event)

class QuestSpeak(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_SPEAK:
            quest_name = "Speak to farmer"
            xp = 100
            if quest_name not in (char.passed_quests | char.taken_quests):
                print("Quest has been taken: {}".format(quest_name))

                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print("Quest has been passed through: {}".format(quest_name))
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print("Passing event further")
            super().handle(char, event)

class QuestHunt(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_HUNT:
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
        else:
            print("Passing event further")
            super().handle(char, event)

class QuestCarry(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_CARRY:
            quest_name = "Carry logs"
            xp = 300
            if quest_name not in (char.passed_quests | char.taken_quests):
                print("Quest has been taken: {}".format(quest_name))

                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print("Quest has been passed through: {}".format(quest_name))
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print("Passing event further")
            super().handle(char, event)

class QuestGiver:
    def __init__(self):
        self.handlers = QuestCarry( QuestHunt(QuestSpeak(NullHandler)) )
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_quests(self, character):
        for event in self.events:
            self.handlers.handle(character, event) 
                
    def remove_quest(self, quest):
        self.quests.remove(quest)

events = [Event(QUEST_CARRY), Event(QUEST_HUNT), Event(QUEST_SPEAK)]

quest_giver = QuestGiver()

for event in events:
    quest_giver.add_event(event)

player = Character()
quest_giver.handle_quests(player)

player.taken_quests = {"Rat hunting", "Bring logs"}
print("-----------")
quest_giver.handle_quests(player)
