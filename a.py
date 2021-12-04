from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# 等待页面加载完成，找到某个条件发生后再继续执行后续代码，如果超过设置时间检测不到则抛出异常
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By                         # 支持的定位器分类
from selenium.webdriver.support import expected_conditions as EC    # 判断元素是否加载
from datetime import date, timedelta
import time, random, re, requests
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import  os


chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('–no-sandbox')
chrome_opt.add_argument('--start-maximized')       # 最大化
chrome_opt.add_argument('--incognito')             # 无痕隐身模式
chrome_opt.add_argument("disable-cache")           # 禁用缓存
chrome_opt.add_argument('log-level=3')
chrome_opt.add_argument('disable-infobars')
chrome_opt.add_argument('--disable-dev-shm-usage')
chrome_opt.add_argument('--disable-gpu')
chrome_opt.add_argument('headless')
# chrome_opt.binary_location = r'./chromedriver.exe'
file_executable_path = r'./chromedriver.exe'  # for Chrome
browser = webdriver.Chrome( executable_path='chromedriver',options=chrome_opt)
# 登陆网址
url = 'https://newids.seu.edu.cn/authserver/login?goto=http://my.seu.edu.cn/index.portal'
# 打卡网址
login_url = "http://ehall.seu.edu.cn/qljfwapp3/sys/lwWiseduElectronicPass/index.do?t_s=1614845255563&amp_sec_version_=1&gid_=Z0V0cEJOMFVKV3JOdWs0VUo0cTF5QzRsV0xxd1d1Ly9ZeEJJaDNVaXRpOXEvYkZuMFRNY25IaVVaZ21TVDIvZklBVmozclYrYjRuVzBJRmJRVisvdkE9PQ&EMAP_LANG=zh&THEME=indigo#/application"
#健康申报网址
url2 = "http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do?t_s=1615010644000&amp_sec_version_=1&gid_=QVJuUm9DYjMvMnNsYVVvMjg1YnNXZHNiSnBqZlhJTkFxV3U4R1lpMlVsWFpWc2hiRWs1c0drWnhTSGozYkNFeXlHR0E4STJTMjJwTmhPZlBIOUpoREE9PQ&EMAP_LANG=zh&THEME=indigo#/dailyReport"
def waitByXPath(browser, loc, timeout=15):
    try:
        WebDriverWait(browser, timeout, 0.5).until(EC.presence_of_element_located((By.XPATH, loc)))
    except:
        print('有异常')
        browser.refresh()
        waitByXPath(browser, loc)

def findByXpath(browser, loc,timeout=15):
    try:
        return WebDriverWait(browser, timeout, 0.5).until(EC.presence_of_element_located((By.XPATH, loc)))
    except:
        print('元素未找到')
        return findByXpath(browser,loc)

# 登陆信息门户
browser.get(url)
time.sleep(30)
waitByXPath(browser,'/html/body/div[1]/div[2]/div[3]/div/div[4]/div/form/p[5]/button')
if "PASSWORD" in os.environ:
        pwd = os.environ["PASSWORD"]
if "ID" in os.environ:
        id = os.environ["ID"]
input_username = browser.find_element_by_id("username")
input_password = browser.find_element_by_id("password")
input_username.send_keys(id)
input_password.send_keys(pwd)
time.sleep(30)
# 多个class 要用下面的形式 不能直接find_element_by_class
botton_login = browser.find_element_by_css_selector("[class='auth_login_btn primary full_width']")
botton_login.click()
waitByXPath(browser,'/html/body/div[2]/div[2]/table/tbody/tr/td/table/tbody/tr/td[2]/div[3]/div/div[2]/div[2]/ul/li[1]')
time.sleep(30)

# 开始健康打卡
###################################
#健康打卡
###################################
browser.get(url2)
waitByXPath(browser,'/html/body/main/article/section/div[2]/div[1]')
botton_add = findByXpath(browser,'/html/body/main/article/section/div[2]/div[1]')
botton_add.click()   #点击增加按钮
time.sleep(30)
#/html/body/div[11]/div/div[1]/section/div[2]/div/div[2]/div[2]/div[1]/div/label
waitByXPath(browser,'/html/body/div[10]/div/div[1]/section/div[2]/div/div[2]/div[2]/div[1]/div/label')
yikatonghao = findByXpath(browser,'/html/body/div[10]/div/div[1]/section/div[2]/div/div[2]/div[2]/div[1]/div/label')
ActionChains(browser).move_to_element(yikatonghao).click()
print('aaa')
time.sleep(30)
waitByXPath(browser,'/html/body/div[10]/div/div[1]/section/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/input')
input_temperature = findByXpath(browser,'//html/body/div[10]/div/div[1]/section/div[2]/div/div[4]/div[2]/div[1]/div[1]/div/input')
temperature = random.uniform(36.3,36.6)
temperature = round(temperature,1)
input_temperature.send_keys(str(temperature))
time.sleep(30)
div = browser.find_element_by_xpath('//*[@id="save"]')
# 滑动滚动条到某个指定的元素
js4 = "arguments[0].scrollIntoView();"
# 将下拉滑动条滑动到当前div区域
browser.execute_script(js4, div)
time.sleep(30)
waitByXPath(browser,'//*[@id="save"]')
botton_save = findByXpath(browser,'//*[@id="save"]')
botton_save.click()
time.sleep(30)
waitByXPath(browser,'/html/body/div[62]/div[1]/div[1]/div[2]/div[2]/a[1]')
botton_confirm = findByXpath(browser,'/html/body/div[62]/div[1]/div[1]/div[2]/div[2]/a[1]')
ActionChains(browser).move_to_element(botton_confirm).click()
botton_confirm.click()
time.sleep(30)

