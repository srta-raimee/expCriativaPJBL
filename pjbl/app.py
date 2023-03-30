import flask as fk
from controllers.render import render
# from controllers.data import data


app = fk.Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(render, url_prefix='/render')
# app.register_blueprint(data, url_prefix='/data')

@app.route('/')
def index():
    return fk.render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)