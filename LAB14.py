#71200670 Renaldo Surya Saputra 
'''
Omega memiliki adik yang suka mengelompokan kata berdasarkam panjang katanya. Mengetahui 
bahwa adiknya memiliki hobi yang aneh dan malah sering merepotkan Omega. Karena kesibukanya 
Omega sebagai Fisikawan, sehingga Ia tidak dapat membantu adiknya setiap saat. Oleh karena itu 
Omega meinta bantuan temannya yang seorang programmer untuk membantu mempersingkat rasa ingin 
tahu adik Omega menggunakan program. Buatlah program yang sekiranya bakalan sama kayak program 
yang akan dibuat temannya Omega !! Harus menggunakan RegEx !

input : kalimat macam buah 

proses : pengecekam panjang kata pada kalimat. pengelompokan berdasarkan panjang kata

output : menampilkan kelompok kata 
'''

import re 
teks = input("Masukan kalimat : ")
print("Kelompok buah dengan panjang 4 ", re.findall(r"\b\w{4}\b", teks))
print("Kelompok buah dengan panjang 5 ", re.findall(r"\b\w{5}\b", teks))