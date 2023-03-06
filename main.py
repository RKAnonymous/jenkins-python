import os

lst1 = [8, 9, 3, 5, 2, 10]
lst1.reverse()

print("The reversed list is: ", lst1)


lst2 = [91, 43, 87, 34, 25, 89, 98, 95, 57, 435]
lst2.sort()
print("The sorted list is: ", lst2)

lst3 = []
lst3 = lst1.copy()
print("lst3 = ", lst3)


indexvalue = lst2[2:6]
print("The index values are: ", indexvalue)