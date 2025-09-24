suhu = [27, 33, 46, 55, 67, 92]
NIM = 46

F1 = 9/5 * suhu[0] + 32
F2 = 9/5 * suhu[1] + 32
K3 = suhu[2] + 273.15
K4 = suhu[3] + 273.15
R5 = 4/5 * suhu[4]
R6 = 4/5 * suhu[5]

jumlah = F1 + F2 + K3 + K4 + R5 + R6
rata2 = jumlah/len(suhu)
bolean = NIM < rata2

print(suhu)
print(suhu[-4:])
print("\nNIM saya adalah :", NIM)
print("\nCelcius To Fahrenheit")
print(suhu[0], "=", F1)
print(suhu[1], "=", F2)
print("\nCelcius To Kelvin")
print(suhu[2], "=", K3)
print(suhu[3], "=", K4)
print("\nCelcius To Reamur")
print(suhu[4], "=", R5)
print(suhu[5], "=", R6)
print("\nTotal semua adalah :", jumlah)
print("\nrata-rata :", rata2)
print("\nNIM < rata-rata :", bolean)