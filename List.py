size = int(input("Enter the size of the list: "))
l1 = []
for i in range(size):
    l1.append(int(input()))
for i in range(size):
    print(l1[i], end=" ")
print("Slicing:")
print(l1[:]) # All elements
print(l1[::-1]) #All elements in reverese
print("Index")
print(l1.index)