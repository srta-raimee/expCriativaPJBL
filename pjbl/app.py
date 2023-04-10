import flask as fk
from controllers.render import render



app = fk.Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(render, url_prefix='/')


@app.route('/')
def index():
    return fk.render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)