#Modified Button class for circles

from graphics import *
class CButton:
    """A button is a labeled Circle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it.
    The update method allows for a change of label."""

    def __init__(self, win, center, radius, label):
        """Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, radius, 'Quit') """

        self.centX, self.centY = center.getX(), center.getY()
        self.center = center
        self.radius = radius

        self.circ = Circle(center, radius)
        self.circ.setFill('lightgray')
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                (self.centX - p.getX()) ** 2 +
                (self.centY - p.getY()) ** 2 <= self.radius ** 2)

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
        self.circ.setWidth(arg1)
        self.active = arg2

    def update(self, win, label):
        self.label.undraw()
        center = self.center
        self.label = Text(center, label)
        self.active = False
        self.label.draw(win)
