import numpy as np
import math
from numpy import ndarray


class Bitvector:

    def __init__(self, vector_size: int) -> None:
        self.__array_index = None
        self.__vector_size = vector_size
        self.__array_size = math.ceil(vector_size / 64)
        self.__array = np.zeros(self.__array_size, dtype="int64")

    @property
    def array(self) -> ndarray:
        return self.__array

    @property
    def array_size(self) -> int:
        return self.__array_size

    @property
    def vector_size(self) -> int:
        return self.__vector_size

    def set(self, index: int) -> None:
        self.__array_index = index // 64
        self.__array[self.__array_index] = (self.__array[self.__array_index]) ^ (1 << ((index % 64) + 29)

    def reset(self, index: int) -> None:
        self.__array_index = index // 64
        self.__array[self.__array_index] = (self.__array[self.__array_index]) ^ (1 << (index % 64))


x = Bitvector(100)
print(x.array)
x.set(98)
print(x.array)
print(int(32*"0" + "1" + 31*"0", 2))