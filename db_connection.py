from typing import Literal
import pymysql
import random


# Employee
####################################################################
TABLE_NAME = "employee"
class Common:
    def __str__(self):
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)

class Employee(Common):
    def __init__(self, eid, ename, esal):
        self.EmpID = eid
        self.EmpName = ename
        self.EmpSalary = esal


def generate_name():
    name = ""  # cjdw
    for i in range(0, random.randint(4, 9)):   # 0 4
        name += chr(64 + random.randint(1, 26))  # chr
    return name.title()


def generate_employee(num):
    list_of_emps = []
    for i in range(1, num+1):  # 1 2 3 4 
        emp_obj = Employee(eid=100+i, ename=generate_name(), esal=random.randint(12000, 85000))              
        list_of_emps.append(emp_obj)
    return list_of_emps
######################################################################


def get_db_connection():
    """returns database connection object"""
    try:
        conn_obj = pymysql.connect(user='root', password='root', host='localhost', database='test_python_db')
        return conn_obj
    except pymysql.err.OperationalError:
        return "Given database does not exist...!"

# result = get_db_connection()
# print(result)

def close_connection(obj):
    obj.close()

# close_connection(result)

def get_databases():
    result = get_db_connection()   # database connection built up
    # print(result)
    query = "show databases"  # query mention
    comm_channel = result.cursor()  # communication channel built up
    comm_channel.execute(query)  # hit query  # DQL -- select
    resultset = comm_channel.fetchall(5)   # fetchall, fetchone, fetchmany(no)
    # print(resultset)
    c = 1
    list_of_database = []
    for db in resultset:
        # print(c,"---", db[0])
        list_of_database.append(db[0])
        # c += 1
    return list_of_database

# print(get_databases())

CREATE_TABLE_QUERY = "create table {} (id int AUTO_INCREMENT, name varchar(50) NOT NULL, salary float, PRIMARY KEY(id))"


def create_table_in_db(table_name):
    conn_obj = get_db_connection()
    comm_channel = conn_obj.cursor()
    comm_channel.execute(CREATE_TABLE_QUERY.format(table_name))
    return f"table '{table_name}' created successfully...!"

# print(create_table_in_db(TABLE_NAME))
# assignment -- drop table -- create krne ke pehle drop wala function call, table if exists -- drop, create

INSERT_QUERY = "insert into {} (name, salary) values ('{}', {})"

def truncate_table(table_name):
    query = f"truncate table {table_name}"
    conn_obj = get_db_connection()
    comm_channel = conn_obj.cursor()
    comm_channel.execute(query)
    conn_obj.commit()
    print("table truncated..!")


# truncate_table(TABLE_NAME)


def data_into_db(table_name, emp_obj):  # emp_obj -- list
    conn_obj = get_db_connection()
    comm_channel = conn_obj.cursor()
    if type(emp_obj) == Employee:
        query = INSERT_QUERY.format(table_name, emp_obj.EmpName, emp_obj.EmpSalary)
        comm_channel.execute(query)
    elif type(emp_obj) == list:
        for emp in emp_obj:
            query = INSERT_QUERY.format(table_name, emp.EmpName, emp.EmpSalary)
            # print(query)
            comm_channel.execute(query)
    else:
        raise ValueError("Incorrecte data type passed...!")
    conn_obj.commit()
    close_connection(conn_obj)
    return "Data inserted successfully..!"

# e1 = Employee(1, "ABC", 25000)

# for i in range(10):
    # data_into_db(TABLE_NAME, e1)

# emp_list = generate_employee(50)

# print(data_into_db(TABLE_NAME,emp_list))