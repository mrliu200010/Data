from pythonds.basic.stack import Stack
# def divide2(desNumber):
#     s = Stack()
#
#     while desNumber>0:
#         rem = desNumber%2
#         s.push(rem)
#         desNumber = desNumber//2
#
#     binString = ''
#     while not s.isEmpty():
#         binString = binString + str(s.pop())
#
#     return binString
# print(divide2(10))


"""
八进制，十六进制
"""
def divide2(desNumber,base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while desNumber>0:
        rem = desNumber % base
        s.push(rem)
        desNumber = desNumber // base

    binString = ''
    while not s.isEmpty():
        binString = binString + digits[s.pop()]

    return binString
print(divide2(233,16))



