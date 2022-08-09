import mysql.connector as connection

mydb = connection.connect(host = "localhost" , user = "root" , passwd  = "soumen123khatua")
print(mydb)
cursor=mydb.cursor()
#cursor.execute("create database if not exists soumen321")
#cursor.execute("show databases")
k = "create table if not exists soumen321.sudha_ineuron(employee_id int(11) ,emp_name varchar(66) , emp_mail_id varchar(77) , emp_salary int , emp_attendence int )"
q2 = cursor.execute(k)
print(q2)

cursor.execute("select * from soumen321.sudha_ineuron")
print(cursor.fetchall())