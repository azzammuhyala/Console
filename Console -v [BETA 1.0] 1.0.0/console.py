try:

  import math, datetime, random, time, os, re, shutil, traceback, socket, pyfiglet

  os.system('title Console')
except Exception as e:
  print("\033[31mERROR! idError: 1\nThe module used is invalid or an error occurred while importing the module or something error to running \033[36mconsole.py \033[31m. Please install module 'pip install {...}' if you haven't already installed it.\n\n\033[0m'\033[33mpip\033[0m install setuptools'\n'\033[33mpip\033[0m install re'\n'\033[33mpip\033[0m install pyfiglet'\n")
  print(f"Error python:\n{e}"); input("press enter to exit..."); exit()
except:
  print("\033[31mERROR! idError: 2\nSomething Error...\033[0m"); exit()

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

def consoleCommand():
  version = "  Version: \033[4m\033[32m[BETA 1.0] 1.0.0\033[0m  "
  tw = shutil.get_terminal_size().columns
  right_left = "=" * ((tw - 29) // 2)
  print(right_left + version + right_left)
  print("\033[36m\nCommands in this Console\n\033[0m")
  print("exit                           \033[33mTerminate a program\033[0m")
  print("clear                          \033[33mClear the entire command\033[0m")
  print("edit.logo_ascii                \033[33mEdit logo ascii\033[0m")
  print("text.ascii_generated           \033[33mGenerated ascii text\033[0m")
  print("del.new_ln=                    \033[33mRemoved special old content related to time, rdm, dupl\033[0m")
  print("ccl=                           \033[33mPerform basic math calculations (+ - / * ^)\033[0m")
  print("sqrt=                          \033[33mCalculate roots\033[0m")
  print("cbrt=                          \033[33mCalculate roots 3\033[0m")
  print("text=                          \033[33mDisplay text\033[0m")
  print("input=                         \033[33mDisplay a prompt for user input\033[0m")
  print("dt=                            \033[33mDuplicate a character\033[0m")
  print("nc=                            \033[33mCount the number of characters\033[0m")
  print("bnr=                           \033[33mConvert words to binary code\033[0m")
  print("bnr_re=                        \033[33mConvert binary code to words\033[0m")
  print("mrs=                           \033[33mConvert words to Morse code\033[0m")
  print("trm.s.get                      \033[33mGet the terminal size\033[0m")
  print("dom.get.ip_address=            \033[33mGet an IP address from a domain\033[0m")
  print("box_text.empty                 \033[33mCreate empty text box\033[0m")
  print("num_box_text.empty             \033[33mCreate empty numeric text box\033[0m")
  print("dupl.text                      \033[33mDuplicate a text\033[0m")
  print("text.typing                    \033[33mCreate animated text\033[0m")
  print("letter=official;english        \033[33mCreate an official English letter\033[0m")
  print("letter=un_official;english     \033[33mCreate an unofficial English letter\033[0m")
  print("letter=official;indonesian     \033[33mCreate an official Indonesian letter\033[0m")
  print("letter=un_official;indonesian  \033[33mCreate an unofficial Indonesian letter\033[0m")
  print("import                         \033[33mImport modules or libraries\033[0m")
  print("import.list                    \033[33mProvides the contents of the list of import commands in the Console\033[0m")
  print("prompt                         \033[33mRun os prompts\033[0m")
  print("forms-c=                       \033[33mCreate a form\033[0m")
  print("time.now                       \033[33mDisplay current time\033[0m")
  print("ccl.time.d=                    \033[33mCalculate past and future dates using days\033[0m")
  print("time.down=                     \033[33mStart countdown timer\033[0m")
  print("time.down.dhms                 \033[33mStart countdown timer with format D HH:MM:SS\033[0m")
  print("time.down.dhms.tick            \033[33mStart countdown timer with custom tick interval (D HH:MM:SS)\033[0m")
  print("time.down.tick                 \033[33mStart countdown timer with custom tick interval\033[0m")
  print("time.down$[set]=               \033[33mStart countdown timer and display start time\033[0m")
  print("time.up.dhmsf                  \033[33mRun a counter up with format D HH:MM:SS.FFF\033[0m")
  print("rdm.[0,1]                      \033[33mGenerate random numbers consisting of 0 and 1\033[0m")
  print("rdm.[n]                        \033[33mGenerate random numbers\033[0m")
  print("rdm.[custom]                   \033[33mGenerate random characters with custom options\033[0m")
  print("games=gs_th_num                \033[33mPlay Guess The Numbers!\033[0m")
  print("games=hgmn                     \033[33mPlay Hangman\033[0m")
  print("games=ro_pa_sci-bot            \033[33mPlay Rock, Paper, Scisors (bot)\033[0m")
  print("games=ti_ta_to-bot             \033[33mPlay Tic Tac Toe (bot)\033[0m")
  print("games=numpuz                   \033[33mPlay Numpuz\033[0m")
  print("games=minswe                   \033[33mPlay Mineswipper\033[0m")
  print("\nidError-Total: \033[36m49\033[0m")

cmd_inp_var_carriage_return = False

def check_internet_connection():
  try:
    socket.create_connection(("8.8.8.8", 53), timeout=1)
    return True
  except OSError:
    pass
  return False

clear_screen()

def command_logo():
  try:
    with open("logo_ascii.txt", "r") as run:
      print(run.read().replace('\\line', '\n').replace('\\clr[black]', '\033[30m').replace('\\clr[red]', '\033[31m').replace('\\clr[green]', '\033[32m').replace('\\clr[yellow]', '\033[33m').replace('\\clr[blue]', '\033[34m').replace('\\clr[magenta]', '\033[35m').replace('\\clr[cyan]', '\033[36m').replace('\\clr[white]', '\033[37m').replace('\\bgclr[black]', '\033[40m').replace('\\bgclr[red]', '\033[41m').replace('\\bgclr[green]', '\033[42m').replace('\\bgclr[yellow]', '\033[43m').replace('\\bgclr[blue]', '\033[44m').replace('\\bgclr[magenta]', '\033[45m').replace('\\bgclr[cyan]', '\033[46m').replace('\\bgclr[white]', '\033[47m').replace('\\style[bold]', '\033[1m').replace('\\style[italic]', '\033[3m').replace('\\style[strike]', '\033[9m').replace('\\r[0]', '\033[0m').replace('\\style[undline]', '\033[4m'))
    if check_internet_connection():
      print("Connection: \033[32mOnline\033[0m")
    else:
      print("Connection: \033[31mOffline\033[0m")
    print("\033[0mConsole (command: console /? or /?) (exit: exit) [BETA]\n")
  except:
    print("Cannot open '\033[36mlogo_ascii.txt\033[0m'\n\n\033[0mConsole (command: console /? or /?) (exit: exit) [BETA]\n")

def edit_command_logo():
  try:
    print("\033[33mPress enter to save. Use '\\line' to make new line. [Ctrl + C] to cancel.\033[0m\n")
    print("ANSI code:\n\ncode              clr name clr\n----              --- --------")
    print("\\r[0]                 (reset)\n\\clr[black]       \033[30m███\033[0m (black)\n\\clr[red]         \033[31m███\033[0m (red)\n\\clr[green]       \033[32m███\033[0m (green)\n\\clr[yellow]      \033[33m███\033[0m (yellow)\n\\clr[blue]        \033[34m███\033[0m (blue)\n\\clr[magenta]     \033[35m███\033[0m (magenta)\n\\clr[cyan]        \033[36m███\033[0m (cyan)\n\\clr[white]       \033[37m███\033[0m (white)\n\\bgclr[black]     \033[40mclr\033[0m (background black)\n\\bgclr[red]       \033[41mclr\033[0m (background red)\n\\bgclr[green]     \033[42mclr\033[0m (background green)\n\\bgclr[yellow]    \033[43mclr\033[0m (background yellow)\n\\bgclr[blue]      \033[44mclr\033[0m (background blue)\n\\bgclr[magenta]   \033[45mclr\033[0m (background magenta)\n\\bgclr[cyan]      \033[46mclr\033[0m (background cyan)\n\\bgclr[white]     \033[47mclr\033[0m (background white)\n\\style[bold]      \033[1msty\033[0m (style bold)\n\\style[italic]    \033[3msty\033[0m (style italic)\n\\style[strike]    \033[9msty\033[0m (style strike)\n\\style[undline]   \033[4msty\033[0m (style underline)\n")
    logo = input("ascii \033[36m>\033[0m ")
    with open("logo_ascii.txt", "w") as edit_ascii:
      edit_ascii.write(logo)
    print("\033[32mSuccessfully changed the ascii logo.\033[0m")
  except:
    print("\033[31mERROR! idError: 45\nCannot save '\033[36mascii_logo.txt\033[31m'\033[0m")

command_logo()
while True:
  try:

    cmd_inp = input("\033[33m[\033[32mconsole.py\033[33m]\033[36m > \033[0m").strip()

    if "exit" in cmd_inp.lower():
      clear_screen()
      def close_terminal():
        if os.name == 'posix':
          os.system('kill -9 $$')
        elif os.name == 'nt':
          os.system('taskkill /F /PID {}'.format(os.getpid()))
        else:
          raise OSError("\033[31mERROR! idError: 3\nError in close terminal.\033[0m")
      close_terminal()
      clear_screen()
      break
    elif "clear" in cmd_inp.lower():
      clear_screen()
      command_logo()
    elif "del.new_ln=" in cmd_inp.lower():
      if cmd_inp[11:] == "true" or cmd_inp[11:] == "True":
        cmd_inp_var_carriage_return = True
        print("Successfully changed to \033[36mTrue\033[0m")
      elif cmd_inp[11:] == "false" or cmd_inp[11:] == "False":
        cmd_inp_var_carriage_return = False
        print("Successfully changed to \033[36mFalse\033[0m")
      else:
        print(f"\033[31mERROR! idError: 42\nERROR! (\033[0m{cmd_inp[11:]}\033[31m)\nInvalid Command. enable[true or false]\033[0m")
    elif "edit.logo_ascii" in cmd_inp:
      edit_command_logo()
    elif cmd_inp:
      if "ccl=" in cmd_inp:
        expression = cmd_inp[4:]
        try:
          result = eval(expression.replace('^', '**'))
          print(f'{result:,}')
        except ZeroDivisionError:
          print(f"\033[31mERROR! idError: 4\nERROR! (\033[0m{expression}\033[31m)\nCannot divide by Zero.\033[0m")
        except:
          print(f"\033[31mERROR! idError: 5\nERROR! (\033[0m{expression}\033[31m)\nInvalid Calculate.\033[0m")

      elif "sqrt=" in cmd_inp:
        expression = cmd_inp[5:]
        try:
          result = math.sqrt(eval(expression.replace('^', '**')))
          print(f"{result}")
        except:
          print(f"\033[31mERROR! idError: 6\nERROR! (\033[0m{expression}\033[31m)\nInvalid Sqrt.\033[0m")

      elif "cbrt=" in cmd_inp:
        expression = cmd_inp[5:]
        try:
          result = math.cbrt(eval(expression.replace('^', '**')))
          print(f"{result}")
        except:
          print(f"\033[31mERROR! idError: 49\nERROR! (\033[0m{expression}\033[31m)\nInvalid Sqrt.\033[0m")

      elif "text=" in cmd_inp:
        print(cmd_inp[5:])

      elif cmd_inp == "text.typing":
        try:
          speed_typing = input("\nSPEED TYPING (#s or 'enter' to use random speed): ")
          text = input("TEXT: ").replace('\\line', '\n')
          if speed_typing.replace('.', '').isdigit():
            speed_typing = float(speed_typing)
            clear_screen()
            for char in text:
              print(char, end='', flush=True)
              time.sleep(speed_typing)
            print()
          else:
            clear_screen()
            for char in text:
              rdm = random.uniform(0.01, 0.15)
              formatted_rdm = "{:.4f}".format(rdm)
              print(char, end='', flush=True)
              time.sleep(rdm)
            print()
        except:
          print(f"\033[31mERROR! idError: 48\nERROR! (\033[0m{speed_typing}\033[31m)\nInvalid Value.\033[0m")

      elif "input=" in cmd_inp:
        input(f"{cmd_inp[6:]}")

      elif "nc=" in cmd_inp:
        print(f"Number of characters: \033[32m{len(cmd_inp[3:])}\033[0m")

      elif "dt=" in cmd_inp:
        try:
          timesdt = int(input("How much text to duplicate: "))
          resultdt = cmd_inp[3:] * timesdt
          print(resultdt)
        except:
          print(f"\033[31mERROR! idError: 7\nERROR! (\033[0m{timesdt}\033[31m)\nInvalid Input.\033[0m"); continue

      elif "bnr=" in cmd_inp:

        def translate_binary(text):
          binary_text = ' '.join(format(ord(char), '08b') for char in text)
          return binary_text

        binary_output = translate_binary(cmd_inp[4:])
        print(binary_output)

      elif "bnr_re=" in cmd_inp:
        try:
          def translate_binary_to_text(binary_text):
            binary_list = binary_text.split()
            text = ''.join(chr(int(binary, 2)) for binary in binary_list)
            return text

          text_output = translate_binary_to_text(cmd_inp[7:])
          print(text_output)
        except:
          print(f"\033[31mERROR! idError: 44\nERROR! (\033[0m{cmd_inp[7:]}\033[31m)\nInvalid Binary.\033[0m"); continue

      elif "mrs=" in cmd_inp:
        morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'}

        def translate_to_morse(text):
          morse_text = ' '.join(morse_code.get(char.upper(), '[None]') for char in text)
          return morse_text

        morse_output = translate_to_morse(cmd_inp[4:])
        print(morse_output)

      elif cmd_inp == "trm.s.get":
        ts_row = shutil.get_terminal_size().lines
        ts_col = shutil.get_terminal_size().columns
        print(f"Terminal Size:\ncol: \033[32m{ts_col}\033[0m\nrow: \033[32m{ts_row}\033[0m")

      elif cmd_inp == "text.ascii_generated":
        text = input("\nTEXT: ")
        font = input("FONT: ")
        auto = input("WIDTH ((True = auto) or number width): ")
        tw = shutil.get_terminal_size().columns
        if auto.isdigit():
          try:
            auto = int(auto)
            print("=" * tw)
            ascii_generated = pyfiglet.figlet_format(text=text, font=font, width=auto)
            print(ascii_generated)
            print("=" * tw)
          except:
            print(f"\033[31mERROR! idError: 46\nERROR! (\033[0m{font}\033[31m), (\033[0m{auto}\033[31m)\nFont not found or Terminal size column is too small.\033[0m")
        else:
          try:
            print("=" * tw)
            ascii_generated = pyfiglet.figlet_format(text=text, font=font, width=tw)
            print(ascii_generated)
            print("=" * tw)
          except:
            print(f"\033[31mERROR! idError: 47\nERROR! (\033[0m{font}\033[31m), (\033[0m{tw}\033[31m)\nFont not found or Terminal size column is too small.\033[0m")

      elif "dom.get.ip_address=" in cmd_inp:
        host_name = cmd_inp[19:]
        try:
          address = socket.gethostbyname(host_name)
          print(f"Domain Name: '\033[36m{host_name}\033[0m'\nIP Address: '\033[32m{address}\033[0m'")
        except:
          print(f"\033[31mERROR! idError: 43\nERROR! (\033[0m{host_name}\033[31m)\nInvalid Domain or no Internet connection.\033[0m")

      elif cmd_inp == "num_box_text.empty":
        clear_screen()
        print("\033[33mexit: in line box = break\nclear: in line box = clear\n\033[0m")
        num = 0
        space = "     "
        while True:
          num += 1
          space1 = space[:-len(str(num))]
          box1 = input(f"{space1}{str(num)}│")
          if box1 == "in line box = break":
            break
          elif box1 == "in line box = clear":
            clear_screen()
            num = 0

      elif cmd_inp == "box_text.empty":
        clear_screen()
        print("\033[33mexit: in line box = break\nclear: in line box = clear\n\033[0m")
        while True:
          box = input("")
          if box == "in line box = break":
            break
          elif box == "in line box = clear":
            clear_screen()

      elif "letter=" in cmd_inp:
        removeCMD = cmd_inp[7:]
        print("\033[36m\nLetter\n\033[0m")
        try:
          if "official;english" in removeCMD.lower():
            print("Measuring line for LITTER HEAD:\n               ========================================================================")
            letterhead1_inp = input("LETTER HEAD 1: ")
            letterhead2_inp = input("LETTER HEAD 2: ")
            letterfrom_inp = input("LETTER FROM: ")
            mailing_address_inp = input("MAILING ADDRESS: ")
            numberletter_inp = input("REFERENCE NUMBER: ")
            letter_attachment_inp = input("LETTER ATTACHMENT: ")
            regardingletter_inp = input("REGARDING LETTER: ")
            print("Measuring line for OPENER:\n          ========================================================================")
            opener1_s_inp = input("OPENER 1: ")
            opener2_s_inp = input("OPENER 2: ")
            opener3_s_inp = input("OPENER 3: ")
            to_s_inp = input("TO: ")
            print("Measuring line for CONTENT 1 - 9 and CLOSING:\n           ========================================================================")
            content1_s_inp = input("CONTENT 1: ")
            content2_s_inp = input("CONTENT 2: ")
            content3_s_inp = input("CONTENT 3: ")
            content4_s_inp = input("CONTENT 4: ")
            content5_s_inp = input("CONTENT 5: ")
            content6_s_inp = input("CONTENT 6: ")
            content7_s_inp = input("CONTENT 7: ")
            content8_s_inp = input("CONTENT 8: ")
            content9_s_inp = input("CONTENT 9: ")
            print("Measuring line for CONTENT 10:\n            ========================================================================")
            content10_s_inp = input("CONTENT 10: ")
            closing1_s_inp = input("CLOSING 1: ")
            closing2_s_inp = input("CLOSING 2: ")
            closing3_s_inp = input("CLOSING 3: ")
            NIP_s_inp = input("INP: ")
            line = 72
            line_letterfrom = 70
            spacesLetterhead1_inp = line - len(letterhead1_inp)
            leftspacesLetterhead1_inp = spacesLetterhead1_inp // 2
            spacesLetterhead2_inp = line - len(letterhead2_inp)
            leftspacesLetterhead2_inp = spacesLetterhead2_inp // 2
            spacesLetterfrom_inp = line_letterfrom - len(letterfrom_inp)
            leftspacesLetterfrom_inp = spacesLetterfrom_inp // 2
            spacesMailing_addres_inp = line - len(mailing_address_inp)
            leftspacesMailing_addres_inp = spacesMailing_addres_inp // 2
            print("\nletter < ?\n————————————————————————————————————————————————————————————————————————")
            print(" " * leftspacesLetterhead1_inp + letterhead1_inp)
            print(" " * leftspacesLetterhead2_inp + letterhead2_inp)
            print(" " * leftspacesLetterfrom_inp + "(" + letterfrom_inp + ")")
            print(" " * leftspacesMailing_addres_inp + mailing_address_inp)
            print("========================================================================")
            current_time_fortime = datetime.datetime.now().strftime("%A %d, %B %Y")
            current_time_fornumberletter = datetime.datetime.now().strftime("%Y")
            spacesCurrent_time_fortime = line - len(current_time_fortime)
            print(" " * spacesCurrent_time_fortime + (current_time_fortime))
            print("\nNumber    :", numberletter_inp + "/" + (current_time_fornumberletter))
            print("Attachment:", letter_attachment_inp)
            print("Regarding :", regardingletter_inp)
            print("")
            print(opener1_s_inp)
            print(opener2_s_inp)
            print(opener3_s_inp)
            print("")
            print(to_s_inp)
            print("")
            print(content1_s_inp)
            print(content2_s_inp)
            print(content3_s_inp)
            print(content4_s_inp)
            print(content5_s_inp)
            print(content6_s_inp)
            print(content7_s_inp)
            print(content8_s_inp)
            print(content9_s_inp)
            print(content10_s_inp)
            print("")
            print(closing1_s_inp)
            print(closing2_s_inp)
            print(closing3_s_inp)
            print(f"[NIP:{NIP_s_inp}]")
            print("————————————————————————————————————————————————————————————————————————\nLetter tester.")

          elif "un_official;english" in removeCMD.lower():
            writer_city_s_non_inp = input("WRITER'S CITY: ")
            from_to_s_non_inp = input("RECIPIENT'S NAME: ")
            mailing_adress_rec_non_inp = input("RECIPIENT'S MAILING ADRESS: ")
            recipient_city_s_non_inp = input("RECIPIENT'S CITY: ")
            print("Measuring line for OPENER:\n          ========================================================================")
            opener1_s_non_inp = input("OPENER 1: ")
            opener2_s_non_inp = input("OPENER 2: ")
            opener3_s_non_inp = input("OPENER 3: ")
            print("Measuring line for CONTENT 1 - 9 and CLOSING:\n           ========================================================================")
            content1_s_non_inp = input("CONTENT 1: ")
            content2_s_non_inp = input("CONTENT 2: ")
            content3_s_non_inp = input("CONTENT 3: ")
            content4_s_non_inp = input("CONTENT 4: ")
            content5_s_non_inp = input("CONTENT 5: ")
            content6_s_non_inp = input("CONTENT 6: ")
            content7_s_non_inp = input("CONTENT 7: ")
            content8_s_non_inp = input("CONTENT 8: ")
            content9_s_non_inp = input("CONTENT 9: ")
            print("Measuring line for CONTENT 10:\n            ========================================================================")
            content10_s_non_inp = input("CONTENT 10: ")
            closing1_s_non_inp = input("CLOSING 1: ")
            closing2_s_non_inp = input("CLOSING 2: ")
            closing3_s_non_inp = input("CLOSING 3: ")
            writer_name_s_non_inp = input("WRITER'S NAME: ")
            print("\nletter <?\n————————————————————————————————————————————————————————————————————————")
            current_time_fortime_non = datetime.datetime.now().strftime("%d %B %Y")
            print(writer_city_s_non_inp + ",", current_time_fortime_non)
            print("")
            print(from_to_s_non_inp)
            print(mailing_adress_rec_non_inp)
            print(recipient_city_s_non_inp)
            print("")
            print(opener1_s_non_inp)
            print(opener2_s_non_inp)
            print(opener3_s_non_inp)
            print("")
            print(content1_s_non_inp)
            print(content2_s_non_inp)
            print(content3_s_non_inp)
            print(content4_s_non_inp)
            print(content5_s_non_inp)
            print(content6_s_non_inp)
            print(content7_s_non_inp)
            print(content8_s_non_inp)
            print(content9_s_non_inp)
            print(content10_s_non_inp)
            print("")
            print(closing1_s_non_inp)
            print(closing2_s_non_inp)
            print(closing3_s_non_inp)
            print("")
            print(writer_name_s_non_inp)
            print("————————————————————————————————————————————————————————————————————————\nLetter tester.")

          elif "official;indonesian" in removeCMD.lower():
            print("Garis ukur untuk KOP SURAT:\n             ========================================================================")
            letterhead1_inp = input("KOP SURAT 1: ")
            letterhead2_inp = input("KOP SURAT 2: ")
            letterfrom_inp = input("SUMBER SURAT: ")
            mailing_address_inp = input("ALAMAT SURAT: ")
            numberletter_inp = input("NOMOR SURAT / URUTAN SURAT: ")
            letter_attachment_inp = input("LAMPIRAN SURAT: ")
            regardingletter_inp = input("PERIHAL SURAT: ")
            print("Garis ukur untuk PEMBUKA:\n           ========================================================================")
            opener1_s_inp = input("PEMBUKA 1: ")
            opener2_s_inp = input("PEMBUKA 2: ")
            opener3_s_inp = input("PEMBUKA 3: ")
            to_s_inp = input("UNTUK: ")
            print("Garis ukur untuk ISI 1 - 9:\n       ========================================================================")
            content1_s_inp = input("ISI 1: ")
            content2_s_inp = input("ISI 2: ")
            content3_s_inp = input("ISI 3: ")
            content4_s_inp = input("ISI 4: ")
            content5_s_inp = input("ISI 5: ")
            content6_s_inp = input("ISI 6: ")
            content7_s_inp = input("ISI 7: ")
            content8_s_inp = input("ISI 8: ")
            content9_s_inp = input("ISI 9: ")
            print("Garis ukur untuk ISI 10:\n        ========================================================================")
            content10_s_inp = input("ISI 10: ")
            print("Garis ukur untuk PENUTUP:\n           ========================================================================")
            closing1_s_inp = input("PENUTUP 1: ")
            closing2_s_inp = input("PENUTUP 2: ")
            closing3_s_inp = input("PENUTUP 3: ")
            NIP_s_inp = input("INP: ")
            line = 72
            line_letterfrom = 70
            spacesLetterhead1_inp = line - len(letterhead1_inp)
            leftspacesLetterhead1_inp = spacesLetterhead1_inp // 2
            spacesLetterhead2_inp = line - len(letterhead2_inp)
            leftspacesLetterhead2_inp = spacesLetterhead2_inp // 2
            spacesLetterfrom_inp = line_letterfrom - len(letterfrom_inp)
            leftspacesLetterfrom_inp = spacesLetterfrom_inp // 2
            spacesMailing_addres_inp = line - len(mailing_address_inp)
            leftspacesMailing_addres_inp = spacesMailing_addres_inp // 2
            print("\nletter < ?\n————————————————————————————————————————————————————————————————————————")
            print(" " * leftspacesLetterhead1_inp + letterhead1_inp)
            print(" " * leftspacesLetterhead2_inp + letterhead2_inp)
            print(" " * leftspacesLetterfrom_inp + "(" + letterfrom_inp + ")")
            print(" " * leftspacesMailing_addres_inp + mailing_address_inp)
            print("========================================================================")
            day_mapping = {
              'Monday': 'Senin',
              'Tuesday': 'Selasa',
              'Wednesday': 'Rabu',
              'Thursday': 'Kamis',
              'Friday': 'Jumat',
              'Saturday': 'Sabtu',
              'Sunday': 'Minggu'
            }

            month_mapping = {
              'January': 'Januari',
              'February': 'Februari',
              'March': 'Maret',
              'April': 'April',
              'May': 'Mei',
              'June': 'Juni',
              'July': 'Juli',
              'August': 'Agustus',
              'September': 'September',
              'October': 'Oktober',
              'November': 'November',
              'December': 'Desember'
            }

            current_time = datetime.datetime.now()
            day_of_week = current_time.strftime("%A")
            indonesian_day = day_mapping.get(day_of_week, day_of_week)
            month = current_time.strftime("%B")
            indonesian_month = month_mapping.get(month, month)
            current_time_formatted_A = current_time.strftime("%d,")
            current_time_formatted_B = current_time.strftime("%Y")
            output_time_in = f"{indonesian_day} {current_time_formatted_A} {indonesian_month} {current_time_formatted_B}"
            current_time_fornumberletter = datetime.datetime.now().strftime("%Y")
            spacesOutput_time_in = line - len(output_time_in)
            print(" " * spacesOutput_time_in + (output_time_in))
            print("")
            print("No.     :", numberletter_inp + "/" + (current_time_fornumberletter))
            print("Lampiran:", letter_attachment_inp)
            print("Perihal :", regardingletter_inp)
            print("")
            print(opener1_s_inp)
            print(opener2_s_inp)
            print(opener3_s_inp)
            print("")
            print(to_s_inp)
            print("")
            print(content1_s_inp)
            print(content2_s_inp)
            print(content3_s_inp)
            print(content4_s_inp)
            print(content5_s_inp)
            print(content6_s_inp)
            print(content7_s_inp)
            print(content8_s_inp)
            print(content9_s_inp)
            print(content10_s_inp)
            print("")
            print(closing1_s_inp)
            print(closing2_s_inp)
            print(closing3_s_inp)
            print(f"[NIP:{NIP_s_inp}]")
            print("————————————————————————————————————————————————————————————————————————\nLetter tester.")

          elif "un_official;indonesian" in removeCMD.lower():
            writer_city_s_non_inp = input("KOTA PENULIS / KOTA ANDA: ")
            from_to_s_non_inp = input("NAMA PENERIMA: ")
            mailing_adress_rec_non_inp = input("ALAMAT PENERIMA: ")
            recipient_city_s_non_inp = input("KOTA PENERIMA: ")
            print("Garis ukur untuk PEMBUKA:\n           ========================================================================")
            opener1_s_non_inp = input("PEMBUKA 1: ")
            opener2_s_non_inp = input("PEMBUKA 2: ")
            opener3_s_non_inp = input("PEMBUKA 3: ")
            print("Garis ukur untuk ISI 1 - 9:\n       ========================================================================")
            content1_s_non_inp = input("ISI 1: ")
            content2_s_non_inp = input("ISI 2: ")
            content3_s_non_inp = input("ISI 3: ")
            content4_s_non_inp = input("ISI 4: ")
            content5_s_non_inp = input("ISI 5: ")
            content6_s_non_inp = input("ISI 6: ")
            content7_s_non_inp = input("ISI 7: ")
            content8_s_non_inp = input("ISI 8: ")
            content9_s_non_inp = input("ISI 9: ")
            print("Garis ukur untuk ISI 10:\n        ========================================================================")
            content10_s_non_inp = input("ISI 10: ")
            print("Garis ukur untuk PENUTUP:\n           ========================================================================")
            closing1_s_non_inp = input("PENUTUP 1: ")
            closing2_s_non_inp = input("PENUTUP 2: ")
            closing3_s_non_inp = input("PENUTUP 3: ")
            writer_name_s_non_inp = input("NAMA PENULIS / NAMA ANDA: ")
            print("\nletter <?\n————————————————————————————————————————————————————————————————————————")
            day_mapping = {
              'Monday': 'Senin',
              'Tuesday': 'Selasa',
              'Wednesday': 'Rabu',
              'Thursday': 'Kamis',
              'Friday': 'Jumat',
              'Saturday': 'Sabtu',
              'Sunday': 'Minggu'
            }

            month_mapping = {
              'January': 'Januari',
              'February': 'Februari',
              'March': 'Maret',
              'April': 'April',
              'May': 'Mei',
              'June': 'Juni',
              'July': 'Juli',
              'August': 'Agustus',
              'September': 'September',
              'October': 'Oktober',
              'November': 'November',
              'December': 'Desember'
            }

            current_time = datetime.datetime.now()
            day_of_week = current_time.strftime("%A")
            indonesian_day = day_mapping.get(day_of_week, day_of_week)
            month = current_time.strftime("%B")
            indonesian_month = month_mapping.get(month, month)
            current_time_formatted_A = current_time.strftime("%d")
            current_time_formatted_B = current_time.strftime("%Y")
            output_time_in = f"{indonesian_day} {current_time_formatted_A} {indonesian_month} {current_time_formatted_B}"
            print(writer_city_s_non_inp + ",", output_time_in)
            print("")
            print(from_to_s_non_inp)
            print(mailing_adress_rec_non_inp)
            print(recipient_city_s_non_inp)
            print("")
            print(opener1_s_non_inp)
            print(opener2_s_non_inp)
            print(opener3_s_non_inp)
            print("")
            print(content1_s_non_inp)
            print(content2_s_non_inp)
            print(content3_s_non_inp)
            print(content4_s_non_inp)
            print(content5_s_non_inp)
            print(content6_s_non_inp)
            print(content7_s_non_inp)
            print(content8_s_non_inp)
            print(content9_s_non_inp)
            print(content10_s_non_inp)
            print("")
            print(closing1_s_non_inp)
            print(closing2_s_non_inp)
            print(closing3_s_non_inp)
            print("")
            print(writer_name_s_non_inp)
            print("————————————————————————————————————————————————————————————————————————\nLetter tester.")
          else:
            print(f"\033[31mERROR! idError: 8\nERROR! (\033[0m{removeCMD}\033[31m)\nCommand Not Found.\033[0m")
        except KeyboardInterrupt or EOFError:
          pass

      elif "import " in cmd_inp:
        from File.IMPORT.ascii import ascii
        from File.IMPORT.ascii import gif
        import_cmd = cmd_inp[7:]
        if import_cmd == "link-feeldreams.github.io/aboutyou":
          from File.IMPORT.link import feeldreamsGithubIoAboutyou
          feeldreamsGithubIoAboutyou.func_main()
        elif import_cmd == "link-cobabuka.htmlku.repl.co":
          from File.IMPORT.link import cobabukaHtmlkuRepl
          cobabukaHtmlkuRepl.func_main()
        elif import_cmd == "project-testkecocokanpasangan.consolePy":
          from File.IMPORT.project import testkecocokanpasanganConsolePy
          testkecocokanpasanganConsolePy.func_main()
        elif import_cmd == "project-pekerjaancocoknama.consolePy":
          from File.IMPORT.project import pekerjaancocoknamaConsolePy
          pekerjaancocoknamaConsolePy.func_main()
        elif import_cmd == "project-artisifatnama.consolePy":
          from File.IMPORT.project import artisifatnamaConsolePy
          artisifatnamaConsolePy.func_main()
        elif import_cmd == "fake-cmd.windows10":
          from File.IMPORT.fake import cmdWindows10
          cmdWindows10.func_main()
        elif import_cmd == "fake-kali.linux":
          from File.IMPORT.fake import kaliLinux
          kaliLinux.func_main()
        elif import_cmd == "fake-iMacPro.apple":
          from File.IMPORT.fake import iMacProApple
          iMacProApple.func_main()
        elif import_cmd == "ascii-windows10.logo":
          ascii.ascii_logo("windows")
        elif import_cmd == "ascii-apple.logo":
          ascii.ascii_logo("apple")
        elif import_cmd == "ascii-kalilinux.logo":
          ascii.ascii_logo("kali-linux")
        elif import_cmd == "ascii-python.logo":
          ascii.ascii_logo("python")
        elif import_cmd == "ascii-ubuntu.logo":
          ascii.ascii_logo("ubuntu")
        elif import_cmd == "ascii-android.logo":
          ascii.ascii_logo("android")
        elif import_cmd == "ascii-memerctichum.gif":
          gif.gif_animation("rcti-meme-chum")
        elif import_cmd == "ascii-rgbcolor.gif":
          gif.gif_animation("rgbfullcolor")
        elif import_cmd == "ascii-clockdigital.gif":
          gif.gif_animation("clockdigital")
        elif import_cmd == "git-camhackers.hack":
          from File.IMPORT.git.CamHackers import camhackers
          camhackers.func_main()
        elif import_cmd == "hack-ddos.hack":
          from File.IMPORT.hack import DDoSattack
          try:
            target = input("\nIP Target: ")
            fake_ip = input("Fake IP: ")
            port = int(input("PORT: "))
            many_attack = int(input("Many times attack: "))
            DDoSattack.run(many_attack, target, fake_ip, port)
          except Exception as e:
            print("Error python:")
            traceback.print_exc()
            print("\033[31mFatal Error!\033[0m")
            continue
        else:
          error_indicator = " " * 15 + ("^" * len(import_cmd))
          print(f"\033[31mERROR! idError: 10\nERROR! (\033[0m{cmd_inp}\033[31m)\n\033[35m{error_indicator}\033[31m\nNo mudule named '\033[35m{import_cmd}\033[31m'\033[0m")

      elif cmd_inp == "import":
        print(f"\033[31mERROR! idError: 11\nERROR! (\033[0m{cmd_inp}\033[31m)\nNo module to import\033[0m")

      elif cmd_inp == "import.list":
        print("Import list in Console.\n\nlink (cmd)>> link-feeldreams.github.io/aboutyou\nlink (cmd)>> link-cobabuka.htmlku.repl.co\nproject (cmd)>> project-testkecocokanpasangan.consolePy\nproject (cmd)>> project-pekerjaancocoknama.consolePy\nproject (cmd)>> project-artisifatnama.consolePy\nfake (cmd)>> fake-cmd.windows10\nfake (cmd)>> fake-kali.linux\nfake (cmd)>> fake-iMacPro.apple\nascii (cmd)>> ascii-windows10.logo\nascii (cmd)>> ascii-apple.logo\nascii (cmd)>> ascii-kalilinux.logo\nascii (cmd)>> ascii-python.logo\nascii (cmd)>> ascii-ubuntu.logo\nascii (cmd)>> ascii-android.logo\nascii (cmd)>> ascii-memerctichum.gif\nascii (cmd)>> ascii-rgbcolor.gif\nascii (cmd)>> ascii-clockdigital.gif\ngit (cmd)>> git-camhackers.hack\nhack (cmd)>> hack-ddos.hack")

      elif "forms-c=" in cmd_inp:
        try:
          choice_many = cmd_inp[8:]
          print(f"\033[36m\nForms {choice_many} coice\n\033[0m")
          title = input("TITLE FORMS: ")
          questions = []
          choices = []
          correct_answers = []
          question_number = 1
          reach_here = input("Is the next question the last question? [y/n]: ")
          while True:
            question = input(f"Question \033[36m{question_number}\033[0m: ")
            choices.append([])
            for i in range(int(choice_many)):
              choice = input(f"Choices {chr(65+i)}: ")
              choices[-1].append(choice)
            correct_answer = input("Correct answer: ")
            questions.append(question)
            correct_answers.append(correct_answer)
            if reach_here.lower() == "y":
              break
            elif reach_here.lower() == "n":
              reach_here = input("Is the next question the last question? (YES: 1, NO: 0): ")
              question_number += 1
            else:
              print(f"\033[31mERROR! idError: 12\nERROR! in input '\033[33mIs the next question the last question? [y/n]: \033[31m'\n(\033[0m{reach_here}\033[31m)\nCommand Not Found.\033[0m")
              break
          if reach_here.lower() == "y":
            clear_screen()
            score = round(100 / len(questions), 1)
            correct_count = 0
            wrong_answers = []
            tw6 = shutil.get_terminal_size().columns
            print("=" * tw6)
            spaces = tw6 - len(title)
            left_spaces = spaces // 2
            print(" " * left_spaces + ("\033[36m" + title + "\033[0m"))
            print("=" * tw6)
            for i, question in enumerate(questions, start=1):
              print(f"\n\033[36m{i}\033[0m. {question}")
              for j, choice in enumerate(choices[i-1]):
                print(f"{chr(65+j)}. {choice}")
              answer = input(f"\033[33m= \033[0m")
              if answer.upper() == correct_answers[i-1].upper():
                correct_count += 1
              else:
                wrong_answers.append((i, correct_answers[i-1]))
            print(f"Score: \033[32m{correct_count * score}\033[0m/{100}")
            if wrong_answers:
              print("Wrong answer:", ", ".join([f"{num} ({choice})" for num, choice in wrong_answers]))
        except:
          print(f"\033[31mERROR! idError: 13\nERROR! (\033[0m{cmd_inp}\033[31m)\nInvalid Value.\033[0m")

      elif cmd_inp == "time.now":
        current_time = datetime.datetime.now().strftime("%H:%M:%S %A %d, %B %Y")
        print(current_time)

      elif "ccl.time.d=" in cmd_inp:
        day = cmd_inp[11:]

        def ccl_total_days():
          datenow = datetime.datetime.now()
          timeLimit = datetime.datetime(1, 1, 1)
          totalDays = (datenow - timeLimit).days
          return totalDays

        def countTime(Number_days):
          timeLimit = datetime.datetime(1, 1, 1)
          datenow = datetime.datetime.now()
          if Number_days > (datenow - timeLimit).days:
            print(f"\033[31mNumber is too big! MAX: \033[33m{(datenow - timeLimit).days}\033[0m")
            return None, None
          cD = datenow - datetime.timedelta(days=Number_days)
          cU = datenow + datetime.timedelta(days=Number_days)
          return cD, cU

        def time_format(TimE):
          return TimE.strftime("%A, %d %B %Y")

        totalDays = ccl_total_days()
        Number_days = day

        try:
          Number_days = int(Number_days)
        except ValueError:
          print("\033[31mERROR! idError: 14\nInvalid Input.\033[0m")
          continue

        cD, cU = countTime(int(Number_days))

        if cD is not None and cU is not None:
          cD_formated = time_format(cD)
          cU_formated = time_format(cU)
          print("\033[34mFrom today ({}), Past time from {} Day:({})".format(time_format(datetime.datetime.now()), Number_days, cD_formated))
          print("\033[32mFrom today ({}), Next time from {} Day:({})".format(time_format(datetime.datetime.now()), Number_days, cU_formated) + "\033[0m")

      elif cmd_inp == "time.down.dhms":

        def countdown(days, hours, minutes, seconds):
          total_seconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
          while total_seconds > 0:
            remaining_days, seconds = divmod(total_seconds, 24 * 60 * 60)
            remaining_hours, seconds = divmod(seconds, 60 * 60)
            remaining_minutes, seconds = divmod(seconds, 60)
            countdown_str = f"{remaining_days} {remaining_hours:02d}:{remaining_minutes:02d}:{seconds:02d}"
            if cmd_inp_var_carriage_return:
              print(countdown_str, end="\r")
            else:
              print(countdown_str, end="\n")
            time.sleep(1)
            total_seconds -= 1
          print("\nTime up!")

        try:
          set_day = 0
          set_hours = 0
          set_minutes = 0
          set_seconds = 0

          day_input = input("\nSET DAY: ")
          hours_input = input("SET HOURS: ")
          if set_hours < 0 or set_hours > 23:
            print("\033[31mHours must be entered between 0 - 23\033[0m")
            continue
          minutes_input = input("SET MINUTES: ")
          if set_minutes < 0 or set_minutes > 59:
            print("\033[31mMinutes must be entered between 0 - 59\033[0m")
            continue
          seconds_input = input("SET SECONDS: ")
          if set_seconds < 0 or set_seconds > 59:
            print("\033[31mSeconds must be entered between 0 - 59\033[0m")
            continue
          set_day = int(day_input)
          set_hours = int(hours_input)
          set_minutes = int(minutes_input)
          set_seconds = int(seconds_input)
        except:
          print("\033[31mERROR! idError: 15\nInvalid Value.\033[0m")
        print(f"Countdown from \033[32m{set_day}\033[0m day, \033[32m{set_hours}\033[0m hours, \033[32m{set_minutes}\033[0m minutes, \033[32m{set_seconds}\033[0m seconds.\n")
        countdown(set_day, set_hours, set_minutes, set_seconds)

      elif cmd_inp == "time.up.dhmsf":
        def count_up():
          start_time = time.time()
          while True:
            current_time = time.time() - start_time
            days = int(current_time // (24 * 60 * 60))
            current_time %= 24 * 60 * 60
            hours = int(current_time // (60 * 60))
            current_time %= 60 * 60
            minutes = int(current_time // 60)
            current_time %= 60
            seconds = int(current_time)
            milliseconds = int((current_time - seconds) * 1000)
            if cmd_inp_var_carriage_return:
              print(f"{days} {hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d} ", end="\r")
            else:
              print(f"{days} {hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}")
            time.sleep(0.001)
        try:
          count_up()
        except KeyboardInterrupt:
          print("\nCount up stopped.")

      elif "time.down=" in cmd_inp:
        timedown_inp = cmd_inp[10:]
        if not timedown_inp.replace('.', '').isdigit():
          print(f"\033[31mERROR! idError: 16\nERROR! (\033[0m{timedown_inp}\033[31m)\nInvalid Input.\033[0m")
        else:
          try:
            countdown_time = int(float(timedown_inp))
            print("Countdown from \033[32m{}\033[0m seconds.\n".format(countdown_time))
            for i in range(countdown_time, -1, -1):
              if cmd_inp_var_carriage_return:
                print(f"{i} ", end="\r")
              else:
                print(i)
              time.sleep(1)
            print("Time up!")
          except ValueError:
            print(f"\033[31mERROR! idError: 17\nERROR! (\033[0m{timedown_inp}\033[31m)\nInvalid Input.\033[0m")

      elif cmd_inp == "time.down.dhms.tick":

        def countdown(days, hours, minutes, seconds, tick):
          total_seconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
          while total_seconds > 0:
            remaining_days, seconds = divmod(total_seconds, 24 * 60 * 60)
            remaining_hours, seconds = divmod(seconds, 60 * 60)
            remaining_minutes, seconds = divmod(seconds, 60)
            countdown_str = f"{remaining_days} {remaining_hours:02d}:{remaining_minutes:02d}:{seconds:02d}"
            if cmd_inp_var_carriage_return:
              print(f"{countdown_str} ", end="\r")
            else:
              print(countdown_str, end="\n")
            time.sleep(tick)
            total_seconds -= 1
          print("\nTime up!")

        try:
          set_day = 0
          set_hours = 0
          set_minutes = 0
          set_seconds = 0
          set_tick = 0

          day_input = input("\nSET DAY: ")
          hours_input = input("SET HOURS: ")
          if set_hours < 0 or set_hours > 23:
            print("\033[31mHours must be entered between 0 - 23\033[0m")
            continue
          minutes_input = input("SET MINUTES: ")
          if set_minutes < 0 or set_minutes > 59:
            print("\033[31mMinutes must be entered between 0 - 59\033[0m")
            continue
          seconds_input = input("SET SECONDS: ")
          if set_seconds < 0 or set_seconds > 59:
            print("\033[31mSeconds must be entered between 0 - 59\033[0m")
            continue
          tick_input = input("SET TICK: ")
          set_day = int(day_input)
          set_hours = int(hours_input)
          set_minutes = int(minutes_input)
          set_seconds = int(seconds_input)
          set_tick = float(tick_input)
        except:
          print("\033[31mERROR! idError: 18\nInvalid Value.\033[0m")

        print(f"Countdown from \033[32m{set_day}\033[0m day, \033[32m{set_hours}\033[0m hours, \033[32m{set_minutes}\033[0m minutes, \033[32m{set_seconds}\033[0m seconds.\n")
        countdown(set_day, set_hours, set_minutes, set_seconds, set_tick)

      elif cmd_inp == "time.down.tick":
        try:
          timedown_inp = input("\nSET TIME DOWN (#s): ")
          tick_inp = input("SET TICK (#s): ")
          countdown_time = int(float(timedown_inp))
          print("Countdown from \033[32m{}\033[0m seconds.\n".format(countdown_time))
          for i in range(countdown_time, -1, -1):
            if cmd_inp_var_carriage_return:
              print(f"{i} ", end="\r")
            else:
              print(i)
            time.sleep(float(tick_inp))
          print("Time up!")
        except ValueError:
          print(f"\033[31mERROR! idError: 19\nERROR! (\033[0m{timedown_inp}\033[31m)\nInvalid Value.\033[0m")

      elif "time.down$[set]=" in cmd_inp:
        try:
          timedown_e_inp = cmd_inp[16:]
          countdown_time = int(float(timedown_e_inp))
          print("Countdown from \033[32m{}\033[0m seconds.\n".format(countdown_time))
          for i in range(countdown_time, -1, -1):
            if cmd_inp_var_carriage_return:
              print(f"{i} / [ {timedown_e_inp} ] ", end="\r")
            else:
              print(f"{i} / [ {timedown_e_inp} ]")
            time.sleep(1)
          print("Time up!")
        except ValueError:
          print(f"\033[31mERROR! idError: 20\nERROR! (\033[0m{timedown_e_inp}\033[31m)\nInvalid Value.\033[0m")

      elif cmd_inp == "prompt":
        while True:
          try:
            name = socket.gethostname()
            dir = os.getcwd()
            def get_os():
              return os.name

            command_style = ""

            if __name__ == "__main__":
              os_name = get_os()
              if os_name == "posix":
                command_style = f"\033[36m┌──(\033[34mConsole-py@{name}\033[36m)-[\033[0m{dir}\033[36m]\n└─\033[32m $ \033[0m"
              elif os_name == "nt":
                command_style = f"\033[34m┌──(\033[31mConsole-py@{name}\033[34m)-[\033[0m{dir}\033[34m]\n└─\033[32m > \033[0m"
              else:
                command_style = f"{name}@( {dir} ) # "

            command = input(command_style)
            if command == "exit":
              break
            os.system(command)
          except KeyboardInterrupt:
            pass
          except EOFError:
            pass
          except:
            pass

      elif cmd_inp == "rdm.[0,1]":
        tick_inp = input("\nTICK (#s): ")
        timeout_inp = input("TIMEOUT (#s): ")
        print("")
        try:
          def generate_random_string(length):
            random_string = ''.join(random.choices(['0', '1'], k=length))
            return random_string

          def main():
            timeout = float(timeout_inp)
            start_time = time.time()
            while True:
              current_time = time.time()
              elapsed_time = current_time - start_time
              if elapsed_time >= timeout:
                break
              tw9 = shutil.get_terminal_size().columns
              random_string = generate_random_string(tw9)
              if cmd_inp_var_carriage_return:
                print(random_string, end="\r")
              else:
                print(random_string)
              time.sleep(float(tick_inp))
          if __name__ == '__main__':
            main()
        except:
          print("\033[31mERROR! idError: 21\nInvalid Value.\033[0m")

      elif cmd_inp == "rdm.[n]":
        tick_inpN = input("\nTICK (#s): ")
        timeout_inpN = input("TIMEOUT (#s): ")
        print("")
        try:

          def generate_random_string(length):
            random_string = ''.join(random.choices(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], k=length))
            return random_string

          def main():
            timeout = float(timeout_inpN)
            start_time = time.time()
            while True:
              current_time = time.time()
              elapsed_time = current_time - start_time
              if elapsed_time >= timeout:
                break
              tw10 = shutil.get_terminal_size().columns
              random_string = generate_random_string(tw10)
              if cmd_inp_var_carriage_return:
                print(random_string, end="\r")
              else:
                print(random_string)
              time.sleep(float(tick_inpN))

          if __name__ == '__main__':
            main()
        except:
          print("\033[31mERROR! idError: 22\nInvalid TICK or TIMEOUT.\033[0m")

      elif cmd_inp == "rdm.[custom]":
        tick_inp = input("\nTICK (#s): ")
        timeout_inp = input("TIMEOUT (#s): ")
        characters_inp = input("CHARACTERS: ")
        print("")
        try:

          def generate_random_string(length):
            random_string = ''.join(random.choice(characters_inp) for _ in range(length))
            return random_string

          def main():
            timeout = float(timeout_inp)
            start_time = time.time()
            while True:
              current_time = time.time()
              elapsed_time = current_time - start_time
              if elapsed_time >= timeout:
                break
              tw11 = shutil.get_terminal_size().columns
              random_string = generate_random_string(tw11)
              if cmd_inp_var_carriage_return:
                print(random_string, end="\r")
              else:
                print(random_string)
              time.sleep(float(tick_inp))

          if __name__ == '__main__':
            main()
        except:
          print("\033[31mERROR! idError: 23\nInvalid TICK or TIMEOUT.\033[0m")

      elif "games=" in cmd_inp:
        game_inp = cmd_inp[6:]
        if "gs_th_num" in game_inp.lower():
          print("\033[36m\nGuess The Numbers!\n\033[0m")
          try:
            min = int(input("Minimum number: "))
            max = int(input("Maximum number: "))
            max_tebakan = int(input("Tries: "))
          except ValueError:
            print("\033[31mERROR! idError: 24\nValue Error!\033[0m")
            continue
          except:
            print("\033[31mERROR! idError: 25\nInvalid Input.\033[0m")
            continue
          def tebak_angka():
            clear_screen()
            print("\033[36m\nGuess The Numbers!\n\033[0m")
            angka = random.randint(min, max)
            tebakan = 0
            maks_tebakan = max_tebakan
            print(f"{min} - {max}")
            print("You only have", maks_tebakan, "tries.\n")
            while tebakan < maks_tebakan:
              print("Tries", tebakan + 1)
              try:
                guess = input("Guess (!end to exit): ")
                if guess == "!end":
                  break
                guess = int(guess)
                if guess < angka:
                  print("\033[34mLow!\n\033[0m")
                elif guess > angka:
                  print("\033[31mHigh!\n\033[0m")
                else:
                  print("\033[32mCongratulations! You have guessed the correct number!\033[0m")
                  break
                tebakan += 1
              except ValueError:
                print("\033[31mERROR! idError: 26\nPlease input number only.\n\033[0m")
            if tebakan == maks_tebakan:
              print(f"\033[33mToo bad! You guessed the wrong number!\nThe correct number is \033[32m{angka}\033[0m")
          tebak_angka()

        elif "hgmn" in game_inp.lower():
          print("\n\033[36mHangman!\033[0m\n\nSelect a language / Pilih bahasa\n1. English (Inggris)\n2. Indonesia")
          language_game = input("= ")
          print("\nSelect a difficulty")
          print("1. \033[32mEasy\033[0m      (3 letters) (have 15 tries)")
          print("2. \033[34mNormal\033[0m    (4 letters) (have 10 tries)")
          print("3. \033[33mMedium\033[0m    (5 letters) (have 8 tries)")
          print("4. \033[31mHard\033[0m      (6 letters) (have 6 tries)")
          print("5. \033[35mVery hard\033[0m (7 letters) (have 5 tries)")
          difficulty_game = input("= ")[:1]
          ascii_help_eng = r"""   ____
  |/   |
  |   (_) [Please help me:(]
  |   \|/ //
  |    |
  |   / \
  |
__|__
"""
          ascii_win_eng = r"""   ____
  |/   |
  |
  |
  |   (_) [Thanks you for helping me:D]
  |   \|/ //
  |    |
__|__ / \
"""
          ascii_lose_eng = r"""   ____
  |/   |
  |   (x) [*dead]
  |   \|/ //
  |    |
  |   / \
  |
__|__
"""
          ascii_help_ind = r"""   ____
  |/   |
  |   (_) [Tolong bantu aku:(]
  |   \|/ //
  |    |
  |   / \
  |
__|__
"""
          ascii_win_ind = r"""   ____
  |/   |
  |
  |
  |   (_) [Terima kasih telah membantuku:D]
  |   \|/ //
  |    |
__|__ / \
"""
          ascii_lose_ind = r"""   ____
  |/   |
  |
  |
  |   (x) [*mati]
  |   \|/ //
  |    |
__|__ / \
"""
          words_ing3 = ['the', 'and', 'you', 'are', 'for', 'not', 'but', 'all', 'yes', 'can', 'day', 'big', 'old', 'one', 'see', 'two', 'man', 'out', 'his', 'get', 'new', 'how', 'own', 'now', 'use', 'few', 'end', 'run', 'she', 'him', 'let', 'try', 'far', 'car', 'box', 'god', 'top', 'pay', 'job', 'art', 'sun', 'law', 'bar', 'boy', 'air', 'dry', 'wet', 'key', 'arm', 'leg', 'bus', 'fly', 'pen', 'tax', 'bag', 'cat', 'dog', 'hat', 'cup', 'tea', 'bed', 'fan', 'car', 'toy', 'egg', 'map', 'day', 'gay', 'lol', 'sus', 'mop', 'let', 'for', 'cap', 'top']
          words_ing4 = ['that', 'have', 'this', 'will', 'what', 'they', 'when', 'with', 'from', 'your', 'like', 'some', 'time', 'make', 'much', 'most', 'take', 'well', 'very', 'come', 'here', 'also', 'back', 'than', 'into', 'look', 'help', 'show', 'give', 'keep', 'been', 'many', 'gear', 'find', 'part', 'life', 'only', 'down', 'want', 'high', 'over', 'tell', 'good', 'work', 'know', 'need', 'hand', 'idea', 'fact', 'best', 'room', 'plan', 'name', 'song', 'rain', 'mind', 'hurt', 'city', 'true', 'blue', 'tree', 'cold', 'swim', 'jump', 'shop', 'food', 'wine', 'park', 'bird', 'fish', 'star', 'moon', 'fire', 'baby', 'book', 'film', 'love', 'fear', 'word', 'luck', 'game', 'team', 'shoe', 'sand', 'snow', 'road', 'rule', 'hill', 'ball', 'girl', 'math']
          words_ing5 = ['about', 'after', 'again', 'along', 'among', 'angel', 'angry', 'apple', 'arrow', 'awake', 'beach', 'beard', 'begin', 'being', 'bella', 'below', 'track', 'birds', 'black', 'blend', 'knife', 'sorry', 'style', 'phone', 'click', 'tiger', 'queen', 'wrist', 'green', 'paint', 'fruit', 'horse', 'laugh', 'hello', 'world', 'mouse', 'clown', 'night', 'hotel', 'sunny', 'dance', 'watch', 'drink', 'brain', 'smile', 'brave', 'strom', 'field', 'heart', 'dirty', 'sound', 'snake', 'money', 'chair', 'wings', 'music', 'dress', 'happy', 'round', 'color', 'flame', 'shine', 'spell', 'clear', 'pilot', 'space', 'shirt', 'magic', 'water', 'truck', 'fairy', 'mouse', 'boost']
          words_ing6 = ['cookie', 'planet', 'purple', 'window', 'dragon', 'guitar', 'marvel', 'banana', 'circle', 'silver', 'hammer', 'sunset', 'jungle', 'rocket', 'spirit', 'flower', 'camera', 'candle', 'forest', 'winter', 'castle', 'pillow', 'basket', 'square', 'coffee', 'bottle', 'cheeze', 'cheery', 'circus', 'closet', 'forest', 'market', 'mother', 'rabbit', 'garden', 'spring', 'doctor', 'turtle', 'yellow', 'friend', 'candle', 'winter', 'render', 'carpet', 'delete', 'python']
          words_ing7 = ['bicycle', 'weather', 'journey', 'cheddar', 'penguin', 'library', 'weekend', 'chicken', 'blanket', 'traffic', 'thunder', 'husbend', 'whistle', 'lantern', 'freedom', 'morning', 'mustang', 'balloon', 'diamond', 'restart', 'storage', 'setting', 'upgrade', 'produce', 'preview', 'version', 'numbers', 'deleted']
          words_indo3 = ['ada', 'api', 'air', 'asa', 'bau', 'ban', 'bis', 'pir', 'hal', 'lah', 'pot', 'vas', 'dan', 'tai', 'eek', 'gas', 'kok', 'apa', 'itu', 'cor', 'jam', 'lem', 'hei', 'hai', 'pas', 'goa', 'gua', 'tol', 'gol', 'aku', 'kas', 'ini', 'jam', 'pas', 'kos', 'gas', 'roh', 'cat', 'loh', 'sah', 'kas', 'tas', 'pah', 'mah', 'nak', 'pos', 'bos', 'dua', 'aku', 'nah', 'jas', 'dia', 'kol', 'esa']
          words_indo4 = ['anda', 'halo', 'mana', 'yoyo', 'mati', 'ungu', 'buat', 'kita', 'kami', 'jaga', 'jauh', 'kalo', 'sapi', 'babi', 'bara', 'beli', 'bata', 'maka', 'coli', 'blok', 'kata', 'kuat', 'mata', 'pada', 'tisu', 'oleh', 'tali', 'baca', 'gigi', 'dada', 'lalu', 'alam', 'muka', 'muak', 'kamu', 'koin', 'uang', 'mini', 'susu', 'pala', 'kata', 'kuku', 'pata', 'kasa', 'saat', 'lama', 'suku', 'jadi', 'maha', 'cita', 'lagi', 'kera', 'paus', 'baru', 'lupa', 'lagu', 'ilmu', 'dari', 'beku', 'akan', 'beri', 'sama', 'coba', 'yang', 'lari']
          words_indo5 = ['sakit', 'ingat', 'kasar', 'rumah', 'pajak', 'kolom', 'piton', 'putus', 'kocok', 'bapak', 'nanah', 'latar', 'masih', 'hitam', 'kenal', 'bajak', 'lihat', 'hidup', 'tanah', 'hujan', 'panas', 'sinar', 'ikut', 'tebal', 'tebak', 'benda', 'badan', 'perut', 'darah', 'makan', 'lapar', 'tiada', 'jahat', 'tanah', 'kerja', 'baris', 'empat', 'tujuh', 'lahar', 'kapak', 'ketek', 'habis', 'jawab', 'harum', 'marah', 'pipis', 'tahan', 'hukum', 'paham', 'jajan', 'papah', 'mamah', 'katak', 'gagah', 'gajah', 'bibir', 'suram', 'biasa', 'sisir', 'pilih', 'cocok', 'patah', 'kasih', 'kalah', 'cinta', 'suara', 'emang', 'rindu', 'lebih', 'meski', 'remuk', 'bikin', 'tahan', 'kasar', 'tagar', 'bosan', 'tahun', 'nyata', 'licin', 'gagal', 'kurus', 'payah']
          words_indo6 = ['tinggi', 'daging', 'amanat', 'durian', 'basahi', 'senyum', 'tempat', 'cintai', 'kalahi', 'pepaya', 'malang', 'pernah', 'tangis', 'takdir', 'ketika', 'pantat', 'contoh', 'goblok', 'kuning', 'soleha', 'selera', 'banget', 'cemara', 'nangis', 'mentah', 'kamera', 'marahi', 'bodohi', 'sambut', 'menang', 'sering', 'bagian', 'kantor']
          words_indo7 = ['disebut', 'sekolah', 'kinerja', 'selamat', 'menjadi', 'mungkin', 'lengkap', 'kecuali', 'bersama', 'terjadi', 'mengapa', 'menerus', 'melihat', 'kenalan', 'berikut', 'belajar', 'akurasi', 'membawa', 'membuka', 'ikutan', 'sebelas', 'menjaga', 'memberi', 'menurut', 'sebenar', 'memilih', 'menyata', 'menilai', 'menabur', 'manusia', 'kandang']

          def hangman(words, tries, difficulty, ascii_help, ascii_win, ascii_lose, lan_difficulty, lan_you_only_have, try_it, guess_inp, nots, congra, lose):
            tries = int(tries)
            word = random.choice(words)
            guessed_letters = []
            print(f"\n{lan_difficulty}: " + difficulty)
            print(f"{lan_you_only_have} {tries} {try_it}.")
            while tries > 0:
              print("\n")
              for letter in word:
                if letter in guessed_letters:
                  print(" " + letter, end="")
                else:
                  print(" \033[31m-\033[0m", end="")
              guess = input(f"\n\n{guess_inp}: "); guess = guess.lower()
              guessed_letters.append(guess)
              if guess == "!end":
                break
              guessed_letters.append(guess)
              if guess not in word:
                tries -= 1
                print(ascii_help)
                print(nots, tries)
              if all(letter in guessed_letters for letter in word):
                print(ascii_win)
                print(congra, word)
                break
            if tries == 0:
              print(ascii_lose)
              print(lose, word)

          if language_game == "1" and difficulty_game == "1":
            hangman(words_ing3, 15, "\033[32mEasy\033[0m", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", "\033[33mThis letter is not in the word. Remaining opportunities:\033[0m", "\033[32mCongratulations! You menaged to guess the word\033[0m", "\033[31mSorry, your chance is up. The correct word is\033[0m")
          elif language_game == "1" and difficulty_game == "2":
            hangman(words_ing4, 10, "\033[34mNormal\033[0m", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", "\033[33mThis letter is not in the word. Remaining opportunities:\033[0m", "\033[32mCongratulations! You menaged to guess the word\033[0m", "\033[31mSorry, your chance is up. The correct word is\033[0m")
          elif language_game == "1" and difficulty_game == "3":
            hangman(words_ing5, 8, "\033[33mMedium\033[0m", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", "\033[33mThis letter is not in the word. Remaining opportunities:\033[0m", "\033[32mCongratulations! You menaged to guess the word\033[0m", "\033[31mSorry, your chance is up. The correct word is\033[0m")
          elif language_game == "1" and difficulty_game == "4":
            hangman(words_ing6, 6, "\033[31mHard\033[0m", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", "\033[33mThis letter is not in the word. Remaining opportunities:\033[0m", "\033[32mCongratulations! You menaged to guess the word\033[0m", "\033[31mSorry, your chance is up. The correct word is\033[0m")
          elif language_game == "1" and difficulty_game == "5":
            hangman(words_ing7, 5, "\033[35mVery hard\033[0m", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", "\033[33mThis letter is not in the word. Remaining opportunities:\033[0m", "\033[32mCongratulations! You menaged to guess the word\033[0m", "\033[31mSorry, your chance is up. The correct word is\033[0m")
          elif language_game == "2" and difficulty_game == "1":
            hangman(words_indo3, 15, "\033[32mMudah (Easy)\033[0m", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", "\033[33mHuruf ini tidak ada dalam kata. Peluang yang tersisa:\033[0m", "\033[32mSelamat! Anda berhasil menebak katanya!\033[0m", "\033[31mMaaf, kesempatan Anda habis. Kata yang benar adalah\033[0m")
          elif language_game == "2" and difficulty_game == "2":
            hangman(words_indo4, 10, "\033[34mNormal (Normal)\033[0m", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", "\033[33mHuruf ini tidak ada dalam kata. Peluang yang tersisa:\033[0m", "\033[32mSelamat! Anda berhasil menebak katanya!\033[0m", "\033[31mMaaf, kesempatan Anda habis. Kata yang benar adalah\033[0m")
          elif language_game == "2" and difficulty_game == "3":
            hangman(words_indo5, 8, "\033[33mSedang (Medium)\033[0m", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", "\033[33mHuruf ini tidak ada dalam kata. Peluang yang tersisa:\033[0m", "\033[32mSelamat! Anda berhasil menebak katanya!\033[0m", "\033[31mMaaf, kesempatan Anda habis. Kata yang benar adalah\033[0m")
          elif language_game == "2" and difficulty_game == "4":
            hangman(words_indo6, 6, "\033[31mSusah (Hard)\033[0m", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", "\033[33mHuruf ini tidak ada dalam kata. Peluang yang tersisa:\033[0m", "\033[32mSelamat! Anda berhasil menebak katanya!\033[0m", "\033[31mMaaf, kesempatan Anda habis. Kata yang benar adalah\033[0m")
          elif language_game == "2" and difficulty_game == "5":
            hangman(words_indo7, 5, "\033[35mSangat susah (Very hard)\033[0m", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", "\033[33mHuruf ini tidak ada dalam kata. Peluang yang tersisa:\033[0m", "\033[32mSelamat! Anda berhasil menebak katanya!\033[0m", "\033[31mMaaf, kesempatan Anda habis. Kata yang benar adalah\033[0m")
          else:
            print(f"\033[31mERROR! idError: 27\nERROR! (\033[0m{language_game}\033[31m), (\033[0m{difficulty_game}\033[31m)\nCommand Not Found.\033[0m")

        elif "ro_pa_sci-bot" in game_inp.lower():

          def determine_winner(player_choice, computer_choice):
            if player_choice == computer_choice:
              return 0
            elif (player_choice == 'scissors' and computer_choice == 'paper') or \
              (player_choice == 'rock' and computer_choice == 'scissors') or \
              (player_choice == 'paper' and computer_choice == 'rock'):
                return 1
            else:
              return -1

          choices = ['rock', 'scissors', 'paper']
          computer_count = 0
          player_count = 0
          series_count = 0
          played = 0

          print("\033[36m\nRock, Paper, Scissors (bot)\n\033[0m")
          while True:
            print("Select one:\n1. Rock\n2. Scissors\n3. Paper\n4. exit")
            player_choice = input("= ")[:1]
            if player_choice == "4":
              break
            if player_choice not in ['1', '2', '3']:
              print("\033[31mERROR! idError: 28\nPlease input number only.\033[0m")
              continue
            player_choice = choices[int(player_choice) - 1]
            computer_choice = random.choice(choices)
            print(f"Your choice: \033[36m{player_choice}\033[0m")
            print(f"\033[33mComputer choice: {computer_choice}\033[0m")
            result = determine_winner(player_choice, computer_choice)
            if result == 0:
              played += 1
              series_count += 1
              print(f"\033[36mSeries!\033[0m\n\nSeries: \033[36m{series_count}\033[0m | Computer: \033[33m{computer_count}\033[0m | You: \033[32m{player_count}\033[0m | Played: \033[35m{played}\033[0m\n")
            elif result == 1:
              played += 1
              player_count += 1
              print(f"\033[32mYou win!\033[0m\n\nSeries: \033[36m{series_count}\033[0m | Computer: \033[33m{computer_count}\033[0m | You: \033[32m{player_count}\033[0m | Played: \033[35m{played}\033[0m\n")
            else:
              played += 1
              computer_count += 1
              print(f"\033[33mComputer win!\033[0m\n\nSeries: \033[36m{series_count}\033[0m | Computer: \033[33m{computer_count}\033[0m | You: \033[32m{player_count}\033[0m | Played: \033[35m{played}\033[0m\n")

        elif "ti_ta_to-bot" in game_inp.lower():
          print("\033[36m\nTic Tac Toe (bot)\n\033[0m")

          def print_board(board):
            print("+---+---+---+")
            for row in board:
              print("|", end=" ")
              for cell in row:
                if cell == "X":
                  print((f"\033[31m{cell}\033[0m"), end=" | ")
                elif cell == "O":
                  print((f"\033[36m{cell}\033[0m"), end=" | ")
                else:
                  print(cell, end=" | ")
              print("\n+---+---+---+")

          def is_winner(board, player):
            for i in range(3):
              if all(cell == player for cell in board[i]):
                return True
              if all(row[i] == player for row in board):
                return True
            if board[0][0] == board[1][1] == board[2][2] == player:
              return True
            if board[0][2] == board[1][1] == board[2][0] == player:
              return True
            return False

          def is_board_full(board):
            for row in board:
              if " " in row:
                return False
            return True

          def get_human_move(board):
            while True:
              try:
                move = input("Choose coordinates (1-9) (type '!' to exit): ")[:1]
                if move == "!":
                  return None
                move = int(move)
                row = (move - 1) // 3
                col = (move - 1) % 3
                if move < 1 or move > 9 or board[row][col] != " ":
                  print("\033[31mPlease input 1-9.\033[0m")
                  continue
                return row, col
              except ValueError:
                print("\033[31mERROR! idError: 29\nPlease input number only.\033[0m")

          def get_computer_move(board):
            best_score = float("-inf")
            best_move = None
            for i in range(3):
              for j in range(3):
                if board[i][j] == " ":
                  board[i][j] = "0"
                  score = minimax(board, 0, False, float("-inf"), float("inf"))
                  board[i][j] = " "
                  if score > best_score:
                    best_score = score
                    best_move = (i, j)
            return best_move

          def minimax(board, depth, is_maximizing, alpha, beta):
            if is_winner(board, "X"):
              return -1
            elif is_winner(board, "O"):
              return 1
            elif is_board_full(board):
              return 0
            if is_maximizing:
              best_score = float("-inf")
              for i in range(3):
                for j in range(3):
                  if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                      break
              return best_score
            else:
              best_score = float("inf")
              for i in range(3):
                for j in range(3):
                  if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                      break
              return best_score

          def play_tic_tac_toe():
            board = [[" " for _ in range(3)] for _ in range(3)]
            current_player = "X"
            while True:
              print_board(board)
              if current_player == "X":
                move = get_human_move(board)
                if move is None:
                  break
                row, col = move
              else:
                print("Computer turn: (\033[36mO\033[0m)")
                row, col = get_computer_move(board)
              board[row][col] = current_player
              if is_winner(board, current_player):
                print_board(board)
                if current_player == "X":
                  print("\033[32mCongratulations! You win!\033[0m")
                else:
                  print("\033[33mComputer wins!\033[0m")
                break
              if is_board_full(board):
                print_board(board)
                print("\033[36mSeries!\033[0m")
                break
              current_player = "O" if current_player == "X" else "X"
          play_tic_tac_toe()

        elif "numpuz" in game_inp.lower():
          print("\033[36m\nNumpuz\n\033[0m")
          input_level = input("Input Level (3-10): ")
          if input_level.isdigit():
            get_inpLevel = int(input_level)
            if get_inpLevel <= 10 and get_inpLevel >= 3:

              class Numpuz:

                def __init__(self, size=get_inpLevel):
                  self.size = size
                  self.board = [[str(i + j * size + 1) for i in range(size)] for j in range(size)]
                  self.board[size - 1][size - 1] = ' '

                def shuffle_board(self, moves=100):
                  row, col = self.find_empty_space()
                  valid_moves = self.get_valid_moves(row, col)
                  for _ in range(moves):
                    random.shuffle(valid_moves)
                    move = valid_moves[0]
                    self.make_move(row, col, move)
                    row, col = self.find_empty_space()
                    valid_moves = self.get_valid_moves(row, col)

                def find_empty_space(self):
                  for i in range(self.size):
                    for j in range(self.size):
                      if self.board[i][j] == ' ':
                        return i, j

                def get_valid_moves(self, row, col):
                  valid_moves = []
                  if row > 0:
                    valid_moves.append('up')
                  if row < self.size - 1:
                    valid_moves.append('down')
                  if col > 0:
                    valid_moves.append('left')
                  if col < self.size - 1:
                    valid_moves.append('right')
                  return valid_moves

                def make_move(self, row, col, move):
                  if move == 'up':
                    self.board[row][col], self.board[row - 1][col] = self.board[row - 1][col], self.board[row][col]
                  elif move == 'down':
                    self.board[row][col], self.board[row + 1][col] = self.board[row + 1][col], self.board[row][col]
                  elif move == 'left':
                    self.board[row][col], self.board[row][col - 1] = self.board[row][col - 1], self.board[row][col]
                  elif move == 'right':
                    self.board[row][col], self.board[row][col + 1] = self.board[row][col + 1], self.board[row][col]

                def is_solved(self):
                  count = 1
                  for i in range(self.size):
                    for j in range(self.size):
                      if i == self.size - 1 and j == self.size - 1:
                        if self.board[i][j] != ' ':
                          return False
                      elif self.board[i][j] != str(count):
                        return False
                      count += 1
                  return True

                def display_board(self):
                  for i in range(self.size):
                    print('+' + '----+' * self.size)
                    for j in range(self.size):
                      print('|{:^4}'.format(self.board[i][j]), end='')
                    print('|')
                  print('+' + '----+' * self.size)

                def play(self):
                  self.shuffle_board()
                  while not self.is_solved():
                    if cmd_inp_var_carriage_return:
                      clear_screen()
                    self.display_board()
                    move = input("Enter move (wasd) (type '!' to exit): ")[:1]; move = move.lower()
                    if move == '!':
                      break
                    row, col = self.find_empty_space()
                    valid_moves = self.get_valid_moves(row, col)
                    if move not in ['w', 'a', 's', 'd']:
                      print("\033[31mERROR! idError: 30\nOnly move 'wasd'.\033[0m")
                    elif move == 'w' and 'up' in valid_moves:
                      self.make_move(row, col, 'up')
                    elif move == 's' and 'down' in valid_moves:
                      self.make_move(row, col, 'down')
                    elif move == 'a' and 'left' in valid_moves:
                      self.make_move(row, col, 'left')
                    elif move == 'd' and 'right' in valid_moves:
                      self.make_move(row, col, 'right')
                    else:
                      print("\033[31mOnly move 'wasd'.\033[0m")
                  if self.is_solved():
                    if cmd_inp_var_carriage_return:
                      clear_screen()
                    self.display_board()
                    print("\033[32mCongratulations! You solved the puzzle.\033[0m")

              if __name__ == '__main__':
                game = Numpuz()
                game.shuffle_board()
                game.play()

            else:
              if get_inpLevel <= 10:
                print("\033[33mIs to LOW! MIN level: 3, MAX level: 10\033[0m")
              if get_inpLevel >= 3:
                print("\033[33mIs to HIGH! MAX level: 10, MIN level: 3\033[0m")

          else:
            print("\033[31mERROR! idError: 31\nInvalid Input.\033[0m")

        elif "minswe" in game_inp.lower():
          print("\033[36m\nMinesweeper\n\033[0m")
          size = input("Size (6-10): ")
          bomb = input("Bomb (5-60): ")
          if size.isdigit() and bomb.isdigit():
            size = int(size)
            bomb = int(bomb)
            if size <= 8 and size >= 6 and bomb <= 30 and bomb >= 5:

              class Board:

                def __init__(self, dim_size, num_bombs):
                  self.dim_size = dim_size
                  self.num_bombs = num_bombs
                  self.board = self.make_new_board()
                  self.assign_values_to_board()
                  self.dug = set()

                def make_new_board(self):
                  board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
                  bombs_planted = 0
                  while bombs_planted < self.num_bombs:
                    loc = random.randint(0, self.dim_size**2 - 1)
                    row = loc // self.dim_size
                    col = loc % self.dim_size
                    if board[row][col] == ' \033[31m*\033[0m ':
                      continue
                    board[row][col] = ' \033[31m*\033[0m '
                    bombs_planted += 1
                  return board

                def assign_values_to_board(self):
                  for r in range(self.dim_size):
                    for c in range(self.dim_size):
                      if self.board[r][c] == ' \033[31m*\033[0m ':
                        continue
                      self.board[r][c] = self.get_num_neighboring_bombs(r, c)

                def get_num_neighboring_bombs(self, row, col):
                  num_neighboring_bombs = 0
                  for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                    for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                      if r == row and c == col:
                        continue
                      if self.board[r][c] == ' \033[31m*\033[0m ':
                        num_neighboring_bombs += 1
                  return num_neighboring_bombs

                def dig(self, row, col):
                  self.dug.add((row, col))
                  if self.board[row][col] == ' \033[31m*\033[0m ':
                    return False
                  elif self.board[row][col] > 0:
                    return True
                  for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                    for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                      if (r, c) in self.dug:
                        continue
                      self.dig(r, c)
                  return True

                def __str__(self):
                  visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
                  for row in range(self.dim_size):
                    for col in range(self.dim_size):
                      if (row, col) in self.dug:
                        visible_board[row][col] = str(self.board[row][col])
                      else:
                        visible_board[row][col] = ' '
                  string_rep = ''
                  indices_row = '   \033[36m' + ' '.join([f'{i:^3}' for i in range(self.dim_size)]) + '\033[0m\n'
                  separator_row = '--+' + '---+' * ((len(indices_row) - 12) // 4) + '\n'
                  string_rep += indices_row + separator_row
                  for i in range(len(visible_board)):
                    row = visible_board[i]
                    cells = [f'{cell:^3}' for cell in row]
                    string_rep += f'\033[36m{i}\033[0m |' + '|'.join(cells) + '|\n'
                    string_rep += separator_row
                  return string_rep

              def play(dim_size=size, num_bombs=bomb):
                board = Board(dim_size, num_bombs)
                safe = True
                while len(board.dug) < board.dim_size ** 2 - num_bombs:
                  if cmd_inp_var_carriage_return:
                    clear_screen()
                  print(board)
                  user_input = input("Choose location (row,col) (type '!' to exit): ")[:4]
                  if user_input == "!":
                    print("\033[36mBye:)\033[0m")
                    break
                  if not re.match(r'^\d+,\s*\d+$', user_input):
                    print("\033[31mERROR! idError: 32\nInvalid Input.\033[0m")
                    continue
                  row, col = map(int, user_input.split(','))
                  if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                    print("\033[31mERROR! idError: 33\nInvalid Location.\033[0m")
                    continue
                  safe = board.dig(row, col)
                  if not safe:
                    if cmd_inp_var_carriage_return:
                      clear_screen()
                    print("\033[31mBooomb!!\033[0m")
                    break
                if safe:
                  if cmd_inp_var_carriage_return:
                      clear_screen()
                  print(board)
                  print("\033[32mCongratulations! You won!\033[0m")
                else:
                  print("\033[31mSorry, You lose!\033[0m")
                  board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
                  print(board)

              if __name__ == '__main__':
                play()

            elif size <= 10 and size >= 9 and bomb <= 60 and bomb >= 5:

              class Board:

                def __init__(self, dim_size, num_bombs):
                  self.dim_size = dim_size
                  self.num_bombs = num_bombs
                  self.board = self.make_new_board()
                  self.assign_values_to_board()
                  self.dug = set()

                def make_new_board(self):
                  board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
                  bombs_planted = 0
                  while bombs_planted < self.num_bombs:
                    loc = random.randint(0, self.dim_size**2 - 1)
                    row = loc // self.dim_size
                    col = loc % self.dim_size
                    if board[row][col] == ' \033[31m*\033[0m ':
                      continue
                    board[row][col] = ' \033[31m*\033[0m '
                    bombs_planted += 1
                  return board

                def assign_values_to_board(self):
                  for r in range(self.dim_size):
                    for c in range(self.dim_size):
                      if self.board[r][c] == ' \033[31m*\033[0m ':
                        continue
                      self.board[r][c] = self.get_num_neighboring_bombs(r, c)

                def get_num_neighboring_bombs(self, row, col):
                  num_neighboring_bombs = 0
                  for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                    for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                      if r == row and c == col:
                        continue
                      if self.board[r][c] == ' \033[31m*\033[0m ':
                        num_neighboring_bombs += 1
                  return num_neighboring_bombs

                def dig(self, row, col):
                  self.dug.add((row, col))
                  if self.board[row][col] == ' \033[31m*\033[0m ':
                    return False
                  elif self.board[row][col] > 0:
                    return True
                  for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                    for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                      if (r, c) in self.dug:
                        continue
                      self.dig(r, c)
                  return True

                def __str__(self):
                  visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
                  for row in range(self.dim_size):
                    for col in range(self.dim_size):
                      if (row, col) in self.dug:
                        visible_board[row][col] = str(self.board[row][col])
                      else:
                        visible_board[row][col] = ' '
                  string_rep = ''
                  indices_row = '   \033[36m' + ' '.join([f'{i:^3}' for i in range(self.dim_size)]) + '\033[0m\n'
                  separator_row = '--+' + '---+' * ((len(indices_row) - 12) // 4) + '\n'
                  string_rep += indices_row + separator_row
                  for i in range(len(visible_board)):
                    row = visible_board[i]
                    cells = [f'{cell:^3}' for cell in row]
                    string_rep += f'\033[36m{i}\033[0m |' + '|'.join(cells) + '|\n'
                    string_rep += separator_row
                  return string_rep

              def play(dim_size=size, num_bombs=bomb):
                board = Board(dim_size, num_bombs)
                safe = True
                while len(board.dug) < board.dim_size ** 2 - num_bombs:
                  if cmd_inp_var_carriage_return:
                    clear_screen()
                  print(board)
                  user_input = input("Choose location (row,col) (type '!' to exit): ")[:4]
                  if user_input == "!":
                    print("\033[36mBye:)\033[0m")
                    break
                  if not re.match(r'^\d+,\s*\d+$', user_input):
                    print("\033[31mERROR! idError: 34\nInvalid Input.\033[0m")
                    continue
                  row, col = map(int, user_input.split(','))
                  if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                    print("\033[31mERROR! idError: 35\nInvalid Location.\033[0m")
                    continue
                  safe = board.dig(row, col)
                  if not safe:
                    if cmd_inp_var_carriage_return:
                      clear_screen()
                    print("\033[31mBooomb!!\033[0m")
                    break
                if safe:
                  if cmd_inp_var_carriage_return:
                      clear_screen()
                  print(board)
                  print("\033[32mCongratulations! You won!\033[0m")
                else:
                  print("\033[31mSorry, You lose!\033[0m")
                  board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
                  print(board)

              if __name__ == '__main__':
                play()

            else:
              print("\033[31mERROR! idError: 36\nOverFlow Size, Bomb\033[0m")
          else:
            print("\033[31mERROR! idError: 37\nInvalid Input.\033[0m")

        else:
          print(f"\033[31mERROR! idError: 38\nERROR! (\033[0m{game_inp}\033[31m)\nCommand Not Found.\033[0m")

      elif cmd_inp == "dupl.text":
        tick_inp = input("\nTICK: ")
        timeout_inp = input("TIMEOUT: ")
        text_inp = input("TEXT: ")
        print("")
        if tick_inp.replace('.', '').isdigit() and timeout_inp.replace('.', '').isdigit():
          def main():
            timeout = float(timeout_inp)
            start_time = time.time()
            while True:
              current_time = time.time()
              elapsed_time = current_time - start_time
              if elapsed_time >= timeout:
                break
              if cmd_inp_var_carriage_return:
                print(text_inp)
              else:
                print(text_inp)
              time.sleep(float(tick_inp))
          if __name__ == '__main__':
            main()
        else:
          print("\033[31mERROR! idError: 39\nInvalid TICK or TIMEOUT.\033[0m")

      elif cmd_inp == "console /?" or cmd_inp == "/?":
        consoleCommand()

      else:
        print(f"\033[31mERROR! idError: Invalid-1\nERROR! (\033[0m{cmd_inp}\033[31m)\nInvalid Command.")
  except EOFError:
    print("You just press [Ctrl + Z (\033[31mEOFError\033[0m)]")
    continue
  except KeyboardInterrupt:
    print("You just press [Ctrl + C (\033[31mKeyboardInterrupt\033[0m)]")
    continue
  except Exception as e:
    print("\033[31mERROR! idError: 40\nThe module used is invalid or an error occurred while importing the module or something error to running \033[36mconsole.py \033[31m. Please install module 'pip install {...}' if you haven't already installed it.\n\n\033[0m'\033[33mpip\033[0m install setuptools'\n'\033[33mpip\033[0m install re'\n'\033[33mpip\033[0m install pyfiglet'\n")
    print(f"Error python:\n{e}")
    con_ex = input("press enter to exit or 'c' to continue...")
    if con_ex.lower() == "c":
      continue
    else:
      exit()
  except:
    print("\033[31mERROR! idError: 41\nOops! Something Error!\033[0m")
    continue