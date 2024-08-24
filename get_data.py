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

def get_data(url):
    if "javascript" in url:
        return
    
    # Gửi yêu cầu HTTP GET đến URL
    response = requests.get(url)

    # Kiểm tra nếu yêu cầu thành công
    if response.status_code == 200:
        # Tạo đối tượng BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm tất cả các thẻ div với class name cụ thể
        class_name = 'job-description__item'
        divs = soup.find_all('div', class_=class_name)

        # In ra nội dung của các thẻ div
        print("DIV 1")
        dicription = '\n'.join(child.text for child in divs[0].find_all())
        print("Dicription:", dicription)

        print("DIV 2")
        for child in divs[1].find_all():
            print(child.name, ":", child.text)

        print("DIV 3")
        for child in divs[2].find_all():
            print(child.name, ":", child.text)

        print("DIV 4")
        for child in divs[3].find_all():
            print(child.name, ":", child.text)

        print("DIV 5")
        for child in divs[4].find_all():
            print(child.name, ":", child.text)

    else:
        print(f"Không thể truy cập trang web. Mã trạng thái: {response.status_code}")

url = 'https://www.topcv.vn/viec-lam'

print("Task 1: Đăng nhập vào TopCV")
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)

print("Task 2: Tìm kiếm nội dụng trên thanh search box")
search_box = driver.find_element(By.ID, 'keyword') # #keyword
search_box.send_keys('Software Engineer')
time.sleep(2)
search_box.send_keys(Keys.RETURN)

print("Task 3: Mở url của các công ty cần tuyển dụng")
try:
    # Tìm thẻ div cụ thể bằng class name (thay 'job-list-search-result' bằng tên class bạn cần)
    div_element = driver.find_element(By.CLASS_NAME, 'job-list-search-result')
    
    # Tìm tất cả các thẻ <a> trong thẻ <div> đó
    anchor_tags = div_element.find_elements(By.TAG_NAME, "a")

    # Lọc các thẻ <a> có thuộc tính href
    anchor_tags_with_href = [a for a in anchor_tags if a.get_attribute("href")]

    print(f"Tìm thấy {len(anchor_tags_with_href)} thẻ <a> có thuộc tính href trong thẻ <div> có class 'job-list-search-result' đã chọn.")
    list_post = [tag_a.get_attribute('href') for tag_a in anchor_tags_with_href]
    # for index, post in enumerate(anchor_tags_with_href):
    #     print(f"Thẻ <a> {index + 1}: href='{post.get_attribute('href')}', text='{post.text}'")
    i = 0
    for post in list_post:
        if 'javascript' in post: continue
        if i >= 10: break
        get_data(post)
        i += 1
        break

except Exception as e:
    print("Không tìm thấy thẻ div hoặc thẻ a phù hợp:", e)


time.sleep(5)