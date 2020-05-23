import yaml

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

hero_yaml = '''
--- !Character1
factory:
    !factory assassin
name:
    7Nagibat0R

'''

def factory_constructor(loader, node):
    data = loader.construct_scalar(node)

    if data == "assassin":
        return AssassinFactory
    if data == "mage":
        return MageFactory
    else:
        return WarriorFactory


class Character1(yaml.YAMLObject):
    yaml_tag = "!Character1"

    def create_hero(self):
        hero = self.factory.create_hero(self.name)

        weapon = self.factory.create_weapon()
        spell = self.factory.create_spell()

        hero.add_weapon(weapon)
        hero.add_spell(spell)

        return hero

yaml.Loader.add_constructor("!factory", factory_constructor)
hero = yaml.load(hero_yaml).create_hero()

hero.hit()
hero.cast()


