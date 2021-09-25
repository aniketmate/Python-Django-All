# # # class Person:
# # #     pass

# # # p1 = Person()
# # # print(type(p1))
# # # print(id(p1))
# # # p2 = Person()
# # # print(type(p2))
# # # print(id(p2))

# # # # class Classname:
# # # #     """docstring"""

# # def details(obj):
# #     print(f"""
# # Name:- {obj.Name}\n Surname:- {obj.Surname}\n Age:- {obj.Age}\n Mobile:- {obj.Mobile}\n Address:- {obj.Address}      
# #     """)
# # class Person:
# #     """for person details"""
# #     def __init__(self, nm, surnm, ag, mob, adr="Pune", *args,**kwargs):
# #         # print(self,"in init")
# #         # print("In init method")
# #         self.Name = nm
# #         self.Surname = surnm
# #         self.Age = ag
# #         self.Mobile = mob
# #         self.Address = adr
# #         # print(args) #tuple
# #         # print(kwargs) #dict
# #     def person_details(self):
# #         if hasattr(self, "id"):
# #             # print("ABC")
# #             data = f"Person Id:- {self.id}"
# #         else:
# #             data = ' '
# #         print(f"""
# #  {data}, \n Name:- {self.Name}\n Surname:- {self.Surname}\n Age:- {self.Age}\n Mobile:- {self.Mobile}\n Address:- {self.Address}      
# #     """)
# #     def set_salary(self, sal):
# #         print("in set salary....!")
# #         self.Salary = sal

# #     def increment_sal(self):
# #         self.Salary += (self.Salary*10/100)    
# # # Person()
# # # for i in range(10):
# # #     Person()    

# # p1 = Person("Aniket", "Mate", 33, 2332443443, "Pune")
# # # print(p1.Name)
# # # print(p1.Surname)
# # # print(p1.Age)
# # # print(p1.Mobile)
# # # print(p1.Address)
# # # print(p1.__dict__)
# # # p1.Surname= "Patil"
# # # p1.Salary = 53000
# # # print(p1.__dict__)
# # print(p1)
# # p1.id = 101
# # p1.person_details()
# # # print(p1.__dict__)
# # # p1.person_details()
# # # p1.set_salary(53000)
# # # print(p1.Salary)
# # # p1.increment_sal()
# # # print(p1.__dict__)

# # # details(p1)
# # # print("---------------------------------")


# # # print(p1)
# # # print(p1)
# # # print(p1.__dict__)
# # # print(p1.Name)
# # # print(p1.Surname)
# # # print(p1.Age)
# # # print(p1.Mobile)
# # # print(p1.Address)

# # p2 = Person("Bhagyashree", "Jagtap", 26, 2324234324, "mumbai" )
# # p2.person_details()
# # # print(p2.__dict__)
# # # print(p2.Name)
# # # print(p2.Surname)
# # # print(p2.Age)
# # # print(p2.Mobile)
# # # print(p2.Address)
# # # details(p2)
# # # print("---------------------------------")
# # # print(p2.Name)
# # # p2.set_salary(43000)
# # # print(p2.Salary)

# # # p3 = Person("Abhijeet", "Mate", 27, 3244355445 )
# # # print(p3.__dict__)
# # # print(p3.Name)
# # # print(p3.Surname)
# # # print(p3.Age)
# # # print(p3.Mobile)
# # # print(p3.Address)
# # # details(p3)
# # # p3.Mobile=232323913192
# # # details(p3)
# # # print("---------------------------------")
# # # p3.set_salary(33000)
# # # print(p3.Salary)


# # # print(p3.Name)

# # # p4=p3
# # # p5=p4
# # # del p3
# # # del p4
# # # print(p5)
# # # details(p5)
# # # print(p1)
# # # print(p1.__doc__)
# # # print(hex(id(p1)))


# import constants 

# # class Employee:
# #     def __init__(self, id, nm, ag, sal, desgn):
# #           self.EmpID = id
# #           self.EmpName = nm
# #           self.EmpAge = ag
# #           self.EmpSalary = sal
# #           self.EmpDesignation = desgn

# #     def __str__(self):
# #         return f"\n{self.__dict__}"
# #         #  return f"\nEmployee ID:-{self.EmpID}------Employee Name:-{self.EmpName}"
# #     def __repr__(self):
# #         return str(self)
          

# # e1 = Employee(id=101, nm="ABC101", ag=24, sal=32423, desgn=constants.SOFTWARE_ENGINEER )          
# # # print(e1.__dict__)
# # # print(e1)
# # e2 = Employee(id=102, nm="ABC102", ag=25, sal=52423, desgn=constants.TESTER )          
# # e3 = Employee(id=103, nm="ABC103", ag=26, sal=55423, desgn=constants.LINUX_ADMIN )          
# # e4 = Employee(id=104, nm="ABC104", ag=27, sal=45423, desgn=constants.DEVOPS_ENGINEER )          
# # e5 = Employee(id=105, nm="ABC105", ag=28, sal=423, desgn=constants.SOFTWARE_ENGINEER )       
# # # print(e1, e2, e3, e4, e5)   

# # emp_list = [e1, e2, e3, e4, e5]
# # # print(emp_list)
# # # for emp in emp_list:
# #     # print(emp, end = '')

# # def get_emp_by_id(eid):
# #     filtered_emp_list = list()
# #     for emp in emp_list:
# #         if emp.EmpID in {eid, 105}:
# #             # print(emp.EmpName)
# #               filtered_emp_list.append(emp)  
# #         return filtered_emp_list          
# # res = get_emp_by_id(103)            
# # print(res)

