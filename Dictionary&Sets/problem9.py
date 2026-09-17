s = { 2,54,45,"deep",(25,45)}
print(s)   
# Key point to remember (important for exams)
# List ([]) → Ordered ✅
# Tuple (()) → Ordered ✅
# Set ({}) → Unordered ❌ (print order can change)
# Dictionary ({key: value}) → Preserves insertion order in modern Python (3.7+)

# So your output is correct because sets
# don't print elements in the order you wrote them. Python arranges them according to its internal hash table.