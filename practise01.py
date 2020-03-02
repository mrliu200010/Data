"""
问题描述：使用函数，求前n个整数的和
"""
#一
import time

def  sumOFN(n):
    start_time = time.time()
    sum=0
    for i in range(n+1):
        sum=sum+i
    end_time = time.time()
    return sum,end_time-start_time
# for i in  range(5):
print("计算结果%d \n需要%10.7f秒"%sumOFN(1000000))
#二
# def foo(l):
#     a = 0
#     for b in range(1,l+1):
#         c = b
#         a = a+c
#     return a
# print(foo(10))



#高斯函数(n*(n+1))/2
def sumOFN2(n):
    return (n*(n+1))/2
start_time=time.time()
print(sumOFN2(1000000))
end_time = time.time()
print('用时：',end_time - start_time)