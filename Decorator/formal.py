class ObjectClassInterface(object):
    def someAction(self):
        pass


class ConcreteObject(ObjectClassInterface):
    def someAction(self):
        print("something")


class Decorator(ObjectClassInterface):
    def __init__(self, obj: ObjectClassInterface):
        self.obj = obj

    def someAction(self):
        self.obj.someAction()
        print("something else")


if __name__ == "__main__":
    obj = ConcreteObject()
    decorator = Decorator(obj)
    decorator = Decorator(decorator)
    decorator.someAction()
