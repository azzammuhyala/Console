#testkecocokanpasangan.consolePy
#func:
import os
import shutil
import random

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def func_main():
  try:
    clear_screen()
    Judul = "✨CEK KECOCOKAN PASANGAN MU✨"
    tw3 = shutil.get_terminal_size().columns
    cl3 = tw3 - 2
    spacesJudul = cl3 - len(Judul)
    leftspacesJudul = spacesJudul // 2
    print(r"Ini g 100% bisa ngeramal ya ges😆 Jadi jangan di masuki ke hati👉👈 kalo mau keluar ketik (!end) aja ya!" + "\n")
    print(" " * leftspacesJudul + Judul)
    while True:
      nm_1 = input("\n+-Nama 1: ")
      nm_2 = input("❤\n+-Nama 2: ")
      persen = random.randint(0, 1000) / 10
      print(f"(✨   {nm_1} ~ {nm_2} | Tingkat Kecocokan: {persen:.1f}%  ✨)\n")
      if nm_1 == "!end" or nm_2 == "!end":
        break
      else:
        persenF = float(persen)
        if persenF <= 10:
          print("\033[32m" + r"Sayang bgt yah kurang dari 10% semoga hubungan kali erat ya;)" + "\033[0m")
        elif persenF <= 20:
          print("\033[32m" + r"Hubungan kalian masih kurang erat nih! ayo lebih akrab lagi!😆" + "\033[0m")
        elif persenF <= 40:
          print("\033[32m" + r"jangan saling cuek dong,, ntar sia-sia deh😁" + "\033[0m")
        elif persenF <= 60:
          print("\033[32m" + r"Kok setengah2 gitu sih😶 ayo jangan setengah2 pacarannya!👀" + "\033[0m")
        elif persenF <= 80:
          print("\033[32m" + r"Ihhh.. lebih deket lagi biar makin cinta lagi!!111!!😆😆❤❤" + "\033[0m")
        elif persenF <= 100:
          print("\033[32m" + r"Wihh lansung ajak nikah aja!11!!!🙌💋🌹💖" + "\033[0m")
  except KeyboardInterrupt:
    print("\033[33mYou just terminated the program.\033[0m")
  except EOFError:
    print("\033[33mYou just terminated the program.\033[0m")
  except:
    print("\033[33mYou just terminated the program.\033[0m")