# class Employee:
#     def __init__(self, eid, nm, sal): 
#         self.EmpID = eid
#         self.EmpName = nm
#         self.EmpSalary = sal

#     def __str__(self):
#         return f"{self.__dict__}"
        

# e1 = Employee(101, "ABC", 45000)
# print(e1)

# # e1.EmpSalary = e1.EmpSalary + (e1.EmpSalary*15/100)
# # print(e1)

# class Test:
#     @staticmethod
#     def increment_salary(emp):
#         emp.EmpSalary = emp.EmpSalary + (emp.EmpSalary*15/100)
#         print(f"Salary incremented by 15 % for {emp.EmpName}")

# t1 = Test()
# t1.increment_salary(e1)
# print(e1)

# class Parent:
#     def __str__(self): 
#         return f"{self.__dict__}"

#     def __repr__(self):
#         return str(self)
        

# class Address(Parent):
#     def __init__(self, pin, area, city):
#         self.Pincode = pin
#         self.Area = area
#         self.city = city


# class Employee(Parent):
#     def __init__(self, eid, nm, sal, address): 
#         self.EmpID = eid
#         self.EmpName = nm
#         self.EmpSalary = sal
#         self.EmpAddress = address

# a1 = Address(pin=410218, area="Wakad", city="Pune")
# # print(a1)
# a2 = Address(pin=400703, area="Kothrud", city="Pune")
# # print(a2)

# e1= Employee(eid=101, nm="ABC", sal=65478, address=[a1, a2])
# print(e1.EmpAddress)

# # from pre import parent
# e2 = Employee(eid=102, nm="XYZ", sal=45663, address=a2)
# # print(e2)
# # print(e2.EmpAddress.city)


# class A:
#     print("in class A")

#     class B:
#         print("in class B")

# a=A()
# print(a)

# b=A.B()
# print(b)

# class Person:
#     def __init__(self, pid, name, addr, dd, mm, yyyy):
#         self.Id = pid
#         self.Name = name
#         self.Address = addr
#         self.date_of_birth = self.DateofBirth(dd,mm,yyyy)

#     def show_person_detials(self):
#         print(f'''
# ID:- {self.Id}
# Name:-{self.Name}
# Address:-{self.Address}
#         ''')
        
#     class DateofBirth:
#         def __init__(self, dd=None, mm=None, yyyy=None):
#             print("In class DOB init")
#             self.DD = dd
#             self.MM = mm
#             self.YYYY = yyyy
        
#         def show_dob_details(self):
#             print(f'''Date: {self.DD} Month: {self.MM} Year: {self.YYYY}''')
        
# # p1 = Person(101, "Raju", "Pune")
# p2 = Person(102, "Shyam", "Mumbai", 10, 1, 1986)
# print(p2.date_of_birth.DD)
# print(p2.date_of_birth.MM)
# print(p2.date_of_birth.YYYY)
# p2.date_of_birth.show_dob_details()

# p1.show_person_detials()
# p2.show_person_detials()
# Person.DateofBirth()

# Person.DateofBirth(31,1,1985).show_dob_details()
# p1.DateofBirth(31,1,1985).show_dob_details()
