#pekerjaancocoknama.consolePy
#func:
import os
import shutil
import time
import random

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def func_main():
  try:
    clear_screen()
    print("\033[33m" + r"[!] WARNING!" + "\n" + r"This is just random text which is 100% incorrect!" + "\n\n" + r"[!] DEVICE UI BUG!" + "\n" + r"ASCII This may be too large that the ASCII UI on a small screen is unsightly." + "\n\033[0m")
    playDelay = 5
    for i in range(5):
      playDelay -= 1
      print(f"Start in {playDelay}", end="\r")
      time.sleep(1)
    clear_screen()
    tw4 = shutil.get_terminal_size().columns + 18
    Judul1 = "\033[32m\033[7m\033[1mPEKERJAAN YANG COCOK DARI NAMA\033[0m"
    spacesJudul1 = tw4 - len(Judul1)
    leftspacesJudul1 = spacesJudul1 // 2
    print("\033[35mKetik (!end) untuk keluar.\n\033[0m")
    print(" " * leftspacesJudul1 + Judul1)
    angkaUrut = 0
    pekerjaan = ['Guru', 'Dokter', 'Perawat', 'Polisi', 'Tentara', 'Pilot', 'Insinyur', 'Akuntan', 'Arsitek', 'Koki', 'Desainer grafis', 'Penulis', 'Penerjemah', 'Programer komputer', 'Marketing', 'Manajer proyek', 'Koruptor', 'Pengacara', 'Ahli biologi', 'Peternak', 'Nelayan', 'Pemadam kebakaran', 'Tukang kayu', 'Petugas kebersian', 'Penjaga toko', 'Satpam', 'Ahli keuangan', 'Pemandu wisata', 'PNS', 'Pengusaha', 'Seniman', 'Fotografer', 'Pedagang', 'Kasir', 'Jurnalis', 'Penyanyi', 'Pencukur rambut', 'Tukang pijat', 'PDI', 'Tukang bangunan', 'Editor', 'Tiktoker', 'Youtuber', 'Gamer', 'Pencuri', 'Artis', 'PLN', 'Dosen', 'Beban', 'Tukang keliling', 'Ustad', 'Dukun', 'PDAM', 'Pembangkit nuklir']
    while True:
      angkaUrut += 1
      nama = input(f"\n{angkaUrut}. ")
      randomPekerjaan = random.choice(pekerjaan)
      garis = 40
      garisnama = len(nama)
      garispekerjaan = len(randomPekerjaan)
      spasinama = garis - garisnama
      spasipekerjaan = garis - garispekerjaan
      print("+----------------------------------------------------+")
      print(f"| NAMA     : {nama}" + " " * spasinama + "|")
      print(f"| PEKERJAAN: {randomPekerjaan}" + " " * spasipekerjaan + "|")
      print("+----------------------------------------------------+")
      if nama == "!end":
        break
  except KeyboardInterrupt:
    print("\033[33mYou just terminated the program.\033[0m")
  except EOFError:
    print("\033[33mYou just terminated the program.\033[0m")
  except:
    print("\033[33mYou just terminated the program.\033[0m")