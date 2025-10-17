# list_Mahasiswa = [74, ['Indonesia', 'Laos', 'Malaysia']]
# print(list_Mahasiswa[1][1])

# # penggunaan append untuk menambahkan di akhir 
# list_Mahasiswa.append(500)
# print(list_Mahasiswa)

# # penggunaan insert untuk menambahkan list sesuai dengan posisi indeks yang kita mau 
# list_Mahasiswa.insert(1, 'Samarinda')
# print(list_Mahasiswa)

# # list awal
# studyclub = ["Data Science", "Robotics", ['indonesia', 'malaysia',['samarinda', 'balikpapan'], 'singapura'], "Multimedia", "Network"]
# print(studyclub)
# # memasukkan elemen ke dalam list yang ada di dalam list
# studyclub[2][2].insert(2, 'samboja')
# print(studyclub)

# # mengganti
# studyclub[0] = 'web'
# print(studyclub)

# # mengganti
# studyclub[2][0] = 'china'
# print(studyclub)

# # penggunaan .pop
# hilang = studyclub.pop(1)
# print(studyclub)
# print(hilang)

# # penggunaan del
# del studyclub[0]
# print(studyclub)

# # remove menghapus elemen berdasarkan nilai
# mata_kuliah = ['apd', 'orsikom', 'pkn', 'apd']
# print(mata_kuliah)
# mata_kuliah.remove('apd')
# print(mata_kuliah)

# # slicing dalam list
# praktikum = [3.14, 'fisdas', True, 55]
# print(praktikum)
# # stop dalam python tidak terdefinisi
# print(praktikum[0:3:2])
# print(len(praktikum))

# for i in range(len(praktikum)):
#     print(i+1,praktikum[1])

kelas = [
["Ridho", "Lian", "Nabil"],
["Daffa", "Dante", "Santoso"],
["Pernanda", "Riyadi", "Ahnaf"],
], [
    ["Ridho", "Lian", "Nabil"],
["Daffa", "Dante", "Santoso"],
["Pernanda", "Riyadi", "Ahnaf"],
]
print(kelas[0][1][1])

# # jika ingin mengubah tuple maka ubah dlu dari tuple ke list lalu kembalikan ke tuple kembali

# #
makanan = ('ayam', 'ikan', 'bebek', 'kepiting')
(darat, sungai, tanah, laut) = makanan
print(darat)
print(sungai)
print(tanah)
print(laut)