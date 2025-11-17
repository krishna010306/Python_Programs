n1 = {1,2,3,4,5}
n2 = {6,7,8,9}
print("Using Union Method:",n1.union(n2))

n3 = {1,2,3}
print("Using intersection Method:",n1.intersection(n3))

n4 = {1,2,3,4,5}
n5 = {5,4,7,6}
n6 = {11,5,23,15}
print("Using difference Method",n4.difference(n5,n6))

print("Using symmetric_difference Mehtod",n5.symmetric_difference(n2))