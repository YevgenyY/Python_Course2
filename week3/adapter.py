import re
from abc import ABC, abstractmethod

class System:
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    # processor = adapter
    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        #print(*result, sep = '\n')
        return result

class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text):
        pass

# this class is an adaptee - processor to adapt
class WordCounter:
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()

# The adapter
class WordCounterAdapter(TextProcessor):
    # adaptee = counter 
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()

        result = sorted(words, 
                key = lambda x: self.adaptee.get_count(x),
                reverse = True)

        return result


text = "A knife (plural knives; possibly from Old Norse knifr (blade)[1]) is a tool with a cutting edge or blade often attached to a handle or hilt. One of the earliest tools used by mankind, knives appeared at least two-and-a-half million years ago, as evidenced by the Oldowan tools.[2][3] Originally made of wood, bone, and stone (such as flint and obsidian), over the centuries, in step with improvements in both metallurgy and manufacturing, knife blades have been made from copper, bronze, iron, steel, ceramic, and titanium. Most modern knives have either fixed or folding blades; blade patterns and styles vary by maker and country of origin. Knives can serve various purposes. Hunters use a hunting knife, soldiers use the combat knife, scouts, campers, and hikers carry a pocket knife; there are kitchen knives for preparing foods (the chefs knife, the paring knife, bread knife, cleaver), table knives (butter knives and steak knives), weapons (daggers or switchblades), knives for throwing or juggling, and knives for religious ceremony or display (the kirpan)."

system = System(text)
counter = WordCounter()
adapter = WordCounterAdapter(counter)

res = system.get_processed_text(adapter)

print(res)


