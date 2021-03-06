import time

from flask import Flask, render_template, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

# 엑셀 사용을 위한 준비
from openpyxl import Workbook
write_wb = Workbook()
write_ws = write_wb.active

# selenium import
from selenium import webdriver

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():

    keyword = request.form['input1']
    page = request.form['input2']

    daum_list = []

    for i in range(1, int(page)+1):
        req = requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=" + keyword + "&p=" + str(i))
        soup = BeautifulSoup(req.text, 'html.parser')

        for i in soup.find_all("a", class_="f_link_b"):
            print(i.text)
            daum_list.append(i.text)

        for i in range(1, len(daum_list) + 1):
            write_ws.cell(i,1, daum_list[i-1])

        write_wb.save("static/result.xlsx")

    return render_template("result.html", daum_list = daum_list)

@app.route('/naver_shopping', methods=['POST'])
def naver_shopping():
    search = request.form['input3']

    search_list = []
    search_list_src = []

    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(3)
    driver.get("https://search.shopping.naver.com/search/all?query=" + search + "&cat_id=&frm=NVSHATC")
    
    # 스크롤 다운
    y = 1000
    for timer in range(0, 10):
        driver.execute_script("window.scrollTo(0, "+str(y) + ")")
        y = y + 1000
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for i in soup.select("#__next > div > div.style_container__1YjHN > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div"):
        search_list.append(i.find("a", class_="basicList_link__1MaTN").text)
        search_list_src.append(i.find("img")["src"])

    # 백화점/홈쇼핑 자동클릭되게 한 후 그 페이지 html 소스 가져오기.
    driver.find_element_by_css_selector("#__next > div > div.style_container__1YjHN > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > div.seller_filter_area > ul > li:nth-child(4) > a").click()

    # 스크롤 다운
    y = 1000
    for timer in range(0, 10):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y = y + 1000
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for i in soup.select("#__next > div > div.style_container__1YjHN > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div"):
        print(i.find("a", class_="basicList_link__1MaTN").text)
        search_list.append(i.find("a", class_="basicList_link__1MaTN").text)
        search_list_src.append(i.find("img")["src"])

    # 크롤링 후 페이지 닫기.
    driver.close()

    return render_template("shopping.html", search_list = search_list, search_list_src = search_list_src, len = len(search_list))

if __name__ == '__main__':
    app.run()