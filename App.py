import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="silsilah"
)
    
cursor = db.cursor() 
if db.is_connected():
    print("Berhasil terhubung ke database")
else:
    print("Gagal terhubung ke database")

def get_all():
    cursor = db.cursor() 
    sql = "SELECT * FROM `silsilah`"
    cursor.execute(sql)
    results = cursor.fetchall()
    myreturn = []

    for data in results:
        myreturn.append(data)
    return myreturn

def create_data(nama, jenis_kelamin, anak_dari):
    sql = "INSERT INTO `silsilah` (nama, jenis_kelamin, anak_dari) VALUE ('" + nama + "','" + jenis_kelamin + "','" + anak_dari + "');"
    cursor.execute(sql)
    db.commit()

def update_data(nama, jenis_kelamin, anak_dari):
    sql = "UPDATE `silsilah` SET jenis_kelamin = '" + jenis_kelamin + "', anak_dari = '" + anak_dari + "' WHERE nama = '" + nama + "';"
    cursor.execute(sql)
    db.commit()

def delete_data(nama):
    sql = "DELETE FROM `silsilah` WHERE nama = '" + nama + "';"
    cursor.execute(sql)
    db.commit()

def set_space(x):
    if x == 4:
        return "    |   "
    elif x == 5:
        return "   |   "
    elif x == 6:
        return "        |  "
    elif x == 8:
        return "      |  "


def menu():
    print("\n\n=== APLIKASI DATABASE PYTHON ===")
    print("1. Tampilkan Semua Keluarga")
    print("2. Tambahkan Data Keluarga")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    #clear screen
    os.system("clear")

    if menu == '1':
        print("Nama    | Jenis Kelamin |   Anak Dari")
        print("----------------------------------------")
        data = get_all()
        for dt in data:
           print(dt[0]+set_space(len(dt[0]))+dt[1]+set_space(len(dt[1])+2)+dt[2])
        kembal = input("Press anything to back : ")
    elif menu == '2':
        print("\n")
        nama   = input("Nama          : ")
        jenkel = input("Jenis Kelamin : ")
        anakdr = input("Anak Dari     : ")
        create_data(nama, jenkel, anakdr)
        print("\n")
    elif menu == '3':
        print("\nInputkan Nama yang akan Di Update")
        nama = input("Nama : ")
        print("\nInputkan Updatean")
        jenkel = input("Jenis Kelamin : ")
        anakdr = input("Anak Dari     : ")
        update_data(nama,jenkel,anakdr)
        print("\n")
    elif menu == '4':
        print("\n")
        nama = input("Nama yang akan dihapus : ")
        delete_data(nama)
        db.commit()
    elif menu == '0':
        os.system(exit())


while True:
    menu()



