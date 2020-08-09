import math

class FreeVector:
    """A vector that is not bound by an initial or terminal point."""

    def __init__(self, name):
        self.name = tuple(name)
    def __eq__(self, other):
        if (isinstance(other, FreeVector) and
        all(math.isclose(a, b) for a, b in zip(
        other.name, self.name))):
            return True
        else:
            return False
a = FreeVector("ramya")
b = FreeVector((1, 2, 3))
c = FreeVector("ramya")
print(a == c)