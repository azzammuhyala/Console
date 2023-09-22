#feeldreams.github.io/aboutyou
#func:2
import os
import time

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def func_main():
  try:
    clear_screen()
    nama_kamu = input("Masukin nama Kamu: ")
    clear_screen()
    print(r'''ascii-nameId:Hai,_str{nama_kamu}[].txt/link-feeldreams.github.io/aboutyou''')
    print(f"\nHai, {nama_kamu}✨")
    input("\ntekan enter untuk lanjut!")
    clear_screen()
    print(r'''ascii-nameId:Iyaa_kamu_yang_cantikkk.txt/link-feeldreams.github.io/aboutyou''')
    print("\nIyaa kamu yang cantikkk")
    input("\ntekan enter untuk lanjut!")
    clear_screen()
    print(r'''ascii-nameId:Baikk.txt/link-feeldreams.github.io/aboutyou''')
    print("\nBaikk")
    input("\ntekan enter untuk lanjut!")
    clear_screen()
    print(r'''ascii-nameId:Lucuuu[].txt/link-feeldreams.github.io/aboutyou''')
    print("\nLucuuu😋")
    input("\ntekan enter untuk lanjut!")
    clear_screen()
    print(r'''ascii-nameId:I'm_proud_of_u,_you_are_my_everything_to_me....txt/link-feeldreams.github.io/aboutyou''')
    print("\nI'm proud of u, you are my everything to me...")
    input("\ntekan enter untuk lanjut!")
    clear_screen()
    print(r'''ascii-classId:inp-####;nameId:Coba_ketik_'love'[].txt/link-feeldreams.github.io/aboutyou''')
    while True:
      love_inp = input("\nCoba ketik 'love'❤️: ")
      if love_inp.lower() == "love":
        clear_screen()
        print(r'''   __  __
  (  ♥♥  )
   \    /
    \  /
     \/
''')
        def animate_typing(text):
          for char in text:
            print(char, end='', flush=True)
            time.sleep(0.1)
            print()
        text_to_type = "I LOVE UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
        animate_typing(text_to_type)
        print("\nI LOVE U FOR EPER💕💕💕")
        break
      else:
        print("aduh bukan itu:(")
  except KeyboardInterrupt:
    print("\033[33mYou just terminated the program.\033[0m")
  except EOFError:
    print("\033[33mYou just terminated the program.\033[0m")
  except:
    print("\033[33mYou just terminated the program.\033[0m")