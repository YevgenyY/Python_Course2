from abc import ABC, abstractmethod

class Engine:
    def __init__(self, *args, **kwargs):
        pass

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
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message["title"])

class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        super().__init__()
        self.achievements = []


    def update(self, message):
        for msg in self.achievements:
            if msg["title"] == message["title"]:
                return

        self.achievements.append(message)

observer = ObservableEngine("ObservableEngine")

short1 = ShortNotificationPrinter()
short2 = ShortNotificationPrinter()

full1= FullNotificationPrinter()
full2= FullNotificationPrinter()

observer.subscribe(short1)
observer.subscribe(full1)
observer.subscribe(short2)
observer.subscribe(full2)

msg1 = { "title": "Conqueror", "text": "Given on reaching all the game goals"}
msg2 = { "title": "Conqueror", "text": "Given on reaching all the game goals"}
observer.notify(msg1)
observer.notify(msg2)

observer.unsubscribe(short1)
observer.unsubscribe(full1)
observer.unsubscribe(full2)
