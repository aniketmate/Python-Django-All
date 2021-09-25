property


class Employee:
    def __init__(self,eid,name,sal,inc):
        self.EmployeeID = eid
        self.EmployeeName = name
        self.EmployeeSalary = sal
        self.validate_increment(inc)

    def get_details(self):
        '''SHOW EMPLOYEE DETAILS '''
        print(f"""
        Employee ID :- {self.EmployeeID}
        Employee Name :- {self.EmployeeName}
        Employee Salary :- {self.EmployeeSalary}
        Employee Increment :- {self.EmployeeIncrement}
        
        """)

    def validate_increment(self,value):
        if value>=5 and value<= 25:
            self.Incrementperc = value
        else:
            raise ValueError("Increment should be between 5 to 25.")



# e1 =Employee(101,"Aniket", 45000, 6)
# print(e1.__dict__)
# e1.EmployeeName = "Abhijeet"
# print(e1.__dict__)
# e1.validate_increment(26)
# print(e1.__dict__)
# e1.Incrementperc =  29
# print(e1.__dict__)

class Celsius:
    def __init__(self, temp=37):
        self.set_temp(temp)

    def celsius_to_farenheit(self):
        fenhr = (self.get_temp()*1.8) +32
        return fenhr

    def set_temp(self,value):
        print("In setter method") 
        if value < -273:
            raise ValueError("Temp should not be below -273 degree celsius ")
        else:
            self._Temp = value

    def get_temp(self):
        print("In getter method")
        return self._Temp

# c1 = Celsius(-274)
# print(c1.Temp)
# print(c1.celsius_to_farenheit())
# print(c1.__dict__)
# print(c1.get_temp())
# c1.set_temp(-272)
# print(c1.get_temp())
# c1.Temp = 56

        
class Celsius:
    def __init__(self, temp=37):
        self.temperature =temp

    def celsius_to_farenheit(self):
        fenhr = (self.get_temp()*1.8) +32
        return fenhr

    def set_temp(self,value):
        print("In setter method") 
        if value < -273:
            raise ValueError("Temp should not be below -273 degree celsius ")
        else:
            self._Temp = value

    def get_temp(self):
        print("In getter method")
        return self._Temp        
        
        
    temperature = property(fget=get_temp,fset=set_temp)
        
# c1 = Celsius(120)
# # print(c1.__dict__)  
# print(c1.temperature)      

    
class Celsius:
    def __init__(self, temp=37):
        self.temperature =temp

    def celsius_to_farenheit(self):
        fenhr = (self.get_temp()*1.8) +32
        return fenhr
    @property
    def temperature(self):
        print("In getter method")
        return self._Temp        
    @temperature.setter
    def temperature(self,value):
        print("In setter method") 
        if value < -273:
            raise ValueError("Temp should not be below -273 degree celsius ")
        else:
            self._Temp = value

c1 = Celsius(-274)
# print(c1.__dict__)  
print(c1.temperature)      
    