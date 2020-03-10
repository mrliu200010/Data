# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# a,b=b,a
# print(a)
# print(b)



# def bubbleSort(alist):
#     flag = True
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i] < alist[i+1]:
#                 alist[i],alist[i+1] = alist[i+1],alist[i]
#                 # temp = alist[i]
#                 # alist[i] = alist[i+1]
#                 # alist[i+1] = temp
#
# alist = [54,65,32,78,51,12,57,64]
# print(alist)
# bubbleSort(alist)
# print(alist)

"""短冒泡排序"""
# def bubbleSort(alist):
#     flag = True
#     passnum = len(alist)-1
#     while passnum>0 and flag:
#         flag = False
#         for i in range(passnum):
#             if alist[i] < alist[i+1]:
#                 flag = True
#                 alist[i],alist[i+1] = alist[i+1],alist[i]
#                 # temp = alist[i]
#                 # alist[i] = alist[i+1]
#                 # alist[i+1] = temp
#         passnum = passnum-1
# alist = [54,65,32,78,51,12,57,64]
# print(alist)
# bubbleSort(alist)
# print(alist)

"""选择排序"""
def selectionSort(alist):
    for fillsort in range(len(alist)-1,0,-1):
        maxPos = 0
        for location in range(1,fillsort+1):
            if alist[location] > alist[maxPos]:
                maxPos = location

        temp = alist[fillsort]
        alist[fillsort] = alist[maxPos]
        alist[maxPos] = temp
alist = [54, 65, 32, 78, 51, 12, 57, 64]
print(alist)
selectionSort(alist)
print(alist)

