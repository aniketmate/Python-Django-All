
from account_file import Account
from address_file import Address
from employee import Employee





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


emp_obj = Employee(eid = Employee.emp_list, nm= Employee.emp_list, ag= Employee.emp_list, sal=Employee.emp_list, addr=Address.addr_list, acc = Account.acc_list)

Employee.emp_list.extend([e1,e2,e3,e4,e5])

# print(Employee.ids_list)
# print(Employee.set_ids_list())
# Employee.update_empdetails(101,{"name": "Swapnil", "age": 23, "sal": 23845, "address": "Panvel", "account": {"acctype": "Saving", "bank": "HDFC", "bal": 5000}})
# Employee.get_single_emp(106)
# Employee.get_all_employees()
# emp_obj.get_all_employees()
# Employee.get_all_employees()
# emp_obj.get_single_emp(103)
# Employee.get_single_emp(103)
# emp_obj.get_single_emp(107)
# Employee.get_single_emp(107)
# Employee.delete_emp(102)
# Employee.delete_emp(109)
# emp_obj.delete_emp(102)
# Employee.get_all_employees()
# emp_obj.delete_emp(109)
# # Employee.increment_sal(50000,"less")
# emp_obj.increment_sal(50000,"less")
# Employee.add_employee(e6,106)
# emp_obj.add_employee(e6,106)
# Employee.get_single_emp(106)








