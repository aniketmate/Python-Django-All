from account_file import Account
from address_file import Address
from parent_file import Parent


class Employee(Parent):
    emp_list = []
    # ids_list = []
    def __init__(self, eid, nm, ag, sal, addr, acc):
        self.EmpID = eid
        self.EmpName = nm
        self.EmpAge = ag
        self.EmpSalary = sal
        self.EmpAddress = addr  
        self.EmpAcc = acc 
        

    def show_employee_details(self):
        """EMPLOYEE DETAILS"""
        return (f"""
            -------ADDRESS-------
        EMPLOYEE ID:- {self.EmpID}
        EMPLOYEE NAME:- {self.EmpName}
        EMPLOYEE AGE:- {self.EmpAge}
        EMPLOYEE SALARY:- {self.EmpSalary}
        EMPLOYEE ADDRESS:- {self.EmpAddress}
        EMPLOYEE ACC:- {self.EmpAcc}
        
         """)

    @classmethod
    def set_ids_list(cls):
        """ EMPLOYEE ID SET"""
        cls.ids_list = list(map(lambda x: x.EmpID, cls.emp_list))
        # Employee.ids_list.extend([101,102,103,104,105])
        return cls.ids_list


    
        
        

        
    @classmethod
    def add_employee(cls,emp,eid):
        """ ADD EMPLOYEE """
        if type(emp) == cls:
            cls.emp_list.append(emp)
        elif type(emp) == list:
             cls.emp_list.extend(emp)
        cls.set_ids_list()  
        print(f"Employee added successfully in Employee List..{cls.emp_list}!")

    @classmethod
    def get_single_emp(cls,eid):
        """ GET SINGLE EMPLOYEE DETAILS"""
        cls.set_ids_list()
        if eid in cls.ids_list:
            for emp in cls.emp_list:   
                if emp.EmpID == eid: 
                    print(emp)
        else:
            print(f"No Employee found with given pid...Available Employee ids:-{cls.ids_list}") 


    @classmethod
    def get_all_employees(cls):
        """ GET ALL EMPLOYEE DETAILS"""
        print(cls.emp_list)

    
    @classmethod
    def increment_sal(cls,sal,flag):
        """INCREMENT FOR EMPLOYEE WITH SALARY LESS THAN 50000 BY 10%"""
        for emp in cls.emp_list:
            if flag == "less":
                if emp.EmpSalary < sal:
                    emp.EmpSalary += (emp.EmpSalary * 10/100)   
        print(f"Incremented salary of employees {cls.emp_list}")

    @classmethod
    def delete_emp(cls, eid):
        """ REMOVE EMPLOYEE DETAILS"""
        cls.set_ids_list()
        if eid in cls.ids_list:
            for emp in cls.emp_list: 
                if emp.EmpID == eid:
                    cls.emp_list.remove(emp)
                    print("Employee deleted successfully....!")
                    break
        else:
            print(f"No employee found with given pid...Available product ids:- {cls.ids_list}")


    @classmethod
    def update_empdetails(cls, eid, data):
        """ Update EMPLOYEE DETAILS """
        cls.set_ids_list()
        for emp in cls.emp_list:
            if emp.EmpID == eid:
                nm = data.get("name")
                ag = data.get("age")
                sal = data.get("sal")
                addr = data.get("address")
                acc = data.get("account")

                if nm:
                    emp.EmpName = nm
                if ag:
                    emp.EmpAge = ag
                if sal:
                    emp.EmpSalary = sal
                if addr:
                    emp.EmpAddress = addr
                if acc:
                    emp.EmpAcc = acc
                if data.get("id"):
                    print("Employee updated successfully .....! but ID cannot be updated as it has a unique value")
                else:
                    print("Employee updated successfully...!")

                break
        else:
            print(f"no Employee found with given pid...Available product ids:-{cls.ids_list}")      






if __name__ == '__main__':
                
   

    acc_obj1 = Account("Saving", "IDBI", 5000)
    acc_obj2 = Account("Saving", "IDBI", 4589)
    acc_obj3 = Account("Saving", "IDBI", 7845)
    acc_obj4 = Account("Saving", "IDBI", 8898)
    acc_obj5 = Account("Saving", "IDBI", 887)

    ad_obj1 = Address("18-1004", "Kalamboli", 410218, "Panvel", "Maharashtra")
    ad_obj2 = Address("17", "Koperkhairne", 400709, "Navi Mumbai", "Maharashtra")
    ad_obj3 = Address("8", "Vashi", 400703, "Navi Mumbai", "Maharashtra")
    ad_obj4 = Address("PL-31", "New Panvel", 410206, "Panvel", "Maharashtra")
    ad_obj5 = Address("KL-55", "Roadpali", 410219, "Panvel", "Maharashtra")

    e1 = Employee(eid=101, nm="Aniket", ag=24, sal=45600,addr= ad_obj1, acc=acc_obj1)
    e2 = Employee(eid=102, nm="Piyush", ag=26, sal=48600,addr=ad_obj2,acc=acc_obj2)
    e3 = Employee(eid=103, nm="Kaustubh", ag=27, sal=35600,addr=ad_obj3,acc=acc_obj3)
    e4 = Employee(eid=104, nm="Rahul", ag=25, sal=65600,addr=ad_obj4,acc=acc_obj4)
    e5 = Employee(eid=105, nm="Kunal", ag=24, sal=54892,addr=ad_obj5,acc=acc_obj5)
    e6 = Employee(eid=106, nm="King", ag=24, sal=54547,addr=ad_obj5,acc=acc_obj5)


    # 

    # print(Employee.emp_list)
emp_obj = Employee(eid = Employee.emp_list, nm= Employee.emp_list, ag= Employee.emp_list, sal=Employee.emp_list, addr=Address.addr_list, acc = Account.acc_list)



# print(Employee.ids_list)
# print(Employee.emp_list)
# Employee.get_all_employees()
# Employee.get_single_emp(103)
# print(Employee.ids_list)
# Employee.ids_list.extend([101,102,103,104,105])
# Employee.delete_emp(103)
# Employee.get_all_employees()
# Employee.set_ids_list()
# Employee.show_employee_details()
# print(e1.show_employee_details())


