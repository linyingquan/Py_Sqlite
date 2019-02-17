'''
修改数据库的数据
'''
import sqlite3
conn = sqlite3.connect("lin01.db")
# 游标对象，创建一个Cursor 对象并调用其execute()方法来执行SQL命令
c = conn.cursor()

# 把id为'004'的数据的name改为'xxx'
c.execute("update user set name='lin2' where id = '004'")

conn.commit()
conn.close()