def vowels(name):
    if name in ("a","e","i","o","u"):
        return True
    else:
        return False
    
name =input("enter the name: ") 
print(vowels(name))  


# remember 
# | If the input is... | Use              |
# | ------------------ | ---------------- |
# | Number (5, 10, 25) | `int(input())`   |
# | Decimal (3.14)     | `float(input())` |
# | Text (deep, apple) | `input()`        |
# def vowels(name):
#     count = 0

#     for ch in name:
#         if ch in ("a", "e", "i", "o", "u"):
#             count += 1

#     return count

# name = input("Enter a word: ")
# print(vowels(name))