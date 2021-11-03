L=[1,2,3,5,8,13,5]
L1=int(input("Enter a no.:"))
print("No .of elements:")
print(L.count(5))

L.append(L1)
print(L)

L.reverse()
print("Reversed List:",L)


print(L.index(3))

L.insert(2,3)
print(L)

print(L.pop())

print(L.pop(3))

L.sort()
print("Sorted List:",L)

del L[2]
print(L)

print("Cleared List:")
print(L.clear())



