# pendaftaran kartu atm nasabah bank
import os 

akun = {
    "admin 1" : ["admin", "123"]
}
pemilik = {}

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

    os.system('cls || clear')           
    if pertama == '2':
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
                jenis1 = "SILVER"
                print(f"DAFTAR KARTU ATM {jenis1}")
                nama = input("\nNAMA : ")
                asal_kota = input("ASAL KOTA : ")
                nomor_hp = input("NOMOR HANDPHONE : ")
                pemilik[nasabah] = [nama, asal_kota, nomor_hp, jenis1]
                for key, value in pemilik.items():
                    print(f"\n{key}")
                    print(f"NAMA        : {value[0]}")
                    print(f"JENIS KARTU : {value[3]}")
                jenis_kartu = False
            
            elif kartu == '2':
                jenis2 = 'GOLD'
                print(f"DAFTAR KARTU ATM {jenis2}")
                nama = input("\nNAMA : ")
                asal_kota = input("ASAL KOTA : ")
                nomor_hp = input("NOMOR HANDPHONE : ")
                pemilik[nasabah] = [nama, asal_kota, nomor_hp, jenis2]
                for key, value in pemilik.items():
                    print(f"\n{key}")
                    print(f"NAMA        : {value[0]}")
                    print(f"JENIS KARTU : {value[3]}")
                jenis_kartu = False

            elif kartu == '3':
                jenis3 = 'PLATINUM'
                print(f"DAFTAR KARTU ATM {jenis3}")
                nama = input("\nNAMA : ")
                asal_kota = input("ASAL KOTA : ")
                nomor_hp = input("NOMOR HANDPHONE : ")
                pemilik[nasabah] = [nama, asal_kota, nomor_hp, jenis3]
                for key, value in pemilik.items():
                    print(f"\n{key}")
                    print(f"NAMA        : {value[0]}")
                    print(f"JENIS KARTU : {value[3]}")
                jenis_kartu = False
            
            else:
                print("\nINVALID COMMAND")
        
            
    elif pertama == '1':
        akun1 = True
        while akun1:
            os.system('cls || clear')
            print("""
                     ADMIN
                |=============|
                | 1. REGISTER |
                | 2. LOGIN    |
                | 3. KELUAR   |
                |=============|
                                """)
            akun2 = input("NOMOR BERAPA : ")
            os.system('cls || clear')

            if akun2 == '1':
                register = True
                sudah_ada = False
                for user in akun.copy().values():
                    os.system('cls || clear')
                    while register:
                        print("===REGISTER===")
                        username = input("masukkan username : ")
                        password = input("masukkan password : ")
                        
                        os.system('cls || clear')
                        if user[0] == username:
                            print("USERNAME TELAH DIGUNAKAN")
                            sudah_ada = True
                        else:
                            key_baru = f"admin {len(user)}"
                            akun[key_baru] = [username, password]
                            print("BERHASIL REGISTRASI")
                            for key, value in akun.items():
                                print(f"""
    {key}
    username : {value[0]}
    password : {value[1]}""")
                            input("\nTEKAN ENTER UNTUK KEMBALI...")
                            register = False


            elif akun2 == '2':
                login = True
                while login:
                    print("\nLOGIN TERLEBIH DAHULU\n")
                    username = input("masukkan username anda : ")
                    password = input("masukkan password anda : ")
                    for key, value in akun.items():

                        if username == value[0] and password == value[1]:
                            print(f"""
    ====ANDA BERHASIL LOGIN====
    SELAMAT DATANG {value[0]}""")
                            admin1 = True
                            while admin1:
                                print("""
                |================|
                | 1. LIHAT DATA  |
                | 2. UPDATE DATA |
                | 3. HAPUS DATA  |
                | 4. KEMBALI     |
                |================|
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
                                            print("\nINVALID COMMAN")

                                elif admin2 == '3':
                                        if len(pemilik) == 0:
                                            print("====BELUM ADA NASABAH====")

                                        hapus = int(input("\nDATA NOMOR BERAPA YANG INGIN DIHAPUS? "))
                                        daftar_key = list(pemilik.keys())

                                        if 1 <= hapus <= len(daftar_key):
                                            key_dihapus = daftar_key[hapus - 1]
                                            del pemilik[key_dihapus]
                                            print(f"Data nasabah '{key_dihapus}' berhasil dihapus!")
                                        else:
                                            print("Nomor nasabah tidak valid!")
                                elif admin2 == '4':
                                    print("\n===ANDA TELAH LOG OUT===\n")
                                    input("TEKAN ENTER UNTUK KEMBALI...")       
                                    admin1 = False
                                    login = False

                                else:
                                    print("INVALID COMMAND")
                                                        
                        elif username != value[0] and password == value[1]:
                            os.system('cls || clear')
                            print("USERNAME ANDA SALAH")

                        elif username == value[0] and password != value[1]:
                            os.system('cls || clear')
                            print("PASSWORD ANDA SALAH")

                        else:
                            os.system('cls || clear')
                            print("USERNAME DAN PASSWORD SALAH")

            elif akun2 == '3':
                akun1 = False

            else:
                print("INVALID COMMAND")
    
    elif pertama == '3':
        print("""
        |============|
        |TERIMA KASIH|
        |============|
              """)
        pilih_menu = False

    else:
        print("INVALID COMMAND")