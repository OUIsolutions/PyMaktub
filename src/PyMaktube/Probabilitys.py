
import ctypes
from typing_extensions import Callable, List, Union
from .ctypes import loader

class Probability:

    def __init__(self,generation_object:ctypes.c_void_p) -> None:
        self.generation_object = generation_object

    def add_probability(self,chance:Union[float,None]=None)->int:
        if not chance:
            chance = -1;
        return loader.MaktubGenerationNum_add_probability(self.generation_object,chance)

    def perform(self):
        return loader.MaktubGenerationNum_perform(self.generation_object)
