from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reclamacao(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(30), nullable = False)
    descricao = db.Column(db.String, nullable = False)

@app.route('/')
def index():
    reclamacoes = Reclamacao.query.all()
    return render_template('index.html', reclamacoes=reclamacoes)

@app.route('/create', methods = ['POST', 'GET'])
def create():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        new_reclamacao = Reclamacao(titulo = titulo, descricao = descricao)
        db.session.add(new_reclamacao)
        db.session.commit()
        return redirect('/')
    return render_template('create.html')

@app.route('/show/<int:id>')
def show(id):
    reclamacao = Reclamacao.query.get_or_404(id)
    return render_template('show.html', reclamacao=reclamacao)

@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    reclamacao = Reclamacao.query.get_or_404(id)
    if request.method == 'POST':
        reclamacao.titulo = request.form['titulo']
        reclamacao.descricao = request.form['descricao']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', reclamacao=reclamacao)

@app.route('/delete/<int:id>')
def delete(id):
    reclamacao = Reclamacao.query.get_or_404(id)
    db.session.delete(reclamacao)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():  
        db.create_all()

    app.run(debug=True, port=5153)