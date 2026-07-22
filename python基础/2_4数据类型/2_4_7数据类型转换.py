# 数字与字符串互转（最高频）
# 场景1：输入的数字是字符串，转成数字才能运算
input_age = input("请输入年龄：")  # 输入18，得到字符串'18'
age = int(input_age)              # 转成整数18
print(age + 2)                    # 输出20（能正常运算）

# 场景2：数字转字符串，用于拼接
score = 95
print('你的成绩是：' + str(score))  # 输出 你的成绩是：95

# 场景3：字符串转浮点数
price = float('29.9')
print(price * 2)  # 输出59.8


# 容器类型互转（列表 / 元组 / 集合）
# 列表转元组（不可变化）
lst = [1, 2, 3]
t = tuple(lst)
print(t)  # 输出 (1, 2, 3)

# 元组转列表（方便修改）
t = (4, 5, 6)
lst = list(t)
print(lst)
lst[0] = 10
print(lst)  # 输出 [10, 5, 6]

# 列表转集合（去重）
lst = [1, 2, 2, 3]
s = set(lst)
print(s)  # 输出 {1, 2, 3}

# 布尔值与其他类型转换
# 数字转布尔：0/0.0转False，非0转True
print(bool(0))    # False
print(bool(5))    # True
print(bool(0.0))  # False
print(bool(3.14)) # True

# 字符串转布尔：空字符串转False，非空转True
print(bool(''))   # False
print(bool('abc'))# True

# 容器转布尔：空容器（空列表/空字典等）转False，非空转True
print(bool([]))   # False
print(bool([1]))  # True
print(bool({}))   # False


# 转换失败的情况
s = '18'
# print(int(s))
if s.isdigit():
    num = int(s)
    print(num)
else:
    print("s 不是有效数字")

# 自动类型转换
print(5 + 3.14)

print(True + 2)
print(False + 5)
