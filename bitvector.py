import numpy as np


class BitVector:

    def __init__(self, vector_size: int) -> None:
        self.__array_size = (vector_size + 63) // 64
        self.__array = np.zeros(self.__array_size, dtype="uint64")

    @property
    def array(self) -> np.ndarray:
        return self.__array

    @property
    def array_size(self) -> int:
        return self.__array_size

    def set(self, index: int) -> None:
        array_index = index // 64
        self.__array[self.__array.size - array_index - 1] |= np.uint64(1 << index % 64)

    def reset(self, index: int) -> None:
        array_index = index // 64
        self.__array[self.__array.size - array_index - 1] ^= np.uint64(1 << index % 64)