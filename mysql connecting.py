'''
#creating a database

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="thennarasu@0712")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("create database stud")
mydb.commit()
mydb.close()


#creating a table#


import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="thennarasu@0712",database="stud")
print("connected")

mycursor=mydb.cursor()
mycursor.execute("create table details"+"(stu_name varchar(20),stu_reg int primary key,stu_dep varchar(20) not null)")
mydb.commit()
print("table created")
mydb.close()


#insert the value

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="thennarasu@0712",database="stud")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("insert into details values('aaa',1001,'cse'),('bbb',1002,'ece')")
mydb.commit()
print(mycursor.rowcount,"rows inserted")
mydb.close()
'''

# select all records #

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="thennarasu@0712",database="stud")
print("connected")
mycursor=mydb.cursor()
mycursor.execute("select *from details")
myresult=mycursor.fetchall()
print(type(myresult))
print(myresult)
print("NAME\tREGNO\tDEPARTMENT")
print("-----------------------")
for i in myresult:
    print(i[0],"\t",i[1],"\t",i[2])
mydb.close()



