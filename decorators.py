# def func():
#     def inner():
#         return"hello"
#     return inner

# a = func()
# print(a) # reference of inner
# print(a()) # returns inner and prints hello


# def func(a):
#     a()

# def add():
#     print("p" + "ython")
# print(add) #refernce of add
# func(add)


# def decor_func(func):
#     print("In decor function 1",func)
#     def inner():
#         print("*************")
#         func()
#         print("*************")
#     print("In decor function 2")
#     return inner

# @decor_func
# def add():
#     print(54 + 65)

# add()
# res = decor_func(add)
# res()
# print(res)

# import time
# def get_time_decor(func):
#     print("in get time decor func")
#     def inner():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         print(f"Time taken by {func.__name__}:{t2-t1}")
#     return inner

# @get_time_decor
# def get_values_list():
#     l =[]
#     for i in range (1,6):
#         time.sleep(2)
#         l.append(i)
#     print(l)

# get_values_list()

# def decor(func):
#     def inner(x,y):
#         if y == 0:
#             print("U cannot divide by 0...!")
#         elif (type(x)==str) or (type(y)==str):
#             print("U cannot divide by string...!")
#         elif (type(x) != int) or (type(y) != int):
#             print("Invalid data type passed")
#         else:
#             func(x,y)
#     return inner
        
# @decor
# def divide(a,b):
#     print(a/b)

# divide(10,"a")

# def decor(func):
#     def wrapper_func(a,*args,**kwargs):
#         print("positional arg:-", a)
#         print("variable length args:- ",args)
#         print("variable length keyword argument:-",kwargs)
#         func(a,*args,**kwargs)
#     return wrapper_func
# @decor
# def addition(v1,*args,**kwargs):
#     total = 0+v1
#     for i in args:
#         total +=i
#     total += sum(list(kwargs.values()))
#     print(total)


# addition(12, 1,2,3,l=2,b=3)


def star_decor(func):
    print("In star func", func.__name__)
    def inner_star():
        print("*********")
        func(), print("hi")
        print("*********")
    return inner_star

def hash_decor(func):
    print("In hash func", func.__name__)
    def inner_hash():
        print("##########")
        func(), print("bye")
        print("##########")
    return inner_hash

def and_decor(func):
    print("In and func", func.__name__)
    def inner_and():
        print("&&&&&&&&&")
        func() , print("sy")
        print("&&&&&&&&&")
    return inner_and

@and_decor
@star_decor
@hash_decor      
def add():
    print(56 + 98)

add()
# res = star_decor(hash_decor(add))
# res()


# class TestClass:
#     def __init__(self):
#         self.var1 = 20
#         self.var2 = 40

#     def __call__(self, *args, **kwargs):
#         print("In call method",args,kwargs)

# t1 = TestClass()
# t1("python", a=10, b=20)


# class TestClassDecor:
#     def __init__(self,f):
#         self.function = f
#         self.start = "Hi welcome to python world"
#         self.end = "Bye Bye"
#         # print(f.__name__)

#     def __call__(self, *args, **kwargs):
#         print(self.start)
#         self.function(*args, **kwargs)
#         print(self.end)

# @TestClassDecor
# def func(*args, **kwargs):
#     print("in func")
#     print("Variable len args:- ", args)
#     print("Variable len keyword args:- ", kwargs)
# func.function()

# # print(func)
# # res = TestClassDecor(func)
# # print(res)
# func(1,2,3,[1,2,3],a=2,b=3)