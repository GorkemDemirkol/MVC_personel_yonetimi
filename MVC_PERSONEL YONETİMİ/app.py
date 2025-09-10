from flask import Flask, render_template, request, redirect, url_for
from model import create_table, add_personel, get_all_personeller, update_personel, delete_personel, calculate_maas

app= Flask(__name__)

@app.route('/')
def index():
    personeller = get_all_personeller()
    return render_template('index.html', personeller=personeller)

@app.route('/add' , methods= ['GET', 'POST'])
def add():
    if request.method== 'POST':
        isim= request.form['isim']
        gunluk_maas=float(request.form['gunluk_maas'])
        add_personel(isim,gunluk_maas)
        return redirect(url_for('index'))
    return render_template('add_personel.html')

@app.route('/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    if request.method=='POST':
        isim=request.form['isim']
        giris_saati=request.form['giris_saati']
        cikis_saati=request.form['cikis_saati']
        izin=request.form.get('izin')=='on'
        update_personel(id, isim, giris_saati, cikis_saati, izin)
        return redirect(url_for('index'))
    personeller= get_all_personeller()
    personel=next((p for p in personeller if p[0]==id),None)
    return render_template('edit_personel.html', personel=personel)
@app.route('/delete/<int:id>')
def delete(id):
    delete_personel(id)
    return redirect(url_for('index'))
@app.route('/maas/<int:id>')
def maas(id):
    maas=calculate_maas(id)
    return f"maaş:{maas:.2f} "

if __name__=='__main__':
    create_table()
    app.run(debug=True)