
from prettytable import PrettyTable
import readchar, os, afterlogin

list = ["REGISTRASI", "LOGIN", "CEK DAFTAR ADMIN", "KELUAR"]
posisi = 0
tabel1 = PrettyTable()
tabel2 = PrettyTable()
tabel3 = PrettyTable()
tabel4 = PrettyTable()

utama = ("manajer", 24)
admin = {
        "admin 1" : ["Attar", "046"],
        "admin 2" : ["Admin", "123"]
    }

def clear():
    os.system("cls || clear")

def pil1():
    global posisi
    ulang1 = True
    while ulang1:
        try:
            tabel1.clear_rows()
            tabel1.add_row(["HANYA MANAJER YANG TAHU"])
            tabel1.header = False
            print(tabel1)
            username = input("MASUKKAN USERNAME : ")
            password = int(input("MASUKKAN PASSWORD : "))

            if username == utama[0] and password == utama[1]:

                ulang2 = True
                while ulang2:
                    tabel2.clear_rows()
                    clear()
                    tabel2.header = False
                    tabel2.align = "l"
                    for i, item in enumerate(list):
                        tanda = ">" if i == posisi else " "
                        tabel2.add_row([tanda, item])

                    print(tabel2)
                    kunci = readchar.readkey()

                    if kunci == readchar.key.UP:
                        posisi = (posisi - 1) % len(list) 

                    elif kunci == readchar.key.DOWN:
                        posisi = (posisi + 1) % len(list) 

                    elif kunci == readchar.key.ENTER:                   
                        if posisi == 0:
                            clear()
                            regis = True 
                            while regis:
                                tabel3.clear()
                                tabel3.add_row(["SILAHKAN REGISTRASI BAGI ADMIN BARU"])
                                tabel3.header = False
                                print(tabel3)
                                username = input("masukkan username anda : ")
                                password = input("masukkan password anda : ")

                                if not password.isdigit():
                                    clear()
                                    print("password wajib berupa angka".upper())
                                    continue

                                elif len(password) < 3 or len(password) > 3:
                                    clear()
                                    print("password wajib 3 angka".upper())
                                    continue

                                cek = False

                                for sama in admin:
                                    if admin[sama][0] == username:
                                        cek = True
                                        break

                                if cek:
                                    clear()
                                    print("======USERSERNAME TELAH DIGUNAKAN======\n")

                                else:
                                    key_baru = "admin " + str(len(admin)+1)
                                    admin[key_baru] = [username, password]
                                    regis = False
                                    print("==BERHASIL REGISTRASI==")


                        elif posisi == 1:
                            clear()
                            ulang3 = True
                            while ulang3:
                                print("\n=====SILAHKAN LOGIN=====\n")
                                username = input("masukkan username anda : ")
                                password = input("masukkan password anda : ")

                                for key, value in admin.items():
                                    if username == value[0] and password == value[1]:
                                        clear()
                                        print(f"""
        ====ANDA BERHASIL LOGIN====
        SELAMAT DATANG {value[0]}""")
                                        afterlogin.AfterLogin()
                                        ulang3 = False
                                    
                                    elif username != value[0] and password == value[1]:
                                        clear()
                                        print("username salah".upper())

                                    elif username == value[0] and password != value[1]:
                                        clear()
                                        print("password salah".upper())

                                    else:
                                        clear()
                                        print("username dan password salah".upper())

                        elif posisi == 2:
                            clear()
                            tabel4.clear()
                            print("\nDAFTAR ADMIN:")
                            tabel4.field_names = ["ID ADMIN", "NAMA", "PASSWORD"]
                            for key, value in admin.items():
                                tabel4.add_row([key, value[0], value[1]])

                            print(tabel4)
                            input("\nENTER TO BACK")
                                    

                        elif posisi == 3:
                            clear()
                            print("\n====TERIMA KASIH=====\n")
                            ulang1 = False
                            ulang2 = False

            elif username != utama[0] and password == utama[1]:
                clear()
                print("======username salah======".upper())

            elif username == utama[0] and password != utama[1]:
                clear()
                print("======password salah======".upper())

            else:
                clear()
                print("username dan password salah")
            
        except ValueError:
            clear()
            print("===password berupa angka===".upper())
