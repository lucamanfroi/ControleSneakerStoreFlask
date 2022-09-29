from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.estoque import Estoque
from datetime import datetime

bp = Blueprint('bp', __name__)

@bp.route('/')
@bp.route('/estoque')
def estoque():
    query = Estoque.query.all()
    return render_template('produtos.html', tenis=query)


@bp.route('/estoque/add', methods=['POST'])
def new_produto():
    nMarca = request.form['marca']
    nModelo = request.form['modelo']
    nCor = request.form['cor']
    nTamanho = request.form['tamanho']
    nData = datetime.strptime(request.form["data"], '%Y-%m-%d')
    nImg_link = request.form['img_link']

    tenis = Estoque(marca=nMarca, modelo=nModelo, cor=nCor,
                    tamanho=nTamanho, data=nData, img_link=nImg_link)
    db.session.add(tenis)
    db.session.commit()

    return redirect(url_for("bp.estoque"))


@bp.route('/estoque/update/<i_id>')
def update_produto(i_id=0):
    query = Estoque.query.filter_by(id=i_id).first()
    return render_template('tenis_update.html', i=query)


@bp.route('/estoque/upd', methods=["POST"])
def upd_estoque():

    id = request.form["id"]
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    cor = request.form["cor"]
    tamanho = request.form["tamanho"]
    data = datetime.strptime(request.form["data"], '%Y-%m-%d')
    img = request.form["img_link"]

    i = Estoque.query.filter_by(id=id).first()
    i.marca = marca
    i.modelo = modelo
    i.cor = cor
    i.tamanho = tamanho
    i.data = data
    i.img_link = img
    db.session.add(i)
    db.session.commit()

    return redirect(url_for("bp.estoque"))

@bp.route('/estoque/delete/<i_id>')
def delete_tenis(i_id=0):
    query = Estoque.query.filter_by(id=i_id).first()
    return render_template('tenis_delete.html', i=query)

@bp.route('/estoque/del', methods=["POST"])
def del_tenis():
    id = request.form["id"]
    i = Estoque.query.filter_by(id=id).first()
    db.session.delete(i)
    db.session.commit()

    return redirect(url_for("bp.estoque"))