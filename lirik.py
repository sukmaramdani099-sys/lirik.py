import sys
import time


def jalanin_lirik():
    # Ubah lirik lagu dan delay hurufnya sesuai yang kalian mau
    lirik = [
        ("Sesi potret yang selalu ku benci", 0.5),
        ("Aneh rasanya kau tak di sini", 0.5),
        ("Susunan barisannya tak sama lagi", 0.5),
        ("Oh ho ho satu dua tiga", 2),
        ("Ini nyata kau telah pergi", 0.5),
        ("Ku bertamu kerumah barumu", 0.5),
        ("Tak ada kamu", 0.5),
        ("Hanya papan dan namamu", 0.5),
        ("Mana ocehan wewangian khasmu", 0.5),
    ]

    # Ubah delay dari setiap baris lagu (sesuaikan jumlah)
    delay = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    # Ubah judul lagu
    print("\n== Sesi Potret - Ari ==")
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    # Ganti nama pembuat
    print("// Code by skmrmd")


jalanin_lirik()
