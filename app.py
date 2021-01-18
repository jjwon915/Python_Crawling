from flask import Flask, render_template, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():

    keyword = request.form['input1']
    page = request.form['input2']

    req = requests.get("https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=" + keyword)
    soup = BeautifulSoup(req.text, 'html.parser')

    for i in soup.find_all("a", class_="f_link_b"):
        print(i.text)

    return render_template("result.html")

if __name__ == '__main__':
    app.run()