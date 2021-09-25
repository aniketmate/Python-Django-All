# OOPs concepts / properties
# - abstraction
    # --- ATM --- 
        # -- hiding implementation -- user is not interested at all in process

# python --   private public   ----    var

# var = 10  -- public
# _var = 10 --- protected  - single underscore
# __var = 10 -- private -- strictly protected  -- double underscore

# Company --
# XYZ

# Amol -- Sales  -- 2 under -- 
# Ashish --  HR -- 
# Ashiwni -- Account 


# - encapsulation - wrapping data in single unit
    # Laptop -- ram, rom, cdrive, usb port, ssd, screen, graphic card -- 
    # classes  -- methods, variables  - BEST Example
        # 
    # object    
        # - Access Specifiers -- Abstraction
            # public, private, protected


# - inheritance- getting properties from parent class
    # --  Parents(1 Acre Plot) -- Son/Daughter(1 Acre)
    #    Parent class Base class -- Sublcass  child class
        # genetic disease -- 

# - polymorphism  -one thing many forms
    # poly -- many
    # morphism -- forms
            # +  
    # Person 

        # - 

# inheritance

class Professors:
    #setters
    def set_id(self, pid):
        self.ID = pid

    def set_name(self, name):
        self.Name = name

    def set_age(self, age):
        self.Age = age

    def set_salary(self, sal):
        self.Salary = sal

        #getters
    def get_id(self):
        return self.ID 

    def get_name(self):
        return self.Name

    def get_age(self):
        return self.Age

    def get_salary(self):
        return self.Salary 

p1 = Professors()
p1.set_id(101)
p1.set_name("ABC")
p1.set_age(25)
# print(p1.__dict__)
# print(p1.get_id(),p1.get_name(), p1.get_age())

class Student(Professors):
    def set_marks(self, mrk):
        self.Marks = mrk

    def get_marks(self):
        return self.Marks

s1 = Student()
s1.set_id(102)
s1.set_name("XYZ")
s1.set_age(19)
s1.set_marks(65)
# print(s1.__dict__)
# print(s1.get_id(),s1.get_name(), s1.get_age(), s1.get_marks())

# print(dir(s1))


class Father:
    def __init__(self,property):
        self.FatherProperty = property

    def show_property(self):
        print(f"Father's Property:- {self.FatherProperty}")

class Daughter(Father):
    def __init__(self, f_property, d_property):
        super().__init__(f_property)
        self.DaughterProperty = d_property

    def show_property(self):
        print(f"Daughter's Property:- {self.DaughterProperty}, Father's Property:- {self.FatherProperty},Total Property has:-{self.DaughterProperty + self.FatherProperty} ")
        

# d1 = Daughter(d_property=5, f_property=10)
# print(d1.__dict__)
# d1.show_property()        

class A:
    def __init__(self, a):
        self.a = a

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __init__(self, a , b, c):
        self.a = a
        self.b = b 
        self.c = c
        
#override- takes the latest value
#overloading - calls the constructor which has that arguments
# a= A(10,20)
# print(a)

# inheritance
    # single level
    # multilevel

class A:
    def m1(self):
        print("In class A-m1")

class B(A):
    def m1(self, flag=None):
        if flag == 'A':
            super().m1()
        elif flag == 'B' or not flag:
            print("In class B-m1")
        elif flag == "AB":
            super().m1()
            print("In class B-m1")

    def m1(self):
        print("In class B-m1")
    
    def m2(self):
        super().m1()

    def m3(self):
        super().m1()
        self.m1

obj = B()
obj.m3

# case 1 -- Child class has no any method/constructor --- access parent's properties
# case 2 -- child class has its own method/constructor --- access own properties
# case 3 -- Child class has its own method/constructor -- access own + parents properties
# case 4 -- Child class has its own method/constructor -- access parents one only

# class Square:
#     def __init__(self, side):
#         self.Side = side
        
#     def area(self):
#         print(f"Area of square is:-{self.Side * self.Side}")

#     def utility_method(self, *args, **kwargs):
#         print("Square utility :- ",args, kwargs)
#         # Square.utility_method(self, *args, **kwargs)

# # l =Square(10)
# # l.area()

# class Rectangle(Square):
#     def __init__(self, side, breadth):
#         super().__init__(side)
#         Square.__init__(self, side)
#         self.Breadth = breadth
        
#     def area(self):
#         # super().area()
#         Square.area(self)
#         print(f"Area of rectangle is:-{self.Side * self.Breadth}")

#     def utility_method(self, *args, **kwargs):
#         print("Rectangle utility :- ",args, kwargs)
#         Square.utility_method(self, *args, **kwargs)


# obj = Rectangle(side=5, breadth=3)
# # obj.area()
# obj.utility_method(4,5,6,7,a=2)

# class A(object):
#     def m1(self):
#         print("In class A-m1")

