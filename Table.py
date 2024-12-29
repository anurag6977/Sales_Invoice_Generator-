'''
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="jiomart")
    smt=conn.cursor()
    smt.execute("create table products(productid int primary key,productname varchar(60),productrate decimal,productoffer decimal)")
    print("Table Created Successfuly...")
    conn.close()

except sql.err.ProgrammingError as err:
    print(err)

except sql.err.OperationalError as err:
    print(err)

except sql.err.DatabaseError as err:
    print(err)
'''
'''
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="jiomart")
    smt=conn.cursor()
    smt.execute("create table bill(billno int primary key,billdate int,customername varchar(60),mobileno int)")
    print("Table Created Successfuly")
    conn.close()

except sql.err.ProgrammingError as err:
    print(err)

except sql.err.OperationalError as err:
    print(err)

except sql.err.DatabaseError as err:
    print(err)
'''

import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="jiomart")
    smt=conn.cursor()
    smt.execute("create table sales(transid int primary key,billno int,productid int,qty int)")
    print("Table Created Successfuly")
    conn.close()

except sql.err.ProgrammingError as err:
    print(err)

except sql.err.OperationalError as err:
    print(err)

except sql.err.DatabaseError as err:
    print(err)

