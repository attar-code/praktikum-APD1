# while True:
#     Nilai = int(input("Masukkan Nilai Mahasiswa :"))
#     if Nilai > 80 and Nilai <= 100 :
#         if Nilai > 85:
#             print("A+")
#         else:
#             print("A-")
#     elif Nilai > 70 and Nilai <=80 :
#         if Nilai > 75 and Nilai <= 80:
#             print("B+")
#         else:
#             print("B-")
#     elif Nilai > 60 and Nilai <=70 :
#         if Nilai > 65 and Nilai <= 70:
#             print("C+")
#         else:
#             print("C-")
#     else:
#         print("D")

nilai = int(input("masukkan nama anda: "))
status = "jompo" if nilai > 30 else "dewasa"
print(status)