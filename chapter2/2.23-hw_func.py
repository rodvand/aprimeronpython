"""
Write three functions
"""

def hw1():
    return 'Hello, World!'

def hw2():
    print 'Hello, World!'

def hw3(one, two):
    print "%s,%s" % (one, two)

print hw1()
hw2()
hw3('Hello ', 'World!')

"""
Running program
Unix>python 2.23-hw_func.py
Hello, World!
Hello, World!
Hello ,World!
"""