from parent_file import Base


class Product(Base):
    """PRODUCT DETAILS"""
    list_of_prods = []
    # prod_names = list(map(lambda x : x.Prodname, list_of_prods))

    def __init__(self, pid, nm, cat, price, qty):
        self.ProdID = pid
        self.ProdName = nm
        self.ProdCat = cat
        self.ProdPrice = price
        self.ProdQty = qty
        


if __name__ == '__main__':
    prod_obj_1 = Product(pid=1001, nm="Laptop", cat="Electronics", price=45126, qty=1)
    prod_obj_2 = Product(pid=1002, nm="Denim", cat="Clothing", price=1245, qty=10)
    prod_obj_3 = Product(pid=1003, nm="Watches", cat="Accessories", price=45126, qty=25)
    prod_obj_4 = Product(pid=1004, nm="BMW car", cat="Toys", price=1245, qty=2)
    prod_obj_5 = Product(pid=1005, nm="Pan", cat="Utensils", price=1245, qty=25)
    prod_obj_6 = Product(pid=1006, nm="Basmati Rice", cat="Groceries", price=1245, qty=50)
    Product.list_of_prods.extend([prod_obj_1, prod_obj_2,prod_obj_3,prod_obj_4,prod_obj_5,prod_obj_6])
    print(Product.list_of_prods)
    
    