# List and Tuple
num=int(input("Enter n:"))
L = []
for i in range(1,num+1) :
  L.append(i)
print(L)
# Add an item to list
L.insert(3,5)
print(L)
# Remove an item from the list
L.pop(2)
print(L)
# The largest and smallest item
print(max(L))
print(min(L))
# Create a tuple and reverse it
Tup=(1,2,3,4,5,6)
print(Tup[::-1])
# Convert a tuple into list
print(list(Tup))