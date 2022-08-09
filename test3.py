import mysql.connector as conn


mydb = conn.connect(host ="localhost" , user = "root" , passwd = "soumen123khatua")
print(mydb)
cursor = mydb.cursor()
cursor.execute("select employee_id , emp_salary from soumya123.sudha_ineuron")
l = []
for i in cursor.fetchall():
    l.append(i)

print(l)
print(type(l[0]))
