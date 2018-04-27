from abc import ABC, abstractmethod


class State(ABC):

    def __init__(self, state_data):
        self.state_data = state_data

    @abstractmethod
    def __repr__(self):
        pass

    @classmethod
    def create_State(cls, state_data):
        return cls.__init__(state_data)

    @staticmethod
    def equals(state_a, state_b):
        pass

    @staticmethod
    def __hash__(self):
        pass