from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from bs4 import BeautifulSoup
import json
import requests
from threading import Thread


def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    books = soup.find("ul", class_="bang_list").find_all("li")
    # books = soup.select("div.bang_list.clearfix.bang_list_mode")
    print(books)
    for item in books:
        book = {
            'rank': item.find('div', class_="list_num").get_text().strip(),
            'name': item.find('div', class_='name').get_text().strip(),
            'author': item.find('div', class_='publisher_info').find('a').get_text(),
            'recommend': item.find('div', class_='star').find('span', class_='tuijian').get_text().strip(),
            'comment': item.find('div', class_='star').find('a').get_text().strip(),
            'press': item.find('div', class_='publisher_info').find('a').get_text().strip(),
            'releasedate': item.find('div', class_='publisher_info').find('span').get_text(),
            'price': item.find('div', class_='price').find('span', class_='price_n').get_text().strip(),
            'image': item.find('div', class_='pic').find('img').get('src')
        }
        print(book)


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-{}'.format(page)
        browser.get(url)
        if page > 1:
            inputbox = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input#t_cp')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.button')))
            inputbox.clear()
            inputbox.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.current'), str(page)))
        parse_page(browser.page_source)
    except Exception as e:
        print(e)


def main():
    for i in range(1, 4):
        index_page(i)


# main()
url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-1'
browser.get(url)
parse_page(browser.page_source)