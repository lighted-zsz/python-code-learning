import time
from selenium import webdriver
import random

def stop(number):
    time.sleep(number)

def rands():
    b = '{:.1f}'.format(random.uniform(35.4, 36.6))
    return b

def write_tem(num,passage):
    print("正在自动填写体温")
    driver = webdriver.Chrome()
    login_url="https://webvpn.sues.edu.cn"
    driver.get(login_url)

    stop(4)
    driver.find_element_by_id("username").click()
    driver.find_element_by_id("username").send_keys(num)

    stop(1)
    driver.find_element_by_id("password").click()
    driver.find_element_by_id("password").send_keys(passage)

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
    print("体温填写完毕")

write_tem('021318131','123456lL')
