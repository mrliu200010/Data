"""搜索和排序"""

# def sequentialSearch(alist,item):
#     found = False
#     pos=0
#
#     while pos<len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         else:
#             pos = pos+1
#
#     return found
#
# testList = [1,2,3,7,23,58,67]
# print(sequentialSearch(testList,1))


"""
升序 [17,20,26,30,44,54,55,65,77,93]
假设寻找的项在列表中
假设寻找的项不在列表中，50
"""

# def orderedSequentialSearch(alist,item):
#     pos = 0
#     found = False
#     stop = False
#     while pos<len(alist) and found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos]>item:
#                 stop = True
#             else:
#                 pos = pos+1
#     return found
#
# testList =[17,20,26,30,44,54,55,65,77,93]
# print(orderedSequentialSearch(testList,55))


"""
    有序列表
    二分查找：每次都从剩余项中元素进行比对
"""
# def binarySearch(alist,item):
#     found = False
#     first = 0
#     last = len(alist)-1
#     while first <= last and not found:
#         #中间项
#         midpoint = (first+last)//2
#         if alist[midpoint] ==item:
#             found = True
#         else:
#             if item <alist[midpoint]:
#                 last = midpoint-1
#             else:
#                 first = midpoint+1
#     return found
#
# testList =[17,20,26,30,44,54,55,65,77,93]
# print(binarySearch(testList,17))


"""递归实现二分查找"""

# def binarySearch(alist,item):
#     if len(alist) == 0:
#         return False
#     midpoint = len(alist)//2
#     if alist[midpoint] == item:
#         return True
#     else:
#         if alist[midpoint] > item:
#             return binarySearch(alist[:midpoint],item)
#         else:
#             return binarySearch(alist[midpoint+1:],item)
# testList =[17,20,26,30,44,54,55,65,77,93]
# print(binarySearch(testList,17))


"""
hash（哈希）查找
"""

