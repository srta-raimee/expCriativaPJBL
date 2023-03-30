import flask as fk

render = fk.Blueprint("render", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@render.route("/")
def default_index():
    return fk.render_template("about.html")

@render.route("/home")
def ret_home():
     return fk.render_template("home.html")
  
@render.route("/pag_cadastro")
def pag_cad():
    return fk.render_template("cadastro.html")

@render.route("/pag_login")
def pag_log():
    return fk.render_template("login.html")

@render.route("/about")
def about():
    return fk.render_template("about.html")

@render.route("/list")
def listar():
    return fk.render_template("list.html")

@render.route("/project")
def projetar():
    return fk.render_template("project.html")