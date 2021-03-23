#71200670 Renaldo Surya Saputra

'''
Tono merupakan mahasiswa IT di kanpusnya. Ia diminta oleh temannya untuk membuat program 
mrngrnai string. Dimana program tersebut harus menampilkan huruf besar pada suatu kalimat jika 
ada huruf yang terulang pada kalimat tersebut. Buatlah program berdasarkan permasalahan tersebut

input :
kalimat

proses :
pengecekan kalimat apakah di kalimat tersebut ada huruf yang terulang

output :
menampilkan huruf yang terulang dlam bentuk upper case
'''

def CekUpperCase(n) : 
     huruf = {}
     for i in n :
          if i in huruf :
               huruf[i] = huruf[i] + 1
          else :
               huruf[i] = 1
     jawab = ""

     for i in n :
          if huruf[i] > 1 :
               i = i.upper()

          jawab = jawab + i
     return jawab



n = str(input("Masukan Kalimat :"))
print(CekUpperCase(n))
