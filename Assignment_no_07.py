


FILE_PATH = "E:\\aniket mate\\test.txt"
FILE_PATH_1 = "E:\\aniket mate\\test1.txt"
FILE_PATH_2 = "E:\\aniket mate\\test2.txt"

f = open(FILE_PATH, mode="r")
# print(type(f))
# print(f.read())
# print(f.readline())
# print(f.readlines())
# print(f.readlines()[-4:])
# data = f.readlines()  
# word = "aniket mate"





    

def read_first_n_lines(n):
    """READ FIRST N LINES"""
        
    f = open(FILE_PATH)
    data = f.readlines()
    for line in (data[:n]):
        if len(data) < n:
            return(f"Given line number does not exist....Range is available: 1 to {len(data)}")
        else:
            print(line, end = " ")
    return(f"The first {n} lines are read successfully ")
    

def read_first_n_lines(): 
    """READ FIRST N LINES"""
    data = f.readlines()  
    try:
        n = int(input("Enter the no of lines to be read:- "))
        for line in (data[:n]):
            if len(data) < n:
                raise IndexError        
            else:
                print(line, end = " ")
        return (f"The first {n} lines are read successfully...!")
    
    except IndexError:
            return(f"Given line number does not exist....Range is available: 1 to {len(data)}")
    except:
        return("The input should be integer")
 

def read_last_n_lines(n):
    """READ LAST N LINES"""
    data = f.readlines()
    for line in (data[-n:]):
        if len(data) < n:
            return(f"Given line number does not exist....Range is available: 1 to {len(data)}")
        else:
            print(line, end = " ")
    return(f"The last {n} lines are read successfully ")

def read_last_n_lines(): 
    """READ LAST N LINES"""
    # f =  open(FILE_PATH, mode="r")
    data = f.readlines()  
    try:
        n = int(input("Enter the no of lines to be read:- "))
        for line in (data[-n:]):
            if len(data) < n:
                raise IndexError        
            else:
                print(line, end = " ")
        return (f"The last {n} lines are read successfully...!")
#     # 
    except IndexError:
            return(f"Given line number does not exist....Range is available: 1 to {len(data)}")
    except:
        return("The input should be integer")

def append_txt():
    """APPEND TEXT"""
    f =  open(FILE_PATH, mode="a+")
    a = input("Enter lines:- ")
    f.write(a + "\n")
    f.seek(0,0)
    return(f.read())

def read_store_in_list():
    """READ LINE BY LINE AND STORE IN A LIST"""
    f = open(FILE_PATH, mode="r")
    data = f.readlines()
    store_list = [data]
    return store_list
    
    
def read_store_in_var():
    """READ LINE BY LINE AND STORE IN A VARIABLE"""
    f = open(FILE_PATH, mode="r")
    data = f.readlines()
    return data

def get_longest_word(): 
    """TO GET THE LONGEST WORD"""
    f = open(FILE_PATH, mode="r")
    data = f.read().split()
    a = sorted(data, key=len)
    return a[-1]
    
def no_of_lines():
    """COUNT NO OF LINES"""
    f = open(FILE_PATH, mode="r")
    data = f.readlines()
    return len(data)

def frequency_of_words():
    """FREQUENCY OF WORDS OCCURING IN TXT FILE"""
    f = open(FILE_PATH, mode="r")
    data = f.read().count("on")
    return data
    
def split(data):
    """FREQUENCY OF WORD OCCURING IN TXT FILE"""
    return list(data)
    # return [char for char in data]
f = open(FILE_PATH, mode="r")
data = f.read()
# print(list(data)) 
# print(split(data))
print(split(data).count("f")) 

def list_to_file():
    f =  open(FILE_PATH, mode="a+")
    a = input("Enter club names separated by space ")
    list_clubs = str(a.split(" "))
    # for element in list_clubs:
    f.write(list_clubs)
    f.seek(0,0)
    return f.read()

def copy_contents_to_file():
    """COPY CONTENTS OF ONE FILE TO OTHER FILE"""
    with open(FILE_PATH, mode="r") as firstfile, open(FILE_PATH_1, mode="a") as secondfile:
        for line in firstfile:
             secondfile.write(line)
        return ("File successfully copied..!")
   