# ---------------------------------------------------OUTPUT------------------------------------------------------------
""" [
{'EmpID': 101, 'EmpName': 'Aniket', 'EmpAge': 24, 'EmpSalary': 45600, 'EmpAddress':
{'AddrHouse': '18-1004', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 336010056, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 5000}},
{'EmpID': 102, 'EmpName': 'Piyush', 'EmpAge': 26, 'EmpSalary': 48600, 'EmpAddress':
{'AddrHouse': '17', 'AddrArea': 'Koperkhairne', 'AddrPin': 400709, 'AddrCity': 'Navi Mumbai', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 533173875, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 4589}},
{'EmpID': 103, 'EmpName': 'Kaustubh', 'EmpAge': 27, 'EmpSalary': 35600, 'EmpAddress':
{'AddrHouse': '8', 'AddrArea': 'Vashi', 'AddrPin': 400703, 'AddrCity': 'Navi Mumbai', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 234895860, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 7845}},
{'EmpID': 104, 'EmpName': 'Rahul', 'EmpAge': 25, 'EmpSalary': 65600, 'EmpAddress':
{'AddrHouse': 'PL-31', 'AddrArea': 'New Panvel', 'AddrPin': 410206, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 867119135, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 8898}},
{'EmpID': 105, 'EmpName': 'Kunal', 'EmpAge': 24, 'EmpSalary': 54892, 'EmpAddress':
{'AddrHouse': 'KL-55', 'AddrArea': 'Roadpali', 'AddrPin': 410219, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 544495228, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 887}}]


{'EmpID': 103, 'EmpName': 'Kaustubh', 'EmpAge': 27, 'EmpSalary': 35600, 'EmpAddress':
{'AddrHouse': '8', 'AddrArea': 'Vashi', 'AddrPin': 400703, 'AddrCity': 'Navi Mumbai', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 441701294, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 7845}}

No Employee found with given pid...Available Employee ids:-[101, 102, 103, 104, 105]

Employee deleted successfully....!
[
{'EmpID': 101, 'EmpName': 'Aniket', 'EmpAge': 24, 'EmpSalary': 45600, 'EmpAddress':
{'AddrHouse': '18-1004', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 646102797, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 5000}},
{'EmpID': 103, 'EmpName': 'Kaustubh', 'EmpAge': 27, 'EmpSalary': 35600, 'EmpAddress':
{'AddrHouse': '8', 'AddrArea': 'Vashi', 'AddrPin': 400703, 'AddrCity': 'Navi Mumbai', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 933998561, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 7845}},
{'EmpID': 104, 'EmpName': 'Rahul', 'EmpAge': 25, 'EmpSalary': 65600, 'EmpAddress':
{'AddrHouse': 'PL-31', 'AddrArea': 'New Panvel', 'AddrPin': 410206, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 592575433, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 8898}},
{'EmpID': 105, 'EmpName': 'Kunal', 'EmpAge': 24, 'EmpSalary': 54892, 'EmpAddress':
{'AddrHouse': 'KL-55', 'AddrArea': 'Roadpali', 'AddrPin': 410219, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 381808411, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 887}}]
No employee found with given pid...Available product ids:- [101, 103, 104, 105]
Incremented salary of employees [
{'EmpID': 101, 'EmpName': 'Aniket', 'EmpAge': 24, 'EmpSalary': 50160.0, 'EmpAddress':
{'AddrHouse': '18-1004', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 495001280, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 5000}},
{'EmpID': 102, 'EmpName': 'Piyush', 'EmpAge': 26, 'EmpSalary': 53460.0, 'EmpAddress':
{'AddrHouse': '17', 'AddrArea': 'Koperkhairne', 'AddrPin': 400709, 'AddrCity': 'Navi Mumbai', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 298463768, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 4589}},
{'EmpID': 103, 'EmpName': 'Kaustubh', 'EmpAge': 27, 'EmpSalary': 39160.0, 'EmpAddress':
{'AddrHouse': '8', 'AddrArea': 'Vashi', 'AddrPin': 400703, 'AddrCity': 'Navi Mumbai', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 773133935, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 7845}},
{'EmpID': 104, 'EmpName': 'Rahul', 'EmpAge': 25, 'EmpSalary': 65600, 'EmpAddress':
{'AddrHouse': 'PL-31', 'AddrArea': 'New Panvel', 'AddrPin': 410206, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 187721290, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 8898}},
{'EmpID': 105, 'EmpName': 'Kunal', 'EmpAge': 24, 'EmpSalary': 54892, 'EmpAddress':
{'AddrHouse': 'KL-55', 'AddrArea': 'Roadpali', 'AddrPin': 410219, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 531705349, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 887}}]

Employee added successfully in Employee List..[
{'EmpID': 101, 'EmpName': 'Aniket', 'EmpAge': 24, 'EmpSalary': 45600, 'EmpAddress':
{'AddrHouse': '18-1004', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 184475581, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 5000}},
{'EmpID': 102, 'EmpName': 'Piyush', 'EmpAge': 26, 'EmpSalary': 48600, 'EmpAddress':
{'AddrHouse': '17', 'AddrArea': 'Koperkhairne', 'AddrPin': 400709, 'AddrCity': 'Navi Mumbai', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 674490442, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 4589}},
{'EmpID': 103, 'EmpName': 'Kaustubh', 'EmpAge': 27, 'EmpSalary': 35600, 'EmpAddress':
{'AddrHouse': '8', 'AddrArea': 'Vashi', 'AddrPin': 400703, 'AddrCity': 'Navi Mumbai', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 475822551, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 7845}},
{'EmpID': 104, 'EmpName': 'Rahul', 'EmpAge': 25, 'EmpSalary': 65600, 'EmpAddress':
{'AddrHouse': 'PL-31', 'AddrArea': 'New Panvel', 'AddrPin': 410206, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 606994576, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 8898}},
{'EmpID': 105, 'EmpName': 'Kunal', 'EmpAge': 24, 'EmpSalary': 54892, 'EmpAddress':
{'AddrHouse': 'KL-55', 'AddrArea': 'Roadpali', 'AddrPin': 410219, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 342399419, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 887}},
{'EmpID': 106, 'EmpName': 'King', 'EmpAge': 24, 'EmpSalary': 54547, 'EmpAddress':
{'AddrHouse': 'KL-55', 'AddrArea': 'Roadpali', 'AddrPin': 410219, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 342399419, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 887}}]!

{'EmpID': 106, 'EmpName': 'King', 'EmpAge': 24, 'EmpSalary': 54547, 'EmpAddress':
{'AddrHouse': 'KL-55', 'AddrArea': 'Roadpali', 'AddrPin': 410219, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'EmpAcc':
{'AccountNo': 342399419, 'Acctype': 'Saving', 'Bank': 'IDBI', 'AccBalance': 887}}

 """
