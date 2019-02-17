'''
删除数据库的数据
'''
import sqlite3
conn = sqlite3.connect("lin01.db")
# 游标对象，创建一个Cursor 对象并调用其execute()方法来执行SQL命令
c = conn.cursor()

# 将id为'001'的数据删除
c.execute("delete from user where id = '003'")

# 保存（提交）更改
conn.commit()
# 如果完成连接，我们也可以关闭连接
conn.close()