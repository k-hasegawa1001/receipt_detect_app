from flask import Flask

app = Flask(__name__)


from apps.receipt_detect import views as receipt_detect_views

app.register_blueprint(
    receipt_detect_views.receipt_detect, url_prefix="/receipt_detect"
)


@app.route("/")
def index():
    print("test")
    return "test"
