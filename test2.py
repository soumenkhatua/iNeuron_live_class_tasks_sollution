import mysql.connector as conn


mydb = conn.connect(host ="localhost" , user = "root" , passwd = "soumen123khatua")
print(mydb)
cursor = mydb.cursor()
s = "insert into soumen321.sudha_ineuron values(100 , 'sudha' , 'sudh@mail ', 600000 ,300) "
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)

mydb.commit()
v = cursor.execute("select * from soumen321.sudha_ineuron")
for i in cursor.fetchall():
    print(i)