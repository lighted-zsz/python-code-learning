import time
from selenium import webdriver
import random
from multiprocessing import Pool

people = []
classnums = ['021318117','021318118','021318119','021318131','021318132','021318113','021318120','021318130','021318129']
passages = ['Aa19973628358','Xq242313','LuangLuang21','123456lL','Hh1234','Guanxinxin@1011','Wan575100','864204318Lyx','Wxz19990925']
for i in range(0,len(classnums),1):
    classnum = classnums[i]
    passage = passages[i]
    get_dict = {
        'classnum': classnum,
        'passage': passage
    }
    people.append(get_dict)

def stop(number):
    time.sleep(number)

def rands():
    b = '{:.1f}'.format(random.uniform(35.4, 36.6))
    return b

def write_tem(get_dict):
    print(get_dict['classnum']+"正在自动填写体温")
    driver = webdriver.Chrome()
    login_url="https://webvpn.sues.edu.cn"
    driver.get(login_url)

    stop(4)
    driver.find_element_by_id("username").click()
    driver.find_element_by_id("username").send_keys(get_dict['classnum'])

    stop(1)
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").send_keys(get_dict['passage'])

    stop(1)
    driver.find_element_by_class_name("login_btn").click()

    write_url="https://webvpn.sues.edu.cn/webvpn/LjIwNC4yMTUuMjE2LjIwOS4xNzA=/LjIxOS4yMTAuMjE0LjIwNC4xNTcuMTYzLjIwOC4xNzAuMTQ4LjE2Ny4yMTQuMTUxLjE2Ny45NS4xNTEuMTQ5LjE3NC4xMDMuMTUxLjE2NA==/default/work/shgcd/jkxxcj/jkxxcj.jsp"
    driver.get(write_url)

    stop(2)
    driver.find_element_by_xpath("//div[@class='input-group']/input").click()

    stop(2)
    driver.find_element_by_xpath("//div[@class='input-group']/input").clear()

    stop(2)
    driver.find_element_by_xpath("//div[@class='input-group']/input").send_keys(rands())

    stop(2)
    driver.find_element_by_xpath("//div[@class='form-item text-center form-actions']/button[@class='btn btn-primary obtn']").click()

    stop(2)
    driver.close()
    print(get_dict['classnum']+"体温填写完毕")

if __name__ == '__main__':
    pool = Pool(processes=2)
    pool.map(write_tem, people)
    pool.close()
    pool.join()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  