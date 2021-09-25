from parent_file import Base

class Order(Base):
    """ORDER DETAILS"""
    all_ordered_list = []
    def __init__(self, transaction_id, cust, amount, type_of_order = "Purchase"):
        self.OrderTransactionID = transaction_id
        self.OrderCust = cust
        self.OrderAmount = amount
