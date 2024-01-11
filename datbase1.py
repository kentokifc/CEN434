import cx_Oracle
conStr='system/carefree@localhost:1521/xepdb1'
#create a connection object
conn=cx_Oracle.connect(conStr)
#get a cursor object from the connection
cur = conn.cursor()

#insert table rows
sqlTxt='insert into "CEN434".STUDENT_INFO (MATNO, NAME, PROGRAMME, ROOMNO, AGE)  values (:1, :2, :3, :4, :5)'
cur.execute(sqlTxt,('20CJ027471','OKARO KENECHUKWU','COMPUTER ENGINEERING', 'F002', '19'))

#insert multiple rows
dataTuples=[('17AB056745','OKO DANIEL','ENGLISH', 'G201', '18'),('20CJ438302','OKARO ERIC','MIS', 'A304', '19'),('20AA940872','DANIEL CHIDOZIE','ARCHITECTURE', 'C410', '20')]
sqlTxt='insert into "CEN434".STUDENT_INFO (MATNO, NAME, PROGRAMME, ROOMNO, AGE)  values (:1, :2, :3, :4, :5)'
cur.executemany(sqlTxt, dataTuples)

#update table rows
sqlTxt='update "CEN434".STUDENT_INFO set NAME=:1 where NAME=:2'
cur.execute(sqlTxt,("ADEJO MELISA","IREK FAVOUR"))
#cur.execute executes the statement 
#name1 replaces name2 in the table

#delete a record
#def delete_student(MATNO, ROOMNO):
#sqlTxt='delete from "CEN434".STUDENT_INFO where MATNO=:1'
#cur.execute(sqlTxt,("20CF940302"))


conn.commit()
# call the Connection.commit() method to apply the changes to the database. If you forget to call the Connection.commit() method, you will see that the change will not take effect.
cur.close()
#close the cursor object to avoid memory leaks
conn.close()
#close the connection  object also