#artisifatnama.consolePy
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
    tw5 = shutil.get_terminal_size().columns + 18
    Judul1 = "\033[36m\033[7m\033[1mSIFAT-SIFAT NAMA KAMU\033[0m"
    spacesJudul1 = tw5 - len(Judul1)
    leftspacesJudul1 = spacesJudul1 // 2
    print("\033[35mKetik (!end) untuk keluar.\n\033[0m")
    print(" " * leftspacesJudul1 + Judul1)
    angkaUrut1 = 0
    sifat = ['Bahagia', 'Sedih', 'Marah', 'Cemas', 'Takut', 'Cemburu', 'Gampang Terkejut', 'Stres', 'Malu', 'Eksrovert', 'Introvert', 'Percaya diri', 'Ramah', 'Sopan', 'Terbuka', 'Tegas', 'Sensitif', 'Sabar', 'Impulsif', 'Ambisius', 'Kreatif', 'Disiplin', 'Fleksibel', 'Mandiri', 'Jujur', 'Pembohong', 'Setia', 'Bertanggung jawab', 'Adil', 'Murah hati', 'Penyayang', 'Pemaaf', 'Penghormat', 'Dermawan', 'Sederhana', 'Cerdas', 'Bego', 'Analitis', 'Kritis', 'Logis', 'G Logis', 'Inovatif', 'Berpikir', 'Antusias', 'Berpemimpin', 'Berkolaborasi', 'Bersahabat', 'Bertoleran', 'Curang', 'Aneh', 'Gila', 'Gugup', 'Nakal', 'Sok Asik', 'Asik', 'Angguh', 'Rasa Ingin Tahu', 'Badmood', 'Bekerja Sama', 'Selalu Waspada']
    while True:
      angkaUrut1 += 1
      nama = input(f"\n{angkaUrut1}. ")
      rdmSifat1 = random.choice(sifat)
      rdmSifat2 = random.choice(sifat)
      rdmSifat3 = random.choice(sifat)
      rdmSifat4 = random.choice(sifat)
      rdmSifat5 = random.choice(sifat)
      if rdmSifat1 == rdmSifat2 or rdmSifat1 == rdmSifat3 or rdmSifat1 == rdmSifat4 or rdmSifat5:
        rdmSifat1 = random.choice([x for x in sifat if x != rdmSifat1])
      if rdmSifat2 == rdmSifat3 or rdmSifat2 == rdmSifat4 or rdmSifat2 == rdmSifat5:
        rdmSifat2 = random.choice([x for x in sifat if x != rdmSifat2])
      if rdmSifat3 == rdmSifat4 or rdmSifat3 == rdmSifat5:
        rdmSifat3 = random.choice([x for x in sifat if x != rdmSifat3])
      if rdmSifat4 == rdmSifat5:
        rdmSifat5 = random.choice([x for x in sifat if x != rdmSifat4])
      garis = 68
      garisnama = len(nama)
      garisrdmSifat1 = len(rdmSifat1)
      garisrdmSifat2 = len(rdmSifat2)
      garisrdmSifat3 = len(rdmSifat3)
      garisrdmSifat4 = len(rdmSifat4)
      garisrdmSifat5 = len(rdmSifat5)
      spasinama = garis - garisnama
      spasirdmSifat = garis - garisrdmSifat1 - garisrdmSifat2 - garisrdmSifat3 - garisrdmSifat4 - garisrdmSifat5 - 8
      print("+----------------------------------------------------------------------------+")
      print(f"| NAMA : {nama}" + " " * spasinama + "|")
      print(f"| SIFAT: {rdmSifat1}, {rdmSifat2}, {rdmSifat3}, {rdmSifat4}, {rdmSifat5}" + " " * spasirdmSifat + "|")
      print("+----------------------------------------------------------------------------+")
      if nama == "!end":
        break
  except KeyboardInterrupt:
    print("\033[33mYou just terminated the program.\033[0m")
  except EOFError:
    print("\033[33mYou just terminated the program.\033[0m")
  except:
    print("\033[33mYou just terminated the program.\033[0m")