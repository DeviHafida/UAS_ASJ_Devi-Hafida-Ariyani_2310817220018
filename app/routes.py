from flask import render_template, request, redirect, url_for
from app import app
from app.models import (
    init_db,
    get_all_cerita,
    add_cerita,
    delete_cerita,
    get_cerita_by_id,
    update_cerita
)

init_db()

@app.route('/')
def index():
    cerita = get_all_cerita()
    return render_template('index.html', cerita=cerita)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        judul = request.form['judul']
        penulis = request.form['penulis']
        genre = request.form['genre']
        link = request.form['link_wattpad']
        add_cerita(judul, penulis, genre, link)
        return redirect(url_for('index'))
    return render_template('tambah.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cerita = get_cerita_by_id(id)
    if not cerita:
        return "Cerita tidak ditemukan", 404

    if request.method == 'POST':
        judul = request.form['judul']
        penulis = request.form['penulis']
        genre = request.form['genre']
        link = request.form['link_wattpad']
        update_cerita(id, judul, penulis, genre, link)
        return redirect(url_for('index'))

    return render_template('edit.html', cerita=cerita)

@app.route('/hapus/<int:id>')
def hapus(id):
    delete_cerita(id)
    return redirect(url_for('index'))
