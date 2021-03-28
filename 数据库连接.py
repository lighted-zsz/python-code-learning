#导入pymysql模块
import pymysql

try:
    db = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user= 'root',
        password = 'Aa19973628358',
        db='db_2',
        charset = 'utf8'
    )
    #创建游标
    cur = db.cursor()
except Exception as e:
    print('连接失败')
else:
    print('连接成功:{}'.format(cur))