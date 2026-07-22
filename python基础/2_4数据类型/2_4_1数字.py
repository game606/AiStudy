age = 25
print(age)
print(type(age))

height = 1.75
print(height)
print(type(height))

flex = 2 + 3j
print(flex)
print(type(flex))

num = 1.0
print(num)
print(type(num))


a = 10
b = 3
print(a + b)   # 13

print(a / b)   # 3.3333333333333335

print(a // b)  # 3

print(a % b)   # 1

print(a ** 2)  # 100（10的平方）


num = 3.9
print(int(num))

num2 = 5
print(float(num2))

# 除法/的结果永远是浮点数，哪怕能整除（比如6/2结果是3.0）
print(6 / 2)

# 整除//只取整数部分，不管小数多少（比如7//2结果是3，不是3.5）
print(7 // 2)

# 数字运算时，整数和浮点数混合运算，结果会变成浮点数（比如5 + 2.0结果是7.0）
print(5 + 2.0)