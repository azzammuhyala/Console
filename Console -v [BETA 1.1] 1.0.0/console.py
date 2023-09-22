try:

  import math, datetime, random, time, os, re, shutil, socket, pyfiglet

except Exception as e:
  print('''\033[31mERROR! idError: 1\nThe module used is invalid or an error occurred while importing the module or something error to running \033[36mconsole.py \033[31m. Please install module 'pip install {...}' if you haven't already installed it.\n\n\033[0m'\033[33mpip\033[0m install setuptools'\n'\033[33mpip\033[0m install re'\n'\033[33mpip\033[0m install pyfiglet'\n''')
  print(f"Error Python:\n{e}"); input("press enter to exit..."); exit()
except:
  print("\033[31mERROR! idError: 2\nSomething Error...\033[0m"); exit()

def clear_screen():
  os.system('title Console' if os.name == 'nt' else 'xtitle Console')
  os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

del_new_ln_config = False
ascii_unicode_config = False
clr_black = "\033[30m"
clr_red = "\033[31m"
clr_green = "\033[32m"
clr_yellow = "\033[33m"
clr_blue = "\033[34m"
clr_magenta = "\033[35m"
clr_cyan = "\033[36m"
clr_white = "\033[37m"
clr_orange = "\033[38;5;208m"
bgclr_black = "\033[40m"
bgclr_red = "\033[41m"
bgclr_green = "\033[42m"
bgclr_yellow = "\033[43m"
bgclr_blue = "\033[44m"
bgclr_magenta = "\033[45m"
bgclr_cyan = "\033[46m"
bgclr_white = "\033[47m"
bgclr_orange = "\033[48;5;208m"
style_bold = "\033[1m"
style_italic = "\033[3m"
style_strike = "\033[9m"
style_underline = "\033[4m"
all_reset = "\033[0m"
uc_1_vertical = "\u2502"
uc_1_horizontal = "\u2500"
uc_1_UpRight = "\u250c"
uc_1_UpLeft = "\u2510"
uc_1_Plus = "\u253c"
uc_1_DownRight = "\u2514"
uc_1_DownLeft = "\u2518"
uc_1_verticalCdown = "\u252c"
uc_1_verticalCup = "\u2534"
uc_1_horizontalCright = "\u251c"
uc_1_horizontalCleft = "\u2524"

