import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    clear_screen()
    # input kendaraan yang di pakai
    kendaraan = int((input('''kendaraan yang kamu pakai 
                          ketik 1500/1000
                          1500. mobil
                          1000. motor

                          pilihan kamu:''')))
    durasi = float(input('berapa lama kamu parkir?'))
    # menghitung durasi dan biaya
    if durasi <= 0:
        print('waduh gak bisa bro')
        break

    elif durasi <= 2:
        tarif = 3000
        print (tarif)

    elif durasi <= 24:

        print (3000 + (durasi - 2) * kendaraan)

    else:

        print (3000 +(durasi - 2) * kendaraan + 10000)

        kondisi = input("\napakah kamu ingin melanjutkan parkir kembali? (y/n)")
    if kondisi == 'n' :
        print('==terimakasih telah parkir di tempat kami==')
        break