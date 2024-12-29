'''
import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="jiomart")
    smt=conn.cursor()
    while(True):
        pid=input("Enter Product ID:")
        pn=input("Enter Product Name:")
        pr=input("Enter Product Rate:")
        po=input("Enter Product Offer:")
        q=f"insert into products values({pid},'{pn}',{pr},{po})"
        smt.execute(q)
        conn.commit()
        print("Data Inserted Successfuly...")
        ch=input("Add More Data (yes/no)?")
        if(ch=='no'):break
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
    while(True):
        bn=input("Enter Bill No:")
        bd=input("Enter Bill Date:")
        cn=input("Enter Customer Name:")
        m=input("Enter Mobile No:")
        q=f"insert into bill values({bn},'{bd}','{cn}',{m})"
        smt.execute(q)
        conn.commit()
        print("Data Inserted Successfuly...")
        ch=input("Add More Data (yes/no)?")
        if(ch=='no'):break
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
    while(True):
        bn=input("Enter Bill No:")
        bd=input("Enter Bill Date:")
        cn=input("Enter Customer Name:")
        m=input("Enter Mobile No:")
        q=f"insert into bill values({bn},'{bd}','{cn}',{m})"
        smt.execute(q)
        conn.commit()
        print("Data Inserted Successfuly...")
        ch=input("Add More Data (yes/no)?")
        if(ch=='no'):break
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
    while(True):
        tid=input("Enter Transaction id:")
        bn=input("Enter Bill No:")
        pid=input("Enter Product id:")
        qty=input("Enter Sale Qty:")
        q=f"insert into sales values({tid},{bn},{pid},{qty})"
        smt.execute(q)
        conn.commit()
        print("Data Inserted Successfuly...")
        ch=input("Add More Data (yes/no)?")
        if(ch=='no'):break
    conn.close()

except sql.err.ProgrammingError as err:
    print(err)

except sql.err.OperationalError as err:
    print(err)

except sql.err.DatabaseError as err:
    print(err)

    

