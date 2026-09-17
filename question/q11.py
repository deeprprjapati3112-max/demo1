# Count vowels in a string

text = "  hi i am deep"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels in the string:", count)


# Vowels are letters that make open sounds when speaking.

# In English, the vowels are:

# a, e, i, o, u

# Examples:

# apple → a is vowel
# elephant → e is vowel
# orange → o is vowel

# Other letters like b, c, d, f are called consonants.