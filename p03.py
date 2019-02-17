'''
向数据库文件中插入数据
'''
import sqlite3
conn = sqlite3.connect("lin01.db")
# 游标对象，创建一个Cursor 对象并调用其execute()方法来执行SQL命令
c = conn.cursor()


# 使用execute()方法往刚刚创建的字段中写入数据

# c.execute('''insert into user values('002','lin', 20, ' ')''')

for user in [('003','lin3',11,' '),('004','ab4',21,' ')]:
    c.execute("insert into user values (?,?,?,?)",user)

# 保存（提交）更改
conn.commit()
# 如果完成连接，我们也可以关闭连接
conn.close()