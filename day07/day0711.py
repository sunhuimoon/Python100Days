# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for index in range(2, len(x)):
#         if x[index] > m1:
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m2:
#             m2 = x[index]
#     return m1, m2


# a1, a2 = (1, 2) if 4 < 3 else (2, 1)
# print(a1, a2)

# 练习5：计算指定的年月日是这一年的第几天。
#
# def is_leap_year(year):
#     """
#     判断指定的年份是不是闰年
#
#     :param year: 年份
#     :return: 闰年返回True平年返回False
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def which_day(year, month, date):
#     """
#     计算传入的日期是这一年的第几天
#
#     :param year: 年
#     :param month: 月
#     :param date: 日
#     :return: 第几天
#     """
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]  #当右边列表条件判断为False时，左列表执行列表右侧的内容
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date
#
#
# def main():
#     print(which_day(1980, 11, 28))
#     print(which_day(1981, 12, 31))
#     print(which_day(2018, 1, 1))
#     print(which_day(2016, 3, 1))
#
#
# if __name__ == '__main__':
#     main()
#
d = [[1, 2, 3], [3, 2, 1], [4, 5, 6]][False]
print(d)
