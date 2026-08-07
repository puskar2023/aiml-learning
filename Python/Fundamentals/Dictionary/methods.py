info = {
    "name": "hello",
    "cgpa": 9.3,
    "subjects": ["Computer Network", "OOPs"]
}

dict_keys = list(info.keys())
dict_values = list(info.values())

print(dict_keys)
print(dict_values)

print(info.items())

print(info.get("cgpa"))

info.update({
    "city": "Delhi"
})

print(info.items())