'''
数据库编程，利用python库sqlite3，建立数据库
'''
import sqlite3
# 连接对象，创建一个数据库对象，将数据存储在lin01.db文件中
conn = sqlite3.connect("lin01.db")
# 游标对象，创建一个Cursor 对象并调用其execute()方法来执行SQL命令
c = conn.cursor()
# 使用execute()方法创建一个表，表中有id(主键),名字(唯一),年龄,备注(默认为空)
# c.execute('''CREATE TABLE user ('id integer primary key', 'name varchar(20) UNIQUE','age integer','comment text NULL')''')
c.execute('''CREATE TABLE user (id text, name varchar(20) UNIQUE, age integer, comment text NULL)''')

# # 使用execute()方法往刚刚创建的字段中写入数据
# c.execute("INSERT INTO user VALUES ('001', 'lin', 19, '帅')")

# 保存（提交）更改
conn.commit()
# 如果完成连接，我们也可以关闭连接
conn.close()
