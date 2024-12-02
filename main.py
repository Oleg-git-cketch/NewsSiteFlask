from flask import Flask, render_template, request

app = Flask(__name__)
news = {}

@app.route("/")
def home():
    return render_template("index.html", news=news)

@app.route("/add-news", methods=["POST"])
def add_news():
    title = request.form.get("title")
    content = request.form.get("content")
    news[title] = content
    return render_template("index.html", news=news)

app.run()
