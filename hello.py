#hello.py


from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    print("visiting the homepage")
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    print("Visiting the about Page")
    return "About me"