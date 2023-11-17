# clase abstracta

from abc import ABC , abstractclassmethod

class Futbolista(ABC):

    @abstractclassmethod
    def get_name(self):
        ...
    @abstractclassmethod
    def hablar_sin_s(self):
        ...