def combine_contents_to_file():
    """COMBINE CONTENTS OF ONE FILE WITH OTHER FILE"""
    with open(FILE_PATH, mode="r") as firstfile, open(FILE_PATH_1, mode="r") as secondfile, open(FILE_PATH_2, mode="a+") as thirdfile:
        for line1, line2 in zip(firstfile,secondfile):
            thirdfile.write(line1 + line2)
        return ("File successfully combined..!")

import random
def read_random_line(f):
    """READ RANDOM LINE FROM TXT FILE"""
    f = open(FILE_PATH, mode="r")
    data = f.read().splitlines()
    return random.choice(data)

def remove_newlines_char(f):
    """REMOVE NEWLINE CHARACTERS"""
    f = open(FILE_PATH, mode="r")
    list_char = f.readlines()
    return [item.strip("\t,\n") for item in list_char]

def get_no_of_words(): 
    """COUNT OF NO OF WORDS IN TXT FILE"""
    f =  open(FILE_PATH, mode="r")
    data = f.readlines()
    count = 0
    for a in data:  
        count += len(a.split())  
    return count


import string
def letters_by_line(n):
    """ LETTERS BY SPECIFIED NO """

    with open(FILE_PATH_2, "w") as f:
       a = string.ascii_uppercase
       letters = [a[i:i + n] + "\n" for i in range(0, len(a), n)]
       f.writelines(letters)

def A_Zfilegen():
    """ GENERATE A TO Z TXT FILES """
    n = 0 
    for n in range (0,26): 
        with open(chr(65+n) + ".txt", "w"):
            n +=1
    return n
    
A_Zfilegen()
    

letters_by_line(5)

print(get_no_of_words()) 





print(remove_newlines_char(FILE_PATH))



print(read_random_line(FILE_PATH))


print(combine_contents_to_file())       
print(copy_contents_to_file())   
print(list_to_file())
print(frequency_of_words())
print(no_of_lines())
print(get_longest_word())
print(read_first_n_lines())
print(read_first_n_lines())

print(read_store_in_var())

print(read_store_in_list())
print(read_last_n_lines())
print(read_last_n_lines(40))
print(append_txt())
print(f.read())




"""
-------------------------------------------------OUTPUT-------------------------------------------------
Enter the no of lines to be read:- 6
init gets called when at the time object creation Automatically magic method
 first argument reserved self
 self points to current object holds object ref
 u can define instance variables?  by using self keyword
 u can use any alternate name instead of self BUT preferred self
 instance  seperate copy for each object
 The first 6 lines are read successfully...!

Enter the no of lines to be read:- 40
Given line number does not exist....Range is available: 1 to 30

in init, we can modify the static variable using classname classname.static_variable_name new_name
 in instance method, we can modify the static variable using classname classname.static_variable_name new_name






         The last 9 lines are read successfully...!

            my name is aniket

           [['init gets called when at the time object creation Automatically magic method\n', 'first argument reserved self\n', 'self points to current object holds object ref\n', 'u can define instance variables?  by using self keyword\n', 'u can use any alternate name instead of self BUT preferred self\n', 'instance  seperate copy for each object  \n', 'static variable class level variable \n', 'local instance access, declare, modify, delete instance variable\n', 'class method access, declare, modify, delete static variable\n', 'if instance var defined same name as static -- takes init variable\n', 'declare inside class and outside method\n', 'access inside class and outside method but after declaring\n', 'in init, by using self if instance var defined same name as static takes init variable\n', 'outside the class,  by using classname\n', 'in init, access the static variable by using classname classname.static_variable_name\n', 'in instance method, using self \n', 'in instance method, using classname classname.static_variable_name\n', 'outside the class, if we try to modify the static variable using object reference/reference variable\n', 'it wil create a new attribute for that object\n', ' inside the class, if we try to modify the static variable using self\n', 'it wil create a new attribute for that object\n', 'in init, we can modify the static variable using classname classname.static_variable_name new_name\n', 'in instance method, we can modify the static variable
using classname classname.static_variable_name new_name\n', '\t\n', '\t\n', '\t\n', '\t\n', '\t\n', '\t\n', '\tmy name is aniket\n']]

classname.static_variable_name

"""
