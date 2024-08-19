from abc import ABC, abstractmethod

# Definir la interfaz Polygon
class Polygon(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def print_area(self):
        pass

# Implementar la clase Triangle
class Triangle(Polygon):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return (self.base * self.height) / 2

    def print_area(self):
        print(f"El área del triángulo es {self.area()}")

# Implementar la clase Rectangle
class Rectangle(Polygon):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def print_area(self):
        print(f"El área del rectángulo es {self.area()}")

# Implementar la clase Square
class Square(Polygon):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side

    def print_area(self):
        print(f"El área del cuadrado es {self.area()}")

# Función para calcular el área
def area(polygon: Polygon) -> float:
    polygon.print_area()
    return polygon.area()

# Función principal
if __name__ == "__main__":
    area(Triangle(10.0, 5.0))
    area(Rectangle(5.0, 7.0))
    area(Square(4.0))
