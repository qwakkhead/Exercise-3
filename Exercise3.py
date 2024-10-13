x = str(input("Enter what's the word"))

vowels = "aeiouAEIOU"

result = ''.join([char.upper() if char in vowels else char for char in x])

print(result)  