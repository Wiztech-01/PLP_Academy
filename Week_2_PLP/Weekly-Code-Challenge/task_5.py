# Task 5
words = input("Enter list of words: ").split()

odd_words = [word for word in words if len(word) % 2 != 0]

print(f"Odd number of characters words are: {odd_words}")
