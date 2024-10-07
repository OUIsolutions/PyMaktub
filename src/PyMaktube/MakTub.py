from typing import Any
from typing_extensions import List

from .Probabilitys import Probability
from .ctypes import loader
from .MakTubSeqs import MakTubSeqs
import ctypes

class MakTub:

    def __init__(self,seed:str) -> None:
        self.c_object = loader.newMakTub(
            "%s".encode("utf-8"),
            seed.encode("utf-8")
        )

    def set_seed(self,seed:str):
        loader.MakTub_set_seed(
            self.c_object,
            "%s".encode("utf-8"),
            seed.encode("utf-8")
        )



    def aply_seed_modification(self,positions:List[int],valid_chars:str=MakTubSeqs.ALFHA_NUNS):
        positions_size = len(positions)
        array = (ctypes.c_int * positions_size)()
        for i in range(positions_size):
            array[i] = int(positions[i])

        loader.MakTub_aply_seed_modification(
            self.c_object,
            array,
            positions_size,
            valid_chars.encode("utf-8")
        )


    def __str__(self) -> str:
        return self.get_seed()


    def get_generation(self)->int:
        return loader.MakTub_get_generation(self.c_object)


    def set_generation(self,generation:int):
        loader.MakTub_set_generation(self.c_object,generation)

    def get_seed(self):
        return loader.MakTub_get_seed(self.c_object).decode()

    def choice(self,values:List[Any])->Any:
        choose = self.generate_num(0,len(values)-1)
        return values[choose]

    #generators
    def new_probability(self):
        obj = loader.MakTub_newGenerationNum(self.c_object)
        return Probability(obj)

    def generate_token(self,size:int=10,valid_chars:str=MakTubSeqs.ALFHA_NUNS)->str:
        return loader.MakTub_generate_token(self.c_object,size,valid_chars.encode("utf-8")).decode()


    def generate_num(self,start:int,end:int):
        return loader.Maktub_generate_num(self.c_object,start,end)



    def __del__(self):
        loader.MakTub_free(self.c_object)
