from flask import Blueprint, render_template

default_pages = Blueprint("default_page", __name__)


@default_pages.route("/")
def index():
    return render_template("index.html")


@default_pages.route("/greet")
def greet():
    return "Hello, Dan!"


@default_pages.route("/about")
def about():
    return render_template("about.html")
