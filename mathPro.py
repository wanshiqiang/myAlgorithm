# 阶乘

def factorial(num):
    '''
        递归求解数字num的阶乘
    '''
    if num == 0 :
        return 1
    return num*factorial(num-1)

def factorial2(num):
    '''
        循环求解数字num的阶乘
    '''
    if num == 0 :
        return 1

    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def testFactorial():
    for i in range(9):
        # 测试0-8的阶乘是否正确
        num = i
        print("函数factorial：数字{}的阶乘：{}".format(num,factorial(num)))
        print("函数factorial2：数字{}的阶乘：{}".format(num,factorial2(num)))


# 最大公约数

def gcd(a,b):
    '''
        循环遍历求解最大公约数
    '''
    minNum = min(a,b)
    for i in range(minNum,0,-1):
        if a%i ==0:
            return i
a=76
b=18
print("{}和{}的最大公约数：{}".format(a,b,gcd(a,b)))

def gcd2(a,b):
    