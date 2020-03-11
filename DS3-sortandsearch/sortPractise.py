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
# def selectionSort(alist):
#     for fillsort in range(len(alist)-1,0,-1):
#         maxPos = 0
#         for location in range(1,fillsort+1):
#             if alist[location] > alist[maxPos]:
#                 maxPos = location
#
#         temp = alist[fillsort]
#         alist[fillsort] = alist[maxPos]
#         alist[maxPos] = temp
# alist = [54, 65, 32, 78, 51, 12, 57, 64]
# print(alist)
# selectionSort(alist)
# print(alist)

"""插入排序"""
# def insertionSort(alist):
#     for i in range(1,len(alist)):
#         currentValue = alist[i]
#         pos = i
#         while pos > 0 and alist[pos-1]>currentValue:
#             alist[pos] = alist[pos-1]
#             pos = pos-1
#
#         alist[pos] = currentValue
#
# alist = [54, 65, 32, 78, 51, 12, 57, 64]
# print(alist)
# insertionSort(alist)
# print(alist)

"""希尔排序"""
# def shellSort(alist):
#     sublistcount = len(alist)//2
#     while sublistcount>0:
#         for startposition in range(sublistcount):
#             gapInsertionSort(alist,startposition,sublistcount)
#
#         print('alist:',alist)
#         sublistcount = sublistcount//2
#
#
# def gapInsertionSort(alist,start,gap):
#     for i in range(start+gap,len(alist),gap):
#         currentValue = alist[i]
#         pos = i
#         while pos > gap and alist[pos-gap]>currentValue:
#             alist[pos] = alist[pos-gap]
#             pos = pos-gap
#
#         alist[pos] = currentValue
#
#
# alist = [54, 65, 32, 78, 51, 12, 57, 64]
# print(alist)
# shellSort(alist)
# print(alist)


"""归并排序"""
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)
        i = 0
        j = 0
        k = 0
        # while i < len(leftHalf) and j<len(rightHalf):
        #     if leftHalf[i] < rightHalf[j]:
        #         alist[k] = leftHalf[i]
        #         i=i+1
        #     else:
        #         alist[k] = rightHalf[j]
        #         j = j+1
        #     k = k+1
        while i <len(leftHalf):
            alist[k] = leftHalf[i]
            i = i+1
            k=k+1
        while j <len(rightHalf):
            alist[k] = rightHalf[j]
            i = j+1
            k = k+1
alist = [54, 65, 32, 78, 51, 12, 57, 64]
print(alist)
mergeSort(alist)
print(alist)

"""快速排序"""
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

#递归调用对数列进行分区
def quickSortHelper(alist,first,last):
    if first<last:
           splitpoint = partition(alist,first,last)

           quickSortHelper(alist,first,splitpoint-1)
           quickSortHelper(alist,splitpoint+1,last)

#选出基准点
def partition(alist,first,last):
    #定义基准点
    pivotvalue = alist[first]
    leftMark= first + 1
    rightMark = last

    #停止比对
    done = False
    while not done:
        while leftMark <= rightMark and alist[leftMark] <=pivotvalue:
            leftMark = leftMark+1

        while alist[rightMark] >=pivotvalue and rightMark >=leftMark:
            rightMark = rightMark-1

        if rightMark < leftMark:
            done = True

        else:
            temp = alist[leftMark]
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = temp










