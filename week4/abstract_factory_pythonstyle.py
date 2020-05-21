class HeroFactory:

    @classmethod
    def create_hero(Class, name):
        return Class.Hero(name)

    @classmethod
    def create_weapon(Class):
        return Class.Weapon()

    @classmethod
    def create_spell(Class):
        return Class.Spell()

class WarriorFactory(HeroFactory):
    class Hero:
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

    class Spell():
        def cast(self):
            return "Power"

    class Weapon:
        def hit(self):
            return "Claymore"

class MageFactory(HeroFactory):
    class Hero:
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

    class Weapon():
        def hit(self):
            return "Staff"

    class Spell():
        def cast(self):
            return "Fireball"


class AssassinFactory(HeroFactory):
    class Hero:
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

    class Weapon():
        def hit(self):
            return "Dagger"

    class Spell():
        def cast(self):
            return "Invisibility"



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


