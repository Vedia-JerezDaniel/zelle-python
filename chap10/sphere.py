#sphere.py
import math

class Sphere:
    """This class represents a geometric solid sphere.
    it will return radius, surface area, and volume
    using getRadius(), surfaceArea(), and volume()."""

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        self.surfaceArea = 4 * math.pi * (self.radius * self.radius)
        return self.surfaceArea

    def volume(self):
        self.volume = 4/3 * math.pi * (self.radius ** 3)
        return self.volume
