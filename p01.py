'''
数据库编程，利用python库sqlite3，建立数据库
'''
import sqlite3
# 连接对象，创建一个数据库对象，将数据存储在lin01.db文件中
conn = sqlite3.connect("lin01.db")
# 游标对象，创建一个Cursor 对象并调用其execute()方法来执行SQL命令
c = conn.cursor()
# 使用execute()方法创建一个表，并在表中加入两个字段，并且字段类型为text
c.execute('''CREATE TABLE stocks (date text, name text)'' ')
# 使用execute()方法往刚刚创建的字段中写入数据
c.execute("INSERT INTO stocks VALUES ('2019.2.17','啊啊啊')")
# 保存（提交）更改
conn.commit()
# 如果完成连接，我们也可以关闭连接。
conn.close()