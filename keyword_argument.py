class PrintValues:
    def display(self, n=None, c=None):
        if isinstance(n, int) and isinstance(c, str):
            print(f"Integer: {n}, Character: {c}")
        elif isinstance(n, str) and isinstance(c, int):
            print(f"Character: {n}, Integer: {c}")
        else:
            print("Invalid parameters!")

obj = PrintValues()

obj.display(10, 'A')
obj.display('B', 20)