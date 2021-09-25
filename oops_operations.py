# CRUD --- Create, Read-- all, single, Update, Delete

# create -- prod data -- add to list
# read -- all --- No data, 
# read single -- id
# update -- id, prod data
# delete -- id

class Product:
    Ecommerce_Platform = "Amazon"
    list_of_products = []
    def __init__(self, pid, pname, pprice, pqty, pcat):
        self.ProductID = pid
        self.ProductName = pname
        self.ProductPrice = pprice
        self.ProductQty = pqty
        self.ProductCategory = pcat

    def show_details(self):
        print(f"""
Product Id:- {self.ProductID}        
Product Name:- {self.ProductName}
Product Price:- {self.ProductPrice}
Product Quantity:- {self.ProductQty}


        """)

    def total_price(self):
        total = self.ProductQty * self.ProductPrice
        return f" Total price for {self.ProductName}:- {total}"   

    def __str__(self): 
        return f"\n{self.__dict__}"    

    def __repr__(self):
        return str(self)  

    @classmethod
    def set_ids_list(cls):
        cls.ids_list = list(map(lambda x: x.ProductID, cls.list_of_products))

    @classmethod
    def add_product(cls, prod):
        if type(prod) == cls:
            cls.list_of_products.append(prod)
        elif type(prod) == list:
             cls.list_of_products.extend(prod)
        cls.set_ids_list()
        
        # print("Product /s added successfully in amazon")

    # @classmethod
    # def multiple_add_product(cls, *args):
    #     cls.list_of_products.extend(args)
    #     print(f"{len(args)} productsadded successfully in amazon")

    @classmethod
    def get_all_products(cls):
        print(cls.list_of_products)    
    
    @classmethod
    def get_single_product(cls, pid):
        cls.ids_list = map(lambda x: x.ProductID, cls.list_of_products)
        # print(ids_list)
        if pid in cls.ids_list:
            for prod in cls.list_of_products:
                if prod.ProductID == pid:
                    return prod
        else:
            return(f"no product found with given pid...Available product ids:-{cls.ids_list}")            

    @classmethod
    def update_product(cls, pid, data):
        for item in cls.list_of_products:
            if item.ProductID == pid:
                name = data.get("name")
                price = data.get("price")
                qty = data.get("qty")
                cat = data.get("cat")
                if name:
                    item.ProductName = name
                if price:
                    item.ProductPrice = price
                if qty:
                    item.ProductQty = qty
                if cat:
                    item.ProductCategory = cat
                if data.get("id"):
                    print("Product updated successfully .....! but ID cannot be updated as it has a unique value")
                else:
                    print("Product updated successfully...!")

                break
            else:
                print(f"no product found with given pid...Available product ids:-{cls.ids_list}")
    @classmethod
    def delete_prod(cls, pid):
        if pid in cls.ids_list:
            for item in cls.list_of_products:
                if item.ProductID == pid:
                    cls.list_of_products.remove(item)
                    print("Product removed successfully....!")
                    break
        else:
            print(f"no product found with given pid...Available product ids:-{cls.ids_list}")        

            # if data.get("price"):

            #         item.ProductPrice = data.get("price")
                    
                

p1 = Product(pid=101, pname="Laptop", pprice=54000, pqty=2, pcat="electronics")         
p2 = Product(pid=102, pname="Table", pprice=5400, pqty=1, pcat="Furniture")         
p3 = Product(pid=103, pname="Bicycle", pprice=12000, pqty=7, pcat="Vehicle")     

basket = [p1,p2,p3]
# # Product.multiple_add_product(p1,p2,p3)
# Product.add_product(basket)
# print(Product.list_of_products)

# print(Product.get_all_products())

# list_of_products = [p1, p2, p3]
# total = 0 
# for item in list_of_products:
#     total += (item.ProductPrice * item.ProductQty)
#     print(item.total_price())
# # print(list_of_objects)
# print(total)

# print(p3.total_price())
Product.get_single_product(103)

# p1.show_details()

# Product.update_product(103, {"name": "ring","price": 656645, "qty": 75, "cat": "gold 23"})
print(Product.get_single_product(103))
# Product.get_all_products()
# Product.delete_prod(102)
# Product.get_all_products()


