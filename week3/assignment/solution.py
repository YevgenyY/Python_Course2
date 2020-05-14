# =============================================================================
# начало секции ВАШ КОД
# =============================================================================
from abc import ABC, abstractmethod

#1 Abstract decorator class
class AbstractEffect(Hero, ABC): 
    
    @abstractmethod
    def apply_effects(self):
        pass

    def __init__(self, base):
        #super().__init__()

        self.base = base
        self.stats = self.base.stats
        self.positive_effects = [] #self.base.positive_effects
        self.negative_effects = [] #self.base.negative_effects
        self.stats = dict() #base.stat.copy()

        # init stats
        for k in self.base.stats.keys():
            self.stats[k] = 0

        self.apply_effects()


    def get_positive_effects(self):
        return self.base.get_positive_effects() + self.positive_effects

    def get_negative_effects(self):
        return self.base.get_negative_effects() + self.negative_effects

    def get_stats(self):
        # calculate stats
        res = self.base.get_stats()
        for k in self.stats.keys():
            res[k] += self.stats[k]

        return res

#2 Abstract Positive effects
class AbstractPositive(AbstractEffect):
    def apply_effects(self):
        self.incMainChars()

    @abstractmethod
    def incMainChars():
        pass

#3 Abstract Negative effects
class AbstractNegative(AbstractEffect):
    def apply_effects(self):
        self.decMainChars()

    @abstractmethod
    def decMainChars(self):
        pass


"""4 Increases: Strength, Endurance, Agility, Luck by 7
   Decreases: Perception, Charisma, Intelligence by 3
   Increases HP by 50
"""
class Berserk(AbstractPositive):

    def incMainChars(self):
        for k in self.stats.keys():
            if k == "Strength" or k == "Endurance" or k == "Agility" or k == "Luck":
                self.stats[k] = 7

            if k == "Perception" or k == "Charisma" or k == "Intelligence":
                self.stats[k] = -3
        
        self.stats["HP"] = 50
        self.positive_effects.append("Berserk")



"""5 Increases: everything by 2
"""
class Blessing(AbstractPositive):
    def incMainChars(self):
        for k in self.stats.keys():
            if k != "HP" and k != "MP" and k != "SP":
                self.stats[k] = 2

        self.positive_effects.append("Blessing")



""": 6 Decreases: Strength, Endurance, Agility by 4 
"""
class Weakness(AbstractNegative):
     def decMainChars(self):
        for k in self.stats.keys():
            if k == "Strength" or k == "Endurance" or k == "Agility":
                self.stats[k] = -4

        self.negative_effects.append("Weakness")


   

"""7 Decreases: everything by 2
"""
class Curse(AbstractNegative):
    def decMainChars(self):
        for k in self.stats.keys():
            if k != "HP" and k != "MP" and k != "SP":
                self.stats[k] = -2

        self.negative_effects.append("Curse")


"""8 Decreases: Luck by 10
"""
class EvilEye(AbstractNegative):
    def decMainChars(self):
        self.stats["Luck"] = -10

        self.negative_effects.append("EvilEye")

# Поместите в этой секции реализацию классов AbstractEffect, AbstractPositive,
# AbstractNegative, Berserk, Blessing, Curse, EvilEye, Weakness из вашего
# решения
# =============================================================================
# конец секции ВАШ КОД
# =============================================================================

