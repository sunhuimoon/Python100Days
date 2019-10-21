# 练习6：打印杨辉三角。
def main():
    num = int(input('Number of rows: '))
    yh = [[]] * num
    #  print(yh)
    for row in range(len(yh)):  # row 0-4
        yh[row] = [None] * (row + 1)
        # yh[row] yh[1]=[]  yh[2] = [], [] ....
        for col in range(len(yh[row])):
            if col == 0 or col == row:   # col 列
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
    