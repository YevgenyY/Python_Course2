class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""

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

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)

class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.ev_type == EV_GET:
            if isinstance(event.kind(), int):
                return obj.integer_field
        elif event.ev_type == EV_SET:
            if issubclass(type(event.kind), int):
                obj.integer_field = event.kind

        #print("IntHandler: Passing the event further")
        return super().handle(obj, event)

class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.ev_type == EV_GET:
            if isinstance(event.kind(), str):
                return obj.string_field
        elif event.ev_type == EV_SET:
            if issubclass(type(event.kind), str):
                obj.string_field = event.kind
        
        #print("StrHandler: Passing the event further")
        return super().handle(obj, event)

class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.ev_type == EV_GET:
            if isinstance(event.kind(), float):
                return obj.float_field
        elif event.ev_type == EV_SET:
            if issubclass(type(event.kind), float):
                obj.float_field = event.kind

        #print("FloatHandler: Passing the event further")
        return super().handle(obj, event)

chain = IntHandler(StrHandler(FloatHandler(NullHandler())))

obj = SomeObject()
obj.integer_field = 43
obj.string_field = "Initialized"
obj.float_field = 0.07

"""
inthand = IntHandler(None)
print( inthand.handle(obj, EventGet(int)) )

inthand.handle(obj, EventSet(10))
print( inthand.handle(obj, EventGet(int)) )

strhand = StrHandler(None)
print( strhand.handle(obj, EventGet(str)) )

strhand.handle(obj, EventSet("It works"))
print( strhand.handle(obj, EventGet(str)) )

floathand = FloatHandler(None)
print( floathand.handle(obj, EventGet(float)) )
floathand.handle(obj, EventSet(0.007))
print( floathand.handle(obj, EventGet(float)) )
"""

print("------------- Chain work ------------")
print (chain.handle(obj, EventGet(str)))
print(chain.handle(obj, EventGet(int)))
print(chain.handle(obj, EventGet(float)))
print("------------- Chain changed values ------------")
chain.handle(obj, EventSet(7))
chain.handle(obj, EventSet("It works"))
chain.handle(obj, EventSet(0.0000007))
print (chain.handle(obj, EventGet(str)))
print(chain.handle(obj, EventGet(int)))
print(chain.handle(obj, EventGet(float)))

