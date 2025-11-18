dictonary1 = {'Google':1,'Facebook':2,'Microsoft':3}
dictonary2 = {'GFG':1,'Microsoft':2,'Youtube':3}
dictonary1.update(dictonary2)
for key, value in dictonary1.items():
    print(key,value)
