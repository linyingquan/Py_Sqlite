'''
查看数据库内容
'''
import sqlite3
conn = sqlite3.connect("lin01.db")
# 游标对象，创建一个Cursor 对象并调用其execute()方法来执行SQL命令
c = conn.cursor()

# 利用循环查看数据库中所有数据
# for row in c.execute('SELECT * FROM user ORDER BY name'):
#     print(row)

c.execute("select * from user")
i = c.fetchone() # 得到游标的第一个值
print(i)
i1 = c.fetchall() # 使用游标的fetch函数,fetchall得到所有的查询记录
print(i1)
