import os

# VARIABEL GLOBAL
utama = ("yok", 24)
admin = {
        "admin 1" : ["Attar", "046"],
        "admin 2" : ["Admin", "123"]
    }
pemilik = {}

# DEF UTAMA UNTUK BISA MASUK KE HALAMAN ADMIN
def utama1():
    utama2 = True
    while utama2:
        try:
            print("=====AKSES MASUK=====")
            username = input("masukkan username : ")
            sandi    = int(input("masukkan sandi : "))

            if utama[0] == username and utama[1] == sandi:
                print("oke kamu berhasil masuk")
                os.system("cls || clear")
                utama2 = False

            elif utama[0] != username and utama[1] == sandi:
                os.system("cls || clear")
                print("USERNAME SALAH")
            
            elif utama[0] == username and utama[1] != sandi:
                os.system("cls || clear")
                print("SANDI SALAH")
            
            else:
                os.system("cls || clear")
                print("USERNAME DAN SANDI SALAH")
        
        except ValueError:
            os.system("cls || clear")
            print("|=SANDI HANYA ANGKA=|")


# DEF REGIS UNTUK MASUK KE HALAMAN REGISTRASI ADMIN BARU
def regis():
    regis = True 
    while regis:
        print("=SILAHKAN REGISTRASI BAGI ADMIN BARU=")
        username = input("masukkan username anda : ")
        password = input("masukkan password anda : ")
        cek = False

        for sama in admin:
            if admin[sama][0] == username:
                cek = True
                break

        if cek:
            os.system("cls || clear") 
            print("======USERSERNAME TELAH DIGUNAKAN======\n")

        else:
            key_baru = "admin " + str(len(admin)+1)
            admin[key_baru] = [username, password]
            regis = False
            print("==BERHASIL REGISTRASI==")

#DEF LOGIN UNTUK MASUK KE HALAMAN LOGIN ADMIN YANG SUDAH TERDAFTAR
def login(u, p):
    os.system("cls || clear")

    for key, value in admin.items():
        if u == value[0] and p == value[1]:
            print(f"""
    ====ANDA BERHASIL LOGIN====
    SELAMAT DATANG {value[0]}\n""")
            return True

    print("username atau password salah")
    return False

# DEF JUMLAH NASABAH
def hitung_nasabah(i=0):
    if i == len(pemilik):
        return 0
    else:
        return 1 + hitung_nasabah(i + 1)

# DEF LIHAT DAFTAR ADMIN
def DaftarAdmin():
    for key, value in admin.items():
        print(f"""
        {key}
        username : {value[0]}
        password : {value[1]}
        """)
        
    input("TEKAN ENTER UNTUK KEMBALI")

# DEF SETELAH ADMIN LOGIN
def AfterLogin():
    admin1 = True
    while admin1:
        print("""
        |===================|
        | 1. LIHAT DATA     |
        | 2. UPDATE DATA    |
        | 3. JUMLAH NASABAH |
        | 4. HAPUS DATA     |
        | 5. KEMBALI        |
        |===================|
                                    """)
        admin2 = input("ADMIN MAU NGAPAIN? ")
        os.system('cls || clear')

        if admin2 == '1':
            if len(pemilik) == 0:   
                print("====BELUM ADA NASABAH====")

            for key, value in pemilik.items():
                print(f"\n{key}\nNAMA : {value[0]}\nASAL KOTA : {value[1]}\nnomor hape : {value[2]}\nJENIS KARTU : {value[3]}")
            input("TEKAN ENTER UNTUK KEMBALI...")
            os.system('cls || clear')

        elif admin2 == '2':
            keys = list(pemilik.keys())
            if len(pemilik) == 0:
                print("====BELUM ADA NASABAH====")

            else:
                # tampilkan semua nasabah
                print("DAFTAR NASABAH :")
                for key, value in pemilik.items():
                    print(f"\n{key}\nNAMA : {value[0]}\nASAL KOTA : {value[1]}\nnomor hape : {value[2]}\nJENIS KARTU : {value[3]}")

                # input dulu
                ganti1 = int(input("\nNASABAH NOMOR BERAPA ? "))
                daftar_key = list(pemilik.keys())
                key_dipilih = daftar_key[ganti1 - 1]
                print("""
                    |====================|
                    | 1. NAMA            |
                    | 2. ASAL KOTA       |
                    | 3. NOMOR HANDPHONE |
                    |====================|
                    """)
                ganti2 = input("APA YANG INGIN DIGANTI ? ")
                if ganti2 == '1':
                    pemilik[key_dipilih][0] = input("masukkan nama baru : ")
                    print("NAMA BERHASIL DIGANTI")

                elif ganti2 == '2':
                    pemilik[key_dipilih][1] = input("masukkan asal kota yang baru : ")
                    print("ASAL KOTA BERHASIL DIGANTI")

                elif ganti2 == '3':
                    pemilik[key_dipilih][2] = input("masukkan nomor handphone yang baru : ")
                    print("NOMOR HANDPHONE BERHASIL DIGANTI")

                else:
                    print("\nINVALID COMMAND")
        
        elif admin2 == '3':
            total = hitung_nasabah()
            print(f"TOTAL NASABAH TERDAFTAR: {total}")

        elif admin2 == '4':
            if len(pemilik) == 0:
                print("====BELUM ADA NASABAH====")
                
            else:  
                hapus = int(input("\nDATA NOMOR BERAPA YANG INGIN DIHAPUS? "))
                daftar_key = list(pemilik.keys())

                if 1 <= hapus <= len(daftar_key):
                    key_dihapus = daftar_key[hapus - 1]
                    del pemilik[key_dihapus]
                    print(f"Data nasabah '{key_dihapus}' berhasil dihapus!")
                else:
                    print("Nomor nasabah tidak valid!")
        elif admin2 == '5':
            print("\n===ANDA TELAH LOG OUT===\n")
            input("TEKAN ENTER UNTUK KEMBALI...")       
            admin1 = False

        else:
            print("INVALID COMMAND")

