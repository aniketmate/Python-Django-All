

from parent_file import Base
from account_file import Account
from address_file import Address
from order_file import Order

class Customer(Base):
    """CUSTOMER DETAILS"""
    def __init__(self, cid, name, addr, acc, mobile_no, email, isplus_member=False):
        self.CustID = cid 
        self.CustName = name
        self.CustAddress = addr
        self.CustAcc = acc
        str_mobile = str(mobile_no)
        if str_mobile[:2] == "91" and len(str_mobile[2:]) == 10:
            self.CustMobile = mobile_no
        else:
            raise ValueError("Mobile number should have indian code and len should be equal to 10 digits...!")

        x = "@"
        y = "gmail.com"
        if x not in email:
            raise ValueError("Email id should have @")
        elif email.count(x)  != 1:
            raise ValueError(f"Email should consist {x} only once")
        elif  y not in (email.split(sep= "@")) :   
            # print ((email.split(sep= "@"))
            raise ValueError("Only gmail accounts are allowed access")
        elif email.count(y)  != 1:
            raise ValueError(f"Email should consist {y} only once")
        self.CustEmail = email
        self.OrderedProds = []
        self.ReturnedProds =[]
        self.OrderTransactionID = []
        self.IsPlusMember = isplus_member
        

        
if __name__ == '__main__':

    ad_obj = Address("45-A", "Hadapsar", 400703, "Pune", "Maharashtra")
    acc_obj =Account("Saving", 5800)
    cust_obj_1 = Customer(cid=123456789, name= "ABC", addr= ad_obj, acc= acc_obj, mobile_no= +919542344756, email = "abc@gmail.com")
    cust_obj_2 = Customer(cid=132547891, name= "XYZ", addr= ad_obj, acc= acc_obj, mobile_no= +919556895219, email = "xyz@gmail.com",isplus_member=False)
    
    print(cust_obj_1)
