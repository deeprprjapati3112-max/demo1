student = {
    "name": "deep",
    "age": 19
}
print(student)
student.update({"age": 20})
print(student)
student.update({"college": "cvm"})

print(student)

removed_value = student.pop("age")
print(student)

print("Removed value:", removed_value)
