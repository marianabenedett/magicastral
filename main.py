from flask import Flask, render_template

#flask recomenda esse app name
app = Flask(__name__)


#criar pagina no site
# route > mariana.com/usuarios
# funcao > o que vc quer exibir na pagina

#isso eh o que vai estar na home page (se chama um decorator)
@app.route("/")
def homepage():
    return render_template("homepage.html")

#criando uma outra pagina de contatos dentro do site
@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar
if __name__== "__main__":
    app.run(debug=True)