from flask import Flask, render_template
import requests
import Task

app = Flask(__name__)

url="http://127.0.0.1:8090/_/#/collections?collectionId=owxx8kl3jswgq6j"

response = requests.get()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
