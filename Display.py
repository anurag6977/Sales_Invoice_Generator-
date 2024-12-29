import pymysql as sql
try:
    conn=sql.connect(host="localhost",user="root",password="1234",port=3306,database="jiomart",cursorclass=sql.cursors.DictCursor)
    smt=conn.cursor()
    bn=int(input("Enter Bill No:"))
    q=f'''select b.billno,b.billdate,b.customername,b.mobileno,p.productname,s.qty,s.transid,p.productrate,p.productoffer,(s.qty * p.productrate) AS amount,(s.qty * p.productoffer) AS offeramount
    from sale s join bill b ON s.billno = b.billno join products p ON s.productid = p.productid
    where b.billno = {bn}
    '''
    smt.execute(q)
    rows=smt.fetchall()
    if(rows):
        total=sum(row['amount'] for row in rows)
        offer=sum(row['offeramount'] for row in rows)
        save=total-offer
        
        print("-"*90)
        print("                                          Invoice")
        print("-"*90)
        for row in rows:
            r=1
        print("Tid :",row['transid'],"                                                              Bill No. :",row['billno'])
        print("Date :",row['billdate'])
        print("Customer Name:",row['customername'])
        print("Mobile No. :",row['mobileno'])
        print("-"*90)
        print('S.no\t\tProduct\t\tQuantity\tRate\t\tOffer Rate\tAmount')
        print("-"*90)
        s=1
        for row in rows:
            print(s,row['productname'],row['qty'],row['productrate'],row['productoffer'],row['offeramount'],sep='\t\t')
            s=s+1
        print("-"*90)
        print('                                                                        '"Total :",offer)
        print('                                                                        '"Save  :",save)
    else:
        print("Record Not Found...")

    conn.close()

except sql.err.ProgrammingError as err:
    print(err)

except sql.err.OperationalError as err:
    print(err)

            

