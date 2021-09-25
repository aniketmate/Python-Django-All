from parent_file import Parent

import random

class Account(Parent):
    """ACCOUNT DETAILS"""
    acc_list = []
    def __init__(self, acctype, bank,bal):
        self.AccountNo = random.randint(111111111, 999999999)
        self.Acctype = acctype
        self.Bank = bank
        self.AccBalance = bal






# if __name__ == '__main__':

acc_obj1 = Account("Saving", "IDBI", 5000)
acc_obj2 = Account("Saving", "IDBI", 4589)
acc_obj3 = Account("Saving", "IDBI", 7845)
acc_obj4 = Account("Saving", "IDBI", 8898)  
acc_obj5 = Account("Saving", "IDBI", 887)
Account.acc_list.extend([acc_obj1,acc_obj2,acc_obj3,acc_obj4,acc_obj5])
# print(Account.acc_list)

        