def consoleCommand():
  global clr_yellow, clr_green, clr_cyan, style_underline, all_reset
  version = f"  Version: {style_underline}{clr_green}[BETA 1.1] 1.0.0\033[0m{all_reset}  "
  tw = shutil.get_terminal_size().columns
  right_left = "=" * ((tw - 29) // 2)
  print(right_left + version + right_left)
  print(f"{clr_cyan}\nCommands in this Console\n{all_reset}")
  print(f"exit                           {clr_yellow}Terminate a program Console{all_reset}")
  print(f"clear                          {clr_yellow}Clear the entire command{all_reset}")
  print(f"edit.ascii_banner              {clr_yellow}Edit banner ascii{all_reset}")
  print(f"text.ascii_generated           {clr_yellow}Generated ascii text{all_reset}")
  print(f"del.new_ln=                    {clr_yellow}Removed special old content related to time, rdm, dupl{all_reset}")
  print(f"ccl=                           {clr_yellow}Perform basic math calculations (+ - / * ^){all_reset}")
  print(f"sqrt=                          {clr_yellow}Calculate roots{all_reset}")
  print(f"cbrt=                          {clr_yellow}Calculate roots 3{all_reset}")
  print(f"text=                          {clr_yellow}Display text{all_reset}")
  print(f"input=                         {clr_yellow}Display a prompt for user input{all_reset}")
  print(f"dt=                            {clr_yellow}Duplicate a character{all_reset}")
  print(f"len=                           {clr_yellow}Count length of characters{all_reset}")
  print(f"bnr=                           {clr_yellow}Convert words to binary code{all_reset}")
  print(f"bnr_re=                        {clr_yellow}Convert binary code to words{all_reset}")
  print(f"mrs=                           {clr_yellow}Convert words to Morse code{all_reset}")
  print(f"python.editor[1]               {clr_yellow}Create a Python system text editor{all_reset}")
  print(f"python.exec.file=              {clr_yellow}Running Python file{all_reset}")
  print(f"trm.s.get                      {clr_yellow}Get the terminal size{all_reset}")
  print(f"dom.get.ip_address=            {clr_yellow}Get an IP address from a domain{all_reset}")
  print(f"box_text.empty                 {clr_yellow}Create empty text box{all_reset}")
  print(f"num_box_text.empty             {clr_yellow}Create empty numeric text box{all_reset}")
  print(f"dupl.text                      {clr_yellow}Duplicate a text{all_reset}")
  print(f"text.typing                    {clr_yellow}Create animated text typing{all_reset}")
  print(f"text.typing.file=              {clr_yellow}Create animated text typing with file path{all_reset}")
  print(f"cat_read.file=                 {clr_yellow}Read the contents of the file{all_reset}")
  print(f"letter=official,english        {clr_yellow}Create an official English letter{all_reset}")
  print(f"letter=un_official,english     {clr_yellow}Create an unofficial English letter{all_reset}")
  print(f"letter=official,indonesian     {clr_yellow}Create an official Indonesian letter{all_reset}")
  print(f"letter=un_official,indonesian  {clr_yellow}Create an unofficial Indonesian letter{all_reset}")
  print(f"import                         {clr_yellow}Import modules or libraries{all_reset}")
  print(f"import.list                    {clr_yellow}Provides the contents of the list of import commands in the Console{all_reset}")
  print(f"prompt                         {clr_yellow}Run os prompts{all_reset}")
  print(f"edit.color.console             {clr_yellow}Change the ANSI color code type of the Console{all_reset}")
  print(f"color.check                    {clr_yellow}Checking a colors Console{all_reset}")
  print(f"forms-c=                       {clr_yellow}Create a form{all_reset}")
  print(f"time.now                       {clr_yellow}Display current time{all_reset}")
  print(f"ccl.time.d=                    {clr_yellow}Calculate past and future dates using days{all_reset}")
  print(f"ccl.time.hms=                  {clr_yellow}Calculate addition and subtraction times (HH:MM:SS){all_reset}")
  print(f"time.down=                     {clr_yellow}Start countdown timer{all_reset}")
  print(f"time.down.dhms                 {clr_yellow}Start countdown timer with format D HH:MM:SS{all_reset}")
  print(f"time.down.dhms.tick            {clr_yellow}Start countdown timer with custom tick interval (D HH:MM:SS){all_reset}")
  print(f"time.down.tick                 {clr_yellow}Start countdown timer with custom tick interval{all_reset}")
  print(f"time.down$[set]=               {clr_yellow}Start countdown timer and display start time{all_reset}")
  print(f"time.up.dhmsf                  {clr_yellow}Run a counter up with format D HH:MM:SS.FFF{all_reset}")
  print(f"rdm.[0,1]                      {clr_yellow}Generate random numbers consisting of 0 and 1{all_reset}")
  print(f"rdm.[n]                        {clr_yellow}Generate random numbers{all_reset}")
  print(f"rdm.[custom]                   {clr_yellow}Generate random characters with custom options{all_reset}")
  print(f"games=gs_th_num                {clr_yellow}Play Guess The Numbers!{all_reset}")
  print(f"games=hgmn                     {clr_yellow}Play Hangman{all_reset}")
  print(f"games=ro_pa_sci-bot            {clr_yellow}Play Rock, Paper, Scisors (bot){all_reset}")
  print(f"games=ti_ta_to-bot             {clr_yellow}Play Tic Tac Toe (bot){all_reset}")
  print(f"games=numpuz                   {clr_yellow}Play Numpuz{all_reset}")
  print(f"games=minswe                   {clr_yellow}Play Mineswipper{all_reset}")
  print(f"\nidError-Total: {clr_cyan}77{all_reset}")

def check_internet_connection():
  try:
    socket.create_connection(("8.8.8.8", 53), timeout=1)
    return True
  except OSError:
    pass
  return False

clear_screen()

def command_logo():
  global all_reset, clr_red, clr_green
  try:
    with open("banner.txt", "r") as run:
      print(run.read().replace('\\ln', '\n').replace('\\clr[black]', '\033[30m').replace('\\clr[red]', '\033[31m').replace('\\clr[green]', '\033[32m').replace('\\clr[yellow]', '\033[33m').replace('\\clr[blue]', '\033[34m').replace('\\clr[magenta]', '\033[35m').replace('\\clr[cyan]', '\033[36m').replace('\\clr[white]', '\033[37m').replace('\\clr[orange]', '\033[38;5;208m').replace('\\bgclr[black]', '\033[40m').replace('\\bgclr[red]', '\033[41m').replace('\\bgclr[green]', '\033[42m').replace('\\bgclr[yellow]', '\033[43m').replace('\\bgclr[blue]', '\033[44m').replace('\\bgclr[magenta]', '\033[45m').replace('\\bgclr[cyan]', '\033[46m').replace('\\bgclr[white]', '\033[47m').replace('\\bgclr[orange]', '\033[48;5;208m').replace('\\style[bold]', '\033[1m').replace('\\style[italic]', '\033[3m').replace('\\style[strike]', '\033[9m').replace('\\r[0]', '\033[0m').replace('\\style[undline]', '\033[4m'))
    if check_internet_connection():
      print(f"\033[0m{all_reset}Connection status: {clr_green}Online{all_reset}")
    else:
      print(f"\033[0m{all_reset}Connection status: {clr_red}Offline{all_reset}")
    print(f"{all_reset}Console (command: console /? or /? or -c) (exit: exit) [BETA]\n")
  except:
    print(f"Cannot open '{clr_cyan}banner.txt{all_reset}'\n\nConsole (command: console /? or /? or -c) (exit: exit) [BETA]\n")

def edit_command_logo():
  global clr_green, clr_cyan, all_reset
  try:
    print(f"{clr_green}Read Banner:{all_reset}")
    try:
      with open("banner.txt", "r") as read_banner:
        banner_print = read_banner.read()
        print(banner_print)
    except:
      print(f"{clr_red}File Not Found. '{clr_cyan}banner.txt{clr_red}'{all_reset}")
    print("\033[0m\033[33m\nPress enter to save. Use '\\ln' to make new line. [Ctrl + C] to cancel.\033[0m\n")
    print("ANSI code:\n\ncode              clr name clr\n----              --- --------")
    print("\\r[0]                 (reset)\n\\clr[black]       \033[30m███\033[0m (black)\n\\clr[red]         \033[31m███\033[0m (red)\n\\clr[green]       \033[32m███\033[0m (green)\n\\clr[yellow]      \033[33m███\033[0m (yellow)\n\\clr[blue]        \033[34m███\033[0m (blue)\n\\clr[magenta]     \033[35m███\033[0m (magenta)\n\\clr[cyan]        \033[36m███\033[0m (cyan)\n\\clr[white]       \033[37m███\033[0m (white)\n\\clr[orange]      \033[38;5;208m███\033[0m (orange)\n\\bgclr[black]     \033[40mclr\033[0m (background black)\n\\bgclr[red]       \033[41mclr\033[0m (background red)\n\\bgclr[green]     \033[42mclr\033[0m (background green)\n\\bgclr[yellow]    \033[43mclr\033[0m (background yellow)\n\\bgclr[blue]      \033[44mclr\033[0m (background blue)\n\\bgclr[magenta]   \033[45mclr\033[0m (background magenta)\n\\bgclr[cyan]      \033[46mclr\033[0m (background cyan)\n\\bgclr[white]     \033[47mclr\033[0m (background white)\n\\bgclr[orange]    \033[48;5;208mclr\033[0m (background orange)\n\\style[bold]      \033[1msty\033[0m (style bold)\n\\style[italic]    \033[3msty\033[0m (style italic)\n\\style[strike]    \033[9msty\033[0m (style strike)\n\\style[undline]   \033[4msty\033[0m (style underline)\n")
    logo = input(f"banner {clr_cyan}>{all_reset} ")
    with open("banner.txt", "w") as edit_ascii:
      edit_ascii.write(logo)
    print(f"{clr_green}Successfully changed the banner.{all_reset}")
  except KeyboardInterrupt:
    print(f"{clr_yellow}Edit banner has been canceled.{all_reset}")
  except EOFError:
    print(f"{clr_yellow}Edit banner has been canceled.{all_reset}")
  except Exception as e:
    print(f"{clr_red}ERROR! idError: 3\nCannot save '{clr_cyan}banner.txt{clr_red}'{all_reset}\nError Python:\n{e}")

command_logo()
while True:
  try:

    cmd_inp = input(f"\033[0m{clr_yellow}[{clr_green}console.py{clr_yellow}]{clr_cyan} > {all_reset}").strip()

    if "exit" in cmd_inp.lower():
      clear_screen()
      def close_terminal():
        if os.name == 'posix':
          os.system('kill -9 $$')
        elif os.name == 'nt':
          os.system('taskkill /F /PID {}'.format(os.getpid()))
        else:
          raise OSError(f"{clr_red}ERROR! idError: 4\nError in close terminal.{all_reset}")
      close_terminal()
      clear_screen()
      break
    elif "clear" in cmd_inp.lower():
      clear_screen()
      command_logo()
    elif "del.new_ln=" in cmd_inp.lower():
      index = cmd_inp.index("del.new_ln=") + len("del.new_ln=")
      if cmd_inp[index:].strip().lower() == "true":
        del_new_ln_config = True
        print(f"Successfully changed to {clr_cyan}True{all_reset}")
      elif cmd_inp[index:].strip().lower() == "false":
        del_new_ln_config = False
        print(f"Successfully changed to {clr_cyan}False{all_reset}")
      else:
        print(f"{clr_red}ERROR! idError: 5\nERROR! ({all_reset}{cmd_inp[index:].strip()}{clr_red})\nInvalid command. enable => [true or false]{all_reset}")
    elif "edit.ascii_banner" in cmd_inp:
      edit_command_logo()
    elif "edit.color.console " in cmd_inp:
      index = cmd_inp.index("edit.color.console ") + len("edit.color.console ")
      prompt_color = cmd_inp[index:].strip()
      if ("--clr[red]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_red = "\033[31m"
        print(f"{clr_red}Success to change color: [RED] => [RED]{all_reset}")
      elif ("--clr[red]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_red = "\033[32m"
        print(f"{clr_red}Success to change color: [RED] => [GREEN]{all_reset}")
      elif ("--clr[red]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_red = "\033[33m"
        print(f"{clr_red}Success to change color: [RED] => [YELLOW]{all_reset}")
      elif ("--clr[red]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_red = "\033[34m"
        print(f"{clr_red}Success to change color: [RED] => [BLUE]{all_reset}")
      elif ("--clr[red]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_red = "\033[35m"
        print(f"{clr_red}Success to change color: [RED] => [MAGENTA]{all_reset}")
      elif ("--clr[red]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_red = "\033[36m"
        print(f"{clr_red}Success to change color: [RED] => [CYAN]{all_reset}")
      elif ("--clr[red]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_red = "\033[37m"
        print(f"{clr_red}Success to change color: [RED] => [WHITE]{all_reset}")
      elif ("--clr[red]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        clr_red = "\033[38;5;208m"
        print(f"{clr_red}Success to change color: [RED] => [ORANGE]{all_reset}")
      elif ("--clr[green]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_green = "\033[31m"
        print(f"{clr_green}Success to change color: [GREEN] => [RED]{all_reset}")
      elif ("--clr[green]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_green = "\033[32m"
        print(f"{clr_green}Success to change color: [GREEN] => [GREEN]{all_reset}")
      elif ("--clr[green]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_green = "\033[33m"
        print(f"{clr_green}Success to change color: [GREEN] => [YELLOW]{all_reset}")
      elif ("--clr[green]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_green = "\033[34m"
        print(f"{clr_green}Success to change color: [GREEN] => [BLUE]{all_reset}")
      elif ("--clr[green]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_green = "\033[35m"
        print(f"{clr_green}Success to change color: [GREEN] => [MAGENTA]{all_reset}")
      elif ("--clr[green]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_green = "\033[36m"
        print(f"{clr_green}Success to change color: [GREEN] => [CYAN]{all_reset}")
      elif ("--clr[green]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_green = "\033[37m"
        print(f"{clr_green}Success to change color: [GREEN] => [WHITE]{all_reset}")
      elif ("--clr[green]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        clr_green = "\033[38;5;208m"
        print(f"{clr_green}Success to change color: [GREEN] => [ORANGE]{all_reset}")
      elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_yellow = "\033[31m"
        print(f"{clr_yellow}Success to change color: [YELLOW] => [RED]{all_reset}")
      elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_yellow = "\033[32m"
        print(f"{clr_yellow}Success to change color: [YELLOW] => [GREEN]{all_reset}")
      elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_yellow = "\033[33m"
        print(f"{clr_yellow}Success to change color: [YELLOW] => [YELLOW]{all_reset}")
      elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_yellow = "\033[34m"
        print(f"{clr_yellow}Success to change color: [YELLOW] => [BLUE]{all_reset}")
      elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_yellow = "\033[35m"
        print(f"{clr_yellow}Success to change color: [YELLOW] => [MAGENTA]{all_reset}")
      elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_yellow = "\033[36m"
        print(f"{clr_yellow}Success to change color: [YELLOW] => [CYAN]{all_reset}")
      elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_yellow = "\033[37m"
        print(f"{clr_yellow}Success to change color: [YELLOW] => [WHITE]{all_reset}")
      elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        clr_yellow = "\033[38;5;208m"
        print(f"{clr_yellow}Success to change color: [YELLOW] => [ORANGE]{all_reset}")
      elif ("--clr[blue]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_blue = "\033[31m"
        print(f"{clr_blue}Success to change color: [BLUE] => [RED]{all_reset}")
      elif ("--clr[blue]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_blue = "\033[32m"
        print(f"{clr_blue}Success to change color: [BLUE] => [GREEN]{all_reset}")
      elif ("--clr[blue]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_blue = "\033[33m"
        print(f"{clr_blue}Success to change color: [BLUE] => [YELLOW]{all_reset}")
      elif ("--clr[blue]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_blue = "\033[34m"
        print(f"{clr_blue}Success to change color: [BLUE] => [BLUE]{all_reset}")
      elif ("--clr[blue]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_blue = "\033[35m"
        print(f"{clr_blue}Success to change color: [BLUE] => [MAGENTA]{all_reset}")
      elif ("--clr[blue]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_blue = "\033[36m"
        print(f"{clr_blue}Success to change color: [BLUE] => [CYAN]{all_reset}")
      elif ("--clr[blue]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_blue = "\033[37m"
        print(f"{clr_blue}Success to change color: [BLUE] => [WHITE]{all_reset}")
      elif ("--clr[blue]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        clr_blue = "\033[38;5;208m"
        print(f"{clr_blue}Success to change color: [BLUE] => [ORANGE]{all_reset}")
      elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_magenta = "\033[31m"
        print(f"{clr_magenta}Success to change color: [MAGENTA] => [RED]{all_reset}")
      elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_magenta = "\033[32m"
        print(f"{clr_magenta}Success to change color: [MAGENTA] => [GREEN]{all_reset}")
      elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_magenta = "\033[33m"
        print(f"{clr_magenta}Success to change color: [MAGENTA] => [YELLOW]{all_reset}")
      elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_magenta = "\033[34m"
        print(f"{clr_magenta}Success to change color: [MAGENTA] => [BLUE]{all_reset}")
      elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_magenta = "\033[35m"
        print(f"{clr_magenta}Success to change color: [MAGENTA] => [MAGENTA]{all_reset}")
      elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_magenta = "\033[36m"
        print(f"{clr_magenta}Success to change color: [MAGENTA] => [CYAN]{all_reset}")
      elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_magenta = "\033[37m"
        print(f"{clr_magenta}Success to change color: [MAGENTA] => [WHITE]{all_reset}")
      elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        clr_magenta = "\033[38;5;208m"
        print(f"{clr_magenta}Success to change color: [MAGENTA] => [ORANGE]{all_reset}")
      elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_cyan = "\033[31m"
        print(f"{clr_cyan}Success to change color: [CYAN] => [RED]{all_reset}")
      elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_cyan = "\033[32m"
        print(f"{clr_cyan}Success to change color: [CYAN] => [GREEN]{all_reset}")
      elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_cyan = "\033[33m"
        print(f"{clr_cyan}Success to change color: [CYAN] => [YELLOW]{all_reset}")
      elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_cyan = "\033[34m"
        print(f"{clr_cyan}Success to change color: [CYAN] => [BLUE]{all_reset}")
      elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_cyan = "\033[35m"
        print(f"{clr_cyan}Success to change color: [CYAN] => [MAGENTA]{all_reset}")
      elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_cyan = "\033[36m"
        print(f"{clr_cyan}Success to change color: [CYAN] => [CYAN]{all_reset}")
      elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_cyan = "\033[37m"
        print(f"{clr_cyan}Success to change color: [CYAN] => [WHITE]{all_reset}")
      elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        clr_cyan = "\033[38;5;208m"
        print(f"{clr_cyan}Success to change color: [CYAN] => [ORANGE]{all_reset}")
      elif ("--clr[orange]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_orange = "\033[31m"
        print(f"{clr_orange}Success to change color: [ORANGE] => [RED]{all_reset}")
      elif ("--clr[orange]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_orange = "\033[32m"
        print(f"{clr_orange}Success to change color: [ORANGE] => [GREEN]{all_reset}")
      elif ("--clr[orange]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_orange = "\033[33m"
        print(f"{clr_orange}Success to change color: [ORANGE] => [YELLOW]{all_reset}")
      elif ("--clr[orange]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_orange = "\033[34m"
        print(f"{clr_orange}Success to change color: [ORANGE] => [BLUE]{all_reset}")
      elif ("--clr[orange]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_orange = "\033[35m"
        print(f"{clr_orange}Success to change color: [ORANGE] => [MAGENTA]{all_reset}")
      elif ("--clr[orange]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_orange = "\033[36m"
        print(f"{clr_orange}Success to change color: [ORANGE] => [CYAN]{all_reset}")
      elif ("--clr[orange]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_orange = "\033[37m"
        print(f"{clr_orange}Success to change color: [ORANGE] => [WHITE]{all_reset}")
      elif ("--clr[orange]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        clr_orange = "\033[38;5;208m"
        print(f"{clr_orange}Success to change color: [ORANGE] => [ORANGE]{all_reset}")
      elif ("--clr[white]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_white = "\033[31m"
        print(f"{clr_white}Success to change color: [WHITE] => [RED]{all_reset}")
      elif ("--clr[white]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_white = "\033[32m"
        print(f"{clr_white}Success to change color: [WHITE] => [GREEN]{all_reset}")
      elif ("--clr[white]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_white = "\033[33m"
        print(f"{clr_white}Success to change color: [WHITE] => [YELLOW]{all_reset}")
      elif ("--clr[white]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_white = "\033[34m"
        print(f"{clr_white}Success to change color: [WHITE] => [BLUE]{all_reset}")
      elif ("--clr[white]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_white = "\033[35m"
        print(f"{clr_white}Success to change color: [WHITE] => [MAGENTA]{all_reset}")
      elif ("--clr[white]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_white = "\033[36m"
        print(f"{clr_white}Success to change color: [WHITE] => [CYAN]{all_reset}")
      elif ("--clr[white]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_white = "\033[37m"
        print(f"{clr_white}Success to change color: [WHITE] => [WHITE]{all_reset}")
      elif ("--clr[white]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        clr_white = "\033[38;5;208m"
        print(f"{clr_white}Success to change color: [WHITE] => [ORANGE]{all_reset}")
      elif ("--clr[reset]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        all_reset = "\033[31m"
        print(f"{all_reset}Success to change color: [RESET] => [RED]{all_reset}")
      elif ("--clr[reset]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        all_reset = "\033[32m"
        print(f"{all_reset}Success to change color: [RESET] => [GREEN]{all_reset}")
      elif ("--clr[reset]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        all_reset = "\033[33m"
        print(f"{all_reset}Success to change color: [RESET] => [YELLOW]{all_reset}")
      elif ("--clr[reset]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        all_reset = "\033[34m"
        print(f"{all_reset}Success to change color: [RESET] => [BLUE]{all_reset}")
      elif ("--clr[reset]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        all_reset = "\033[35m"
        print(f"{all_reset}Success to change color: [RESET] => [MAGENTA]{all_reset}")
      elif ("--clr[reset]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        all_reset = "\033[36m"
        print(f"{all_reset}Success to change color: [RESET] => [CYAN]{all_reset}")
      elif ("--clr[reset]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        all_reset = "\033[37m"
        print(f"{all_reset}Success to change color: [RESET] => [WHITE]{all_reset}")
      elif ("--clr[reset]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
        all_reset = "\033[38;5;208m"
        print(f"{all_reset}Success to change color: [RESET] => [ORANGE]{all_reset}")
      elif ("--clr[*all]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[31m", "\033[31m", "\033[31m", "\033[31m", "\033[31m", "\033[31m", "\033[31m", "\033[31m", "\033[31m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to change colors => [RED]")
      elif ("--clr[*all]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[32m", "\033[32m", "\033[32m", "\033[32m", "\033[32m", "\033[32m", "\033[32m", "\033[32m", "\033[32m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to change colors => [GREEN]")
      elif ("--clr[*all]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[33m", "\033[33m", "\033[33m", "\033[33m", "\033[33m", "\033[33m", "\033[33m", "\033[33m", "\033[33m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to change colors => [YELLOW]")
      elif ("--clr[*all]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[34m", "\033[34m", "\033[34m", "\033[34m", "\033[34m", "\033[34m", "\033[34m", "\033[34m", "\033[34m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to change colors => [BLUE]")
      elif ("--clr[*all]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[35m", "\033[35m", "\033[35m", "\033[35m", "\033[35m", "\033[35m", "\033[35m", "\033[35m", "\033[35m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to change colors => [MAGENTA]")
      elif ("--clr[*all]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[36m", "\033[36m", "\033[36m", "\033[36m", "\033[36m", "\033[36m", "\033[36m", "\033[36m", "\033[36m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to change colors => [CYAN]")
      elif ("--clr[*all]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[37m", "\033[37m", "\033[37m", "\033[37m", "\033[37m", "\033[37m", "\033[37m", "\033[37m", "\033[37m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to change colors => [WHITE]")
      elif ("--clr[*all]" in prompt_color) and ("--nw=clr[reset]" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[0m", "\033[0m", "\033[0m", "\033[0m", "\033[0m", "\033[0m", "\033[0m", "\033[0m", "\033[0m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to change colors => [RESET]")
      elif ("--clr[*all]" in prompt_color) and ("-r" in prompt_color):
        clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, all_reset = "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m", "\033[38;5;208m", "\033[0m"
        print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE]\n{all_reset}Success to reset colors.")
      else:
        print(f"{clr_red}ERROR! idError: 6\nERROR! ({all_reset}{prompt_color}{clr_red})\nColor error or colors not found.{all_reset}\nCommand: '{clr_yellow}--clr[<name color>] --nw=[<new color>]{all_reset}'. Reset all color: '{clr_cyan}--clr[*all] -r{all_reset}'")
    elif "edit.color.console" == cmd_inp:
      print(f"{clr_red}ERROR! idError: 76\nNo colors have been edited.{all_reset}")
    elif cmd_inp:
      if "ccl=" in cmd_inp:
        index = cmd_inp.index("ccl=") + len("ccl=")
        expression = cmd_inp[index:].strip()
        try:
          result = eval(expression.replace('^', '**').replace('pi', '3.1415926535897932384626433832795').replace('e', '2.7182818284590452353602874713527'))
          print(f'{result:_}')
        except ZeroDivisionError:
          print(f"{clr_red}ERROR! idError: 7\nERROR! ({all_reset}{expression}{clr_red})\nCannot divide by zero.{all_reset}")
        except:
          print(f"{clr_red}ERROR! idError: 8\nERROR! ({all_reset}{expression}{clr_red})\nInvalid calculate.{all_reset}")

      elif "sqrt=" in cmd_inp:
        index = cmd_inp.index("sqrt=") + len("sqrt=")
        expression = cmd_inp[index:].strip()
        try:
          result = math.sqrt(eval(expression.replace('^', '**').replace('pi', '3.1415926535897932384626433832795').replace('e', '2.7182818284590452353602874713527')))
          print(f"{result:_}")
        except:
          print(f"{clr_red}ERROR! idError: 9\nERROR! ({all_reset}{expression}{clr_red})\nInvalid sqrt.{all_reset}")

      elif "cbrt=" in cmd_inp:
        index = cmd_inp.index("cbrt=") + len("cbrt=")
        expression = cmd_inp[index:].strip()
        try:
          result = math.cbrt(eval(expression.replace('^', '**').replace('pi', '3.1415926535897932384626433832795').replace('e', '2.7182818284590452353602874713527')))
          print(f"{result:_}")
        except:
          print(f"{clr_red}ERROR! idError: 10\nERROR! ({all_reset}{expression}{clr_red})\nInvalid cbrt.{all_reset}")

      elif "text=" in cmd_inp:
        index = cmd_inp.index("text=") + len("text=")
        LINEs = shutil.get_terminal_size().lines
        COLUMNs = shutil.get_terminal_size().columns
        SECONDS, MINUTES, HOURS, DATES, MOUNTS, YEARS = datetime.datetime.now().strftime("%S"), datetime.datetime.now().strftime("%M"), datetime.datetime.now().strftime("%H"), datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%m"), datetime.datetime.now().strftime("%Y")
        print(cmd_inp.replace("$LINE", f"{LINEs}").replace("$COLUMN", f"{COLUMNs}").replace('$SECONDS', f'{SECONDS}').replace('$MINUTES', f'{MINUTES}').replace('$HOURS', f'{HOURS}').replace('$DATES', f'{DATES}').replace('$MOUNTS', f'{MOUNTS}').replace('$YEARS', f'{YEARS}').replace('\\ln', '\n').replace('\\clr[black]', '\033[30m').replace('\\clr[red]', '\033[31m').replace('\\clr[green]', '\033[32m').replace('\\clr[yellow]', '\033[33m').replace('\\clr[blue]', '\033[34m').replace('\\clr[magenta]', '\033[35m').replace('\\clr[cyan]', '\033[36m').replace('\\clr[white]', '\033[37m').replace('\\clr[orange]', '\033[38;5;208m').replace('\\bgclr[black]', '\033[40m').replace('\\bgclr[red]', '\033[41m').replace('\\bgclr[green]', '\033[42m').replace('\\bgclr[yellow]', '\033[43m').replace('\\bgclr[blue]', '\033[44m').replace('\\bgclr[magenta]', '\033[45m').replace('\\bgclr[cyan]', '\033[46m').replace('\\bgclr[white]', '\033[47m').replace('\\bgclr[orange]', '\033[48;5;208m').replace('\\style[bold]', '\033[1m').replace('\\style[italic]', '\033[3m').replace('\\style[strike]', '\033[9m').replace('\\r[0]', '\033[0m').replace('\\style[undline]', '\033[4m')[index:])

      elif "color.check" == cmd_inp:
        print(f"\033[0mcolors   : {clr_black}[BLACK] \033[0m{clr_red}[RED] \033[0m{clr_green}[GREEN] \033[0m{clr_yellow}[YELLOW] \033[0m{clr_blue}[BLUE] \033[0m{clr_magenta}[MAGENTA] \033[0m{clr_cyan}[CYAN] \033[0m{clr_orange}[ORANGE]\033[0m")
        print(f"\033[0mbg colors: {bgclr_black}[BLACK]\033[0m {bgclr_red}[RED]\033[0m {bgclr_green}[GREEN]\033[0m {bgclr_yellow}[YELLOW]\033[0m {bgclr_blue}[BLUE]\033[0m {bgclr_magenta}[MAGENTA]\033[0m {bgclr_cyan}[CYAN]\033[0m {bgclr_orange}[ORANGE]\033[0m")
        print(f"\033[0mstyle    : {style_bold}[BOLD] \033[0m{style_italic}[ITALIC] \033[0m{style_strike}[STRIKE]\033[0m {style_underline}[UNDERLINE]\033[0m")

      elif cmd_inp == "text.typing":
        try:
          speed_typing = input("\nSPEED TYPING (#s or 'enter' to use random speed): ")
          text = input("TEXT: ").replace('\\ln', '\n')
          if speed_typing.replace('.', '').isdigit():
            speed_typing = float(speed_typing)
            clear_screen()
            for char in text:
              print(char, end='', flush=True)
              time.sleep(speed_typing)
            print()
          else:
            try:
              min_rdm_speed = float(input("MIN RANDOM SPEED (#s): "))
              max_rdm_speed = float(input("MAX RANDOM SPEED (#s): "))
              clear_screen()
              for char in text:
                rdm = random.uniform(min_rdm_speed, max_rdm_speed)
                formatted_rdm = "{:.4f}".format(rdm)
                print(char, end='', flush=True)
                time.sleep(rdm)
              print()
            except ValueError:
              print(f"{clr_red}ERROR! idError: 11\nERROR! ({all_reset}{min_rdm_speed}{clr_red}), ({all_reset}{max_rdm_speed}{clr_red})\nInvalid value.{all_reset}")
            except KeyboardInterrupt or EOFError:
              print(f"{clr_yellow}Typing stoped.{all_reset}")
        except ValueError:
          print(f"{clr_red}ERROR! idError: 12\nERROR! ({all_reset}{speed_typing}{clr_red})\nInvalid value.{all_reset}")
        except:
          print(f"{clr_red}ERROR! idError: 13\nInvalid input.{all_reset}"); continue

      elif "text.typing.file=" in cmd_inp:
        try:
          speed_typing = input("\nSPEED TYPING (#s or 'enter' to use random speed): ")
          index = cmd_inp.index("text.typing.file=") + len("text.typing.file=")
          text = cmd_inp[index:]
          with open(f'{text}', 'r') as text_file:
            animated_this = text_file.read()
          if speed_typing.replace('.', '').isdigit():
            speed_typing = float(speed_typing)
            clear_screen()
            for char in animated_this:
              print(char, end='', flush=True)
              time.sleep(speed_typing)
            print()
          else:
            try:
              min_rdm_speed = float(input("MIN RANDOM SPEED (#s): "))
              max_rdm_speed = float(input("MAX RANDOM SPEED (#s): "))
              clear_screen()
              for char in animated_this:
                rdm = random.uniform(min_rdm_speed, max_rdm_speed)
                formatted_rdm = "{:.4f}".format(rdm)
                print(char, end='', flush=True)
                time.sleep(rdm)
              print()
            except ValueError:
              print(f"{clr_red}ERROR! idError: 67\nERROR! ({all_reset}{min_rdm_speed}{clr_red}), ({all_reset}{max_rdm_speed}{clr_red})\nInvalid value.{all_reset}")
            except KeyboardInterrupt or EOFError:
              print(f"{clr_yellow}Typing stoped.{all_reset}")
        except ValueError:
          print(f"{clr_red}ERROR! idError: 68\nERROR! ({all_reset}{speed_typing}{clr_red})\nInvalid value.{all_reset}")
        except FileNotFoundError:
          print(f"{clr_red}ERROR! idError: 69\nERROR! ({all_reset}{text}{clr_red})\nFile or Directory not found. Please check again path file.{all_reset}")
        except:
          print(f"{clr_red}ERROR! idError: 70\nInvalid input.{all_reset}"); continue

      elif "input=" in cmd_inp:
        index = cmd_inp.index("input=") + len("input=")
        LINEs = shutil.get_terminal_size().lines
        COLUMNs = shutil.get_terminal_size().columns
        SECONDS, MINUTES, HOURS, DATES, MOUNTS, YEARS = datetime.datetime.now().strftime("%S"), datetime.datetime.now().strftime("%M"), datetime.datetime.now().strftime("%H"), datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%m"), datetime.datetime.now().strftime("%Y")
        input(cmd_inp.replace("$LINE", f"{LINEs}").replace("$COLUMN", f"{COLUMNs}").replace('$SECONDS', f'{SECONDS}').replace('$MINUTES', f'{MINUTES}').replace('$HOURS', f'{HOURS}').replace('$DATES', f'{DATES}').replace('$MOUNTS', f'{MOUNTS}').replace('$YEARS', f'{YEARS}').replace('\\ln', '\n').replace('\\clr[black]', '\033[30m').replace('\\clr[red]', '\033[31m').replace('\\clr[green]', '\033[32m').replace('\\clr[yellow]', '\033[33m').replace('\\clr[blue]', '\033[34m').replace('\\clr[magenta]', '\033[35m').replace('\\clr[cyan]', '\033[36m').replace('\\clr[white]', '\033[37m').replace('\\clr[orange]', '\033[38;5;208m').replace('\\bgclr[black]', '\033[40m').replace('\\bgclr[red]', '\033[41m').replace('\\bgclr[green]', '\033[42m').replace('\\bgclr[yellow]', '\033[43m').replace('\\bgclr[blue]', '\033[44m').replace('\\bgclr[magenta]', '\033[45m').replace('\\bgclr[cyan]', '\033[46m').replace('\\bgclr[white]', '\033[47m').replace('\\bgclr[orange]', '\033[48;5;208m').replace('\\style[bold]', '\033[1m').replace('\\style[italic]', '\033[3m').replace('\\style[strike]', '\033[9m').replace('\\r[0]', '\033[0m').replace('\\style[undline]', '\033[4m')[index:])

      elif "len=" in cmd_inp:
        index = cmd_inp.index("len=") + len("len=")
        print(f"Number of characters: {clr_green}{len(cmd_inp[index:])}{all_reset}")

      elif "dt=" in cmd_inp:
        try:
          timesdt = int(input("How much text to duplicate: "))
          index = cmd_inp.index("dt=") + len("dt=")
          resultdt = cmd_inp[index:] * timesdt
          print(resultdt)
        except:
          print(f"{clr_red}ERROR! idError: 14\nERROR! ({all_reset}{timesdt}{clr_red})\nInvalid input.{all_reset}"); continue

      elif "bnr=" in cmd_inp:
        index = cmd_inp.index("bnr=") + len("bnr=")

        def translate_binary(text):
          binary_text = ' '.join(format(ord(char), '08b') for char in text)
          return binary_text

        binary_output = translate_binary(cmd_inp[index:])
        print(binary_output)

      elif "bnr_re=" in cmd_inp:
        try:
          index = cmd_inp.index("bnr_re=") + len("bnr_re=")

          def translate_binary_to_text(binary_text):
            binary_list = binary_text.split()
            text = ''.join(chr(int(binary, 2)) for binary in binary_list)
            return text

          text_output = translate_binary_to_text(cmd_inp[index:])
          print(text_output)
        except:
          print(f"{clr_red}ERROR! idError: 15\nERROR! ({all_reset}{cmd_inp[index:]}{clr_red})\nInvalid binary.{all_reset}"); continue

      elif "mrs=" in cmd_inp:
        index = cmd_inp.index("mrs=") + len("mrs=")
        morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'}

        def translate_to_morse(text):
          morse_text = ' '.join(morse_code.get(char.upper(), '[None]') for char in text)
          return morse_text

        morse_output = translate_to_morse(cmd_inp[index:])
        print(morse_output)

      elif cmd_inp == "python.editor[1]":
        while True:
          try:
            text_py = input(f"{clr_green}>>> {all_reset}").replace("\\ln", "\n").replace('exit()', 'pass').replace("os.system('kill -9 $$')", 'pass').replace("os.system('taskkill /F /PID {}'.format(os.getpid()))", 'pass').replace('os.system("kill -9 $$"")', 'pass').replace('os.system("taskkill /F /PID {}".format(os.getpid()))', 'pass')
            if text_py == "console.python(exit)":
              break
            elif text_py == "console.python(clr)":
              clear_screen()
            else:
              exec(text_py)
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 16\nError Python dettected! {clr_green}('console.python(exit)' to exit.){all_reset}\n{e}")

      elif cmd_inp == "trm.s.get":
        ts_row = shutil.get_terminal_size().lines
        ts_col = shutil.get_terminal_size().columns
        print(f"Terminal Size:\ncol: {clr_green}{ts_col}{all_reset}\nrow: {clr_green}{ts_row}{all_reset}")

      elif cmd_inp == "text.ascii_generated":
        text = input("\nTEXT: ")
        font = input("FONT: ")
        auto = input("WIDTH: ")
        tw = shutil.get_terminal_size().columns
        if auto.isdigit():
          try:
            auto = int(auto)
            print("=" * tw)
            ascii_generated = pyfiglet.figlet_format(text=text, font=font, width=auto)
            print(ascii_generated)
            print("=" * tw)
          except pyfiglet.FontNotFound:
            print(f"{clr_red}ERROR! idError: 17\nERROR! ({all_reset}{font}{clr_red})\nFont not found.{all_reset}"); continue
          except pyfiglet.CharNotPrinted:
            print(f"{clr_red}ERROR! idError: 71\nERROR! ({all_reset}{auto}{clr_red})\nCharNotPrinted. Width size is too small.{all_reset}"); continue
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 72\nAn unexpected Error occurred.\n{all_reset}Error Python:\n{e}"); continue
        else:
          try:
            print("=" * tw)
            ascii_generated = pyfiglet.figlet_format(text=text, font=font, width=tw)
            print(ascii_generated)
            print("=" * tw)
          except pyfiglet.FontNotFound:
            print(f"{clr_red}ERROR! idError: 18\nERROR! ({all_reset}{font}{clr_red})\nFont not found.{all_reset}"); continue
          except pyfiglet.CharNotPrinted:
            print(f"{clr_red}ERROR! idError: 73\nERROR! ({all_reset}{tw}{clr_red})\nCharNotPrinted. Width size is too small.{all_reset}"); continue
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 74\nAn unexpected Error occurred.\n{all_reset}Error Python:\n{e}"); continue

      elif "dom.get.ip_address=" in cmd_inp:
        index = cmd_inp.index("dom.get.ip_address=") + len("dom.get.ip_address=")
        host_name = cmd_inp[index:].strip()
        try:
          address = socket.gethostbyname(host_name)
          print(f"Domain Name: '{clr_cyan}{host_name}{all_reset}'\nIP Address: '{clr_green}{address}{all_reset}'")
        except:
          print(f"{clr_red}ERROR! idError: 19\nERROR! ({all_reset}{host_name}{clr_red})\nInvalid domain or no internet connection.{all_reset}")

      elif "python.exec.file=" in cmd_inp:
        dir_file = cmd_inp[17:]
        try:
          with open(f"{dir_file}", "r", encoding="utf8") as exec_file:
            py_file = exec_file.read().replace('exit()', 'pass').replace("os.system('kill -9 $$')", 'pass').replace("os.system('taskkill /F /PID {}'.format(os.getpid()))", 'pass').replace('os.system("kill -9 $$")', 'pass').replace('os.system("taskkill /F /PID {}".format(os.getpid()))', 'pass')
            exec(py_file)
          print(f"exit()\n{clr_yellow}Python program '{clr_green}{dir_file}{clr_yellow}' Finished.")
          continue
        except FileNotFoundError:
          print(f"{clr_red}ERROR! idError: 20\nERROR! ({all_reset}{dir_file}{clr_red})\nFile or Directory is not Found. Please check your location path file.{all_reset}")
        except Exception as e:
          print(f"{clr_red}ERROR! idError: 21\nERROR! ({all_reset}{dir_file}{clr_red})\nAn unknown Error occurred while trying to locate the specified file or a Python Error occurred in the target file.{all_reset}\n{e}")

      elif "cat_read.file=" in cmd_inp:
        dir_file_cat = cmd_inp[14:]
        try:
          with open(f'{dir_file_cat}', 'r', encoding="utf8") as cat_file:
            file = cat_file.read()
            print(file)
          print(f"{clr_green}READ FILE: '{clr_cyan}{dir_file_cat}{clr_green}'{all_reset}")
        except FileNotFoundError:
          print(f"{clr_red}ERROR! idError: 22\nERROR! ({all_reset}{dir_file_cat}{clr_red})\nFile or Directory is not Found. Please check your location path file.{all_reset}")
        except Exception as e:
          print(f"{clr_red}ERROR! idError: 23\nERROR! ({all_reset}{dir_file_cat}{clr_red})\nAn unknown Error occurred while trying to locate the specified file.{all_reset}\nError Python:\n{e}")

      elif cmd_inp == "num_box_text.empty":
        clear_screen()
        print(f"{clr_yellow}exit: in line box = break\nclear: in line box = clear\n{all_reset}")
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
        print(f"{clr_yellow}exit: in line box = break\nclear: in line box = clear\n{all_reset}")
        while True:
          box = input("")
          if box == "in line box = break":
            break
          elif box == "in line box = clear":
            clear_screen()

      elif "letter=" in cmd_inp:
        index = cmd_inp.index("letter=") + len("letter=")
        removeCMD = cmd_inp[index:].strip()
        try:
          letter_type, language_type = map(str, removeCMD.split(','))
          print(f"{clr_cyan}\nLetter\n{all_reset}")
          if ("official" in letter_type) and ("english" in language_type):
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

          elif ("un_official" in letter_type) and ("english" in language_type):
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

          elif ("official" in letter_type) and ("indonesian" in language_type):
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

          elif ("un_official" in letter_type) and ("indonesian" in language_type):
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
            print(f"{clr_red}ERROR! idError: 24\nERROR! ({all_reset}{removeCMD}{clr_red})\nCommand not found.{all_reset}")
        except ValueError:
          print(f"{clr_red}ERROR! idError: 75\nERROR ({all_reset}{removeCMD}{clr_red})\nThe value entered is more or less than the command (requires 2 values).{all_reset}")
        except KeyboardInterrupt or EOFError:
          print()

      elif "import " in cmd_inp:
        try:
          def run_file_import(dir_maps):
            global clr_yellow, clr_red, all_reset
            with open(f'{dir_maps}', 'r', encoding="utf8") as programFile:
              main = programFile.read()
              try:
                exec(main)
              except KeyboardInterrupt or EOFError:
                print(f"{clr_yellow}\nYou just terminated the program.{all_reset}")
              except Exception as e:
                print(f"{clr_red}ERROR! idError: 25\nGot ERROR. Program terminated.{all_reset}\nERROR:\n{e}")
          from File.IMPORT.ascii import ascii
          from File.IMPORT.ascii import gif
          index = cmd_inp.index("import ") + len("import ")
          import_cmd = cmd_inp[index:].strip()
          if import_cmd == "link-feeldreams.github.io/aboutyou":
            run_file_import('File/IMPORT/link/feeldreamsGithubIoAboutyou.py')
          elif import_cmd == "link-cobabuka.htmlku.repl.co":
            run_file_import('File/IMPORT/link/cobabukaHtmlkuRepl.py')
          elif import_cmd == "project-testkecocokanpasangan.consolePy":
            run_file_import('File/IMPORT/project/testkecocokanpasanganConsolePy.py')
          elif import_cmd == "project-pekerjaancocoknama.consolePy":
            run_file_import('File/IMPORT/project/pekerjaancocoknamaConsolePy')
          elif import_cmd == "project-artisifatnama.consolePy":
            run_file_import('File/IMPORT/project/artisifatnamaConsolePy.py')
          elif import_cmd == "fake-cmd.windows10":
            run_file_import('File/IMPORT/fake/cmdWindows10.py')
          elif import_cmd == "fake-kali.linux":
            run_file_import('File/IMPORT/fake/kaliLinux.py')
          elif import_cmd == "fake-iMacPro.apple":
            run_file_import('File/IMPORT/fake/iMacProApple.py')
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
            run_file_import('File/IMPORT/git/CamHackers/camhackers.py')
          elif import_cmd == "hack-ddos.hack":
            from File.IMPORT.hack import DDoSattack
            try:
              target = input("\nIP Target: ")
              fake_ip = input("Fake IP: ")
              port = int(input("PORT: "))
              many_attack = int(input("Many times attack: "))
              DDoSattack.run(many_attack, target, fake_ip, port)
            except Exception as e:
              print(f"Error Python:\n{e}")
              print(f"{clr_red}Fatal Error!{all_reset}")
              continue
          elif import_cmd == "games-classicsnake.game":
            if os.name == 'posix':
              from File.IMPORT.games.ClassicSnake import forLinux
              forLinux.main()
            else:
              from File.IMPORT.games.ClassicSnake import forWindows
              forWindows.main()
          else:
            print(f"{clr_red}ERROR! idError: 26\nERROR! ({all_reset}{cmd_inp}{clr_red})\nNo mudule named '{clr_magenta}{import_cmd}{clr_red}'{all_reset}")
        except ModuleNotFoundError:
          print(f"{clr_red}ERROR! idError: 27\nERROR! ({all_reset}{import_cmd}{clr_red})\nImported module or Python Directory or File not found. Please do not edit Console files or directories!\n{clr_yellow}If you find this error delete this old Console file. Then reinstall the latest Console file!{all_reset}")
        except KeyboardInterrupt:
          print(" [KeyboardInterrupt] ")
        except EOFError:
          print(" [EOFError] ")
        except Exception as e:
          print(f"{clr_red}ERROR! idError: 28\nERROR! ({all_reset}{import_cmd}{clr_red})\nAn unexpected Error Occurred! Please do not change any of the 'IMPORT' directories or files in the Console.{all_reset}\nError Python:\n{e}")

      elif cmd_inp == "import":
        print(f"{clr_red}ERROR! idError: 29\nNo module to import.{all_reset}")

      elif cmd_inp == "import.list":
        print("Import list in Console.\n\nlink (cmd)>> link-feeldreams.github.io/aboutyou\nlink (cmd)>> link-cobabuka.htmlku.repl.co\nproject (cmd)>> project-testkecocokanpasangan.consolePy\nproject (cmd)>> project-pekerjaancocoknama.consolePy\nproject (cmd)>> project-artisifatnama.consolePy\nfake (cmd)>> fake-cmd.windows10\nfake (cmd)>> fake-kali.linux\nfake (cmd)>> fake-iMacPro.apple\nascii (cmd)>> ascii-windows10.logo\nascii (cmd)>> ascii-apple.logo\nascii (cmd)>> ascii-kalilinux.logo\nascii (cmd)>> ascii-python.logo\nascii (cmd)>> ascii-ubuntu.logo\nascii (cmd)>> ascii-android.logo\nascii (cmd)>> ascii-memerctichum.gif\nascii (cmd)>> ascii-rgbcolor.gif\nascii (cmd)>> ascii-clockdigital.gif\ngit (cmd)>> git-camhackers.hack\nhack (cmd)>> hack-ddos.hack\ngames (cmd)>> games-classicsnake.game")

      elif "forms-c=" in cmd_inp:
        try:
          index = cmd_inp.index("forms-c=") + len("forms-c=")
          choice_many = cmd_inp[index:].strip()
          print(f"{clr_cyan}\nForms {choice_many} coice\n{all_reset}")
          title = input("TITLE FORMS: ")
          questions = []
          choices = []
          correct_answers = []
          question_number = 1
          reach_here = input("Is the next question the last question? [y/n]: ")
          while True:
            question = input(f"Question {clr_cyan}{question_number}{all_reset}: ")
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
              print(f"{clr_red}ERROR! idError: 30\nERROR! in input '{clr_yellow}Is the next question the last question? [y/n]: {clr_red}'\n({all_reset}{reach_here}{clr_red})\nCommand not found.{all_reset}")
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
            print(" " * left_spaces + (f"{clr_cyan}{title}{all_reset}"))
            print("=" * tw6)
            for i, question in enumerate(questions, start=1):
              print(f"\n{clr_cyan}{i}{all_reset}. {question}")
              for j, choice in enumerate(choices[i-1]):
                print(f"{chr(65+j)}. {choice}")
              answer = input(f"{clr_yellow}= {all_reset}")
              if answer.upper() == correct_answers[i-1].upper():
                correct_count += 1
              else:
                wrong_answers.append((i, correct_answers[i-1]))
            print(f"Score: {clr_green}{correct_count * score}{all_reset}/{100}")
            if wrong_answers:
              print("Wrong answer:", ", ".join([f"{num} ({choice})" for num, choice in wrong_answers]))
        except ValueError:
          print(f"{clr_red}ERROR! idError: 31\nERROR! ({all_reset}{cmd_inp}{clr_red})\nInvalid value.{all_reset}")
        except:
          print(f"{clr_red}ERROR! idError: 32\nERROR! ({all_reset}{cmd_inp}{clr_red})\nInvalid input.{all_reset}")

      elif cmd_inp == "time.now":
        current_time = datetime.datetime.now().strftime("%H:%M:%S %A %d, %B %Y")
        print(current_time)

      elif "ccl.time.d=" in cmd_inp:
        index = cmd_inp.index("ccl.time.d=") + len("ccl.time.d=")
        day = cmd_inp[index:].strip()

        def ccl_total_days():
          datenow = datetime.datetime.now()
          timeLimit = datetime.datetime(1, 1, 1)
          totalDays = (datenow - timeLimit).days
          return totalDays

        def countTime(Number_days):
          timeLimit = datetime.datetime(1, 1, 1)
          datenow = datetime.datetime.now()
          if Number_days > (datenow - timeLimit).days:
            print(f"{clr_red}Number is too big! MAX: {clr_yellow}{(datenow - timeLimit).days}{all_reset}")
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
          print(f"{clr_red}ERROR! idError: 33\nInvalid input.{all_reset}")
          continue

        cD, cU = countTime(int(Number_days))

        if cD is not None and cU is not None:
          cD_formated = time_format(cD)
          cU_formated = time_format(cU)
          print(f"{clr_blue}" + "From today ({}), Past time from {} Day: ({})".format(time_format(datetime.datetime.now()), Number_days, cD_formated))
          print(f"{clr_green}" + "From today ({}), Next time from {} Day: ({})".format(time_format(datetime.datetime.now()), Number_days, cU_formated) + f"{all_reset}")

      elif "ccl.time.hms=" in cmd_inp:
        index = cmd_inp.index("ccl.time.hms=") + len("ccl.time.hms=")
        SECONDS, MINUTES, HOURS, DATES, MOUNTS, YEARS = datetime.datetime.now().strftime("%S"), datetime.datetime.now().strftime("%M"), datetime.datetime.now().strftime("%H"), datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%m"), datetime.datetime.now().strftime("%Y")
        data_time_hms = cmd_inp.replace('$SECONDS', f'{SECONDS}').replace('$MINUTES', f'{MINUTES}').replace('$HOURS', f'{HOURS}').replace('$DATES', f'{DATES}').replace('$MOUNTS', f'{MOUNTS}').replace('$YEARS', f'{YEARS}')[index:].strip()
        try:
          time1, time2 = map(str, data_time_hms.split(','))
          def waktu_ke_detik(waktu):
            hh, mm, ss = map(int, waktu.split(':'))
            total_detik = (hh * 3600) + (mm * 60) + ss
            return total_detik
  
          def detik_ke_waktu(detik):
            jam = detik // 3600
            sisa_detik = detik % 3600
            menit = sisa_detik // 60
            detik = sisa_detik % 60
            return f"{jam:02d}:{menit:02d}:{detik:02d}"
      
          def tambah_waktu(waktu1, waktu2):
            detik_waktu1 = waktu_ke_detik(waktu1)
            detik_waktu2 = waktu_ke_detik(waktu2)
            total_detik = detik_waktu1 + detik_waktu2
            return detik_ke_waktu(total_detik)
      
          def kurang_waktu(waktu1, waktu2):
            detik_waktu1 = waktu_ke_detik(waktu1)
            detik_waktu2 = waktu_ke_detik(waktu2)
            selisih_detik = detik_waktu1 - detik_waktu2
            return detik_ke_waktu(abs(selisih_detik))
      
          hasil_tambah = tambah_waktu(time1, time2)
          hasil_kurang = kurang_waktu(time1, time2)
      
          print(f"Time ({clr_green}+{all_reset}): {clr_orange}{time1.strip()}{all_reset} + {clr_cyan}{time2.strip()}{all_reset} = {clr_green}{hasil_tambah}{all_reset}")
          print(f"Time ({clr_red}-{all_reset}): {clr_orange}{time1.strip()}{all_reset} - {clr_cyan}{time2.strip()}{all_reset} = {clr_green}{hasil_kurang}{all_reset}")
        except ValueError:
          print(f"{clr_red}ERROR! idError: 77\nERROR! ({all_reset}{data_time_hms}{clr_red})\nAn unexpected Error occurred. Maybe (value or in : or ,){all_reset}")

      elif cmd_inp == "time.down.dhms":

        def countdown(days, hours, minutes, seconds):
          total_seconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
          while total_seconds > 0:
            remaining_days, seconds = divmod(total_seconds, 24 * 60 * 60)
            remaining_hours, seconds = divmod(seconds, 60 * 60)
            remaining_minutes, seconds = divmod(seconds, 60)
            countdown_str = f"{remaining_days} {remaining_hours:02d}:{remaining_minutes:02d}:{seconds:02d}"
            if del_new_ln_config:
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
            print(f"{clr_red}Hours must be entered between 0 - 23{all_reset}")
            continue
          minutes_input = input("SET MINUTES: ")
          if set_minutes < 0 or set_minutes > 59:
            print(f"{clr_red}Minutes must be entered between 0 - 59{all_reset}")
            continue
          seconds_input = input("SET SECONDS: ")
          if set_seconds < 0 or set_seconds > 59:
            print(f"{clr_red}Seconds must be entered between 0 - 59{all_reset}")
            continue
          set_day = int(day_input)
          set_hours = int(hours_input)
          set_minutes = int(minutes_input)
          set_seconds = int(seconds_input)
          print(f"Countdown from {clr_green}{set_day}{all_reset} day, {clr_green}{set_hours}{all_reset} hours, {clr_green}{set_minutes}{all_reset} minutes, {clr_green}{set_seconds}{all_reset} seconds.\n")
          countdown(set_day, set_hours, set_minutes, set_seconds)
        except ValueError:
          print(f"{clr_red}ERROR! idError: 34\nInvalid value.{all_reset}")
        except KeyboardInterrupt or EOFError:
          print(f"{clr_red}ERROR! idError: 35\nInvalid input.{all_reset}")

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
            if del_new_ln_config:
              print(f"{days} {hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d} ", end="\r")
            else:
              print(f"{days} {hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}")
            time.sleep(0.001)
        try:
          count_up()
        except KeyboardInterrupt or EOFError:
          print("\nCount up stopped.")

      elif "time.down=" in cmd_inp:
        index = cmd_inp.index("time.down=") + len("time.down=")
        timedown_inp = cmd_inp[index:].strip()
        if not timedown_inp.replace('.', '').isdigit():
          print(f"{clr_red}ERROR! idError: 36\nERROR! ({all_reset}{timedown_inp}{clr_red})\nInvalid value.{all_reset}")
        else:
          try:
            countdown_time = int(float(timedown_inp))
            print(f"Countdown from {clr_green}{countdown_time}{all_reset} seconds.\n")
            for i in range(countdown_time, -1, -1):
              if del_new_ln_config:
                print(f"{i} ", end="\r")
              else:
                print(i)
              time.sleep(1)
            print("Time up!")
          except KeyboardInterrupt or EOFError:
            print(f"{clr_red}ERROR! idError: 37\nERROR! ({all_reset}{timedown_inp}{clr_red})\nInvalid input.{all_reset}")

      elif cmd_inp == "time.down.dhms.tick":

        def countdown(days, hours, minutes, seconds, tick):
          total_seconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
          while total_seconds > 0:
            remaining_days, seconds = divmod(total_seconds, 24 * 60 * 60)
            remaining_hours, seconds = divmod(seconds, 60 * 60)
            remaining_minutes, seconds = divmod(seconds, 60)
            countdown_str = f"{remaining_days} {remaining_hours:02d}:{remaining_minutes:02d}:{seconds:02d}"
            if del_new_ln_config:
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
            print(f"{clr_red}Hours must be entered between 0 - 23{all_reset}")
            continue
          minutes_input = input("SET MINUTES: ")
          if set_minutes < 0 or set_minutes > 59:
            print(f"{clr_red}Minutes must be entered between 0 - 59{all_reset}")
            continue
          seconds_input = input("SET SECONDS: ")
          if set_seconds < 0 or set_seconds > 59:
            print(f"{clr_red}Seconds must be entered between 0 - 59{all_reset}")
            continue
          tick_input = input("SET TICK: ")
          set_day = int(day_input)
          set_hours = int(hours_input)
          set_minutes = int(minutes_input)
          set_seconds = int(seconds_input)
          set_tick = float(tick_input)
          print(f"Countdown from {clr_green}{set_day}{all_reset} day, {clr_green}{set_hours}{all_reset} hours, {clr_green}{set_minutes}{all_reset} minutes, {clr_green}{set_seconds}{all_reset} seconds.\n")
          countdown(set_day, set_hours, set_minutes, set_seconds, set_tick)
        except ValueError:
          print(f"{clr_red}ERROR! idError: 38\nInvalid value.{all_reset}")
        except KeyboardInterrupt or EOFError:
          print(f"{clr_red}ERROR! idError: 39\nInvalid input.{all_reset}")

      elif cmd_inp == "time.down.tick":
        try:
          timedown_inp = input("\nSET TIME DOWN (#s): ")
          tick_inp = input("SET TICK (#s): ")
          countdown_time = int(float(timedown_inp))
          print(f"Countdown from {clr_green}{countdown_time}{all_reset} seconds.\n")
          for i in range(countdown_time, -1, -1):
            if del_new_ln_config:
              print(f"{i} ", end="\r")
            else:
              print(i)
            time.sleep(float(tick_inp))
          print("Time up!")
        except ValueError:
          print(f"{clr_red}ERROR! idError: 40\nERROR! ({all_reset}{timedown_inp}{clr_red})\nInvalid value.{all_reset}")
        except KeyboardInterrupt or EOFError:
          print(f"{clr_red}ERROR! idError: 41\nERROR! ({all_reset}{timedown_inp}{clr_red})\nInvalid input.{all_reset}")

      elif "time.down$[set]=" in cmd_inp:
        try:
          index = cmd_inp.index("time.down$[set]=") + len("time.down$[set]=")
          timedown_e_inp = cmd_inp[index:].strip()
          countdown_time = int(float(timedown_e_inp))
          print(f"Countdown from {clr_green}{countdown_time}{all_reset} seconds.\n")
          for i in range(countdown_time, -1, -1):
            if del_new_ln_config:
              print(f"{i} / [ {timedown_e_inp} ] ", end="\r")
            else:
              print(f"{i} / [ {timedown_e_inp} ]")
            time.sleep(1)
          print("Time up!")
        except ValueError:
          print(f"{clr_red}ERROR! idError: 42\nERROR! ({all_reset}{timedown_e_inp}{clr_red})\nInvalid value.{all_reset}")
        except KeyboardInterrupt or EOFError:
          print(f"{clr_red}ERROR! idError: 43\nERROR! ({all_reset}{timedown_e_inp}{clr_red})\nInvalid input.{all_reset}")

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
                command_style = f"{clr_cyan}┌──({clr_blue}Console-py@{name}{clr_cyan})-[{all_reset}{dir}{clr_cyan}]\n└─{clr_green} $ {all_reset}"
              elif os_name == "nt":
                command_style = f"{clr_blue}┌──({clr_red}Console-py@{name}{clr_blue})-[{all_reset}{dir}{clr_blue}]\n└─{clr_green} > {all_reset}"
              else:
                command_style = f"{name}@( {dir} ) # "

            command = input(command_style)
            if command == "exit":
              break
            os.system(command)
          except KeyboardInterrupt or EOFError:
            print()
          except:
            print()

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
              if del_new_ln_config:
                print(random_string, end="\r")
              else:
                print(random_string)
              time.sleep(float(tick_inp))
          if __name__ == '__main__':
            main()
        except ValueError:
          print(f"{clr_red}ERROR! idError: 44\nInvalid value.{all_reset}")
        except KeyboardInterrupt or EOFError:
          print(f"{clr_red}ERROR! idError: 45\nInvalid input.{all_reset}")

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
              if del_new_ln_config:
                print(random_string, end="\r")
              else:
                print(random_string)
              time.sleep(float(tick_inpN))

          if __name__ == '__main__':
            main()
        except ValueError:
          print(f"{clr_red}ERROR! idError: 46\nInvalid value.{all_reset}")
        except KeyboardInterrupt or EOFError:
          print(f"{clr_red}ERROR! idError: 47\nInvalid input.{all_reset}")

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
              if del_new_ln_config:
                print(random_string, end="\r")
              else:
                print(random_string)
              time.sleep(float(tick_inp))

          if __name__ == '__main__':
            main()
        except ValueError:
          print(f"{clr_red}ERROR! idError: 48\nInvalid value.{all_reset}")
        except KeyboardInterrupt or EOFError:
          print(f"{clr_red}ERROR! idError: 49\nInvalid input.{all_reset}")

      elif "games=" in cmd_inp:
        index = cmd_inp.index("games=") + len("games=")
        game_inp = cmd_inp[index:].strip()
        if "gs_th_num" in game_inp.lower():
          print(f"{clr_cyan}\nGuess The Numbers!\n{all_reset}")
          try:
            min = int(input("Minimum number: "))
            max = int(input("Maximum number: "))
            max_tebakan = int(input("Tries: "))
          except ValueError:
            print(f"{clr_red}ERROR! idError: 50\nInvalid value.{all_reset}")
            continue
          except:
            print(f"{clr_red}ERROR! idError: 51\nInvalid input.{all_reset}")
            continue
          def tebak_angka():
            clear_screen()
            print(f"{clr_cyan}\nGuess The Numbers!\n{all_reset}")
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
                  print(f"{clr_blue}Low!\n{all_reset}")
                elif guess > angka:
                  print(f"{clr_red}High!\n{all_reset}")
                else:
                  print(f"{clr_green}Congratulations! You have guessed the correct number!{all_reset}")
                  break
                tebakan += 1
              except ValueError:
                print(f"{clr_red}ERROR! idError: 52\nInvalid value.\n{all_reset}")
            if tebakan == maks_tebakan:
              print(f"{clr_yellow}Too bad! You guessed the wrong number!\nThe correct number is {clr_green}{angka}{all_reset}")
          tebak_angka()

        elif "hgmn" in game_inp.lower():
          print(f"\n{clr_cyan}Hangman!{all_reset}\n\nSelect a language / Pilih bahasa\n1. English (Inggris)\n2. Indonesia")
          language_game = input("= ")
          print("\nSelect a difficulty")
          print(f"1. {clr_green}Easy{all_reset}      (3 letters) (have 15 tries)")
          print(f"2. {clr_blue}Normal{all_reset}    (4 letters) (have 10 tries)")
          print(f"3. {clr_yellow}Medium{all_reset}    (5 letters) (have 8 tries)")
          print(f"4. {clr_red}Hard{all_reset}      (6 letters) (have 6 tries)")
          print(f"5. {clr_magenta}Very hard{all_reset} (7 letters) (have 5 tries)")
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
          words_ing3 = ['the', 'and', 'you', 'are', 'for', 'not', 'but', 'all', 'yes', 'can', 'day', 'big', 'old', 'one', 'see', 'two', 'man', 'was', 'out', 'his', 'get', 'new', 'how', 'own', 'now', 'use', 'few', 'end', 'run', 'she', 'zoo', 'him', 'got', 'let', 'try', 'far', 'set', 'car', 'box', 'god', 'top', 'pay', 'job', 'art', 'sun', 'law', 'bar', 'boy', 'bat', 'air', 'dry', 'wet', 'key', 'arm', 'leg', 'bus', 'fly', 'pen', 'tax', 'bag', 'cat', 'dog', 'hat', 'cup', 'tea', 'bed', 'fan', 'car', 'toy', 'too', 'egg', 'map', 'gay', 'lol', 'sus', 'mop', 'let', 'for', 'cap', 'top', 'bye', 'min', 'max', 'mod']
          words_ing4 = ['that', 'have', 'this', 'will', 'page', 'what', 'they', 'when', 'with', 'from', 'your', 'like', 'some', 'time', 'make', 'guys', 'much', 'most', 'take', 'well', 'pick', 'very', 'come', 'then', 'here', 'also', 'edit', 'back', 'than', 'into', 'look', 'help', 'show', 'give', 'keep', 'been', 'many', 'gear', 'find', 'dont', 'part', 'open', 'life', 'only', 'home', 'pear', 'hate', 'hell', 'down', 'want', 'high', 'over', 'tell', 'away', 'text', 'good', 'work', 'know', 'main', 'care', 'need', 'hand', 'idea', 'fact', 'best', 'room', 'plan', 'name', 'song', 'rain', 'mind', 'hurt', 'city', 'true', 'blue', 'tree', 'cold', 'swim', 'jump', 'shop', 'food', 'wine', 'park', 'bird', 'fish', 'star', 'moon', 'fire', 'baby', 'file', 'book', 'film', 'love', 'fear', 'word', 'luck', 'ruby', 'game', 'team', 'shoe', 'sand', 'snow', 'road', 'rule', 'hill', 'ball', 'girl', 'math', 'note', 'stop', 'seed', 'gold', 'just']
          words_ing5 = ['about', 'after', 'again', 'along', 'among', 'angel', 'angry', 'apple', 'arrow', 'awake', 'beach', 'beard', 'begin', 'three', 'being', 'error', 'bella', 'below', 'track', 'noice', 'clock', 'birds', 'black', 'blend', 'knife', 'sorry', 'toxic', 'style', 'phone', 'click', 'tiger', 'enter', 'queen', 'wrist', 'green', 'close', 'paint', 'fruit', 'horse', 'laugh', 'hello', 'world', 'mouse', 'clown', 'night', 'hotel', 'print', 'sunny', 'input', 'dance', 'watch', 'drink', 'brain', 'smile', 'brave', 'strom', 'field', 'heart', 'dirty', 'sound', 'snake', 'money', 'chair', 'wings', 'music', 'dress', 'happy', 'round', 'color', 'flame', 'shine', 'spell', 'clear', 'pilot', 'space', 'shirt', 'magic', 'water', 'truck', 'fairy', 'mouse', 'boost']
          words_ing6 = ['orange', 'prompt', 'cookie', 'planet', 'purple', 'window', 'dragon', 'guitar', 'marvel', 'banana', 'circle', 'silver', 'hammer', 'sunset', 'jungle', 'rocket', 'spirit', 'flower', 'camera', 'candle', 'forest', 'winter', 'castle', 'pillow', 'basket', 'square', 'coffee', 'bottle', 'cheeze', 'cheery', 'circus', 'insert', 'closet', 'forest', 'market', 'mother', 'rabbit', 'escape', 'gaming', 'garden', 'spring', 'doctor', 'turtle', 'yellow', 'friend', 'candle', 'winter', 'render', 'carpet', 'delete', 'python', 'heaven', 'equals']
          words_ing7 = ['english', 'bicycle', 'weather', 'journey', 'cheddar', 'penguin', 'library', 'weekend', 'chicken', 'blanket', 'traffic', 'thunder', 'husbend', 'whistle', 'lantern', 'freedom', 'morning', 'mustang', 'balloon', 'diamond', 'restart', 'storage', 'setting', 'upgrade', 'produce', 'preview', 'version', 'numbers', 'deleted', 'control', 'replace', 'kidding']
          words_indo3 = ['ada', 'api', 'air', 'asa', 'bau', 'ban', 'bis', 'pir', 'hal', 'lah', 'pot', 'vas', 'dan', 'tai', 'eek', 'gas', 'kok', 'apa', 'itu', 'cor', 'jam', 'lem', 'hei', 'hai', 'oke', 'pas', 'goa', 'gua', 'tol', 'gol', 'aku', 'kas', 'kau', 'tua', 'ini', 'jam', 'pas', 'kos', 'gas', 'roh', 'cat', 'loh', 'sah', 'kas', 'tas', 'pah', 'mah', 'nak', 'pos', 'bos', 'dua', 'aku', 'nah', 'jas', 'dia', 'kol', 'esa']
          words_indo4 = ['anda', 'halo', 'mana', 'yoyo', 'mati', 'ungu', 'buat', 'kita', 'kami', 'jaga', 'jauh', 'kalo', 'sapi', 'babi', 'bara', 'tapi', 'beli', 'bata', 'maka', 'coli', 'blok', 'kata', 'kuat', 'mata', 'pada', 'tisu', 'oleh', 'tali', 'baca', 'gigi', 'dada', 'lalu', 'tiga', 'alam', 'muka', 'muak', 'kamu', 'koin', 'batu', 'uang', 'enam', 'mini', 'susu', 'puas', 'pala', 'kata', 'kuku', 'asli', 'bila', 'lima', 'gila', 'pata', 'kasa', 'saat', 'lama', 'suka', 'suku', 'jadi', 'maha', 'cita', 'lagi', 'kera', 'paus', 'baru', 'lupa', 'satu', 'lagu', 'ilmu', 'dari', 'beku', 'akan', 'beri', 'sama', 'coba', 'yang', 'lari', 'liar', 'teks']
          words_indo5 = ['sakit', 'ingat', 'kasar', 'rumah', 'pajak', 'kolom', 'piton', 'putus', 'kocok', 'bapak', 'nanah', 'latar', 'masih', 'hitam', 'kebun', 'kenal', 'bajak', 'lihat', 'hidup', 'bahan', 'tanah', 'hujan', 'panas', 'sinar', 'ikut', 'tebal', 'berat', 'sudah', 'perlu' 'tebak', 'benda', 'akhir', 'duduk', 'badan', 'perut', 'pergi', 'darah', 'makan', 'lapar', 'layer', 'tiada', 'jahat', 'tanah', 'kerja', 'baris', 'empat', 'zebra', 'tujuh', 'balik', 'lahar', 'ganda', 'kapak', 'ketek', 'habis', 'jawab', 'harum', 'marah', 'pipis', 'tahan', 'hukum', 'paham', 'jajan', 'resmi', 'papah', 'mamah', 'katak', 'gagah', 'gajah', 'bibir', 'suram', 'biasa', 'jalan', 'sisir', 'pilih', 'cocok', 'patah', 'kasih', 'kalah', 'cinta', 'suara', 'emang', 'rindu', 'lebih', 'meski', 'remuk', 'bikin', 'tahan', 'kasar', 'tagar', 'bosan', 'tahun', 'nyata', 'licin', 'gagal', 'kurus', 'payah']
          words_indo6 = ['tinggi', 'daging', 'amanat', 'durian', 'basahi', 'senyum', 'tempat', 'cintai', 'kalahi', 'pepaya', 'malang', 'pernah', 'tangis', 'takdir', 'ketika', 'pantat', 'diskon', 'contoh', 'kuning', 'soleha', 'selera', 'campur', 'banget', 'pulang', 'cemara', 'nangis', 'mentah', 'begini', 'kamera', 'langka', 'marahi', 'bodohi', 'sambut', 'menang', 'sering', 'bagian', 'kantor', 'sayang', 'ganjil', 'sampah', 'gambar', 'pusing', 'kurung', 'masjid']
          words_indo7 = ['disebut', 'sekolah', 'kinerja', 'selamat', 'menjadi', 'mungkin', 'lengkap', 'kecuali', 'bersama', 'terjadi', 'mengapa', 'menerus', 'melihat', 'kenalan', 'berikut', 'belajar', 'akurasi', 'membawa', 'membuka', 'ikutan', 'sebelas', 'menjaga', 'memberi', 'menurut', 'sebenar', 'memilih', 'menyata', 'menilai', 'menabur', 'manusia', 'kandang', 'delapan', 'sepuluh']

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
                  print(f" {clr_red}-{all_reset}", end="")
              guess = input(f"\n\n{guess_inp}: "); guess = guess.lower()
              if del_new_ln_config:
                clear_screen()
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
            hangman(words_ing3, 15, f"{clr_green}Easy{all_reset}", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", f"{clr_green}This letter is not in the word. Remaining opportunities:{all_reset}", f"{clr_green}Congratulations! You menaged to guess the word{all_reset}", f"{clr_red}Sorry, your chance is up. The correct word is{all_reset}")
          elif language_game == "1" and difficulty_game == "2":
            hangman(words_ing4, 10, f"{clr_blue}Normal{all_reset}", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", f"{clr_green}This letter is not in the word. Remaining opportunities:{all_reset}", f"{clr_green}Congratulations! You menaged to guess the word{all_reset}", f"{clr_red}Sorry, your chance is up. The correct word is{all_reset}")
          elif language_game == "1" and difficulty_game == "3":
            hangman(words_ing5, 8, f"{clr_green}Medium{all_reset}", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", f"{clr_green}This letter is not in the word. Remaining opportunities:{all_reset}", f"{clr_green}Congratulations! You menaged to guess the word{all_reset}", f"{clr_red}Sorry, your chance is up. The correct word is{all_reset}")
          elif language_game == "1" and difficulty_game == "4":
            hangman(words_ing6, 6, f"{clr_red}Hard{all_reset}", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", f"{clr_green}This letter is not in the word. Remaining opportunities:{all_reset}", f"{clr_green}Congratulations! You menaged to guess the word{all_reset}", f"{clr_red}Sorry, your chance is up. The correct word is{all_reset}")
          elif language_game == "1" and difficulty_game == "5":
            hangman(words_ing7, 5, f"{clr_magenta}Very hard{all_reset}", ascii_help_eng, ascii_win_eng, ascii_lose_eng, "Difficulty", "You only have", "tries", "Guess (type '!end' to exit)", f"{clr_green}This letter is not in the word. Remaining opportunities:{all_reset}", f"{clr_green}Congratulations! You menaged to guess the word{all_reset}", f"{clr_red}Sorry, your chance is up. The correct word is{all_reset}")
          elif language_game == "2" and difficulty_game == "1":
            hangman(words_indo3, 15, f"{clr_green}Mudah (Easy){all_reset}", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", f"{clr_green}Huruf ini tidak ada dalam kata. Peluang yang tersisa:{all_reset}", f"{clr_green}Selamat! Anda berhasil menebak katanya!{all_reset}", f"{clr_red}Maaf, kesempatan Anda habis. Kata yang benar adalah{all_reset}")
          elif language_game == "2" and difficulty_game == "2":
            hangman(words_indo4, 10, f"{clr_blue}Normal (Normal){all_reset}", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", f"{clr_green}Huruf ini tidak ada dalam kata. Peluang yang tersisa:{all_reset}", f"{clr_green}Selamat! Anda berhasil menebak katanya!{all_reset}", f"{clr_red}Maaf, kesempatan Anda habis. Kata yang benar adalah{all_reset}")
          elif language_game == "2" and difficulty_game == "3":
            hangman(words_indo5, 8, f"{clr_green}Sedang (Medium){all_reset}", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", f"{clr_green}Huruf ini tidak ada dalam kata. Peluang yang tersisa:{all_reset}", f"{clr_green}Selamat! Anda berhasil menebak katanya!{all_reset}", f"{clr_red}Maaf, kesempatan Anda habis. Kata yang benar adalah{all_reset}")
          elif language_game == "2" and difficulty_game == "4":
            hangman(words_indo6, 6, f"{clr_red}Susah (Hard){all_reset}", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", f"{clr_green}Huruf ini tidak ada dalam kata. Peluang yang tersisa:{all_reset}", f"{clr_green}Selamat! Anda berhasil menebak katanya!{all_reset}", f"{clr_red}Maaf, kesempatan Anda habis. Kata yang benar adalah{all_reset}")
          elif language_game == "2" and difficulty_game == "5":
            hangman(words_indo7, 5, f"{clr_magenta}Sangat susah (Very hard){all_reset}", ascii_help_ind, ascii_win_ind, ascii_lose_ind, "Kesulitan", "Kamu hanya memiliki", "percobaan", "Tebak (ketik '!end' untuk keluar)", f"{clr_green}Huruf ini tidak ada dalam kata. Peluang yang tersisa:{all_reset}", f"{clr_green}Selamat! Anda berhasil menebak katanya!{all_reset}", f"{clr_red}Maaf, kesempatan Anda habis. Kata yang benar adalah{all_reset}")
          else:
            print(f"{clr_red}ERROR! idError: 53\nERROR! ({all_reset}{language_game}{clr_red}), ({all_reset}{difficulty_game}{clr_red})\nCommand not found.{all_reset}")

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

          print(f"{clr_cyan}\nRock, Paper, Scissors (bot)\n{all_reset}")
          while True:
            print("Select one:\n1. Rock\n2. Scissors\n3. Paper\n4. exit")
            player_choice = input("= ")[:1]
            if player_choice == "4":
              break
            if player_choice not in ['1', '2', '3']:
              print(f"{clr_red}ERROR! idError: 54\nInvalid value.{all_reset}")
              continue
            player_choice = choices[int(player_choice) - 1]
            computer_choice = random.choice(choices)
            print(f"Your choice: {clr_cyan}{player_choice}{all_reset}")
            print(f"{clr_yellow}Computer choice: {computer_choice}{all_reset}")
            result = determine_winner(player_choice, computer_choice)
            if result == 0:
              played += 1
              series_count += 1
              print(f"{clr_cyan}Series!{all_reset}\n\nSeries: {clr_cyan}{series_count}{all_reset} | Computer: {clr_yellow}{computer_count}{all_reset} | You: {clr_green}{player_count}{all_reset} | Played:{clr_magenta}{played}{all_reset}\n")
            elif result == 1:
              played += 1
              player_count += 1
              print(f"{clr_green}You win!{all_reset}\n\nSeries: {clr_cyan}{series_count}{all_reset} | Computer: {clr_yellow}{computer_count}{all_reset} | You: {clr_green}{player_count}{all_reset} | Played: {clr_magenta}{played}{all_reset}\n")
            else:
              played += 1
              computer_count += 1
              print(f"{clr_yellow}Computer win!{all_reset}\n\nSeries: {clr_cyan}{series_count}{all_reset} | Computer: {clr_yellow}{computer_count}{all_reset} | You: {clr_green}{player_count}{all_reset} | Played:{clr_magenta}{played}{all_reset}\n")

        elif "ti_ta_to-bot" in game_inp.lower():
          print("{clr_cyan}\nTic Tac Toe (bot)\n{all_reset}")

          def print_board(board):
            print("+---+---+---+")
            for row in board:
              print("|", end=" ")
              for cell in row:
                if cell == "X":
                  print((f"{clr_red}{cell}{all_reset}"), end=" | ")
                elif cell == "O":
                  print((f"{clr_cyan}{cell}{all_reset}"), end=" | ")
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
                  print(f"{clr_red}Please input 1-9.{all_reset}")
                  continue
                return row, col
              except ValueError:
                print(f"{clr_red}ERROR! idError: 55\nInvalid value.{all_reset}")

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
                print(f"Computer turn: ({clr_cyan}O{all_reset})")
                row, col = get_computer_move(board)
              board[row][col] = current_player
              if is_winner(board, current_player):
                print_board(board)
                if current_player == "X":
                  print(f"{clr_green}Congratulations! You win!{all_reset}")
                else:
                  print(f"{clr_yellow}Computer wins!{all_reset}")
                break
              if is_board_full(board):
                print_board(board)
                print(f"{clr_cyan}Series!{all_reset}")
                break
              current_player = "O" if current_player == "X" else "X"
          play_tic_tac_toe()

        elif "numpuz" in game_inp.lower():
          print(f"{clr_cyan}\nNumpuz\n{all_reset}")
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
                      print(f'|{clr_cyan}' + '{:^4}'.format(self.board[i][j]) + f'{all_reset}', end='')
                    print('|')
                  print('+' + '----+' * self.size)

                def play(self):
                  self.shuffle_board()
                  while not self.is_solved():
                    if del_new_ln_config:
                      clear_screen()
                    self.display_board()
                    move = input("Enter move (wasd) (type '!' to exit): ")[:1]; move = move.lower()
                    if move == '!':
                      break
                    row, col = self.find_empty_space()
                    valid_moves = self.get_valid_moves(row, col)
                    if move not in ['w', 'a', 's', 'd']:
                      print(f"{clr_red}ERROR! idError: 56\nOnly move 'wasd'{all_reset}")
                    elif move == 'w' and 'up' in valid_moves:
                      self.make_move(row, col, 'up')
                    elif move == 's' and 'down' in valid_moves:
                      self.make_move(row, col, 'down')
                    elif move == 'a' and 'left' in valid_moves:
                      self.make_move(row, col, 'left')
                    elif move == 'd' and 'right' in valid_moves:
                      self.make_move(row, col, 'right')
                    else:
                      print(f"{clr_red}Only move 'wasd'.{all_reset}")
                  if self.is_solved():
                    if del_new_ln_config:
                      clear_screen()
                    self.display_board()
                    print(f"{clr_green}Congratulations! You solved the puzzle.{all_reset}")

              if __name__ == '__main__':
                game = Numpuz()
                game.shuffle_board()
                game.play()

            else:
              if get_inpLevel <= 3:
                print(f"{clr_yellow}Is to LOW! MIN level: 3, MAX level: 30{all_reset}")
              if get_inpLevel >= 10:
                print(f"{clr_yellow}Is to HIGH! MAX level: 30, MIN level: 3{all_reset}")

          else:
            print(f"{clr_red}ERROR! idError: 57\nInvalid input.{all_reset}")

        elif "minswe" in game_inp.lower():
          print(f"{clr_cyan}\nMinesweeper\n{all_reset}")
          size = input("Size (6-35): ")
          bomb = input("Bomb (5-1070): ")
          if size.isdigit() and bomb.isdigit():
            size = int(size)
            bomb = int(bomb)

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
                  if board[row][col] == f' {clr_red}*{all_reset} ':
                    continue
                  board[row][col] = f' {clr_red}*{all_reset} '
                  bombs_planted += 1
                return board
          
              def assign_values_to_board(self):
                for r in range(self.dim_size):
                  for c in range(self.dim_size):
                    if self.board[r][c] == f' {clr_red}*{all_reset} ':
                      continue
                    self.board[r][c] = self.get_num_neighboring_bombs(r, c)
          
              def get_num_neighboring_bombs(self, row, col):
                num_neighboring_bombs = 0
                for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                  for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if r == row and c == col:
                      continue
                    if self.board[r][c] == f' {clr_red}*{all_reset} ':
                      num_neighboring_bombs += 1
                return num_neighboring_bombs
          
              def dig(self, row, col):
                self.dug.add((row, col))
                if self.board[row][col] == f' {clr_red}*{all_reset} ':
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
                color_mapping = {
                  0: f'{all_reset}',
                  1: f'{clr_green}',
                  2: f'{clr_cyan}',
                  3: f'{clr_blue}',
                  4: f'{clr_yellow}',
                  5: f'{clr_orange}',
                  6: f'{clr_red}',
                  7: f'{clr_magenta}',
                  8: f'{bgclr_red}{clr_white}',
                }
              
                visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
              
                for row in range(self.dim_size):
                  for col in range(self.dim_size):
                    if (row, col) in self.dug:
                      cell_value = self.board[row][col]
                      if cell_value == ' ':
                        visible_board[row][col] = ' '
                      else:
                        if cell_value == f' {clr_red}*{all_reset} ':
                          visible_board[row][col] = f' {clr_red}*{all_reset} '
                        else:
                          visible_board[row][col] = f'{color_mapping[cell_value]} {cell_value} {all_reset}'
                    else:
                      visible_board[row][col] = ' '
          
                string_rep = ''
                indices_row = f'   {clr_cyan}' + ' '.join([f'{i:^3}' for i in range(self.dim_size)]) + f'{all_reset}\n'
                separator_row = '--+' + '---+' * ((len(indices_row) - 12) // 4) + '\n'
                string_rep += indices_row + separator_row
              
                for i in range(len(visible_board)):
                  row = visible_board[i]
                  cells = [f'{cell:^3}' for cell in row]
                  add_space_string_rep = ' ' if len(f'{i}') == 1 else ''
                  string_rep += f'{clr_cyan}{i}{all_reset}{add_space_string_rep}|' + '|'.join(cells) + '|\n'
                  string_rep += separator_row
              
                return string_rep
          
            def play(dim_size, num_bombs):
              board = Board(dim_size, num_bombs)
              safe = True
              while len(board.dug) < board.dim_size ** 2 - num_bombs:
                if del_new_ln_config:
                  clear_screen()
                print(board)
                user_input = input("Choose location (row,col) (type '!' to exit): ").strip()
                if user_input == "!":
                  print(f"{clr_cyan}Bye:){all_reset}")
                  break
                if not re.match(r'^\d+,\s*\d+$', user_input):
                  print(f"{clr_red}ERROR! idError: 58\nInvalid input.{all_reset}")
                  continue
                row, col = map(int, user_input.split(','))
                if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                  print(f"{clr_red}ERROR! idError: 59\nInvalid location.{all_reset}")
                  continue
                safe = board.dig(row, col)
                if not safe:
                  if del_new_ln_config:
                    clear_screen()
                  print(f"{clr_red}Booomb!!{all_reset}")
                  break
              if safe:
                if del_new_ln_config:
                    clear_screen()
                print(board)
                print(f"{clr_green}Congratulations! You won!{all_reset}")
              else:
                print(f"{clr_red}Sorry, You lose!{all_reset}")
                board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
                print(board)

            if size <= 8 and size >= 6 and bomb <= 30 and bomb >= 5:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 11 and size >= 9 and bomb <= 70 and bomb >= 5:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 14 and size >= 12 and bomb <= 130 and bomb >= 5:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 17 and size >= 15 and bomb <= 210 and bomb >= 5:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 20 and size >= 18 and bomb <= 310 and bomb >= 5:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 23 and size >= 21 and bomb <= 430 and bomb >= 10:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 26 and size >= 24 and bomb <= 560 and bomb >= 15:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 29 and size >= 27 and bomb <= 710 and bomb >= 20:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 32 and size >= 30 and bomb <= 890 and bomb >= 20:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            elif size <= 35 and size >= 33 and bomb <= 1070 and bomb >= 25:
              if __name__ == '__main__':
                play(dim_size=size, num_bombs=bomb)
            else:
              print(f"{clr_red}ERROR! idError: 60\nOver Size, Bomb!{all_reset}\n\nSIZE 6 - 8:\n  BOMB 5 - 30\nSIZE 9 - 11:\n  BOMB 5 - 70\nSIZE 12 - 14:\n  BOMB 5 - 130\nSIZE 15 - 17:\n  BOMB 5 - 210\nSIZE 18 - 20:\n  BOMB 5 - 310\nSIZE 21 - 23:\n  BOMB 10 - 430\nSIZE 24 - 26:\n  BOMB 15 - 560\nSIZE 27 - 29:\n  BOMB 20 - 710\nSIZE 30 - 32:\n  BOMB 20 - 890\nSIZE 33 - 35:\n  BOMB 25 - 1070")
          else:
            print(f"{clr_red}ERROR! idError: 61\nInvalid input.{all_reset}")

        else:
          print(f"{clr_red}ERROR! idError: 62\nERROR! ({all_reset}{game_inp}\033[31m)\nCommand not found.{all_reset}")

      elif cmd_inp == "dupl.text":
        tick_inp = input("\nTICK: ")
        timeout_inp = input("TIMEOUT: ")
        text_inp = input("TEXT: ")
        print("")
        try:
          def main():
            timeout = float(timeout_inp)
            start_time = time.time()
            while True:
              current_time = time.time()
              elapsed_time = current_time - start_time
              if elapsed_time >= timeout:
                break
              if del_new_ln_config:
                print(text_inp)
              else:
                print(text_inp)
              time.sleep(float(tick_inp))
          if __name__ == '__main__':
            main()
        except ValueError:
          print(f"{clr_red}ERROR! idError: 63\nInvalid value.{all_reset}")
        except KeyboardInterrupt or EOFError:
          print(f"{clr_red}ERROR! idError: 64\nInvalid input.{all_reset}")

      elif cmd_inp == "console /?" or cmd_inp == "/?" or cmd_inp == "-c" or cmd_inp == "console -c":
        consoleCommand()

      else:
        print(f"{clr_red}ERROR! idError: Invalid-1\nERROR! ({all_reset}{cmd_inp}{clr_red})\nInvalid command.{all_reset}")
  except EOFError:
    print(f"\nYou just press [Ctrl + Z or D ({clr_red}EOFError{all_reset})]")
    continue
  except KeyboardInterrupt:
    print(f"\nYou just press [Ctrl + C ({clr_red}KeyboardInterrupt{all_reset})]")
    continue
  except Exception as e:
    print(f"\033[31mERROR! idError: 65\nAn unexpected Fatal Error occurred while running \033[36mconsole.py\033[31m . Don't worry! We'll fix it soon.\033[0m\nError Python:\n{e}")
    con_ex = input("press enter to exit or 'c' to continue...")
    if con_ex.lower() == "c":
      continue
    else:
      exit()
  except:
    print("\033[31mERROR! idError: 66\nOops! Something Error!\033[0m")
    continue