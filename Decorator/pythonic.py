class ConcreteObject(object):
    def someAction(self):
        print("something")


def someAction_Decorator(obj):
    # This is important instead of using
    # obj.someAction in the wrapper function
    # for a recursion problem
    func = obj.someAction

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("something else ")

    # Monkey patching
    obj.someAction = wrapper


if __name__ == "__main__":
    obj = ConcreteObject()
    someAction_Decorator(obj)
    obj.someAction()
