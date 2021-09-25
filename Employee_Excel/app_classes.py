class Common:
    def __str__(self):
        return f"\n{self.__dict__}"
    
    def __repr__(self):
        return str(self)




class Employee(Common):
    
    def __init__(self,eid,ename,eage,esal,eadr):
        self.EmpID = eid
        self.EmpName = ename
        self.EmpAge = eage
        self.EmpSalary = esal
        self.EmpAddress = []
        if type(eadr) == list:
            self.EmpAddress.extend(eadr)
            
class Address(Common):
    def __init__(self,pin,city,state):
        self.AddrPin = pin
        self.AddrCity = city
        self.AddrState = state

    
    def __str__(self):
        return f"{self.__dict__}"


# if __name__ == '__main__':

    # eadr= Address(pin=410218, city="Navi Mumbai", state="MH")

    # e= Employee(eid=121,ename="aa",eage=23,esal=258,eadr= eadr)



    # print(eadr)

    # print(e.EmpAddress)


        