# class B(A):
#     # def m1(self):
#     #     print("In class B-m1")
#     pass
# class C(B):
#     # def m1(self):
#     #     print("In class C-m1")
#     pass

# class D(C):
#     # def m1(self):
#     #     print("In class D-m1")
#     pass
    
# obj = D()
# # obj.m1()

# class Sample(object):
#     def __new__(cls):
#         print("In new method")
#         print("Creating Instance")
#         return super().__new__(cls)

#     def __init__(self):
#         print("In init method")

# s1 = Sample()


# d = {"a": 2, "b":10, "c": 20}
# class A:
#     def __init__(self, **kwargs):
#         print(kwargs)
#         self.A = kwargs.pop("a")
#         print(self.A, "hi")
#         print(kwargs)

# a = A(**d)

# import time

# def func(num):
#     l = []
#     for i in range(1, num+1):
#         l.append(i)
#     return l

# t1 = time.time()

# print(func(10000))

# t2 = time.time()
# print(t2-t1)

# multiple  -- multiple parents -- 
# class Father:
#     # def height(self):
#     #     print("Height:- 5.6")
#     pass

# class Mother:
#     def complexion(self):
#         print("fair")
#     pass

# class Son(Father,Mother):
#     # def height(self):
#     #     print("Height:- 6.6")
#     # pass
    
#     # def complexion(self):
#     #     print("Black")
#     pass

# # s = Son()
# # s.height()
# # s.complexion()
# # if hasattr(s, "height"):
# #     s.height()
# # else:
# #     print("Son has no attribute height")

# print(Son.__mro__)

# class A(object):
#     def m1(self):
#         print("In A-m1--1")
#         super().m1()
#         print("In A-m1--2")

# class B(object):
#     def m1(self):
#         print("In B-m1--1")
#         super().m1()
#         print("In B-m1--2")

# class C(object):
#     def m1(self):
#         print("In C-m1--1")
#         # super().m1()
#         print("In C-m1--2")

# class D(A, B):
#     def m1(self):
#         print("In D-m1--1")
#         super().m1()
#         print("In D-m1--2")

# class E(B, C):
#     def m1(self):
#         print("In E-m1--1")
#         super().m1()
#         print("In E-m1--2")

# class Z(D, E, C):
#     def m1(self):
#         print("In Z-m1--1")
#         super().m1()
#         print("In Z-m1--2")
#     pass

# z= Z()
# print(Z.mro())
# z.m1()


from abc import ABC, abstractmethod

# class RBI(ABC):
#     @abstractmethod
#     def atm_count_50_in_city(self):
#         pass


#     @abstractmethod
#     def loan_interest_rate_10_to_15(self):
#         pass

#     @abstractmethod
#     def NEFT(self):
#         pass

#     @abstractmethod
#     def Netbanking(self):
#         pass


# class HDFC(RBI):

 
#     # def atm_count_50_in_city(self):
#     #     print("67 ATM's in city")
    
#     # def loan_interest_rate_10_to_15(self):
#     #     print("11.5% on personal loan")

#     # def NEFT(self):
#     #     print("NEFT and RTGS are both avaialble")
    
#     # def Netbanking(self):
#     #     print("Secured Netbanking")

#     pass

# # h1 = HDFC()
# # h1.NEFT()

# class SBI(RBI):

 
#     def atm_count_50_in_city(self):
#         print("95 ATM's in city")
    
#     def loan_interest_rate_10_to_15(self):
#         print("10.5% on personal loan")

#     def NEFT(self):
#         print("NEFT and RTGS are both avaialble")
    
#     def Netbanking(self):
#         print("Secured Netbanking and mobile banking")

# # s1 = SBI()
# # s1.Netbanking()


# class Car(ABC):
#     @abstractmethod
#     def steering(self):
#         pass

#     @abstractmethod
#     def braking(self):
#         pass

#     def airbag(self):
#         print("available")

# class Tata(Car):
 
#     def steering(self):
#         print("Power Steering")

    
#     def braking(self):
#         print("ABS braking system")

# nexon = Tata()
# nexon.airbag()
# print(nexon)
# tiago = Tata()
# # print(tiago)


# class FileOpeClass(ABC):
#     @abstractmethod
#     def open(self):
#         pass


#     @abstractmethod
#     def close(self):
#         pass

# class Excel(FileOpeClass):
#     def open(self, path):
#         print("Excel File is opened path for that file:- ", path)

#     def close(self):
#         print("Excel file is closed")

# e1 = Excel()
# e1.open()
# e1.close()

# class Text(FileOpeClass):
#     def open(self):
#         print(" Text file is opened:- ")

#     def close(self):
#         print("Text file is closed")


# class Implementationclass:
#     user_input = input("enter a file type:- ")
#     class_name = globals()[user_input]
#     obj = class_name()
#     obj.open()
    # obj.close()

# def foo():
#     flag = True
#     if not flag:
#         return not True
#     print (foo())

# f = foo()
# print (f())
