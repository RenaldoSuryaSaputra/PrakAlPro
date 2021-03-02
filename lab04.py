#71200670 Renaldo Surya Saputra
''' Aryo merupakan mahasiswa IT yang sedang bertugas untuk mengajar anak smp. 
Dari hasil survey Aryo mengenai kebutuhan anak smp, Aryo menemukan keulitan yang dihadapi anak smp
tentang menghitung volume suatu bangun ruang. 
Aryo mendapat ide untuk membuat program penghitung volume bangun 
ruang yang sekiranya mudah digunakan anak smp di tempat ia mengajar. 
coba buatlah program penghitung volume kubus, balok, dan tabung 
menggunakan modular program yang sekiranya akan dibuat Aryo. 

'''
'''
input = kubus : panjang sisi ; balok : panjang alas, lebar, dan tinggi ; tabung : jari-jari dan tinggi tabung

proses =
1. membuat fungsi penghitung volume kubus menggunakan modular program
2. valome balok menggunakan mondular program
3. volume tabung menggunakan modular program

output :
1. hasil perhitungan volume kubus
2. hasil perhitungan volume balok
3. hasil perhitungan volume tabung

'''
def volumeKubus(n) :
     hasil = n**3
     return hasil
def volumeBalok(a,l,t) :
     hasil = a * l * t
     return hasil
def volumeTabung(r,t):
     phi = 22/7
     hasil = phi * r * r * t
     return hasil

list=["Kubus", "Balok", "Tabung"]
print("~"*10, "SELAMAT DATANG DIPROGRAM PENGHITUNG VOLUME", "~"*10)
for i in range(3):
     print("%d."%(i + 1), list[i])

inp = input("Masukan pilihan anda :")
if inp == "1" :
     sisi = int(input("Masukan panjang sisi kebus :"))
     print("Besarnya volume kubus tersebut ialah", volumeKubus(sisi), "m^3")
elif inp == "2" :
     alas = int(input("Masukan panjang alas :"))
     lebar = int(input("Masukan lebar balok :"))
     tinggi = int(input("Masukan tinggi balok :"))
     print("besar volume balok tersebut ialah", volumeBalok(alas,lebar,tinggi), "m^3")
elif inp == "3" :
     jari = int(input("Masukan panjang jari-jari :"))
     tinggiT = int(input("Masikan tinggi tabung :"))
     print("Besar volume tabung sebesar", volumeTabung(jari,tinggiT), "m^3")
else :
     print("input tidak tersedia")