def someAction_Decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("something else")

    return wrapper


class someAction_ClassDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self.func(self, *args, **kwargs)
        print("something else")


class ConcreteObject(object):
    @someAction_Decorator
    def someAction(self):
        print("something")


class ConcreteObject2(object):
    @someAction_ClassDecorator
    def someAction(self):
        print("something")


class ConcreteObject3(object):
    def someAction(self):
        print("something")


if __name__ == "__main__":
    obj = ConcreteObject()
    obj.someAction()

    obj2 = ConcreteObject2()
    obj2.someAction()
