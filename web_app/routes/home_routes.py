# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return render_template("prediction_form.html")

    return f"Hello World! {x}"

@home_routes.route("/")
def index():
    print("Visiting the homepage")
    x = 2 + 2

    return f"Hello World! {x}"


@home_routes.route("/about")
def about():
    print("Visiting the about page")
    return "About me"