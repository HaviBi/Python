

# 数值的输入
# 让用户输入一个三位数
num = input("please enter a number(three order):")

# 输入数据的验证，是否为三位数
# print(len(num))
num = int(num)
# print(num, type(num))
if not (100 <= num <= 999):
    print('error!')
    exit()
print('continue!')

# 数据处理
numTemp = num
firstNum = num // 100

numTemp = num % 100
secondNum = numTemp // 10

numTemp = num % 10
thirdNum = numTemp

result = firstNum ** 3 + secondNum ** 3 + thirdNum ** 3 == num

# 打印输出
print(firstNum, secondNum, thirdNum, result)
