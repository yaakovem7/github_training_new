import pymysql

# Establishing a connection to DB
#conn = pymysql.connect(host='remotemysql.com', port=3306, user='root', passwd='123', db='SCHEMA_NAME')
conn = pymysql.connect(host='db4free.net', port=3306, user='yaakovem', passwd='QAZWSXedc12!', db='yaakovem_db')
# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM yaakovem_db.users;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()
