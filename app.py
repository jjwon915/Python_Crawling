from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print(request.form['input1'])
    print(request.form['input2'])

    return render_template("result.html")

if __name__ == '__main__':
    app.run()