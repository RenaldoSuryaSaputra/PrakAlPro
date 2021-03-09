#71200670_Renaldo Surya Saputra

'''Andi diminta temannya ubtuk membuat program dengan menggunakan python. Program yang diminta teman 
Andi uialah program untuk menghitung rata-rata penjualan buah berdasarkam banyak hari yang ditentukan.
Buatlah progam tersebut menggunakan struktur kontrol perulanagan while!

input :
banyak hari ; buah dalam kg

proses : 
mencari rata-rata penjualan buah selama n hari

output :
rata-rata buah yang dijual dalam n hari

'''
data = int(input("Masukan banyak hari :"))
x = 0
jumlah = 0
while x < data :
      kg = int(input("Masukan angka penjualan : "))
      jumlah = jumlah + kg
      x = x + 1
hasil = jumlah / data
print("Rata-rata penjualan sebesar", hasil)
