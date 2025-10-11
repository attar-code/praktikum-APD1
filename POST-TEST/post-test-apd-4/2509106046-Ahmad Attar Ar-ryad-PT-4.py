# login

print("""
    =========
    | LOGIN |
    =========
    """)
while True:
    username = input("masukkan username anda : ")
    password = input("masukkan password anda : ")

    if username == 'Attar' and password == '046':
        print("""
    ==============
    LOGIN BERHASIL
    ==============
              """)
        break

    elif username != 'Attar' and password == '046':
        print("""
    ==============
    USERNAME SALAH
    ==============
              """)
        
    elif username == 'Attar' and password !='046':
        print("""
    ==============
    PASSWORD SALAH
    ==============
              """)

    else :
        print("""
    ===========================
    USERNAME DAN PASSWORD SALAH
    ===========================
              """)

# data nampung
total_A1 = 0
total_A2 = 0
total_B1 = 0
total_B2 = 0
total_AB1 = 0
total_AB2 = 0
total_O1 = 0
total_O2 = 0

# input golongan
input_data = True
while input_data:        
         
    golongan_darah = input("\nAPA GOLONGAN DARAH MU |A/B/AB/O| ? ")
    
    if golongan_darah == 'A':
        while True:
            golongan = input("\nAPAKAH GOLONGAN DARAH TERDAPAT RHESUS (Y/T)? ")
            if golongan == 'Y':
                kantongA1 = int(input("\nADA BERAPA KANTONG DARAH ? "))
                konversiA1 = kantongA1 * 500
                total_A1 += konversiA1
                break

            elif golongan == 'T':
                kantongA2 = int(input("\nADA BERAPA KANTONG DARAH ? "))
                konversiA2 = kantongA2 * 500
                total_A2 += konversiA2
                break

            else:
                print("\nINVALID COMMAND")

    elif golongan_darah == 'B':
        while True:
            golongan = input("\nAPAKAH GOLONGAN DARAH TERDAPAT RHESUS (Y/T)? ")
            if golongan == 'Y':
                kantongB1 = int(input("\nADA BERAPA KANTONG DARAH ? "))
                konversiB1 = kantongB1 * 500
                total_B1 += konversiB1
                break
            
            elif golongan == 'T':
                kantongB2 = int(input("\nADA BERAPA KANTONG DARAH ? "))
                konversiB2 = kantongB2 * 500
                total_B2 += konversiB2
                break

            else:
                print("\nINVALID COMMAND")

    elif golongan_darah == 'AB':
        while True:
            golongan = input("\nAPAKAH GOLONGAN DARAH TERDAPAT RHESUS (Y/T)? ")
            if golongan == 'Y':
                kantongAB1 = int(input("\nADA BERAPA KANTONG DARAH ? "))
                konversiAB1 = kantongAB1 * 500
                total_AB1 += konversiAB1
                break
            
            elif golongan == 'T':
                kantongAB2 = int(input("\nADA BERAPA KANTONG DARAH ? "))
                konversiAB2 = kantongAB2 * 500
                total_AB2 += konversiAB2
                break

            else:
                print("\nINVALID COMMAND")

    elif golongan_darah == 'O':
        while True:
            golongan = input("\nAPAKAH GOLONGAN DARAH TERDAPAT RHESUS (Y/T)? ")
            if golongan == 'Y':
                kantongO1 = int(input("\nADA BERAPA KANTONG DARAH ? "))
                konversiO1 = kantongO1 * 500
                total_O1 += konversiO1
                break
            
            elif golongan == 'T':
                kantongO2 = int(input("\nADA BERAPA KANTONG DARAH ? "))
                konversiO2 = kantongO2 * 500
                total_O2 += konversiO2
                break

            else:
                print("\nINVALID COMMAND")
    
    else:
            print("\nINVALID COMMAND  ")
    
    pengulangan = True
    while pengulangan:
        ulang = input("\nAPAKAH MAU DITAMBAH (Y/T)? ")

        if ulang == 'Y':
            break

        elif ulang == 'T':
            pengulangan = False
            input_data = False

        else:  
             print("\nINVALID COMMAND")

#output
print(f"""
A+  : {total_A1} ML
A-  : {total_A2} ML
B+  : {total_B1} ML
B-  : {total_B2} ML
AB+ : {total_AB1} ML
AB- : {total_AB2} ML
O+  : {total_O1} ML
O-  : {total_O2} ML
""")