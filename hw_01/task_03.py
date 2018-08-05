#Class of rotations of a square

import numpy as np

def singleton_for_rotation(cls):
    instances = {}
    def wrapper(degree):
        if degree not in instances:
            instances[degree] = cls(degree)
        return instances[degree]
    return wrapper

@singleton_for_rotation
class Rotation:
    def __init__(self, degree):
        assert degree % 90 == 0
        self.degree = degree % 360

    def __call__(self, matrix):
        if self.degree == 90:
            matrix = np.rot90(matrix, -1)
        if self.degree == 180:
            matrix = np.rot90(matrix, -2)
        if self.degree == 270:
            matrix = np.rot90(matrix, 1)
        return matrix

    def __mul__(self, other):
        return Rotation(self.degree + other.degree)

matrix = np.array(([1, 2], [3, 4]))
a = Rotation(270)
b = Rotation(90)
print(a(matrix))

c = a * b
print(c(matrix))
