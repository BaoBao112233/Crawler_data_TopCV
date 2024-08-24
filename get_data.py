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

def login_web(url):
    print("Task 1: Đăng nhập vào TopCV")
    # Mở trình duyệt, vào trang TopCV

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    return driver

def find_search_box(driver, attribute_elm, name, key)
    print("Task 2: Tìm kiếm nội dụng trên thanh search box")
    search_box = driver.find_element(attribute_elm, name) # #keyword
    search_box.send_keys(key)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)

def get_data(url);
    response = requests.get(url)
    
    # Kiểm tra nếu yêu cầu thành công (HTTP status code 200)
    if response.status_code == 200:
        # Tạo đối tượng BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')  # hoặc 'html.parser'
        
        
    else:
        print(f"Yêu cầu không thành công` với mã trạng thái: {response.status_code}")


def save_data(driver, attribute_elm, name):
    print("Task 3: Mở url của các công ty cần tuyển dụng")

    try:
        # Tìm thẻ div cụ thể bằng class name (thay 'ten-class-cua-ban' bằng tên class bạn cần)
        div_element = driver.find_element(attribute_elm, name)
        
        # Tìm tất cả các thẻ <a> trong thẻ <div> đó
        anchor_tags = div_element.find_elements(By.TAG_NAME, "a")

        # Lọc các thẻ <a> có thuộc tính href
        anchor_tags_with_href = [a for a in anchor_tags if a.get_attribute("href")]

        print(f"Tìm thấy {len(anchor_tags_with_href)} thẻ <a> có thuộc tính href trong thẻ <div> có class 'job-list-search-result' đã chọn.")
        list_post = [tag_a.get_attribute('href') for idx, tag_a in enumerate(anchor_tags_with_href) if idx <= 10]
        # for index, post in enumerate(anchor_tags_with_href):
        #     print(f"Thẻ <a> {index + 1}: href='{post.get_attribute('href')}', text='{post.text}'")
        
        for post in list_post:
            response = requests.get(post)

            print(post)


    except Exception as e:
        print("Không tìm thấy thẻ div hoặc thẻ a phù hợp:", e)

def main():
    url = 'https://www.topcv.vn/viec-lam'
    driver = login_web(url)
    find_search_box(driver, By.ID, 'keyword', "Software Engineer")
    save_data(driver, By.CLASS_NAME, 'job-list-search-result')

# Tải nội dung trang web
# response = requests.get(url)

# # Kiểm tra nếu yêu cầu thành công (HTTP status code 200)
# if response.status_code == 200:
#     # Tạo đối tượng BeautifulSoup
#     soup = BeautifulSoup(response.content, 'lxml')  # hoặc 'html.parser'
    
#     # Tìm tất cả các thẻ <a>
#     all_a_tags = soup.find_all('a')
    
#     # In ra tất cả các thẻ <a> và các thuộc tính của chúng
#     for a_tag in all_a_tags:
#         print(f" - href: {a_tag.get('href')}")
# else:
#     print(f"Yêu cầu không thành công với mã trạng thái: {response.status_code}")


time.sleep(5)