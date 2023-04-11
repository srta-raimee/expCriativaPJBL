import flask as fk

render = fk.Blueprint("render", __name__, template_folder="./views/", static_folder='./static/', root_path="./")


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

# @render.route("/login")
# def login():
#     global nomes, emails, senhas, cpfs
#     if nomes[i] == 

@render.route("/sensores")
def sens():
    return fk.render_template("sensores.html")

@render.route("/about")
def about():
    return fk.render_template("about.html")

@render.route("/list", methods = ["get"])
def listar():
    global sensores, tempos, qtd, tempoTrav
    return fk.render_template("list.html", sensores=sensores, tempos=tempos, qtd=qtd, tempoTrav=tempoTrav ) # declarando todas as listas que podem ser usadas posteriormente

@render.route("/list_users", methods = ["get"])
def listar_users():
     global nomes, emails, senhas, cpfs
     return fk.render_template("list_users.html", nomes=nomes, emails=emails, senhas=senhas, cpfs=cpfs) 

@render.route("/project")
def projetar():
    return fk.render_template("project.html")


# rotas post

sensores = []
tempos = []
qtd = []
tempoTrav = []

nomes = []
emails = []
senhas = []
cpfs = []


@render.route("/registrar_sensor", methods=["get", "post"]) # vai ser chamado pelo botão no form html usando a chamaada action
def reg_sens():
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

@render.route("/registrar_user", methods=["get", "post"]) # vai ser chamado pelo botão no form html usando a chamaada action
def reg_user():
    nome = fk.request.form.get('nome',None)
    email = fk.request.form.get('email', None)
    senha = fk.request.form.get('senha', None)
    cpf = fk.request.form.get('cpf', None)

    global nomes, emails, senhas, cpfs
    nomes.append(nome)
    emails.append(email)
    senhas.append(senha)
    cpfs.append(cpf)
    print(nomes)
    
    return fk.redirect(fk.url_for('render.pag_log')) 