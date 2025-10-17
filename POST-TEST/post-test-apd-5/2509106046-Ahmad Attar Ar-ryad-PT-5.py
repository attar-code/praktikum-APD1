# pendaftaran kartu atm nasabah bank
import os 

akun = [
    ["Attar", "046", "admin"]
]
pemilik = []

pilih_menu = True
while pilih_menu:
    print("DAFTAR PEMBUATAN KARTU ATM")

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

            if kartu == '1':
                jenis = "SILVER"
                print(f"DAFTAR KARTU ATM {jenis}")
                nama = input("\nNAMA : ")
                asal_kota = input("ASAL KOTA : ")
                nomor_hp = input("NOMOR HANDPHONE : ")
                pemilik.append([nama, asal_kota, nomor_hp, jenis])
                for i in range(len(pemilik)):
                    print(f"\nNASABAH {i+1}\nNAMA : {pemilik[i][0]}\nJENIS KARTU : {pemilik[i][3]}")
                jenis_kartu = False
            
            elif kartu == '2':
                jenis = 'GOLD'
                print(f"DAFTAR KARTU ATM {jenis}")
                nama = input("\nNAMA : ")
                asal_kota = input("ASAL KOTA : ")
                nomor_hp = input("NOMOR HANDPHONE : ")
                pemilik.append([nama, asal_kota, nomor_hp, jenis])
                for i in range(len(pemilik)):
                    print(f"\nNASABAH {i+1}\nNAMA : {pemilik[i][0]}\nJENIS KARTU : {pemilik[i][3]}")
                jenis_kartu = False

            elif kartu == '3':
                jenis = 'PLATINUM'
                print(f"DAFTAR KARTU ATM {jenis}")
                nama = input("\nNAMA : ")
                asal_kota = input("ASAL KOTA : ")
                nomor_hp = input("NOMOR HANDPHONE : ")
                pemilik.append([nama, asal_kota, nomor_hp, jenis])
                for i in range(len(pemilik)):
                    print(f"\nNASABAH {i+1}\nNAMA : {pemilik[i][0]}\nJENIS KARTU : {pemilik[i][3]}")
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
                | 3. CEK DATA |
                | 4. KELUAR   |
                |=============|
                                """)
            akun2 = input("NOMOR BERAPA : ")
            os.system('cls || clear')

            if akun2 == '1':
                register = True
                for user in akun:
                    os.system('cls || clear')
                    while register:
                        print("===REGISTER===")
                        username = input("masukkan username : ")
                        password = input("masukkan password : ")

                        os.system('cls || clear')
                        if username == user[0]:
                            print("USERNAME TELAH DIGUNAKAN!")
                        else:
                            akun.append([username, password, "admin"])
                            print("Akun berhasil dibuat!")
                            for user in range(len(akun)):
                                print(f"Username admin {user+1}: {akun[user][0]}")
                            input("TEKAN ENTER UNTUK KEMBALI...")
                            register = False


            elif akun2 == '2':
                login = True
                while login:
                    print("\nLOGIN TERLEBIH DAHULU\n")
                    username = input("masukkan username anda : ")
                    password = input("masukkan password anda : ")
                    for user in akun:

                        if username == user[0] and password == user[1]:
                            print(f"""
    ====ANDA BERHASIL LOGIN====
    SELAMAT DATANG {user[0]}""")
                            admin1 = True
                            while admin1:
                                print("""
                |================|
                | 1. LIHAT DATA  |
                | 2. UPDATE DATA |
                | 3. KEMBALI     |
                |================|
                                """)
                                admin2 = input("ADMIN MAU NGAPAIN? ")
                                os.system('cls || clear')
                                if admin2 == '1':
                                    if len(pemilik) == 0:
                                        print("====BELUM ADA NASABAH====")

                                    for i in range(len(pemilik)):
                                        print(f"\nNASABAH {i+1}\nNAMA : {pemilik[i][0]}\nASAL KOTA : {pemilik[i][1]}\nnomor hape : {pemilik[i][2]}\nJENIS KARTU : {pemilik[i][3]}")

                                elif admin2 == '2':
                                    if len(pemilik) == 0:
                                        print("====BELUM ADA NASABAH====")

                                    else:
                                        ganti1 = int(input("NASABAH NOMOR BERAPA ? "))
                                        print("""
                |====================|
                | 1. NAMA            |
                | 2. ASAL KOTA       |
                | 3. NOMOR HANDPHONE |
                |====================|
                """)
                                        ganti2 = input("APA YANG INGIN DIGANTI ? ")
                                        if ganti2 == '1':
                                            pemilik[ganti1-1][0] = input("masukkan nama baru : ")
                                            print("NAMA BERHASIL DIGANTI")

                                        elif ganti2 == '2':
                                            pemilik[ganti1-1][1] = input("masukkan asal kota yang baru : ")
                                            print("ASAL KOTA BERHASIL DIGANTI")

                                        elif ganti2 == '3':
                                            pemilik[ganti1-1][2] = input("masukkan nomor handphone yang baru : ")
                                            print("NOMOR HANDPHONE BERHASIL DIGANTI")

                                        else:
                                            print("\nINVALID COMMAN")

                                elif admin2 == '3':
                                        if len(pemilik) == 0:
                                            print("====BELUM ADA NASABAH====")
                                        for i in pemilik:
                                            hapus = int(input("DATA NOMOR BERAPA ? "))
                                            del i[hapus-1]
                                            print("data berhasil dihapus")
                                elif admin2 == '4':
                                    print("===ANDA TELAH LOG OUT===")
                                    akun1 = False
                                    admin1 = False
                                    login = False

                                else:
                                    print("INVALID COMMAND")

                        elif username != user[0] and password == user[1]:
                            print("USERNAME ANDA SALAH")

                        elif username == user[0] and password != user[1]:
                            print("PASSWORD ANDA SALAH")

                        else:
                            print("USERNAME DAN PASSWORD SALAH")

            elif akun2 == '3':
                akun1 = False

            else:
                print("INVALID COMMAND")
    
    elif pertama == '3':
        print("======TERIMA KASIH=====")
        pilih_menu = False

    else:
        print("INVALID COMMAND")