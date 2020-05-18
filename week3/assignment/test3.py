from abc import ABC, abstractmethod

class AbstractObserver(ABC):
    def __init__(self, name="ABO"):
        self.__name = name

    @abstractmethod
    def update(self):
        pass

class ObservableEngine(Engine):
    def __init__(self, name="ObservableEngine"):
        super().__init__()
        self.__subscribers = []
        self.__name = name

    def subscribe(self, subscriber):
        for obj in self.__subscribers:
            if hash(obj) == hash(subscriber):
                return

        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for obj in self.__subscribers:
            obj.update(message)

class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        super().__init__()
        #self.__name = name
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message["title"])
        #print("{}: received {}".format(self.__name, message["title"]))

class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        super().__init__()
        #self.__name = name
        self.achievements = []


    def update(self, message):
        for msg in self.achievements:
            if msg["title"] == message["title"]:
                return

        self.achievements.append(message)
        #print("{}: received {}, description {}".format(self.__name, message["title"], message["text"]))


