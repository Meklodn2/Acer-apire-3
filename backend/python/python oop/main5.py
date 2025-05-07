# Abstraction (Abstraksiya)

# ABC - Abstact base class
from abc import ABC,abstractmethod

class WashingMachine(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class MyWashingMachine(WashingMachine):
    def start(self):
        print("washing machine started.")
    def stop(self):
        print("washing machine stopped.")


wm = MyWashingMachine()
wm.start()
wm.stop()
wm1 =WashingMachine()