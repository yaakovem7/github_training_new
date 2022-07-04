import pymysql

# Establishing a connection to DB
#conn = pymysql.connect(host='remotemysql.com', port=3306, user='root', passwd='123', db='SCHEMA_NAME')

# Establishing a connection to DB
conn = pymysql.connect(host='db4free.net', port=3306, user='yaakovem', passwd='QAZWSXedc12!', db='yaakovem_db')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into yaakovem_db.users (name, id) VALUES ('yaakov', 5)")

cursor.close()
conn.close()