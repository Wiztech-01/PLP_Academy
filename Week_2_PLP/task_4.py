# Task 4
set1 = set(map(int, input("Enter the elements 1: ").split()))
set2 = set(map(int, input("Enter the elements 2: ").split()))


common_elements = set1 & set2


print(f"Common elements are: {common_elements}")
