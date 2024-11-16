list_a = [1, 2, 3, 4, 5]
# index   0, 1, 2, 3, 4

print(list_a[3])

# Python lists are mutable. Meaning lists are changeable.
list_a[0] = 20
print(list_a[0])

list_a.insert(len(list_a), 6)

# adds an item to the list
list_a.append(7)

# adds all items to the list
list_a.extend([8,9])

# returns and removes item present at the given index
list_a.pop(8)

# remove one or more items from a list
del list_a[7]

print(list_a)

# to look for an item
for item in list_a:
    print(item)


capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ", capital_city)

capital_city["Japan"] = "Tokyo"
capital_city["Kenya"] = "Nairobi"
print("Updated Dictionary: ", capital_city)

name = 'Lynn'
country  = 'Kenya'

print(f'{name} habite un {country}')