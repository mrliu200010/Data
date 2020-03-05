#队列

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



# 打印机
"""
1.创建打印任务的队列。每个任务都有个时间戳，队列启动的时候为空
2.是否创建新的打印任务？如果是，创建时间戳添加到队列
3.打印机不忙并且有任务在等待:
    从打印机队列中删除一个任务并将其分配给打印机
    当前时间减去创建任务的时间戳，计算该任务的等待时间
    将该任务的等待时间添加到列表中稍后处理
    根据打印的页数，确定需要多少时间
4.打印机需要1s打印，所以得从2分钟内-1s = 等待时间
5.任务完成，所需要的是时间是0，打印机空闲
6.模拟完成后，从生成的等待时间列表中计算平均等待时间


Printer 打印机对象  两种状态，默认空闲
PrinterQueue 打印队列对象，用来创建任务
Task 任务对象
"""
class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm #打印机的速率
        self.currnetTask = None # 空闲状态
        self.timeRemaining = 0 # 打印任务需要的时间

    def tick(self):
        if self.currnetTask !=None:
            self.timeRemaining = self.timeRemaining -1
            if self.timeRemaining <=0:
                self.currnetTask = None

    def busy(self):
        if self.currnetTask !=None:
            return True
        else:
            return False

    def startNext(self,newTask):
        self.currnetTask = newTask
        self.timeRemaining = newTask.getPages()*60/self.pagerate


import random
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime-self.timestamp

from pythonds.basic.queue import Queue

#newPrintTask 决定是否创建一个新的打印任务,一个小时之内20任务打印完成，打印任务每180秒到达一
def simulation(numSeconds,pagesPerMinute):
    labprinter = Printer(pagesPerMinute)#初始化打印机
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingtimes.append(nextTask.waitTime(currentSecond))
            labprinter.startNext(nextTask)
        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("平均等待时间为：%6.2f"%averageWait)




def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)#一个小时，速率5页






