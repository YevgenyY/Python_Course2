EV_GET, EV_SET = 0, 1

class EventGet:
    def __init__(self, kind):
        self.kind = kind
        self.ev_type = EV_GET
        
class EventSet:
    def __init__(self, kind):
        self.kind = kind
        self.ev_type = EV_SET

class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj=None, event=None):
        if isinstance(self, NullHandler):
            if self.__successor is not None:
                return self.__successor.handle(obj, event)

class IntHandler(NullHandler):
    def handle(self, obj=None, event=None):
        if obj == None or event == None:
            return

        if event.ev_type == EV_GET:
            if isinstance(event.kind(), int):
                return obj.integer_field
        elif event.ev_type == EV_SET:
            if issubclass(type(event.kind), int):
                obj.integer_field = event.kind

        #print("IntHandler: Passing the event further")
        return super().handle(obj, event)

class StrHandler(NullHandler):
    def handle(self, obj=None, event=None):
        if obj == None or event == None:
            return

        if event.ev_type == EV_GET:
            if isinstance(event.kind(), str):
                return obj.string_field
        elif event.ev_type == EV_SET:
            if issubclass(type(event.kind), str):
                obj.string_field = event.kind
        
        #print("StrHandler: Passing the event further")
        return super().handle(obj, event)

class FloatHandler(NullHandler):
    def handle(self, obj=None, event=None):
        if obj == None or event == None:
            return

        if event.ev_type == EV_GET:
            if isinstance(event.kind(), float):
                return obj.float_field
        elif event.ev_type == EV_SET:
            if issubclass(type(event.kind), float):
                obj.float_field = event.kind

        #print("FloatHandler: Passing the event further")
        return super().handle(obj, event)


