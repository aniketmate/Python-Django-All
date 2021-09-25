from app_classes import Employee, Address
import random

city_state = {"Pune":"MH", "Chennai": "Tamil Nadu", "Banglore": "Karnataka", "Hyderabad": "Telangana"}

def generate_name():
    name = ""
    for i in range(0, random.randint(4,9)):
        name += chr(65 + random.randint(1,25))
    return(name)

# generate_name()

def generate_employee(num):
    list_of_emp = []
    for i in range(1, num+1):
        city_name = random.choice(list(city_state.keys()))
        emp_obj = Employee(eid =100+i, ename = generate_name(), eage = random.randint(25,45),esal=random.randint(12000,85000),
                  eadr=Address(pin= random.randint(123456,987456),city=city_name,state= city_state.get(city_name)))
        list_of_emp.append(emp_obj)

    return list_of_emp

def data_with_multiple_addresses():
    ad1 = Address(pin=456123, city="Pune", state="MH")
    ad2 = Address(pin=123458, city="Mumbai", state="MH")
    ad3 = Address(pin=321654, city="Alibaug", state="MH")
    ad4 = Address(pin=789456, city="Panvel", state="MH")


    e1 = Employee(eid=101, ename="ABC", eage=23, esal=45623, eadr=[ad1,ad2])
    e2 = Employee(eid=102, ename="XYZ", eage=23, esal=47896, eadr=[ad1])
    e3 = Employee(eid=103, ename="PQR", eage=23, esal=56563, eadr=[ad1,ad2,ad3])
    e4 = Employee(eid=104, ename="STU", eage=23, esal=45214, eadr=[ad1,ad4])

    list_of_emp = [e1,e2,e3,e4]
    return list_of_emp

if __name__ == '__main__':
    print(data_with_multiple_addresses())

# print(generate_employee(10))