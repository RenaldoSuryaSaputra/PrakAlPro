#Nama : Renaldo Surya Saputra
#NIM : 71200670

'''Suryo adalah salah satu karyawan dari perusahaan terkenal. Gaji yang diperloh Suryo tiap bulan 
ialah gaji pokok ditambah gaji tunjangan fungsional dari perusahaan.
Tetapi Suryo juga harus memenuhi kebutuhan tiap bulannya, 
setiap bulan ia akan menggunakan 30% dari gajinya untuk berbelanja kebutuhan sehari-hari,
5% untuk keperluan alat tulis kerja,
10% untuk biaya perjalanan ke perusahaan, dan 15% untuk kebutuhan internet di rumahnya. 
Buatlah program untuk keuangan baik pengeluaran maupun sisanya.'''

'''
input : 
banyaknya gaji pokok 
banyaknya gaji fungsional


proses : 
total gaji
banyaknya biasya sandang 
banyaknya biaya alat tulis
biaya transport
biaya internet
pengeluaran
tabungan


output :
1. Jumlah gaji Suryo selama bekerja dalam 1 bulan
2. jumlah uang yang dibutuhkan Suryo untuk keperluan sandang dalam 1 bulan
3. jumlah pengeluaran Suryo untuk keperluan alat tulis dalam 1 bulan
4. Jumlah biaya perjalanan suryo selama satu bulan
5. Jumlah biaya internet Suryo selama satu bulan
6. Total pengeluaram Suryo selama satu bulan 
7. Total tabungan Suryo selama 1 bulan

'''
print("PROGRAM KEUANGAN SURYO")

pokok = int(input("Jumlah gaji pokok yang didapat sebesar :"))
fungsional = int(input("jumlah gaji fungsional yang didapat sebesar :"))

total_gaji = pokok + fungsional
print("Banyaknya gaji yang Suryo dapat sebesar Rp", total_gaji)

sandang = total_gaji * 0.30
print("Banyaknya biaya yang dikeluarkan untuk kebutuhan sandang sebesar Rp", sandang)

alat = total_gaji * 0.05
print("banyaknya biaya yang dikeluarkan untuk kebutuhan alat tulis sebesar Rp", alat)

transport = total_gaji * 0.10
print("Banyaknya biaya yang dikeluarkan untuk transport sebesar Rp", transport)

internet = total_gaji * 0.15
print("Biaya yang dikeluarkan untuk kebutuhan internet sebesar Rp", internet)

pengeluaran = sandang + alat + transport + internet
print('Jumlah pengeluaran suryo sebesar Rp', pengeluaran)

tabungan = total_gaji - pengeluaran
print("Jumlah tabungan Suryo sebesar Rp", tabungan)