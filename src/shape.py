class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"{self.name} with area {self.area()}"