import random
import re
import string
import time
class Bank:
    """Bank application having all type of transaction"""
    bank_name = "ICICI"
    customer_details = []
    def __init__(self, cusername, ciasact=True, cbal= 3000 ):  
        self.CustomerID = random.randint(101, 1000)
        self.CustomerName = cusername
        self.CustomerAccNo = random.randint(111111111, 999999999)
        self.CustomerBalance = cbal
        self.CustomerIsActive = ciasact
        self.Customerpassword = self.generate_password()
        print(f"Account created successfully for Username:- {self.CustomerName}...Account No:-{self.CustomerAccNo}...Account Balance:-{self.CustomerBalance}...Password:-{self.Customerpassword} ")
        Bank.customer_details.append(self)
        # self.Loan_eligibility = self.loan_eligible()
        
       

        

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        print(type(characters))  
        l = [random.choice(characters) for i in range (0, random.randint(5, 9))]
        pswd = "".join(l)
        return pswd

    def __str__(self):
        return f"\n {self.__dict__}" 

    def __repr__(self):
        return self(str)

    @classmethod
    def bank_login(cls, username, password):
        username_list = list(map(lambda x: x.CustomerName, cls.customer_details))    
        if username in username_list:
            for cust in cls.customer_details:
                if cust.CustomerName == username and cust.Customerpassword == password:
                    return cust
        else:
            print("Invalid Credentials....!")           

    def show_account_details(self):
        return f"""
        ------Account Details------
        Customer ID: {self.CustomerID}
        Customer Name: {self.CustomerName}
        Customer Acc No: {self.CustomerAccNo}
        Customer Balance: {self.CustomerBalance}
        Customer Password: {self.Customerpassword}
        Customer is Activate: {self.CustomerIsActive}
        """  

    def check_balance(self):
        return f"Available balance for {self.CustomerName}:- {self.CustomerBalance}Rs."


    def deposit(self, amt):
        self.CustomerBalance += amt
        res = self.check_balance()
        msg = f"{amt}Rs. is deposited in your account {self.CustomerAccNo} successfully! \n{res}"
        return msg

    def withdraw(self, amt):
        if self.CustomerBalance > amt:
            self.CustomerBalance -= amt
            res = self.check_balance()
            msg = f"{amt}Rs. is withdrawn from your account {self.CustomerAccNo} successfully! \n{res}"
            return msg


    def change_password(self, old_pass, new_pass):
        """TO CHANGE PASSWORD"""
        pass_list = list(map(lambda x:x.Customerpassword,self.customer_details))
        print(pass_list)
        if old_pass in pass_list:
            if self.Customerpassword == old_pass:
                print("Old Password Matches")
        else:
            return("old Password does not match")        
        flag = 0
        while True:

            if (len(new_pass)<8):
                flag = -1
                break
            elif not re.search("[a-z]", new_pass):
                flag = -1
                break
            elif not re.search("[A-Z]", new_pass):
                flag = -1
                break
            elif not re.search("[0-9]", new_pass):
                flag = -1
                break
            elif not re.search("[_@$]", new_pass):
                flag = -1
                break
            elif re.search("\s", new_pass):
                flag = -1
                break
            else:
                flag = 0
                print("New Password is Valid")
                confirm_pass = input("Confirm the new Password:-  ")
                print(confirm_pass) 
                if new_pass != confirm_pass:
                    return("Entered passwords do not match")
                else:
                    new_pass == confirm_pass
                    print(f"New Password is {confirm_pass}")  
                    return(f"Account created successfully for Username:- {self.CustomerName}...Account No:-{self.CustomerAccNo}...Account Balance:-{self.CustomerBalance}...Password:-{new_pass} ")
                

        if flag == -1:
            return("New Password Not a Valid") 
            
               
  
        
            
        
            
             

           
            # else:

            #     if i == 4:
            #     print("Too many invalid choices ...!")
            #     break
            # i += 1
            #     print("Invalid Choice")

            # else:
            #     break
                    
                    

        
        
       

        

            

    # def loan_eligible(self, amt=20000):
    #     if self.CustomerBalance >= 15000:
    #         print(f"you are eligible for loan of Rs.{amt} \n If you want to avail loan press  Y for Yes and N for N")
    #         self.get_loan(amt)
    #     else:
    #         print (f"If you maintain a balance of 15000 Rs you will be eligible for a loan of {amt}")

    # def get_loan(self, amt= 20000):
    #     choice = input("Enter a choice Y or N : ") 
    #     if choice == "Y":
    #         for i in range(10):
    #             time.sleep(1)
    #             print (i)
    #         res = self.deposits(amt)
    #         print(res)
    #     elif choice == "N":
    #         print("Thank you for your time")


