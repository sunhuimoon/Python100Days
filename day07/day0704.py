list1 = [1, 3, 5, 7, 100]
# 通过循环用下标遍历列表元素
for a in range(len(list1)):  # range() 方法
    print(a, list1[a], " ", end='')
print()
# 通过for循环遍历列表元素
for elem in list1:
    print(elem, " ", end="")
print()
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):  # enumerate（）同时列出数据和数据下标，
    print(index, elem)
list1.append(200)
list1.insert(1, '400a')
list1.extend([1000, 2000])
list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
for index, elem in enumerate(list1):  # enumerate（）同时列出数据和数据下标，
    print(index, elem)
for a in range(3,8):  # range() 方法
    print(a,  " ", end='')
print(len(list1))