# DEF TAMBAH NASABAH
def TambahNasabah(nama, asal_kota, nomor_hp):
    os.system('cls || clear')
    jenis_kartu = True
    while jenis_kartu:
        print("""
        |=================|  
        |JENIS-JENIS KARTU|
        |   1. SILVER     |
        |   2. GOLD       |
        |   3. PLATINUM   |
        |=================|              
                """)
        kartu = input("MAU JENIS KARTU APA ? ")
        os.system('cls || clear')
        nasabah = f"NASABAH {len(pemilik)+1}"

        if kartu == '1':
            jenis = "SILVER"
        
        elif kartu == '2':
            jenis = 'GOLD'

        elif kartu == '3':
            jenis = 'PLATINUM'
        
        else:
            print("\nINVALID COMMAND")

        pemilik[nasabah] = [nama, asal_kota, nomor_hp, jenis]
        
        os.system('cls || clear')
        print(f"DATA BERHASIL DITAMBAHKAN!\n")
        print(f"{nasabah}")
        print(f"NAMA        : {nama}")
        print(f"ASAL KOTA   : {asal_kota}")
        print(f"NOMOR HP    : {nomor_hp}")
        print(f"JENIS KARTU : {jenis}")
        break

pilih_menu = True
while pilih_menu:
    print("\nDAFTAR PEMBUATAN KARTU ATM")

    print("""
    |=================|
    | 1. Admin        |
    | 2. Daftar Kartu |
    | 3. Keluar       |
    |=================|
    """)

    pertama = input("PILIH MENU : ")
    if pertama == '1':
        os.system('cls || clear')
        utama1()
        os.system('cls || clear')
        akun1 = True
        while akun1:
            os.system('cls || clear')
            print("""
                     ADMIN
                |=================|
                | 1. REGISTER     |
                | 2. LOGIN        |
                | 3. DAFTAR ADMIN |
                | 4. KELUAR       |
                |=================|
                                """)
            akun2 = input("NOMOR BERAPA : ")
            os.system('cls || clear')

            if akun2 == '1':
                regis()

            elif akun2 == '2':
                while True:
                    print("\n=====SILAHKAN LOGIN=====\n")
                    username = input("masukkan username anda : ")
                    password = input("masukkan password anda : ")

                    if login(username, password):
                        AfterLogin()
                        break       
                    
                    else:
                        input("ENTER UNTUK LOGIN KEMBALI")
                
            elif akun2 == '3':
                DaftarAdmin()

            elif akun2 == '4':
                akun1 = False
            
            else:
                print("1/2/3/4 SAJA")

    elif pertama == '2':
        tambah = True
        while tambah:
            nama = input("\nNAMA : ")
            asal_kota = input("ASAL KOTA : ")
            nomor_hp = input("NOMOR HANDPHONE : ")
            TambahNasabah(nama, asal_kota, nomor_hp)
            print("""
        |===================|
        | 1. TAMBAH KEMBALI |
        | 2. SUDAH CUKUP    |
        |===================|
            """)
            tambah2 = input("MASUKKAN NOMOR YANG DIPILIH : ")
            if tambah2 == '1':
                tambah = True

            elif tambah2 == '2':
                tambah = False

    elif pertama == '3':
        pilih_menu = False

    else:
        print("TIDAK ADA PILIHANNYA")