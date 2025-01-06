import array
arr = array.array('i',[1,2,3,4,5])
for elem in arr:
    print(elem, end=" ")
print("Slicing: ")
print(arr[:])
print(arr[::-1])
print(arr[:2])
