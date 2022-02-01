#button.py
from graphics import *

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """

        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.center = Point(x, y)
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self._extracted_from_deactivate_3('black', 2, True)

    def deactivate(self):
        "sets this button to 'inactive'."
        self._extracted_from_deactivate_3('darkgrey', 1, False)

    # TODO Rename this here and in `activate` and `deactivate`
    def _extracted_from_deactivate_3(self, arg0, arg1, arg2):
        self.label.setFill(arg0)
        self.rect.setWidth(arg1)
        self.active = arg2

    def update(self, win, label):
        self.label.undraw()
        center = self.center
        self.label = Text(center, label)
        self.active = False
        self.label.draw(win)

    
