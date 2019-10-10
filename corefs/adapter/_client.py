from utils import _logging


class Client():

    def __init__(self, name):
        self.name = name
        self.log = _logging.create_logger(self.__class__.__name__, True)
        self.log.info("Init %s", name)
        self.observers = dict()

    def run(self):
        raise NotImplementedError(
            "Method \"run\" of class " + self.__class__.__name__ + " not implemented.")

    def register(self, event, callback):
        if event not in self.observers:
            self.observers[event] = []
        self.observers[event].append(callback)

    def deregister(self, event, callback):
        if event in self.observers:
            callbacks = self.observers[event]
            for cb in callbacks:
                if cb == callback:
                    self.observers[event].remove(callback)

    def notify(self, event, *args):
        self.log.debug("Event (%d) with %s", event, args)
        if event in self.observers:
            for cb in self.observers[event]:
                cb(*args)
