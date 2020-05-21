from abc import ABC, abstractmethod

class HeroFactory(ABC):

    @abstractmethod
    def create_hero(self, name):
        pass

    @abstractmethod
    def create_spell(self):
        pass

    @abstractmethod
    def create_weapon(self):
        pass

class WarriorFactory(HeroFactory):
    def create_hero(self, name):
        return Warrior(name)

    def create_spell(self):
        return Power()

    def create_weapon(self):
        return Claymore()

class MageFactory(HeroFactory):
    def create_hero(self, name):
        return Mage(name)

    def create_spell(self):
        return Fireball()

    def create_weapon(self):
        return Staff()

class AssassinFactory(HeroFactory):
    def create_hero(self, name):
        return Assassin(name)

    def create_spell(self):
        return Invisible()

    def create_weapon(self):
        return Dagger()


class Warrior:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print("WARRIOR {} hits with {}".format(self.name, self.weapon.hit()))

    def cast(self):
        print("WARRIOR {} casts {}".format(self.name, self.spell.cast()))

class Mage:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print("Mage {} hits with {}".format(self.name, self.weapon.hit()))

    def cast(self):
        print("Mage {} casts {}".format(self.name, self.spell.cast()))

class Assassin:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print("Assassin {} hits with {}".format(self.name, self.weapon.hit()))

    def cast(self):
        print("Assassin {} casts {}".format(self.name, self.spell.cast()))


class Claymore:
    def hit(self):
        return "Claymore"

class Dagger():
    def hit(self):
        return "Dagger"

class Staff():
    def hit(self):
        return "Staff"

class Power():
    def cast(self):
        return "Power"

class Invisible():
    def cast(self):
        return "Invisibility"

class Fireball():
    def cast(self):
        return "Fireball"



def create_hero(factory):
    hero = factory.create_hero("Nagibator")

    weapon = factory.create_weapon()
    spell = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(spell)

    return hero

player = create_hero(AssassinFactory())
player.hit()
player.cast()


