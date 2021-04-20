#71200670 Renaldo Surya Saputra

''' Buatlah sebuah fungsi untuk menghitung berapa jum;ah karakter dalam suatu list. 
Fungsi tersebut akan menampilkan banyak nya karakter dalam satu list. Dan isi list
sudah diisikan pada program.

input : list yang telah di tuliskan pada program

proses : membuat fungsi, pengecekan karakter pada list

output; jumlah karakter yang ada pada list tersebut

'''

def jumlahKarakter(list1) :
     angka= []
     count = 0
     for karakter in list1 :
          if karakter not in angka :
               count = count + 1
               angka.append(karakter)
     return count



list1 = ["r","e","n","a","l","d","o"]
print("Jumlah karakter pada list tersebut adalah", jumlahKarakter(list1))

