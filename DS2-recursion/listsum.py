"""
[1,3,5,7,9]
"""


# def listSum(numList):
#     sum = 0
#     for i in numList:
#         sum = sum + i
#
#     return sum
#
#
# print(listSum([1, 3, 5, 7, 9]))


# 不能使用while或者for
# 使用小学的内容：连加

# def listSum2(numlist):
#     if len(numlist)== 1:
#         return numlist[0]
#     else:
#         return numlist[0]+listSum2(numlist[1:])
#         # numlist[len(numlist-2)]=numlist[len(numlist-2)]+numlist[len(numlist-1)]
#         # listSum2(numlist)
#
# print(listSum2([1,3,5,7,9]))


# def toStr(n, base):
#     str1 = '0123456789ABCDEF'
#
#     if n < base:
#         return str1[n]
#     else:
#         return toStr(n // base, base) +str1[n%base]
#
# print(toStr(1453,16))


#栈 实现递归
from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n,base):
    convertString = '0123456789ABCDEF'

    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])

        n = n//base
    res = ""
    while not rStack.isEmpty():
        res = res+ str(rStack.pop())
    return res

print(toStr(7,2))
