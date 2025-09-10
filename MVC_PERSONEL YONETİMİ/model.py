import sqlite3 
from datetime import datetime

def db_connection():
    conn=sqlite3.connect('personel_veritabanı.db')
    return conn
def create_table():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personeller(
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            isim TEXT NOT NULL,
            giris_saati TEXT,
            cikis_saati TEXT,
            izin BOOLEAN DEFAULT 0,
            gunluk_maas REAL NOT NULL                                              
        )                            
    ''')
    conn.commit()
    conn.close()
def get_all_personeller():
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM personeller ")
    personeller=cursor.fetchall()
    conn.close()
    return personeller
def add_personel(isim, gunluk_maas):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('INSERT INTO personeller (isim, gunluk_maas) VALUES(?,?)',(isim, gunluk_maas))
    conn.commit()
    conn.close()

def update_personel(id, isim, giris_saati, cikis_saati, izin):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('UPDATE personeller SET isim= ?, giris_saati= ?, cikis_saati= ?, izin=? WHERE id=?',(isim, giris_saati, cikis_saati,izin,id))
    conn.commit()
    conn.close()

def delete_personel(id):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('DELETE FROM personeller WHERE id=?',(id,))
    conn.commit()
    conn.close
    
def calculate_maas(id):
    conn=db_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT gunluk_maas, giris_saati, cikis_saati FROM personeller WHERE id=?',(id,))
    result=cursor.fetchone()
    
    conn.close
    
    if result:
        gunluk_maas, giris_saati, cikis_saati = result
        if giris_saati and cikis_saati:
            giris_saati = datetime.fromisoformat(giris_saati)
            cikis_saati = datetime.fromisoformat(cikis_saati)
            calisma_suresi = (cikis_saati-giris_saati).total_seconds() /3600
            maas=(calisma_suresi / 8)* gunluk_maas
            return maas
    return 0      

