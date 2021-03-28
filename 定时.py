import time
while True:
  time_now = time.strftime("%H:%M:%S", time.localtime()) # 刷新
  if time_now == "13:56:10" or time_now == "7:53:10": #此处设置每天定时的时间、
      import time
      from selenium import webdriver
      login_url = "https://cas.sues.edu.cn/cas/login?service=https%3A%2F%2Fworkflow.sues.edu.cn%2Fdefault%2Fwork%2Fshgcd%2Fjkxxcj%2Fjkxxcj.jsp"
      write_url = "https://workflow.sues.edu.cn/default/work/shgcd/jkxxcj/jkxxcj.jsp"
      driver = webdriver.Chrome()
      driver.get(login_url)
      time.sleep(2)
      driver.find_element_by_id("username").click()
      driver.find_element_by_id("username").send_keys('021318117')
      time.sleep(2)
      driver.find_element_by_id("password").click()
      driver.find_element_by_id("password").send_keys('Aa19973628358')
      time.sleep(2)
      driver.find_element_by_class_name("login_btn").click()
      time.sleep(2)
      driver.get(write_url)
      time.sleep(2)

      # <div class="input-group">
      # <input name="tw" maxlength="4" type="text" class="form-control" value="" placeholder="范围35.0-45.0">
      # <span class="input-group-addon">℃</span></div>
      driver.find_element_by_xpath("//div[@class='input-group']/input").click()
      time.sleep(2)
      driver.find_element_by_xpath("//div[@class='input-group']/input").clear()
      time.sleep(2)
      driver.find_element_by_xpath("//div[@class='input-group']/input").send_keys('36.3')
      time.sleep(2)
      driver.find_element_by_xpath(
          "//div[@class='form-item text-center form-actions']/button[@class='btn btn-primary obtn']").click()
      # <div class="form-item text-center form-actions" name="btns">
      # 							<button class="btn btn-primary obtn" id="post">提交</button>
      # 							<button class="btn btn-default obtn" id="cancel">关闭</button>
      # 						</div>


