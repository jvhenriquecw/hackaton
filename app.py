from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'
db = SQLAlchemy(app)

class Reclamacao(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(30), nullable = False)
    descricao = db.Column(db.String, nullable = False)

@app.route('/')
def ola():
    reclamacoes = Reclamacao.query.all()
    return render_template('index.html', reclamacoes=reclamacoes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)