#71200670 Renaldo Surya Saputra
''' Martin adalah mahasiswa IT yang magang untuk membantu anak sd. Martin diminta membantu mengajari anak sd
mengenai bilangan prima. sayangnya Martin sendiri tidak hafal urutan bilangan prima. oleh karena itu, 
sebagai ahli IT Martin ingin membuat program untuk mengetahui bilangan prima. 
Buatlah program untuk mengetahui urutan bilangan prima.

input :
akhir bilangan prima

proses :
pengcekan bilangan n1 - nakhir yang merupakan prima

output : 
bilangan prima dari terkecil ke terbesar
'''

inp = int(input("Batas bilangan : "))

i = 2
while(i < inp) :
     counter = 2
     while(counter <= (i/counter)) :
          if (i % counter) == 0 :
               break
          else :
               counter = counter + 1     
     if(counter > (i/counter)):
          print(i, "merupakan prima")
     i = i + 1
print("Selesai")
