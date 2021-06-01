#71200670 RENALDO SURYA SAPUTRA

'''
temanmu, Rena adalah seorang mahasiswa matematika di kampus yang sama denganmu.
suatu hari Rena meminta kamu untuk membantunya dalam menghitung pangkat dari suaatu 
angka. Berhubung kamu adalah seorang programmer maka masalah tersebut dapat diselessaikan 
dengan membuat progran. Supaya tidak memakan waktu dalam pembuatan program maka kamu harus 
membuat program tersebut dalam bentuk fungsi rekursif. Buatlah program 
pangkat dalam rekursif ! 

input : angkanya ; pangkatnya

proses : memasukan input angka dan pangkat kedalam fungsi dan mengeluarkan hasilnya
sebagai output

output : hasil dari pangkat tersebut
'''
def pangkat(x, y) : 
     if(y == 1) :
          return x
     else : 
          return x * pangkat(x,y-1)

inputAngka = 5
inputPangkat = 5

print(pangkat(inputAngka,inputPangkat))