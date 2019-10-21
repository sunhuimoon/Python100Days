# set1 = {1, 2, 3, 3, 3, 2}
# print(set1)
# print('Length =', len(set1))
# # 创建集合的构造器语法(面向对象部分会进行详细讲解)
# set2 = set(range(1, 10))
# set3 = {1, 2, 3, 3, 2, 1}
# # print(set2, set3)
# # 创建集合的推导式语法(推导式也可以用于推导集合)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
# print(set4)

# set1.add(4)
# set1.add(5)
# set2.update([11, 12])
# set2.discard(5)
# if 4 in set2:
#     set2.remove(4)
# print(set1, set2)
# print(set3.pop())  #pop 删除并返回
# print(set3)

list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
set1 = {1, 2, 3, 4, 5}
site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
print(list1.pop())       # 列表默认删除最后一个
# print(tuple1.pop())    # 元组不能修改内部
print(set1.pop())        # 集合默认删除第一个
print(site.pop('name'))  # 字典没有默认
