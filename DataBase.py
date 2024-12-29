import pymysql as sql
try:
    conn=sql.Connect(host="localhost",user="root",password="1234",port=3306)
    smt=conn.cursor()
    db=input("Enter DataBase Name:")
    q=f"create schema {db}"
    smt.execute(q)
    print("Database Created Successfuly....")
    conn.close()

except sql.err.ProgrammingError as err:
    print(err)

except sql.err.OperationalError as err:
    print(err)

except sql.err.DatabaseError as sql:
    print(sql)




