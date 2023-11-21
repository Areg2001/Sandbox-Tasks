import numpy as np


class BitVector:

    def __init__(self, vector_size: int) -> None:
        self.array_size = (vector_size // 64) + 1
        self.array = np.zeros(self.array_size, dtype="uint64")

    def set(self, index: int) -> None:
        array_index = index // 64
        self.array[self.array.size - array_index - 1] |= np.uint64(1 << index % 64)

    def reset(self, index: int) -> None:
        array_index = index // 64
        self.array[self.array.size - array_index - 1] &= ~np.uint64(1 << index % 64)