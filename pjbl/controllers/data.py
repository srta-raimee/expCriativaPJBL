import flask as fk

data = fk.Blueprint("data", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@data.route("/")
def product_index():
    return fk.render_template("product_index.html") # aqui add todas as variaveis a serem renderizadas

# ainda precisamos decidir os dados a serem armazenados, mas por enquanto esses são os base
sensores = []
tempos = []

@data.route("/registrar", methods=["post"]) # vai ser chamado pelo botão no form html usando a chamaada action
def reg():
    nome_sensor = data.form.get('nome_sensor',None)
    tempo = data.form.get('tempo', None)
   
    global sensores, tempos
    sensores.append(nome_sensor)
    tempo.append(tempos)
   

    return fk.redirect(fk.url_for('render.listar')) # vai redirecionar para a função de renderização da página "listar"