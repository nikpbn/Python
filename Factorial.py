# 1. calculate factorial of given number.
# 2. Find the number of trailing zeros in factorial.

# while(num =1):
#     print(num)
#     num-=1
#     # mul = num*(num-1)

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


def trailingZerosOldWay(n):
    fac = fact(n)
    cnt =0
    # print("factorial=",fac)
    while(fac%10 == 0):
        cnt+=1
        fac = fac/10
    return cnt

def trailingZeros(n):
    cnt = 0
    i = 5
    # 5! = 5*4*3*2*1
    # 6! = 6*5*4*3*2*1
    #
    while(n//i != 0):
        cnt+= int(n/i)
        i=i*5
    return cnt


if __name__ == '__main__':
    num = int(input("Enter the number: "))
    factorial = fact(num)
    print("Factorial of num ", num, " is ", factorial)

    # trail_old =trailingZerosOldWay(num)
    # print("Trailing zeros old",trail_old)

    trail =trailingZeros(num)
    print("Trailing zeros ",trail)
