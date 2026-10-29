# json file to python file
# import json

# with open("data.json", "r") as f:
#     py_obj = json.load(f)
#     print(py_obj)





# python file to json file
import json

data = {
    "name": "Sarthak",
    "age": 26,
    "isTeacher": True
}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)



'''
json_str = '{"name": "Sarthak", "isTeacher": true}'

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)
'''

# To convert dict to json string => json.dumps(dict)