# # def increment_sal(sal, incre_perc, flag):
# #     """increment employees salary by given percentage"""
# #     for emp in emp_list:
# #         if flag == "greater":
# #             if emp.EmpSalary >= sal:
# #                 emp.EmpSalary -= (emp.EmpSalary * incre_perc/100)
# #         elif flag == "smaller":   
# #             if emp.EmpSalary <= sal:
# #                  emp.EmpSalary += (emp.EmpSalary * incre_perc/100) 
# #     return f"Salary Increment by {increment_sal} %"        

# # res = increment_sal(50000, 10, "smaller")
# # print(res)    
# # print(emp_list)


# class Student:
#     school_name = "Fr Agnel"
#     # print(school_name)
#     def __init__(self, sid, nm, age, marks, bg): 
#         self.StudId = sid
#         self.StudName = nm
#         self.StudAge = age
#         self.StudMarks = marks
#         self.Bloodgroup = bg
#         self.StudName = "sfsfsd"
#         # self.school_name = "NMMC"
#         # Student.school_name = "NMMC"

#         # del self.StudAge
#         # print("School Name:- ", self.school_name)

#     def __str__(self):
#         return f"\n{self.__dict__}"

#     def __repr__(self):
#         return str(self)
        

#     def show_details(self):
#         print(f""" 
# Stud ID:- {self.StudId}
# Stud Name:- {self.StudName}
# Stud Age:- { self.StudAge} 
# Stud Marks:- {self.StudMarks}  
#         """)

#     def show_result(self):
#         if self.StudMarks < 35:
#             print(f"{self.StudName} got C grade")
#         elif (self.StudMarks >= 35) and (self.StudMarks <= 65):
#             print(f"{self.StudName} got B grade")
#         elif (self.StudMarks > 65) and (self.StudMarks <= 100):
#             print(f"{self.StudName} got A grade")

#     def set_topper_tag(self):
#         print("inside instance method:-",self.StudName)
#         self.is_topper = True

#     def modify_marks(self, marks):
#         self.StudMarks = marks    
#         self.school_name = "ABC"

#     def remove_bloodgroup(self):
#         del self.Bloodgroup
#     @classmethod
#     def get_class_name(cls):
#         # print(cls)    
#         print(cls.school_name)
#         print(Student.school_name)

        
# s1 = Student(sid=101, nm="ABC", age=23, marks=56, bg="A+") 
# s1.get_class_name()
# # print(s1.school_name)
# # print(Student.school_name)

# # s1.school_name = "NMMC"
# # print(s1.__dict__)
# # print("S1---------------",s1) 
# # s1.is_topper = True
# # print(s1) 

# # s2 = Student(sid=102, nm="XYZ", age=25, marks=56, bg="B+")   
# # print(s2.school_name) 
# # s2.school_name
# # print(s2.__dict__)
# # s2.set_topper_tag()
# # s2.modify_marks(45)
# # s2.remove_bloodgroup()
# # s2.modify_marks(88)
# # print(s2)
# # print("S2------------------",s2)  
# # print(Student.school_name)
# # print(s2.__dict__)
# # s1.show_details()
# # list_of_stud = []
# # no_of_studs = int(input("Enter number of students:- "))

# # for i in range(1, no_of_studs+1):
# #     print(f"-------------------Stud Number:- {i}------------------")
# #     stud_name = input("Enter name of stud:-  ")
# #     stud_age = int(input("Enter age of stud:-  "))
# #     stud_marks = int(input("Enter marks of stud:-  "))

# #     stud_obj = Student(sid=100+i, nm=stud_name, age=stud_age, marks=stud_marks)
# #     stud_obj.show_result()
# #     list_of_stud.append(stud_obj)
    

# # print(list_of_stud)

class Product:
    no_of_objects = 0
    def __init__(self, pid, nm, price):
        self.ProductID = pid
        self.ProductName = nm
        self.ProductPrice = price
        Product.no_of_objects += 1
    @classmethod
    def get_no_of_objects(cls):
        print("No of Objects for {} is {}".format(cls, cls.no_of_objects))    


    @staticmethod
    def calculate(v1, v2, v3):
        print(f"Addition:- ", v1+v2+v3)

    def get_prod_details(self):
        print(f"""Product Id:- {self.ProductID}, Product Name:- {self.ProductName}, Product Price:-{ self.ProductPrice}""")    

#     def call_instance_method(self):
#         self.get_prod_details()


# p1 = Product(101, "Laptop", 45009)
# p2 = Product(102, "Mobile", 15009)
# p3 = Product(103, "Refrigerator", 35009)
# p4 = Product(104, "Tablet", 25009)
# p5 = Product(105, "TV", 55009)
# # Product.get_no_of_objects()
# # Product.calculate(4524, 45242, 543242)
# p1.call_instance_method()

# class ListOperations:
#     def __init__(self,lst): 
#         self.list1 = lst


#     def l_append(self, val):
#         self.list1.append(val)
#         print("given value appended successfully....")

#     def l_insert(self, val, ind=None):
#         if ind:
#             self.list1.insert(ind, val)
#         else:
#             self.list1.append(val)

#         print("given value inserted successfully.....")    

#     def get_list(self):
#         print(self.list1)    

# my_list = [4,2,4,25,1,58,6,25]    
# lo_obj = ListOperations(my_list)    
# # lo_obj.l_append("Python")
# lo_obj.l_insert(val="django")
# lo_obj.get_list()



