import time
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from anticaptchaofficial.recaptchav2proxyless import *
from webdriver_manager.chrome import ChromeDriverManager

print("Task 1: Đăng nhập vào TopCV")
# Mở trình duyệt, vào trang TopCV

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url = 'https://www.topcv.vn/login'
driver.get(url)

# Tìm kiếm box đăng nhập
email_field = driver.find_element(By.NAME, "email")
pass_field = driver.find_element(By.ID, "password")

# Nhập tên người dùng và mật khẩu
time.sleep(1)
email_field.send_keys('baox2official@gmail.com')
time.sleep(1)
pass_field.send_keys("BaoBao15072002")
time.sleep(2)

# Bấm nút đăng nhập
login_field = driver.find_element(By.XPATH, '//*[@id="form-login"]/div[4]/button')
login_field.click()

# Xử lý captcha

sitekey = driver.find_element(By.XPATH, '//*[@id="recaptcha-demo"]').get_attribute('outerHTML')
sitekey_clean = sitekey.split('" data-callback')[0].split('data-sitekey="')[1]
print(sitekey_clean)

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
anticaptcha_api_key = 'bb41b7f7b9b19435aef753137db38e00'
solver.set_key(anticaptcha_api_key)
solver.set_website_url(url)
solver.set_website_key(sitekey_clean)

g_response = solver.solve_and_return_solution()
if g_response!= 0:
    print("g_response"+g_response)
else:
    print("task finished with error "+solver.error_code)

time.sleep(20)

print("Task 2: Tìm kiếm nội dụng trên thanh search box")
search_box = driver.find_element(By.ID, "keyword") # #keyword
search_box.send_keys("Software Engineer")# input("Nhập nghề nghiệp, vị trí muốn tìm: "))
time.sleep(2)
search_box.send_keys(Keys.RETURN)