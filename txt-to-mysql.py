import pymysql

try:
       db_test = pymysql.connect(
       host='localhost',
       port=3306,
       user='root',
       password='Aa19973628358',
       db='db_2',
       charset='utf8'
        )
       cur_test = db_test.cursor()
except Exception as flase:
       print("failed")
else :
    print('连接成功')
    val = open('../爬虫练习/小说春物/第1章遇见，失去.txt','r',encoding='utf-8')
    cur_test.execute("insert into novel values(%s)",val)
    db_test.commit()
    cur_test.close()
    db_test.close()