while True:
    print(f"Welcome to {Bank.bank_name} Bank...!")
    print(""" 
    Enter 1 to open account
    Enter 2 to use exisiting account
    Enter 3 to cancel the process
    
    """)
    user_inp = int(input("Enter your choice:- "))

    if user_inp == 1:
        username = input("Enter username:- ")
        initial_balance = int(input("Enter initial amount:- "))
        Bank(cusername=username, cbal=initial_balance)

    elif user_inp == 2:
        print("U need to login first:- ")
        username = input("Enter username:- ")
        password = input("Enter password:- ")
        logged_in_cust_obj = Bank.bank_login(username, password)
        if logged_in_cust_obj:
            print("Logged in customer:- ", logged_in_cust_obj)
            i = 1
            while True:
                print("""
        Enter 1 to check balance
        Enter 2 to deposit
        Enter 3 to withdraw
        Enter 4 to show account details
        Enter 5 to change password 
        Enter 6 to transfer
        Enter 7 to exit       
                
                """)
                user_option = int(input("Enter a choice:- "))
                if user_inp == 1:
                    print(logged_in_cust_obj.check_balance())

                elif user_option == 2:
                    amt_inp = int(input("Enter a amount to be deposited:---  "))
                    print(logged_in_cust_obj.deposit(amt_inp))

                elif user_option == 3:
                    amt_inp = int(input("Enter a amount to be withdrawn:---  "))
                    print(logged_in_cust_obj.withdraw(amt_inp))  

                elif user_option == 4:
                    print(logged_in_cust_obj.show_account_details())  

                elif user_option == 5:
                    old_pass = input("Enter your old password:-  ")
                    print("Enter a new password which must contain atleast one uppercase and lowercase alphabet, one digit, one special character" )
                    new_pass = input("Enter a new Password:-  ")      
                    print (logged_in_cust_obj.change_password(old_pass,new_pass))

                    
                elif user_option == 6:
                    pass

                elif user_option == 7:
                    pass



                else:
                    if i == 4:
                        print("Too many invalid choices ...!")
                        break
                    i += 1
                    print("Invalid Choice")

        else:
            break


    elif user_inp == 3:
        print("Thanks for using this application....!")
        break     
    else:
        print("Invalid Choice...!")

    print("--------------------------------------------------")
print("After Bank Application")

# print()

# ---------------------------------------OUTPUT------------------------------------------------------------------
  
# username = input("Enter username:- ")
# initial_balance = int(input("Enter initial amount:- "))            
# cust_01 = Bank(cusername=username, cbal=initial_balance)


# Enter a choice:- 5
# Enter your old password:-  oI6^~
# Enter a new password which must contain atleast one uppercase and lowercase alphabet, one digit, one special character
# Enter a new Password:-  Arsenal@88
# ['oI6^~']
# Old Password Matches
# New Password is Valid
# Confirm the new Password:-  Arsenal@89
# Arsenal@89
# Entered passwords do not match

# Enter a choice:- 5
# Enter your old password:-  6}32i!$
# Enter a new password which must contain atleast one uppercase and lowercase alphabet, one digit, one special character
# Enter a new Password:-  Arsen
# ['6}32i!$']
# Old Password Matches
# New Password Not a Valid

# Enter a choice:- 5
# Enter your old password:-  u$7AyrtS)
# Enter a new password which must contain atleast one uppercase and lowercase alphabet, one digit, one special character
# Enter a new Password:-  Arsenal@88
# ['u$7AyrtS)']
# Old Password Matches
# New Password is Valid
# Confirm the new Password:-  Arsenal@88
# Arsenal@88
# New Password is Arsenal@88
# Account created successfully for Username:- aniket...Account No:-592425969...Account Balance:-50...Password:-Arsenal@88

# Enter a choice:- 5
# Enter your old password:-  dasd
# Enter a new password which must contain atleast one uppercase and lowercase alphabet, one digit, one special character
# Enter a new Password:-  asdsdd
# ["4@^T'"]
# old Password does not match


        



