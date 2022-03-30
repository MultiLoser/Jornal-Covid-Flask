from flask import Flask, render_template
from noticia import Noticia

app = Flask(__name__)

lista_noticia = [
    Noticia(0, 'LEgal', '13/03/2022', 'Titulo', 'https://th.bing.com/th/id/OIP.gNXdeGhpX3WziyQa40V4YAHaEK?pid=ImgDet&rs=1'),
    Noticia(1, 'BlaBlaBla', '29/12/2013', 'Titulo_2', 'https://th.bing.com/th/id/OIP.gNXdeGhpX3WziyQa40V4YAHaEK?pid=ImgDet&rs=1'),
    Noticia(2, 'é foda...', '29/12/2005', 'Titulo_3', 'https://th.bing.com/th/id/OIP.gNXdeGhpX3WziyQa40V4YAHaEK?pid=ImgDet&rs=1')
]

lista_estados_bandeiras = [
    Estado(0, 'Acre', 'AC', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Acre-300x210.png'),
    Estado(1, 'Alagoas', 'AL', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Alagoas-300x200.png'),
    Estado(2, 'Amapá', 'AP', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amapa-300x210.png' ),
    Estado(3, 'Amazonas', 'AM', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amazonas-300x214.png' ),
    Estado(4, 'Bahia', 'BA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Bahia-300x200.png'),
    Estado(5, 'Ceará', 'CE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Ceara-300x210.png'),
    Estado(6, 'Distrito Federal', 'DF', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Distrito_Federal_Brasil-300x210.png'),
    Estado(7, 'Espírito Santo', 'ES', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Espirito_Santo-300x210.png'),
    Estado(8, 'Goiás', 'GO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Goias-300x210.png'),
    Estado(9, 'Maranhão', 'MA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Maranhao-300x200.png'),
    Estado(10, 'Mato Grosso', 'MT', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso-300x210.png'),
    Estado(11, 'Grosso do Sul', 'MS', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso_do_Sul-300x210.png'),
    Estado(12, 'Minas Gerais', 'MG','https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Minas_Gerais-300x210.png'),
    Estado(13, 'Pará', 'PA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Para-300x200.png'),
    Estado(14, 'Paraíba', 'PB', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Paraiba-300x210.png'),
    Estado(15, 'Paraná', 'PR', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Parana-300x210.png'),
    Estado(16, 'Pernambuco', 'PE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Pernambuco-300x210.png'),
    Estado(17, 'Piauí', 'PI', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Piaui-300x200.png'),
    Estado(18, 'Rio de Janeiro', 'RJ', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Rio_de_Janeiro-300x210.png'),
    Estado(19, 'Rio Grande do Norte', 'RN', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Norte-300x200.png'),
    Estado(20, 'Rio Grande do Sul', 'RS', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Sul-300x210.png'),
    Estado(21, 'Rondônia', 'RO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Rondonia-300x210.png'),
    Estado(22, 'Roraima', 'RR', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Roraima-300x200.png'),
    Estado(23, 'Santa Catarina', 'SC', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Santa_Catarina-300x218.png'),
    Estado(24, 'São Paulo', 'SP', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Sao_Paulo-300x200.png'),
    Estado(25, 'Sergipe', 'SE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Sergipe-300x210.png'),
    Estado(26, 'Tocantins', 'TO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Tocantins-300x210.png')]

@app.route("/")
def home():
    return render_template("index.html", noticias = lista_noticia, bandeiras = lista_estados_bandeiras)

@app.route("/produto")
def listar_noticia():
    return render_template("lista-noticia.html", noticias = lista_noticia)

@app.route("/produto/<id>")
def exibir_noticia(id):
    for noticia in lista_noticia:
        if int(noticia.get_id()) == int(id):
            return render_template('listadinho.html', noticia = lista_noticia[int(id)])        