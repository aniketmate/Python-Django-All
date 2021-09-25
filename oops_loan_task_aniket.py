import random
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
        self.Loan_eligibility = self.loan_eligible()
        
       

        

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


    def show_account_details(self):
        return f"""
        Customer ID: {self.CustomerID}
        Customer Name: {self.CustomerName}
        Customer Acc No: {self.CustomerAccNo}
        Customer Balance: {self.CustomerBalance}
        Customer Password: {self.Customerpassword}
        Customer is Activate: {self.CustomerIsActive}
        """  

    def check_balance(self):
        return f"Available balance for {self.CustomerName}:- {self.CustomerBalance}Rs."


    def deposits(self, amt):
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

    def loan_eligible(self, amt=20000):
        if self.CustomerBalance >= 15000:
            print(f"you are eligible for loan of Rs.{amt} \n If you want to avail loan press  Y for Yes and N for N")
            self.get_loan(amt)
        else:
            print (f"If you maintain a balance of 15000 Rs you will be eligible for a loan of {amt}")

    def get_loan(self, amt= 20000):
        choice = input("Enter a choice Y or N : ") 
        if choice == "Y":
            for i in range(10):
                time.sleep(1)
                print (i)
            res = self.deposits(amt)
            print(res)
        elif choice == "N":
            print("Thank you for your time")



  
username = input("Enter username:- ")
initial_balance = int(input("Enter initial amount:- "))            
cust_01 = Bank(cusername=username, cbal=initial_balance)




# OUTPUT-I
# Enter username:- aniket
# Enter initial amount:- 15000
# <class 'str'>
# Account created successfully for Username:- aniket...Account No:-506717480...Account Balance:-15000...Password:-{v_4y;l
# you are eligible for loan of Rs.20000
#  If you want to avail loan press  Y for Yes and N for N
# Enter a choice Y or N : Y
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 20000Rs. is deposited in your account 506717480 successfully!
# Available balance for aniket:- 35000Rs.

# C:\Users\Mate>python "e:/aniket mate/oops_operations.py"
# Enter username:- aniket
# Enter initial amount:- 18695
# <class 'str'>
# Account created successfully for Username:- aniket...Account No:-380588182...Account Balance:-18695...Password:-PK8;7u
# you are eligible for loan of Rs.20000
#  If you want to avail loan press  Y for Yes and N for N
# Enter a choice Y or N : Y
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 20000Rs. is deposited in your account 380588182 successfully!
# Available balance for aniket:- 38695Rs.

# OUTPUT II

# Enter username:- aniket
# Enter initial amount:- 10000
# <class 'str'>
# Account created successfully for Username:- aniket...Account No:-787083429...Account Balance:-10000...Password:-dWv3/j7
# If you maintain a balance of 15000 Rs you will be eligible for a loan of 20000

# OUTPUT 3

# Enter username:- aniket
# Enter initial amount:- 15891
# <class 'str'>
# Account created successfully for Username:- aniket...Account No:-544417419...Account Balance:-15891...Password:-$d`2pS"
# you are eligible for loan of Rs.20000
#  If you want to avail loan press  Y for Yes and N for N
# Enter a choice Y or N : N
# Thank you for your time

