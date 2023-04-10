import flask as fk

render = fk.Blueprint("render", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

# aqui estão todas as funções de renderização de páginas (somente e apenas), para fins de organização

sensores = []
tempos = []
qtd = []
tempoTrav = []

print(sensores)

@render.route("/")
def default_index():
    return fk.render_template("home.html")

@render.route("/home")
def ret_home():
     return fk.render_template("home.html")
  
@render.route("/pag_cadastro_sensor")
def pag_cad_sens():
    return fk.render_template("cadastro_sensor.html")

@render.route("/pag_cadastro_user")
def pag_cad_user():
    return fk.render_template("cadastro_user.html")

@render.route("/pag_login")
def pag_log():
    return fk.render_template("login.html")

@render.route("/sensores")
def sens():
    return fk.render_template("sensores.html")

@render.route("/about")
def about():
    return fk.render_template("about.html")

@render.route("/list", methods = ["get"])
def listar():
    global sensores, tempos, qtd, tempoTrav
    return fk.render_template("list.html", sensores=sensores, tempos=tempos, qtd=qtd, tempoTrav=tempoTrav )

@render.route("/project")
def projetar():
    return fk.render_template("project.html")


# rotas post

@render.route("/registrar", methods=["get", "post"]) # vai ser chamado pelo botão no form html usando a chamaada action
def reg():
    nomeSensor = fk.request.form.get('nomeSensor',None)
    tempoLigado = fk.request.form.get('tempoLigado', None)
    qtdFaixa = fk.request.form.get('qtdFaixa', None)
    tempoTravessia = fk.request.form.get('tempoTravessia', None)

    global sensores, tempos, qtd, tempoTrav
    sensores.append(nomeSensor)
    tempos.append(tempoLigado)
    qtd.append(qtdFaixa)
    tempoTrav.append(tempoTravessia)

    
    return fk.redirect(fk.url_for('render.listar')) # vai redirecionar para a função de renderização da página "listar"

