from copy import deepcopy
from parent_file import Base
# from customer_file import Customer
from product_file import Product
from order_file import Order
import random


class Flipkart(Base):
    """FLIPKART APPLICATION"""
    def __init__(self, location, no_of_warehouses, products, acc=1000000,  headq = "Banglore"):
        self.FlipLocation = location
        self.FlipHeadQuarter = headq
        self.FlipNoOfWarehouses = no_of_warehouses
        self.FlipProducts = products
        self.FlipAcc = acc
        self.prods_names = list(map(lambda x : x.ProdName, self.FlipProducts))

    def purchase_products(self, productname, cust, qty):
        """PURCHASE PRODUCT DETAILS"""
        # print()
        if productname in self.prods_names:
            for prod in self.FlipProducts:
                if productname == prod.ProdName:
                    # print(prod)
                    if qty <= prod.ProdQty:
                        total_price = qty * prod.ProdPrice
                        # print(f"total price for purchase is {total_price}")
                        if cust.CustAcc.AccBalance >= total_price:
                            print(prod, "Flipkart stock before order")
                            # flag = 0
                            while True:
                                # check if order is more than 15000
                                if total_price >= 15000:
                                    # flag == 0
                                    total_price = total_price - total_price *(5/100)
                                # check customer is plus member
                                if cust.IsPlusMember == True:
                                    # flag == 1
                                    total_price = total_price - total_price *(5/100)
                                # check customer purchase less than 15000 and not isplus member
                                # else:
                                #     flag == 0
                                #     print("No Discount avialable")
                                    # total_price = total_price - total_price *(5/100)         
                                # cust.CustAcc.AccBalance =  cust.CustAcc.AccBalance - total_price
                                cust.CustAcc.AccBalance -= total_price
                                self.FlipAcc.AccBalance += total_price
                                actual_quantity = prod.ProdQty
                                prod.ProdQty = qty
                                cust.OrderedProds.append(deepcopy(prod))
                                prod.ProdQty = actual_quantity - qty
                                # create transaction id
                                trans_id = random.randint(1111111, 9999999)
                                print("Total price after discount", total_price)
                                order_obj = Order(transaction_id=trans_id, cust= cust, amount=total_price)
                                Order.all_ordered_list.append(order_obj)
                                print(f"Thanks for purchasing product with Flipkart....Your transaction ID generated is:- {trans_id}")
                                cust.OrderTransactionID.append(trans_id)
                                print(prod, "Flipkart stock after order")
                                break
                                
                            
                        else:
                            print("Insufficient amount to purchase this product....!")
                    else:
                        print(f"Qty should be less than or equal to {prod.ProdQty}")
                        return

        else:
            print(f"Given product is not available.Available products are:- {Product.prods_names}")

    def return_products(self,productname, cust, qty):
        """RETURN PRODUCT DETAILS"""
        if productname in self.prods_names:
            for prod in self.FlipProducts:
                if productname == prod.ProdName:
                    print(prod, "Flipkart stock before return")
                    actual_quantity = prod.ProdQty
                    prod.ProdQty = qty
                    cust.ReturnedProds.append(deepcopy(prod))
                    prod.ProdQty = actual_quantity + qty
                    print(prod, "Flipkart stock after return")
                    return_total_price = qty * prod.ProdPrice
                    print(f"total price for return is {return_total_price}")
                    cust.CustAcc.AccBalance += return_total_price
                    self.FlipAcc.AccBalance -= return_total_price
                    trans_id = random.randint(111, 999)
                    order_obj = Order(transaction_id=trans_id, cust= cust, amount=return_total_price)
                    Order.all_ordered_list.append(order_obj)
                    print(f"Successfully returned product to Flipkart....Your transaction ID generated is:- {trans_id}")
                

if __name__ == '__main__':
    prod_obj_1 = Product(pid=1001, nm="Laptop", cat="Electronics", price=45126, qty=1)
    prod_obj_2 = Product(pid=1002, nm="Denim", cat="Clothing", price=1245, qty=10)
    prod_obj_3 = Product(pid=1003, nm="Watches", cat="Accessories", price=45126, qty=25)
    prod_obj_4 = Product(pid=1004, nm="BMW car", cat="Toys", price=1245, qty=2)
    prod_obj_5 = Product(pid=1005, nm="Pan", cat="Utensils", price=1245, qty=25)
    prod_obj_6 = Product(pid=1006, nm="Basmati Rice", cat="Groceries", price=1245, qty=50)
    flip_obj = Flipkart(location="Mumbai", no_of_warehouses=4, products=[prod_obj_1,prod_obj_2,prod_obj_3, prod_obj_4, prod_obj_5, prod_obj_6])
    # cust_obj_1 = Customer(cid=123456789, name= "ABC", addr= ad_obj, acc= acc_obj, mobile_no= +919542344756, email = "abc@gmail.com")
    
    print(flip_obj)
   

