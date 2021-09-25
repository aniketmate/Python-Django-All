from account_file import Account
from address_file import Address
from customer_file import Customer
from flipkart import Flipkart
from product_file import Product

# Account("Savings", 45455)


prod_obj_1 = Product(pid=1001, nm="Laptop", cat="Electronics", price=45126, qty=1)
prod_obj_2 = Product(pid=1002, nm="Denim", cat="Clothing", price=1245, qty=10)
prod_obj_3 = Product(pid=1003, nm="Watches", cat="Accessories", price=45126, qty=25)
prod_obj_4 = Product(pid=1004, nm="BMW car", cat="Toys", price=1245, qty=2)
prod_obj_5 = Product(pid=1005, nm="Pan", cat="Utensils", price=1245, qty=25)
prod_obj_6 = Product(pid=1006, nm="Basmati Rice", cat="Groceries", price=124, qty=50)

Product.list_of_prods.extend([prod_obj_1, prod_obj_2, prod_obj_3, prod_obj_4, prod_obj_5, prod_obj_6])
# print(Product.list_of_prods)
flip_acc_obj = Account("Current", 10000000)
flip_obj = Flipkart(location="Mumbai", no_of_warehouses=4, products=Product.list_of_prods, acc= flip_acc_obj)
# print(flip_obj)
ad_obj = Address("21-B", "Kalamboli", 410218, "Panvel", "Maharashtra")
ad_obj1 = Address("41-B", "Vashi", 400718, "Navi Mumbai", "Maharashtra")

acc_obj = Account("Saving", 320000)
acc_obj1 = Account("Saving", 220000)



cust_obj_1 = Customer(cid=123456789, name= "ABC", addr= ad_obj, acc= acc_obj, mobile_no= +919542344756, email = "abc@gmail.com",isplus_member=True)
cust_obj_2 = Customer(cid=132547891, name= "XYZ", addr= ad_obj1, acc= acc_obj1, mobile_no= +919556895219, email = "xyz@gmail.com",isplus_member=False)
# print("----------------------------------------------")
# print(cust_obj_1)
# print("----------------------------------------------")
# flip_obj.purchase_products("Laptop", cust_obj_1, 1)
# flip_obj.purchase_products("Pan", cust_obj_1, 2)
# flip_obj.purchase_products("Basmati Rice", cust_obj_1,5)
# flip_obj.purchase_products("Basmati Rice", cust_obj_2,5)
# flip_obj.purchase_products("Laptop", cust_obj_1, 1)
# flip_obj.purchase_products("Laptop", cust_obj_2, 1)

# print("----------------------------------------------")

print(cust_obj_1)

print("----------------------------------------------")

flip_obj.return_products("Basmati Rice", cust_obj_1, 4)

print(cust_obj_1)


print("----------------------------------------------")


# print(cust_obj_1)
# print(flip_obj.FlipProducts)

# print(flip_obj)



"""
OUTPUT
1-----------------------------------------------------------------------------------------------
{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 43055, 'Acctype': 'Saving', 'AccBalance': 3200}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [], 'ReturnedProds': [], 'IsPlusMember': True}
----------------------------------------------

{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 50} Flipkart stock before order
Total price after discount 589.0
Thanks for purchasing product with Flipkart....Your transaction ID generated is:- 7796762

{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 45} Flipkart stock after order
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 43055, 'Acctype': 'Saving', 'AccBalance': 2611.0}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [
{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 5}], 'ReturnedProds': [], 'IsPlusMember': True}
----------------------------------------------

{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 45} Flipkart stock before return

{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 49} Flipkart stock after return
total price for return is 496
Successfully returned product to Flipkart....Your transaction ID generated is:- 399
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 43055, 'Acctype': 'Saving', 'AccBalance': 3107.0}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [
{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 5}], 'ReturnedProds': [
{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 4}], 'IsPlusMember': True}

2-------------------------------------------------------------------------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 40701, 'Acctype': 'Saving', 'AccBalance': 320000}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [], 'ReturnedProds': [], 'IsPlusMember': True}
----------------------------------------------

{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 1} Flipkart stock before order
Total price after discount 40726.215
Thanks for purchasing product with Flipkart....Your transaction ID generated is:- 6559068

{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 0} Flipkart stock after order
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 40701, 'Acctype': 'Saving', 'AccBalance': 279273.78500000003}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [
{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 1}], 'ReturnedProds': [], 'IsPlusMember': True}
----------------------------------------------

3-------------------------------------------------------------------------------------------------------------
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 77659, 'Acctype': 'Saving', 'AccBalance': 320000}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [], 'ReturnedProds': [], 'IsPlusMember': True}
----------------------------------------------

{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 1} Flipkart stock before order
Total price after discount 40726.215
Thanks for purchasing product with Flipkart....Your transaction ID generated is:- 8297187

{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 0} Flipkart stock after order
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 77659, 'Acctype': 'Saving', 'AccBalance': 279273.78500000003}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [
{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 1}], 'ReturnedProds': [], 'IsPlusMember': True}
----------------------------------------------
4-------------------------------------------------------------------------------------------------------------
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 66701, 'Acctype': 'Saving', 'AccBalance': 320000}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [], 'ReturnedProds': [], 'IsPlusMember': True}
----------------------------------------------

{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 50} Flipkart stock before order
Total price after discount 589.0
Thanks for purchasing product with Flipkart....Your transaction ID generated is:- 8840338

{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 45} Flipkart stock after order
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 66701, 'Acctype': 'Saving', 'AccBalance': 319411.0}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [
{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 5}], 'ReturnedProds': [], 'IsPlusMember': True}
----------------------------------------------
5----------------------------------------------------------------------------------------------------------------
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 55716, 'Acctype': 'Saving', 'AccBalance': 320000}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [], 'ReturnedProds': [], 'IsPlusMember': False}
----------------------------------------------

{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 1} Flipkart stock before order
Total price after discount 42869.7
Thanks for purchasing product with Flipkart....Your transaction ID generated is:- 4947836

{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 0} Flipkart stock after order
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 55716, 'Acctype': 'Saving', 'AccBalance': 277130.3}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [
{'ProdID': 1001, 'ProdName': 'Laptop', 'ProdCat': 'Electronics', 'ProdPrice': 45126, 'ProdQty': 1}], 'ReturnedProds': [], 'IsPlusMember': False}
----------------------------------------------
6--------------------------------------------------------------------------------------------------------------
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 13124, 'Acctype': 'Saving', 'AccBalance': 320000}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [], 'ReturnedProds': [], 'IsPlusMember': False}
----------------------------------------------

{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 50} Flipkart stock before order
Total price after discount 620
Thanks for purchasing product with Flipkart....Your transaction ID generated is:- 6041970

{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 45} Flipkart stock after order
----------------------------------------------

{'CustID': 123456789, 'CustName': 'ABC', 'CustAddress':
{'AddrHouse': '21-B', 'AddrArea': 'Kalamboli', 'AddrPin': 410218, 'AddrCity': 'Panvel', 'AddrState': 'Maharashtra'}, 'CustAcc':

{'AccountNo': 13124, 'Acctype': 'Saving', 'AccBalance': 319380}, 'CustMobile': 919542344756, 'CustEmail': 'abc@gmail.com', 'OrderedProds': [
{'ProdID': 1006, 'ProdName': 'Basmati Rice', 'ProdCat': 'Groceries', 'ProdPrice': 124, 'ProdQty': 5}], 'ReturnedProds': [], 'IsPlusMember': False}
----------------------------------------------
"""