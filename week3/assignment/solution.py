# =============================================================================
# Скрипт для тестирования решений студентов по заданию "Создание декоратора
# класса" (тесты содержат примеры, приведенные в описании задания)
# https://stepik.org/lesson/106937/step/4?unit=81460
# Скопируйте код вашего решения в секцию ВАШ КОД и запустите скрипт
# =============================================================================
from abc import ABC, abstractmethod

class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


# =============================================================================
# начало секции ВАШ КОД
# =============================================================================
from abc import ABC, abstractmethod

#1 Abstract decorator class
class AbstractEffect(Hero):
    def __init__(self, base):
        self.base = base
        self.stats = self.base.stats
        self.positive_effects = [] #self.base.positive_effects
        self.negative_effects = [] #self.base.negative_effects
        self.stats = dict() #base.stat.copy()

        # init stats
        for k in self.base.stats.keys():
            self.stats[k] = 0

        self.apply_effects()

        @abstractmethod
        def apply_effects(self):
            pass

    def get_positive_effects(self):
        return self.positive_effects + self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.negative_effects + self.base.get_negative_effects()

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
class Blessing:
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

        self.positive_effects.append("Weakness")


   

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

if __name__ == '__main__':
    # создадим героя
    hero = Hero()
    # проверим правильность характеристик по-умолчанию
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    # проверим список отрицательных эффектов
    assert hero.get_negative_effects() == []
    # проверим список положительных эффектов
    assert hero.get_positive_effects() == []
    # наложим эффект Berserk
    brs1 = Berserk(hero)
    # проверим правильность изменения характеристик
    #print(brs1.get_stats())
    assert brs1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 22,
                                'Perception': 1,
                                'Endurance': 15,
                                'Charisma': -1,
                                'Intelligence': 0,
                                'Agility': 15,
                                'Luck': 8}
    # проверим неизменность списка отрицательных эффектов
    #print(brs1.get_negative_effects())
    assert brs1.get_negative_effects() == []
    # проверим, что в список положительных эффектов был добавлен Berserk
    #print(brs1.get_positive_effects())
    assert brs1.get_positive_effects() == ['Berserk']
    # повторное наложение эффекта Berserk
    brs2 = Berserk(brs1)
    # наложение эффекта Curse
    cur1 = Curse(brs2)
    # проверим правильность изменения характеристик
    #print(cur1.get_stats())
    assert cur1.get_stats() == {'HP': 228,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 27,
                                'Perception': -4,
                                'Endurance': 20,
                                'Charisma': -6,
                                'Intelligence': -5,
                                'Agility': 20,
                                'Luck': 13}
    # проверим правильность добавления эффектов в список положительных эффектов
    #print(cur1.get_positive_effects())
    assert cur1.get_positive_effects() == ['Berserk', 'Berserk']
    # проверим правильность добавления эффектов в список отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # снятие эффекта Berserk
    cur1.base = brs1
    # проверим правильность изменения характеристик
    #print("--------- brs1 ----------")
    #print(brs1.get_positive_effects())
    """
    assert cur1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 20,
                                'Perception': -1,
                                'Endurance': 13,
                                'Charisma': -3,
                                'Intelligence': -2,
                                'Agility': 13,
                                'Luck': 6}
    """
    # проверим правильность удаления эффектов из списка положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk']
    # проверим правильность эффектов в списке отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # проверим незменность характеристик у объекта hero
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    print('All tests - OK!')
