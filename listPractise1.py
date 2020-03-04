###列表

# 拼接
def test1():
    list1 = []
    for i in range(1000):  # n
        list1 = list1 + [i]


# append方式
def test2():
    list1 = []
    for i in range(1000):  # n
        list1.append(i)


# 列表推导式
def test3():
    list1 = [i for i in range(1000)]


# 转格式
def test4():
    list1 = list(range(1000))


from timeit import Timer

t1 = Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "seconds")
if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()

# pop操作
x = range(2000000)
x = list(x)
pop_zero = Timer("x.pop(0)", "from __main__ import x")  # n
print("pop_zero", pop_zero.timeit(number=1000), "seconds")

pop_end = Timer("x.pop()", "from __main__ import x")  # 1
print("pop_end ", pop_end.timeit(number=1000), "seconds")

# dict







