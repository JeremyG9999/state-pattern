from abc import ABC, abstractmethod
class Context:
    def __init__(self, state):
        self.state = state
    def change_state(self, state):
        self.state = state
    def freezes(self):
        self.state.freeze(self)
    def melts(self):
        self.state.melt(self)
    def evaporates(self):
        self.state.evaporate(self)
class State(ABC):
    @abstractmethod
    def freeze(self, context):
        pass
    @abstractmethod
    def melt(self, context):
        pass
    @abstractmethod
    def evaporate(self, context):
        pass
class Solid(State): #concrete state
    def freeze(self, context):
        print("Already a solid")
    def melt(self, context):
        print("Melting to a Liquid")
        context.change_state(Liquid())
    def evaporate(self, context):
        context.change_state(Gas())
        print("We shall sublime instead")
class Liquid(State): #concrete state
    def freeze(self, context):
        print("Freeze to a Solid")
        context.change_state(Solid())
    def melt(self, context):
        print("Already a Liquid")
    def evaporate(self, context):
        print("Evaporate to a Gas")
        context.change_state(Gas())
class Gas(State): #concrete state
    def freeze(self, context):
        print("Deposition to a solid")
        context.change_state(Solid())
    def melt(self, context):
        print("We shall do condensation instead")
        context.change_state(Liquid())
    def evaporate(self, context):
        print("Already a Gas")
def main():
    context = Context(Solid())
    context.freezes()  
    context.melts()  
    context.evaporates()
    context.freezes()
main()