# import os
# import time
# import random


# # 练习1：在屏幕上显示跑马灯文字。
# def main():
#     content = "北京欢迎你为你开天辟地…………"
#     while True:
#         # 清理屏幕上的输出
#         # os.system('cls')
#         # os.system('clear')
#         print(content)
#         # 休眠200毫秒
#         time.sleep(0.1)
#         content = content[1:] + content[0]
#
#
# if __name__ == '__main__':
#     main()


# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
# def generate_code(code_len=4):
#     """
#     生成指定长度的验证码
#     :param code_len: 验证码的长度(默认4个字符)
#     :return: 由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     print(last_pos)
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)  # random.randint() 选取随机数
#         print(all_chars[index])
#         code += all_chars[index]
#     print(code)
#     return code
#
#
# print(generate_code())

# 练习3：设计一个函数返回给定文件名的后缀名
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')  # Python rfind() 返回字符串最后一次出现的位置(从右向左查询)，
                               # 如果没有匹配项则返回-1。
    print(pos)
    if 0 < pos < len(filename) - 1:  # . 不在第一个也不在最后一个
        #index = pos if has_dot else pos + 1
        index = pos + 1
        print(index)
        return filename[index:]
    else:
        return ''


print(get_suffix("012txtdd"))
