l = [ "deep","mahi","janvi","hemali"]
l.append("love")                    # list
print(l)

s =  {"deep","mahi","janvi","hemali"}  # set
s.add("love") # if try
print(s)

name_age = {
    
    "name":"deep",  # dict
    "age":19,
    "name":"janvi",
    "age":19
}
print(name_age["name"])

k = (48848,84512,4841,848,1454)  # tuple
# k.append(545485) 




# # This will raise an AttributeError since tuples are immutable

 #| Feature          | List  | Tuple | Dictionary                   | Set   |
# | ---------------- | ----- | ----- | ---------------------------- | ----- |
# | Symbol           | `[]`  | `()`  | `{key:value}`                | `{}`  |
# | Ordered          | ✅ Yes | ✅ Yes | ✅ Yes (Python 3.7+)          | ❌ No  |
# | Changeable       | ✅ Yes | ❌ No  | ✅ Yes                        | ✅ Yes |
# | Duplicate Values | ✅ Yes | ✅ Yes | ❌ Duplicate keys not allowed | ❌ No  |
# | Indexing         | ✅ Yes | ✅ Yes | ❌ Use key                    | ❌ No  |