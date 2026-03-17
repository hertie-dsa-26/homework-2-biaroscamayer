import math
from circle import Circle

def test_perimeter():
    c = Circle(1)
    expected = 2 * math.pi * 1
    assert math.isclose(c.perimeter(), expected)

def test_area():
    c = Circle(1)
    expected = math.pi * (1 ** 2)
    assert math.isclose(c.area(), expected)
