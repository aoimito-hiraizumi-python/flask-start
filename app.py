from flask import Flask
from flask import render_template
from flask import request

# flaskが来たら別fileのHTMLのfileを開く

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def helloHiraizumi():
    return "Hi! Sekaiisan"


@app.route("/user/<name>")
# 動的に変わる変数 2つ以上入れても良い
def heyName(name):
    return name


@app.route("/user/<name>/<age>")
# 変数 2つ以上入れても良い
def heyAge(name, age):
    return name + age


# from flask import render_template
@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")

@app.route("/html/<name>")
def htmlName(name):
    return render_template("name.html", name=name)
    # htmlの後に動的なものを渡してあげる name1=name2 name1=htmlnのfileに渡す name2=変数に入れる

@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("age.html", htmlAge=age)

# from flask import request
@app.route("/query")
def query():
    search_text = request.args.get("search_text")
    if search_text is not None:
    # request.args.get -> serch_textでとってきたものを変数に入れる
        return search_text
    return ""
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
