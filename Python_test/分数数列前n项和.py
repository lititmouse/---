n = int(input())
a, b = 1, 2
flag = -1
total = 1.0
# 除了首项，分子是1到n-1的公差为1的等差数列，
for i in range(1, n):
    total = total + flag * a / b
    a, b = i + 1, a + b
    flag = -flag  # 每循环一次flag乘-1
print(total)