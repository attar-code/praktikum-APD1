import os

pemilik = {
    "NASABAH 1" : ["Attar", "samarinda", "081258031880", "SILVER"]
} 

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

def hitung_nasabah(i=0):
    if i == len(pemilik):
        return 0
    else:
        return 1 + hitung_nasabah(i + 1)

def AfterLogin():
    admin1 = True
    while admin1:
        print("""
        |===================|
        | 1. LIHAT DATA     |
        | 2. UPDATE DATA    |
        | 3. JUMLAH NASABAH |
        | 4. HAPUS DATA     |
        | 5. LOG OUT        |
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
                os.system('cls || clear')
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