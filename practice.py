# txt = "abc@gjhjh.com"
# x = txt.split(sep= "@")
# print (x)
# txt.
# raise ValueError


    
# dict_football_clubs = {1:"Arsenal", 2:"Man City", 3:"Liverpool", 4:"Chelsea", 5:"Man U", 6:"Tottenham"}

# def get_val(val):
#     if key, value in dict_football_clubs.items():
#         return key
#     else:
#         print("Football club not present in the current dictionary")


# val = input("Enter a football Club name:- ")
# a = get_val(val)
# print(a)
# import os
# FILE_PATH_3 = "E:\\aniket mate\\"

# def A_Zfilegen():
#     n = 0 
#     for n in range (0,26): 
#         with open(chr(65+n) + ".txt", "w"):
#             n +=1
#     return n
    
# A_Zfilegen()
    

# # # f = open(FILE_PATH_3, mode="a+")
# import string
# # for i in range(string.ascii_uppercase):
# for i in range (0,26):
#     n=0
#     a = chr(65+n)
#     letters = [:n]


# class Product:
#     no_of_objects = 0
#     def __init__(self, pid, nm, price):
#         self.ProductID = pid
#         self.ProductName = nm
#         self.ProductPrice = price
#         Product.no_of_objects += 1

#     @classmethod
#     def get_list_of_objects(cls):
#         print(f"No of Objects are {cls.list_objects}")    

#     @staticmethod
#     def calculate(v1, v2):
#         print(f"Addition:- ", v1+v2)

#     def get_prod_details(self):
#         print(f"""Product Id:- {self.ProductID}, Product Name:- {self.ProductName}, Product Price:-{ self.ProductPrice}""")    



# p1 = Product(101, "Television", 45009)
# p2 = Product(102, "Mobile", 15009)


# Product.calculate(45000,15009,35000)
# Product.get_list_of_objects()
# p1.get_prod_details()

# def div(a,b):
#     try:
#         user_input_1=input("Enter first no:- ")
#         user_input_2 =input("Enter second no:- ")
#         div(user_input_1,user_input_2)
#     except ZeroDivisionError: 
#         print("Denominator cannot be zero")

#     except TypeError:
#         if type(a) == str or type(b) == str:
#             print("cannot pass string in any input")

#     else:
#         print("division done successfully")
        
       

# div(2,4)


# d = {"a":1,"b":2,"c":3}
# print(d.values())
# print(d.keys())

# def get_value(val):
#     if val == d.values in d:
#         print(d.key())
#     else:
#         print("Key not able to fetch")
    
# get_value(1)



# import openpyxl
# FILE_PATH = r"E:\aniket mate\Excel_file_handling\first.xlsx"
# workbook = openpyxl.load_workbook(FILE_PATH)
# del workbook["Sheet"]
# workbook.save(FILE_PATH)
    