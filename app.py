from flask import Flask, render_template, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

# 엑셀 사용을 위한 준비
from openpyxl import Workbook
write_wb = Workbook()
write_ws = write_wb.active

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

if __name__ == '__main__':
    app.run()