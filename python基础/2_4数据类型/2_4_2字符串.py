name = '小明'
print(type(name))

info = "小明说了一句话"
print(type(info))

content = '''
第一行
第二行
第三行
'''
print(type(content))


# 基础操作
first = 'Hello'
second = 'Python'
print(first + second)
# print(first + 2) 错误
print(first + str(2))

print("=======================")

s = 'Python'
print(s[0])
print(s[3])
print(s[-1])

print("=======================")

ss = 'Python教程'
print(ss[0: 6])
print(ss[: 6])
print(ss[6:])

print("=======================")

sss = '     Hello Python    '
print(sss)

print(sss.strip()) # 去除首尾空格
print(sss.lower()) # 转小写
print(sss.upper()) # 转大写

print(sss.replace('Python', 'Java')) # 替换字符

print(sss.count('o')) # 统计字符出现次数

sss = sss.strip()
print(sss.startswith('Hello')) # 判断是否以指定字符开头
print(sss.endswith('Python')) # 判断是否以指定字符结尾


# 字符串格式化
name = '小红'
score = 98.58
print(f'{name} 的数学成绩是 {score} 分')
print(f'成绩保留 1 位小数：{score:.1f}')



# 1. 字符串是不可变的：不能直接修改字符串里的单个字符（比如 s[0] = 'p' 会报错）；
# name[0] = '大'
# print(name[0])

# 2. 引号嵌套：单引号里不能直接放单引号（要转义 \' 或用双引号包裹）；
# content = '我的家在东北，\'松花江\'上'
content = '我的家在东北，"松花江"上'
print(content)

# 3. 索引越界：如果字符串长度是 6，索引最大是 5，用 s[6] 会报错。
ssss = '012345'
print(ssss[5])