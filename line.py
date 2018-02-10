import random
from typing import TypeVar

Number = TypeVar('Number', int, float)


class Line(object):
    """
    Represents a linear function in the form ax+b
    """
    def __init__(self, a: Number, b: Number):
        self.a = a
        self.b = b

    def __call__(self, x: Number) -> Number:
        return self.a * x + self.b

    def __add__(self, other):
        """
        Merge two functions together by calculating the average of a and b.

        :return: a new Line object.
        """
        a = (self.a + other.a) / 2
        b = (self.b + other.b) / 2

        return Line(a, b)

    def __str__(self):
        return 'f(x) = {}x + {}'.format(self.a, self.b)


def random_line(random_range=(0, 100)) -> Line:
    """
    Generates a random Line object.
    """

    a, b = random.sample(range(*random_range), k=2)
    return Line(a, b)
