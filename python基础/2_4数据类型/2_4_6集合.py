nums = {1, 2, 2, 3, 3, 3}
print(nums)

empty_set = set()
wrong_empty_set = {}  # 这是空字典，不是集合

list1 = [1, 2, 2, 3]
s = set(list1)
print(s)

print(type(nums))
print(type(empty_set))
print(type(wrong_empty_set))
print(type(s))

print("==============================")

fruits = {'苹果', '香蕉', '橙子'}
print('香蕉' in fruits)    # 输出 True
print('葡萄' not in fruits) # 输出 True

print("==============================")

fruits = {'苹果', '香蕉', '橙子'}
fruits.add('葡萄')
print(fruits)

fruits.update(['梨', '芒果'])
print(fruits)

fruits.remove('香蕉')
print(fruits)

# fruits.remove('菠萝')
fruits.discard('西瓜')
print(fruits)

fruits = fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

print("==============================")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 并集
print(a | b)          # 输出 {1, 2, 3, 4, 5, 6}
print(a.union(b))     # 同上

# 交集
print(a & b)          # 输出 {3, 4}
print(a.intersection(b)) # 同上

# 差集
print(a - b)          # 输出 {1, 2}
print(a.difference(b)) # 同上
print(b - a)
print(b.difference(a))



# 1. 集合无序，不能用索引取值（比如 fruits[0] 会报错）；
aa = {1, 2, 3}
# print(a[0])

# 2. 集合元素必须不可变：列表、字典不能作为集合元素（元组可以）；
# bb = {[1, 2], 3}
bb = {(1, 2), 3}
print(bb)
