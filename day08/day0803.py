# 练习1：定义一个类描述数字时钟。
from time import sleep
class Clock(object):
    """数字时钟"""
    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        #print(self, hour, minute, second, '初始化 23:59:58')
        self._hour = hour
        self._minute = minute
        self._second = second
        print(hour, minute, second, '赋值 23:59:58')

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        # 2是宽度。如果整数不够2列就补上0
        return '%03d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
