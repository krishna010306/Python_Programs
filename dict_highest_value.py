data = {'a': 10, 'b': 50, 'c': 30, 'd': 20, 'e': 40}

highest_values = sorted(data.values(), reverse=True)[:3]
print("Top three values:", highest_values)