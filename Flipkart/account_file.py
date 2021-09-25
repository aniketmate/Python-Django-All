from parent_file import Base

import random

class Account(Base):
    """ACCOUNT DETAILS"""
    def __init__(self, acctype, balance=3000):
        self.AccountNo = random.randint(11111, 99999)
        self.Acctype = acctype
        if balance < 3000:
            raise ValueError("Account Balance should be more than or equal to 3000")
        self.AccBalance = balance


if __name__ == '__main__':
    acc_obj = Account("Saving", 320000)
    print(acc_obj)
        