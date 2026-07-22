student = {
    'name': '小明',
    'age': 18,
    'gender': '男',
    'score': [90, 85, 95]
}

empty_dict = {}
print(type(student))
print(type(empty_dict))

student = {
    'name': '小明',
    'age': 18,
}
print(student['name'])
# print(student['height'])

print(student.get('name'))
print(student.get('height'))
print(student.get('height', 175))

print("===============================")

student = {
    'name': '小明',
    'age': 18,
}
student['age'] = 175
print(student)

student['height'] = 175
student['hobby'] = ['篮球', '看书']
print(student)

print("=============================")

student = {
    'name': '小明',
    'age': 18,
    'height': 175
}
print(student)
del student['height']
print(student)

age = student.pop('age')
print(age)
print(student)

print("==========================")

student = {
    'name': '小明',
    'age': 18,
    'gender': '男'
}
print(student.keys())
print(student.values())

print(student)
print(student.items())
for key, value in student.items():
    print(f'{key}: {value}')

print(student)
student.clear()
print(student)



# 1. 键必须唯一：同一字典中不能有重复的键（后定义的会覆盖先定义的）；
d = {'a': 1, 'a': 2}
print(d)

# 2. 键必须不可变：列表、字典等可变类型不能作为键（字符串、数字、元组可以）；
# d = {[1, 2] : 'test'}
d = {(1, 2): 'test'}
print(d)

# 3. 字典是无序的（Python3.7 + 会保留插入顺序），不能用索引取值，只能用键。