'''from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hnhpomgm:CLuRF-zUmYxUcKBds49UAb8pUkP552Kl@balarama.db.elephantsql.com/hnhpomgm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route('/')
def hello():
    return 'Hello, World!'


'''


from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://hnhpomgm:CLuRF-zUmYxUcKBds49UAb8pUkP552Kl@balarama.db.elephantsql.com/hnhpomgm"

#app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:postgres@localhost:5432/gqlapp_flask"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



from flask import render_template


@app.route('/')
def hello():
    titulo = "Hola Mundo"
    mensaje = "Esto es una prueba"


    lista_personas = [
        {
            "nombre": "Juan",
            "apellido": "Perez",
            "edad": 25
        }
        ,
        {
            "nombre": "Maria",
            "apellido": "Gonzalez",
            "edad": 30
        }
    ]
    
    data = {
        "titulo": titulo,
        "mensaje": mensaje,
        "lista_personas": lista_personas
    }

    return render_template('index.html', **data)

""""
@app.route('/api/v1/posts', methods=['GET'])
def get_posts():
    try :
        posts = db.session.query(Post).all()
        return jsonify(posts=[post.to_dict() for post in posts])
    except Exception as e:
        return jsonify(error=str(e)), 500
"""


