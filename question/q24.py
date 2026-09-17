text = " my name is deep"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] +=1
    else:
        frequency[char] = 1