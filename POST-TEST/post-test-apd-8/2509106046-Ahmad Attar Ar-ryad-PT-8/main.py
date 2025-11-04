from prettytable import PrettyTable
import admin, readchar, os, afterlogin

kotak = PrettyTable()
letak = 0
urutan = ["ADMIN  ", "NASABAH", "KELUAR"]

def clear():
    os.system("clear || cls")

ulang = True
while ulang:
    kotak.clear_rows()
    clear()
    print("SISTEM PENDAFTARAN KARTU ATM")
    kotak.header = False
    kotak.align = "l"
    for i, item in enumerate(urutan):
        tanda = ">" if i == letak else " "
        kotak.add_row([tanda, item])

    print(kotak)
    kunci = readchar.readkey()

    if kunci == readchar.key.UP:
        letak = (letak - 1) % len(urutan) 

    elif kunci == readchar.key.DOWN:
        letak = (letak + 1) % len(urutan) 

    elif kunci == readchar.key.ENTER:     
        if letak == 0:
            clear()
            admin.pil1()

        elif letak == 1:
            clear()
            tambah = True
            while tambah:
                print("NASABAH BARU :")
                nama = input("\nNAMA : ")
                asal_kota = input("ASAL KOTA : ")
                nomor_hp = input("NOMOR HANDPHONE : ")
                afterlogin.TambahNasabah(nama, asal_kota, nomor_hp)
                tambah1 = True
                while tambah1:
                    print("""
        |===================|
        | 1. TAMBAH NASABAH |
        | 2. SUDAH CUKUP    |
        |===================|
            """)
                    tambah2 = input("MASUKKAN NOMOR YANG DIPILIH : ")
                    if tambah2 == '1':
                        clear()
                        tambah1 = False

                    elif tambah2 == '2':
                        tambah1 = False
                        tambah = False

                    else:
                        clear()
                        print("NOMOR 1 ATAU 2 SAJA")
        
        elif letak == 2:
            ulang = False
            clear()
            print("TERIMA KASIH")