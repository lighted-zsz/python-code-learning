import hashlib
import json
from time import time
from flask import Flask,render_template #render_template传送自己的网页操作

app = Flask(import_name="") #创建一个app
@app.route('/',methods=["get","post"])  #定义路由与根目录符号 请求方式
def function():
    return render_template("./conflux.html")
@app.route('/zsz/<in：zsz_id>') #定义一个整形int参数
def get_id():

if __name__ == '__main__':
    app.run()      #在服务器上运行程序
