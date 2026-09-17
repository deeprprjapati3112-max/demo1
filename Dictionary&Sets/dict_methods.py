markes  = {
    
    "deep":100,
    "shubham":38,
    "ayan":99,
    "daksh":12,
    0:"harry"
}
print(markes.items())

print(markes.keys())

print(markes.values())



markes.update({"deep":99})

print(markes)

print(markes.get("deep"))#print a none output

print(markes["deep"])#print in the code error
# In Python, a **dictionary** is a built-in data structure used to store data in **key-value pairs**. It is **mutable**, **unordered** (in versions before 3.7), and **indexed by keys**.

# ---

# ### **Basic Syntax**

# ```python
# # Empty dictionary
# my_dict = {}

# # Dictionary with values
# my_dict = {
#     "name": "Deep",
#     "age": 21,
#     "city": "Ahmedabad"
# }

# print(my_dict)
# ```

# ---

# ### **Accessing Values**

# ```python
# print(my_dict["name"])       # Output: Deep
# print(my_dict.get("age"))    # Output: 21
# ```

# ---

# ### **Adding / Updating Items**

# ```python
# my_dict["country"] = "India"  # Add new key-value
# my_dict["age"] = 22           # Update existing key
# print(my_dict)
# ```

# ---

# ### **Removing Items**

# ```python
# my_dict.pop("city")       # Remove by key
# del my_dict["age"]        # Delete by key
# my_dict.clear()           # Remove all items
# ```

# ---

# ###**Dictionary Methods**

# | Method               | Description                               |
# | -------------------- | ----------------------------------------- |
# | `dict.keys()`        | Returns all keys                          |
# | `dict.values()`      | Returns all values                        |
# | `dict.items()`       | Returns all key-value pairs as tuples     |
# | `dict.update({...})` | Update dictionary with another dictionary |
# | `dict.pop(key)`      | Remove item by key                        |
# | `dict.clear()`       | Remove all items                          |

# ---

# ### **Example with Loop**

# ```python
# student = {
#     "name": "Deep",
#     "course": "Data Science",
#     "marks": 90
# }

# # Loop through keys and values
# for key, value in student.items():
#     print(key, ":", value)
# ```

# ---

# 👉 Do you want me to also give you a **full list of dictionary methods with examples** or a **small project using dictionary** (like a phonebook or word counter)?
