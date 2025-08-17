from flask import Blueprint, render_template

receipt_detect = Blueprint(
    "receipt_detect", __name__, template_folder="templates", static_folder="static"
)


@receipt_detect.route("/")
def index():
    return render_template("receipt_detect/index.html")
