"""
列表表示
"""
# myTree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]
# print('左树', myTree[1])
# print('根节点', myTree[0])
# print('右树', myTree[2])

"""
抽象数据类型   ADT或者节点表示方式
"""


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        # 新的根节点
        self.leftChind = None
        self.rightChind = None

    # 插入左树
    def insertLeft(self, newMode):
        if self.leftChind == None:
            self.leftChind = BinaryTree(newMode)
        else:
            temp = BinaryTree(newMode)
            temp.leftChind = self.leftChind
            self.leftChind = temp

    # 插入右树
    def insertRight(self, newMode):
        if self.rightChind == None:
            self.rightChind = BinaryTree(newMode)
        else:
            temp = BinaryTree(newMode)
            temp.rightChind = self.rightChind
            self.rightChind = temp

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def getLeftChind(self):
        return self.leftChind

    def getRightChind(self):
        return self.rightChind


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChind())
r.insertLeft('b')
print(r.getLeftChind())
print(r.getLeftChind().getRootVal())
r.insertRight('c')
print(r.getRightChind())
print(r.getRightChind().getRootVal())
r.getRightChind().setRootVal('hello')
print(r.getRightChind().getRootVal())
