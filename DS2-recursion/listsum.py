"""
[1,3,5,7,9]
"""


def listSum(numList):
    sum = 0
    for i in numList:
        sum = sum + i

    return sum


print(listSum([1, 3, 5, 7, 9]))


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


def toStr(n, base):
    str1 = '0123456789ABCDEF'

    if n < base:
        return str1[n]
    else:
        return toStr(n // base, base) +str1[n%base]

print(toStr(1453,16))