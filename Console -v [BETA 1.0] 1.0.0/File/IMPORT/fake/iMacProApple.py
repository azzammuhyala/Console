#iMacPro.apple
#func:
import os
import datetime

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def func_main():
  name_imac = input("Input Mac name: ")
  clear_screen()
  current_time_for_lastloginmac = datetime.datetime.now().strftime("%A %B  %d, %H:%M:%S")
  print(f"Last login: {current_time_for_lastloginmac} on ttys003")
  while True:
    try:
      imac_inp = input(f"{name_imac}@MacBook-Pro ~ % ")
      if imac_inp.lower() == "exit":
        break
      if imac_inp.lower() == "clear":
        clear_screen()
      if imac_inp:
        if "echo ".lower() in imac_inp:
          print(imac_inp[5:], "\n")
        else:
          print("")
    except KeyboardInterrupt:
      print("\033[33mYou just terminated the program.\033[0m")
      break
    except EOFError:
      print("\033[33mYou just terminated the program.\033[0m")
      break
    except:
      print("\033[33mYou just terminated the program.\033[0m")
      break