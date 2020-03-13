"""
字典：connectedTo
addNeighbor方法用于从这个顶点添加一个链接到另一个点点
getConnections方法返回邻接表中的所有点
getWeight方法放回权重
"""


# class Vertex:
#     def __init__(self,key):
#         self.id = key
#         self.connectedTo = {}
#
#     def addNeighbor(self,nbr,weight):
#         self.connectedTo[nbr] = weight
#
#     def __str__(self):
#         return str(self.id) + 'connectedTo:' + str([x.id for x in self.connectedTo])
#
#     def getConnections(self):
#         return self.connectedTo.keys()
#
#     def getId(self):
#         return self.id
#
#     def getWeight(self,nbr):
#         return self.connectedTo[nbr]
#
#
#
# #图
# class Graph():
#     def __init__(self):
#         self.vertList = {}
#         self.numVertices = 0
#
#     def addVertex(self,key):
#         self.numVertices = self.numVertices + 1
#         newVertex = Vertex(key)
#         self.vertList[key] = newVertex
#         return newVertex
#
#     def getVertex(self,n):
#         if n in self.vertList:
#             return self.vertList[n]
#         else:
#             return None
#     #返回所有顶点
#     def __contains__(self, n):
#         return n in self.vertList
#
#     def addEdge(self,fromVert,toVert,weight=0):
#         if fromVert not in self.vertList:
#             nv = self.addVertex(fromVert)
#         if toVert not in self.vertList:
#             nv = self.addVertex(toVert)
#
#         self.vertList[fromVert].addNeighbor(self.vertList[toVert],weight)
#
#     def getVertices(self):
#         return self.vertList.keys()
#
#     def __iter__(self):
#         return iter(self.vertList.values())
#
# g = Graph()
# for i in range(6):
#     g.addVertex(i)
#
# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,2,1)
# g.addEdge(5,4,8)
#
#
# for v in g:
#     for w in v.getConnections():
#         print("( %s,%s )"%(v.getId(),w.getId()))


"""
字梯问题：将单词Fool转化成SAGE
描述：每次必须转换一个字母
比如：
FOOL
POOL
POLL
POLE
PALE
SALE
SAGE
我们的目的：计算最小转换次数
步骤：1.将字之间的关系表示为图
      2.使用广度优先搜索的图算法来找到有效路径
如果两个词只有一个字母不同，我们就创建他们两个之间的一条边

"""
from pythonds.graphs import  Graph
#wordfile 单词文件
def buildGraph(wordFile):
    d = {}
    wfile = open('./wordFile', 'r')
    i = 0
    for line in wfile:
        if i % 2 == 0:
            word = line[:-1]
        i = i + 1


