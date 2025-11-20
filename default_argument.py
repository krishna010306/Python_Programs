class AreaCalculator:
    def area(self, length, breadth=None):
        if breadth is None:
            print(f"Area of Square: {length * length}")
        else:
            print(f"Area of Rectangle: {length * breadth}")

obj = AreaCalculator()

obj.area(5)
obj.area(5, 10)