from flask import Flask, render_template
from noticia import Noticia

app = Flask(__name__)

lista_noticia = [
    Noticia(0, 'LEgal', '13/03/2022', 'Titulo', 'https://th.bing.com/th/id/OIP.gNXdeGhpX3WziyQa40V4YAHaEK?pid=ImgDet&rs=1'),
    Noticia(1, 'BlaBlaBla', '29/12/2013', 'Titulo_2', 'https://th.bing.com/th/id/OIP.gNXdeGhpX3WziyQa40V4YAHaEK?pid=ImgDet&rs=1'),
    Noticia(2, 'é foda...', '29/12/2005', 'Titulo_3', 'https://th.bing.com/th/id/OIP.gNXdeGhpX3WziyQa40V4YAHaEK?pid=ImgDet&rs=1')
]

@app.route("/")
def home():
    return render_template("index.html", noticias = lista_noticia)

@app.route("/produto")
def listar_noticia():
    return render_template("lista-noticia.html", noticias = lista_noticia)

@app.route("/produto/<id>")
def exibir_noticia(id):
    for noticia in lista_noticia:
        if int(noticia.get_id()) == int(id):
            return render_template('listadinho.html', noticia = lista_noticia[int(id)])        