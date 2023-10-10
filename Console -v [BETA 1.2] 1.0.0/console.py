try:

  import math, datetime, random, time, os, re, socket, pyfiglet
  from File.Tools import asciiGUI

except Exception as e:
  print('''\033[31mERROR! idError: 1\nThe module used is invalid or an error occurred while importing the module or something error to running \033[36mconsole.py\033[31m. Please install module 'pip install <module>' if you haven't already installed it.\n\n\033[0m'\033[33mpip\033[0m install setuptools'\033[32m (distribute Python packages)\n\033[0m'\033[33mpip\033[0m install re'\n'\033[33mpip\033[0m install pyfiglet'\n\n\033[31mIf you omit the file in the path '\033[36mFile/Tools/asciiGUI.py\033[31m'. The Console cannot be started. Please reinstall the latest Console (if you really lost it).\033[0m''')
  print(f"Error Python:\n{e}"); input("Press ENTER to exit..."); exit()
except:
  print("\033[31mERROR! idError: 2\nSomething Error...\033[0m"); exit()

def clear_screen():
  os.system('title Console' if os.name == 'nt' else 'xtitle Console')
  os.system('cls' if os.name == 'nt' else 'clear')

def replace_rules_ansi_default(text_target):
  return text_target.replace('\\ln', '\n').replace('\\clr[black]', '\033[30m').replace('\\clr[red]', '\033[31m').replace('\\clr[green]', '\033[32m').replace('\\clr[yellow]', '\033[33m').replace('\\clr[blue]', '\033[34m').replace('\\clr[magenta]', '\033[35m').replace('\\clr[cyan]', '\033[36m').replace('\\clr[white]', '\033[37m').replace('\\clr[orange]', '\033[38;5;208m').replace('\\clr[gray]', '\033[90m').replace('\\bgclr[black]', '\033[40m').replace('\\bgclr[red]', '\033[41m').replace('\\bgclr[green]', '\033[42m').replace('\\bgclr[yellow]', '\033[43m').replace('\\bgclr[blue]', '\033[44m').replace('\\bgclr[magenta]', '\033[45m').replace('\\bgclr[cyan]', '\033[46m').replace('\\bgclr[white]', '\033[47m').replace('\\bgclr[orange]', '\033[48;5;208m').replace('\\bgclr[gray]', '\033[100m').replace('\\style[bold]', '\033[1m').replace('\\style[italic]', '\033[3m').replace('\\style[strike]', '\033[9m').replace('\\r[0]', '\033[0m').replace('\\style[none]', '\033[0m').replace('\\style[undline]', '\033[4m').replace('\\uc[1vertical]', '\u2502').replace('\\uc[1horizontal]', '\u2500').replace('\\uc[1up_right]', '\u250c').replace('\\uc[1up_left]', '\u2510').replace('\\uc[1plus]', '\u253c').replace('\\uc[1down_right]', '\u2514').replace('\\uc[1down_left]', '\u2518').replace('\\uc[1horizontal_c_down]', '\u252c').replace('\\uc[1horizontal_c_up]', '\u2534').replace('\\uc[1vertical_c_right]', '\u251c').replace('\\uc[1vertical_c_left]', '\u2524').replace('\\uc[2vertical]', '\u2551').replace('\\uc[2horizontal]', '\u2550').replace('\\uc[2up_right]', '\u2554').replace('\\uc[2up_left]', '\u2557').replace('\\uc[2plus]', '\u256c').replace('\\uc[2down_right]', '\u255a').replace('\\uc[2down_left]', '\u255d').replace('\\uc[2horizontal_c_down]', '\u2566').replace('\\uc[2horizontal_c_up]', '\u2569').replace('\\uc[2vertical_c_right]', '\u2560').replace('\\uc[2vertical_c_left]', '\u2563').replace('\\uc[1full_block]', '\u2588').replace("$LINE", f"{asciiGUI.terminal_size('y')}").replace("$COLUMN", f"{asciiGUI.terminal_size('x')}").replace("$SECONDS", f"{datetime.datetime.now().strftime('%S')}").replace("$MINUTES", f"{datetime.datetime.now().strftime('%M')}").replace("$HOURS", f"{datetime.datetime.now().strftime('%H')}").replace("$DATES", f"{datetime.datetime.now().strftime('%d')}").replace("$MOUNTS", f"{datetime.datetime.now().strftime('%m')}").replace("$YEARS", f"{datetime.datetime.now().strftime('%Y')}")

clear_screen()

def FILECONFIGSYSTEM(file='', config='r', tf=False):
  if 'w' in config:
    with open(f'{file}' , 'w', encoding='utf8') as view:
      if tf:
        view.write('True')
        return True
      else:
        view.write('False')
        return False
  elif 'r' in config:
    try:
      with open(f'{file}' , 'r', encoding='utf8') as view:
        trueORfalse = view.read()
        if trueORfalse == 'True':
          return True
        else:
          return False
    except:
      return False
    
def FILECONFIGSTYLESYSTEM(file='', new_value='', defaut=''):
  try:
     if new_value != 'read':
       with open(f'{file}' , 'w', encoding='utf8') as view:
        value = view.write(new_value)
        return replace_rules_ansi_default(value)
     elif new_value == 'read':
       try:
         with open(f'{file}' , 'r', encoding='utf8') as view:
           reads = view.read()
           return replace_rules_ansi_default(reads)
       except:
         return replace_rules_ansi_default(defaut)
  except:
    return replace_rules_ansi_default(defaut)

version = "[BETA 1.2] 1.0.0"
del_new_ln_config = FILECONFIGSYSTEM('File/System Config/DELNEWLINE.console', 'r', False)
ascii_unicode_config = FILECONFIGSYSTEM('File/System Config/ASCIIUNICODE.console', 'r', False)
python_editor_line_num_config = FILECONFIGSYSTEM('File/System Config/PYTHONEDITORLINENUM.console', 'r', False)
style_none = FILECONFIGSTYLESYSTEM('File/System Config/style/style_none.sc', 'read', '\\style[none]')
clr_black = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', 'read', '\\clr[black]')
clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', 'read', '\\clr[red]')
clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', 'read', '\\clr[green]')
clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', 'read', '\\clr[yellow]')
clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', 'read', '\\clr[blue]')
clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', 'read', '\\clr[magenta]')
clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', 'read', '\\clr[cyan]')
clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', 'read', '\\clr[white]')
clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', 'read', '\\clr[orange]')
clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', 'read', '\\clr[gray]')
bgclr_black = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_black.sc', 'read', '\\bgclr[black]')
bgclr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_red.sc', 'read', '\\bgclr[red]')
bgclr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_green.sc', 'read', '\\bgclr[green]')
bgclr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_yellow.sc', 'read', '\\bgclr[yellow]')
bgclr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_blue.sc', 'read', '\\bgclr[blue]')
bgclr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_magenta.sc', 'read', '\\bgclr[magenta]')
bgclr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_cyan.sc', 'read', '\\bgclr[cyan]')
bgclr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_white.sc', 'read', '\\bgclr[white]')
bgclr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_orange.sc', 'read', '\\bgclr[orange]')
bgclr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_gray.sc', 'read', '\\bgclr[gray]')
style_bold = FILECONFIGSTYLESYSTEM('File/System Config/style/style_bold.sc', 'read', '\\style[bold]')
style_italic = FILECONFIGSTYLESYSTEM('File/System Config/style/style_italic.sc', 'read', '\\style[italic]')
style_strike = FILECONFIGSTYLESYSTEM('File/System Config/style/style_strike.sc', 'read', '\\style[strike]')
style_underline = FILECONFIGSTYLESYSTEM('File/System Config/style/style_underline.sc', 'read', '\\style[undline]')
all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', 'read', '\\r[0]')
uc_1_FullBlock = "\u2588"
uc_1_vertical, uc_2_vertical = "\u2502", "\u2551"
uc_1_horizontal, uc_2_horizontal = "\u2500", "\u2550"
uc_1_UpRight, uc_2_UpRight = "\u250c", "\u2554"
uc_1_UpLeft, uc_2_UpLeft = "\u2510", "\u2557"
uc_1_Plus, uc_2_Plus = "\u253c", "\u256c"
uc_1_DownRight, uc_2_DownRight = "\u2514", "\u255a"
uc_1_DownLeft, uc_2_DownLeft = "\u2518", "\u255d"
uc_1_horizontalCdown, uc_2_horizontalCdown = "\u252c", "\u2566"
uc_1_horizontalCup, uc_2_horizontalCup = "\u2534", "\u2569"
uc_1_verticalCright, uc_2_verticalCright = "\u251c", "\u2560"
uc_1_verticalCleft, uc_2_verticalCleft = "\u2524", "\u2563"
calculate_ans = 0
vars_input = ''
running_main = True

def replace_rules_ansi(text_target):
  return text_target.replace('\\ln', '\n').replace('\\clr[black]', f'{clr_black}').replace('\\clr[red]', f'{clr_red}').replace('\\clr[green]', f'{clr_green}').replace('\\clr[yellow]', f'{clr_yellow}').replace('\\clr[blue]', f'{clr_blue}').replace('\\clr[magenta]', f'{clr_magenta}').replace('\\clr[cyan]', f'{clr_cyan}').replace('\\clr[white]', f'{clr_white}').replace('\\clr[orange]', f'{clr_orange}').replace('\\clr[gray]', f'{clr_gray}').replace('\\bgclr[black]', f'{bgclr_black}').replace('\\bgclr[red]', f'{bgclr_red}').replace('\\bgclr[green]', f'{bgclr_green}').replace('\\bgclr[yellow]', f'{bgclr_yellow}').replace('\\bgclr[blue]', f'{bgclr_blue}').replace(f'\\bgclr[magenta]', f'{bgclr_magenta}').replace('\\bgclr[cyan]', f'{bgclr_cyan}').replace('\\bgclr[white]', f'{bgclr_white}').replace('\\bgclr[orange]', f'{bgclr_orange}').replace('\\bgclr[gray]', f'{bgclr_gray}').replace('\\style[bold]', f'{style_bold}').replace('\\style[italic]', f'{style_italic}').replace('\\style[strike]', f'{style_strike}').replace('\\r[0]', f'{all_reset}').replace('\\style[undline]', f'{style_underline}').replace('\\uc[1vertical]', f'{uc_1_vertical}').replace('\\uc[1horizontal]', f'{uc_1_horizontal}').replace('\\uc[1up_right]', f'{uc_1_UpRight}').replace('\\uc[1up_left]', f'{uc_1_UpLeft}').replace('\\uc[1plus]', f'{uc_1_Plus}').replace('\\uc[1down_right]', f'{uc_1_DownRight}').replace('\\uc[1down_left]', f'{uc_1_DownLeft}').replace('\\uc[1horizontal_c_down]', f'{uc_1_horizontalCdown}').replace('\\uc[1horizontal_c_up]', f'{uc_1_horizontalCup}').replace('\\uc[1vertical_c_right]', f'{uc_1_verticalCright}').replace('\\uc[1vertical_c_left]', f'{uc_1_verticalCleft}').replace('\\uc[2vertical]', f'{uc_2_vertical}').replace('\\uc[2horizontal]', f'{uc_2_horizontal}').replace('\\uc[2up_right]', f'{uc_2_UpRight}').replace('\\uc[2up_left]', f'{uc_2_UpLeft}').replace('\\uc[2plus]', f'{uc_2_Plus}').replace('\\uc[2down_right]', f'{uc_2_DownRight}').replace('\\uc[2down_left]', f'{uc_2_DownLeft}').replace('\\uc[2horizontal_c_down]', f'{uc_2_horizontalCdown}').replace('\\uc[2horizontal_c_up]', f'{uc_2_horizontalCup}').replace('\\uc[2vertical_c_right]', f'{uc_2_verticalCright}').replace('\\uc[2vertical_c_left]', f'{uc_2_verticalCleft}').replace('\\uc[1full_block]', f'{uc_1_FullBlock}').replace('$ANS', f'{calculate_ans}').replace('$INPUT', f"{vars_input}").replace("$LINE", f"{asciiGUI.terminal_size('y')}").replace("$COLUMN", f"{asciiGUI.terminal_size('x')}").replace("$SECONDS", f"{datetime.datetime.now().strftime('%S')}").replace("$MINUTES", f"{datetime.datetime.now().strftime('%M')}").replace("$HOURS", f"{datetime.datetime.now().strftime('%H')}").replace("$DATES", f"{datetime.datetime.now().strftime('%d')}").replace("$MOUNTS", f"{datetime.datetime.now().strftime('%m')}").replace("$YEARS", f"{datetime.datetime.now().strftime('%Y')}")

def remove_ansi_len(text_target):
  return len(text_target.replace('\n', '').replace('\033[30m', '').replace('\033[31m', '').replace('\033[32m', '').replace('\033[33m', '').replace('\033[34m', '').replace('\033[35m', '').replace('\033[36m', '').replace('\033[37m', '').replace('\033[38;5;208m', '').replace('\033[90m', '').replace('\033[40m', '').replace('\033[41m', '').replace('\033[42m', '').replace('\033[43m', '').replace('\033[44m', '').replace('\033[45m', '').replace('\033[46m', '').replace('\033[47m', '').replace('\\033[48;5;208m', '').replace('\033[100m', '').replace('\033[1m', '').replace('\033[3m', '').replace('\033[9m', '').replace('\033[0m', '').replace('\033[4m', ''))

def consoleCommand():
  global clr_yellow, clr_green, clr_cyan, style_underline, all_reset, version
  version_label = f"  Version: {style_underline}{clr_green}{version}{style_none}{all_reset}  "
  version_labels = asciiGUI.justify(version_label, 'center', space='=', minus=-17, width=asciiGUI.terminal_size('x'))
  print(version_labels)
  print(f"{clr_cyan}\nCommands in this Console\n{all_reset}")
  print(f"exit                           {clr_yellow}Terminate a program Console{all_reset}")
  print(f"clear                          {clr_yellow}Clear the entire command{all_reset}")
  print(f"edit.ascii_banner              {clr_yellow}Edit banner ascii{all_reset}")
  print(f"text.ascii_generated           {clr_yellow}Generated ascii text{all_reset}")
  print(f"del.new_ln=                    {clr_yellow}Removed special old content related to time, rdm, dupl, games if True{all_reset}")
  print(f"unicode.config=                {clr_yellow}Creates board with unicode if True{all_reset}")
  print(f"python.editor.line_num.config= {clr_yellow}Adds row number in python.editor function if True{all_reset}")
  print(f"ccl=                           {clr_yellow}Calculate perform basic math calculations (+ - / * ^){all_reset}")
  print(f"sqrt=                          {clr_yellow}Calculate roots{all_reset}")
  print(f"cbrt=                          {clr_yellow}Calculate roots 3{all_reset}")
  print(f"factorial=                     {clr_yellow}Calculate factorials{all_reset}")
  print(f"text=                          {clr_yellow}Display text{all_reset}")
  print(f"input=                         {clr_yellow}Display a prompt for user input{all_reset}")
  print(f"dt=                            {clr_yellow}Duplicate a character{all_reset}")
  print(f"len=                           {clr_yellow}Count length of characters{all_reset}")
  print(f"bnr=                           {clr_yellow}Convert words to binary code{all_reset}")
  print(f"bnr_re=                        {clr_yellow}Convert binary code to words{all_reset}")
  print(f"mrs=                           {clr_yellow}Convert words to Morse code{all_reset}")
  print(f"python.editor                  {clr_yellow}Create a Python system text editor{all_reset}")
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
  print(f"time.get                       {clr_yellow}Display current time{all_reset}")
  print(f"ccl.time.d=                    {clr_yellow}Calculate past and future dates using days{all_reset}")
  print(f"ccl.time.hms=                  {clr_yellow}Calculate addition and subtraction times (HH:MM:SS){all_reset}")
  print(f"time.sleep=                    {clr_yellow}Provides program delay time{all_reset}")
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
  print(f"\nidError-Total: {clr_cyan}106{all_reset}")

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
    with open("banner.txt", "r", encoding="utf8") as run:
      print(replace_rules_ansi(run.read()))
    if check_internet_connection():
      print(f"{style_none}{all_reset}Connection status: {clr_green}Online{all_reset}")
    else:
      print(f"{style_none}{all_reset}Connection status: {clr_red}Offline{all_reset}")
    print(f"{all_reset}Console (command: console /? or /? or -c) (exit: exit) [BETA]\n")
  except:
    print(f"Cannot open '{clr_cyan}banner.txt{all_reset}'")
    if check_internet_connection():
      print(f"{style_none}{all_reset}Connection status: {clr_green}Online{all_reset}")
    else:
      print(f"{style_none}{all_reset}Connection status: {clr_red}Offline{all_reset}")
    print(f"{all_reset}Console (command: console /? or /? or -c) (exit: exit) [BETA]\n")

def edit_command_logo(argv1_logo):
  global clr_green, clr_cyan, all_reset
  try:
    print(f"{clr_green}Read Banner:{all_reset}")
    try:
      with open("banner.txt", "r", encoding="utf8") as read_banner:
        banner_print = read_banner.read()
        print(banner_print)
    except:
      print(f"{clr_red}File Not Found. '{clr_cyan}banner.txt{clr_red}'{all_reset}")
    print("\033[0m\033[33m\nPress enter to save. Use '\\ln' to make new line. [Ctrl + C] to cancel.\033[0m\n")
    print("ANSI code:\n\ncode                     clr name clr\n----                     --- --------")
    print("\\r[0]                        (reset)\n\\clr[black]              \033[30m\u2588\u2588\u2588\033[0m (black)\n\\clr[red]                \033[31m\u2588\u2588\u2588\033[0m (red)\n\\clr[green]              \033[32m\u2588\u2588\u2588\033[0m (green)\n\\clr[yellow]             \033[33m\u2588\u2588\u2588\033[0m (yellow)\n\\clr[blue]               \033[34m\u2588\u2588\u2588\033[0m (blue)\n\\clr[magenta]            \033[35m\u2588\u2588\u2588\033[0m (magenta)\n\\clr[cyan]               \033[36m\u2588\u2588\u2588\033[0m (cyan)\n\\clr[white]              \033[37m\u2588\u2588\u2588\033[0m (white)\n\\clr[orange]             \033[38;5;208m\u2588\u2588\u2588\033[0m (orange)\n\\clr[gray]               \033[90m\u2588\u2588\u2588\033[0m (gray)\n\\bgclr[black]            \033[40mclr\033[0m (background black)\n\\bgclr[red]              \033[41mclr\033[0m (background red)\n\\bgclr[green]            \033[42mclr\033[0m (background green)\n\\bgclr[yellow]           \033[43mclr\033[0m (background yellow)\n\\bgclr[blue]             \033[44mclr\033[0m (background blue)\n\\bgclr[magenta]          \033[45mclr\033[0m (background magenta)\n\\bgclr[cyan]             \033[46mclr\033[0m (background cyan)\n\\bgclr[white]            \033[47mclr\033[0m (background white)\n\\bgclr[orange]           \033[48;5;208mclr\033[0m (background orange)\n\\bgclr[gray]             \033[100mclr\033[0m (background gray)\n\\style[bold]             \033[1msty\033[0m (style bold)\n\\style[italic]           \033[3msty\033[0m (style italic)\n\\style[strike]           \033[9msty\033[0m (style strike)\n\\style[undline]          \033[4msty\033[0m (style underline)\n\\uc[1vertical]            \u2502  (unicode style:1 vertical)\n\\uc[1horizontal]          \u2500  (unicode style:1 horizontal)\n\\uc[1up_right]            \u250c  (unicode style:1 up right)\n\\uc[1up_left]             \u2510  (unicode style:1 up left)\n\\uc[1plus]                \u253c  (unicode style:1 plus)\n\\uc[1down_right]          \u2514  (unicode style:1 down right)\n\\uc[1down_left]           \u2518  (unicode style:1 down left)\n\\uc[1horizontal_c_down]   \u252c  (unicode style:1 horizontal center down)\n\\uc[1horizontal_c_up]     \u2534  (unicode style:1 horizontal center up)\n\\uc[1vertical_c_right]    \u251c  (unicode style:1 vertical center right)\n\\uc[1vertical_c_left]     \u2524  (unicode style:1 vertical center left)\n\\uc[2vertical]            \u2551  (unicode style:2 vertical)\n\\uc[2horizontal]          \u2550  (unicode style:2 horizontal)\n\\uc[2up_right]            \u2554  (unicode style:2 up right)\n\\uc[2up_left]             \u2557  (unicode style:2 up left)\n\\uc[2plus]                \u256c  (unicode style:2 plus)\n\\uc[2down_right]          \u255a  (unicode style:2 down right)\n\\uc[2down_left]           \u255d  (unicode style:2 down left)\n\\uc[2horizontal_c_down]   \u2566  (unicode style:2 horizontal center down)\n\\uc[2horizontal_c_up]     \u2569  (unicode style:2 horizontal center up)\n\\uc[2vertical_c_right]    \u2560  (unicode style:2 vertical center right)\n\\uc[2vertical_c_left]     \u2563  (unicode style:2 vertical center left)\n\\uc[1full_block]          \u2588  (unicode style:1 full block)")
    if argv1_logo:
      logo = argv1_logo
    else:
      logo = input(f"\nbanner {clr_cyan}>{all_reset} ")
    with open("banner.txt", "w", encoding="utf8") as edit_ascii:
      edit_ascii.write(logo)
    print(f"{clr_green}Successfully changed the banner.{all_reset}")
  except KeyboardInterrupt:
    print(f"{clr_yellow}Edit banner has been canceled.{all_reset}")
  except EOFError:
    print(f"{clr_yellow}Edit banner has been canceled.{all_reset}")
  except Exception as e:
    print(f"{clr_red}ERROR! idError: 3\nCannot save '{clr_cyan}banner.txt{clr_red}'{all_reset}\nError Python:\n{e}")

if asciiGUI.terminal_size('x') <= 72 or asciiGUI.terminal_size('y') <= 15:
  print(f"{clr_yellow}[WARNING!]{all_reset}\nThe current terminal size is much smaller than specified (x:72, y:15). This may cause ascii corruption in the Console shell.\nx: {asciiGUI.terminal_size('x')}\ny: {asciiGUI.terminal_size('y')}"); time.sleep(5)

command_logo()
while running_main:
  try:

    prompt_inp = input(f"{style_none}{clr_yellow}[{clr_green}console.py{clr_yellow}]{clr_cyan} > {all_reset}")

    commands = prompt_inp.split('\\;')
    for command in commands:
      cmd_inp = command.strip()
      if cmd_inp.lower() == "exit":
        clear_screen()
        def close_terminal():
          if os.name == 'posix':
            os.system('kill -9 $$')
          elif os.name == 'nt':
            os.system('taskkill /F /PID {}'.format(os.getpid()))
          else:
            raise OSError(f"{clr_red}ERROR! idError: 4\nError in close terminal.{all_reset}")
        running_main = False
        close_terminal()
        clear_screen()
      elif cmd_inp.lower() == "clear":
        clear_screen()
        command_logo()
      elif "del.new_ln=" in cmd_inp.lower():
        index = cmd_inp.index("del.new_ln=") + len("del.new_ln=")
        if cmd_inp[index:].strip().lower() == "true":
          del_new_ln_config = FILECONFIGSYSTEM('File/System Config/DELNEWLINE.console', 'w', True)
          print(f"Successfully changed to {clr_cyan}True{all_reset}")
        elif cmd_inp[index:].strip().lower() == "false":
          del_new_ln_config = FILECONFIGSYSTEM('File/System Config/DELNEWLINE.console', 'w', False)
          print(f"Successfully changed to {clr_cyan}False{all_reset}")
        else:
          print(f"{clr_red}ERROR! idError: 5\nERROR! '{all_reset}{cmd_inp[index:].strip()}{clr_red}'\nInvalid command. enable => [true or false]{all_reset}")
      elif "unicode.config=" in cmd_inp.lower():
        index = cmd_inp.index("unicode.config=") + len("unicode.config=")
        if cmd_inp[index:].strip().lower() == "true":
          ascii_unicode_config = FILECONFIGSYSTEM('File/System Config/ASCIIUNICODE.console', 'w', True)
          print(f"Successfully changed to {clr_cyan}True{all_reset}")
        elif cmd_inp[index:].strip().lower() == "false":
          ascii_unicode_config = FILECONFIGSYSTEM('File/System Config/ASCIIUNICODE.console', 'w', False)
          print(f"Successfully changed to {clr_cyan}False{all_reset}")
        else:
          print(f"{clr_red}ERROR! idError: 79\nERROR! '{all_reset}{cmd_inp[index:].strip()}{clr_red}'\nInvalid command. enable => [true or false]{all_reset}")
      elif "python.editor.line_num.config=" in cmd_inp.lower():
        index = cmd_inp.index("python.editor.line_num.config=") + len("python.editor.line_num.config=")
        if cmd_inp[index:].strip().lower() == "false":
          python_editor_line_num_config = FILECONFIGSYSTEM('File/System Config/PYTHONEDITORLINENUM.console', 'w', False)
          print(f"Successfully changed to {clr_cyan}False{all_reset}")
        elif cmd_inp[index:].strip().lower() == "true":
          python_editor_line_num_config = FILECONFIGSYSTEM('File/System Config/PYTHONEDITORLINENUM.console', 'w', True)
          print(f"Successfully changed to {clr_cyan}True{all_reset}")
        else:
          print(f"{clr_red}ERROR! idError: 96\nERROR! '{all_reset}{cmd_inp[index:].strip()}{clr_red}'\nInvalid command. enable => [true or false]{all_reset}")
      elif "edit.ascii_banner" in cmd_inp:
        if "edit.ascii_banner" == cmd_inp:
          edit_command_logo('')
        elif "edit.ascii_banner => " in cmd_inp:
          index_argv = cmd_inp.index("edit.ascii_banner => ") + len("edit.ascii_banner => ")
          edit_command_logo(cmd_inp[index_argv:])
      elif "edit.color.console " in cmd_inp:
        index = cmd_inp.index("edit.color.console ") + len("edit.color.console ")
        prompt_color = cmd_inp[index:].strip()
        if ("--clr[red]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_red}Success to change color: [RED] => [RED]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_red}Success to change color: [RED] => [GREEN]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_red}Success to change color: [RED] => [YELLOW]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_red}Success to change color: [RED] => [BLUE]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_red}Success to change color: [RED] => [MAGENTA]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_red}Success to change color: [RED] => [CYAN]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_red}Success to change color: [RED] => [WHITE]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_red}Success to change color: [RED] => [ORANGE]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_red}Success to change color: [RED] => [BLACK]{all_reset}")
        elif ("--clr[red]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_red = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_green}Success to change color: [RED] => [GRAY]{all_reset}")

        elif ("--clr[green]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_green}Success to change color: [GREEN] => [RED]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_green}Success to change color: [GREEN] => [GREEN]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_green}Success to change color: [GREEN] => [YELLOW]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_green}Success to change color: [GREEN] => [BLUE]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_green}Success to change color: [GREEN] => [MAGENTA]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_green}Success to change color: [GREEN] => [CYAN]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_green}Success to change color: [GREEN] => [WHITE]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_green}Success to change color: [GREEN] => [ORANGE]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_green}Success to change color: [GREEN] => [BLACK]{all_reset}")
        elif ("--clr[green]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_green = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_green}Success to change color: [GREEN] => [GRAY]{all_reset}")

        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [RED]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [GREEN]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [YELLOW]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [BLUE]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [MAGENTA]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [CYAN]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [WHITE]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [ORANGE]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [BLACK]{all_reset}")
        elif ("--clr[yellow]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_yellow = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_yellow}Success to change color: [YELLOW] => [GRAY]{all_reset}")

        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_blue}Success to change color: [BLUE] => [RED]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_blue}Success to change color: [BLUE] => [GREEN]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_blue}Success to change color: [BLUE] => [YELLOW]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_blue}Success to change color: [BLUE] => [BLUE]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_blue}Success to change color: [BLUE] => [MAGENTA]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_blue}Success to change color: [BLUE] => [CYAN]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_blue}Success to change color: [BLUE] => [WHITE]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_blue}Success to change color: [BLUE] => [ORANGE]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_blue}Success to change color: [BLUE] => [BLACK]{all_reset}")
        elif ("--clr[blue]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_blue = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_blue}Success to change color: [BLUE] => [GRAY]{all_reset}")

        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [RED]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [GREEN]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [YELLOW]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [BLUE]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [MAGENTA]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [CYAN]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [WHITE]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [ORANGE]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [BLACK]{all_reset}")
        elif ("--clr[magenta]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_magenta = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_magenta}Success to change color: [MAGENTA] => [GRAY]{all_reset}")

        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [RED]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [GREEN]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [YELLOW]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [BLUE]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [MAGENTA]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [CYAN]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [WHITE]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [ORANGE]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [BLACK]{all_reset}")
        elif ("--clr[cyan]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_cyan = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_cyan}Success to change color: [CYAN] => [GRAY]{all_reset}")

        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [RED]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [GREEN]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [YELLOW]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [BLUE]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [MAGENTA]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [CYAN]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [WHITE]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [ORANGE]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [BLACK]{all_reset}")
        elif ("--clr[orange]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_orange = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_orange}Success to change color: [ORANGE] => [GRAY]{all_reset}")

        elif ("--clr[white]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_white}Success to change color: [WHITE] => [RED]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_white}Success to change color: [WHITE] => [GREEN]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_white}Success to change color: [WHITE] => [YELLOW]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_white}Success to change color: [WHITE] => [BLUE]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_white}Success to change color: [WHITE] => [MAGENTA]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_white}Success to change color: [WHITE] => [CYAN]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_white}Success to change color: [WHITE] => [WHITE]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_white}Success to change color: [WHITE] => [ORANGE]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_white}Success to change color: [WHITE] => [BLACK]{all_reset}")
        elif ("--clr[white]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_white = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_white}Success to change color: [WHITE] => [GRAY]{all_reset}")

        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[red]', '\\clr[red]')
          print(f"{all_reset}Success to change color: [RESET] => [RED]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[green]', '\\clr[green]')
          print(f"{all_reset}Success to change color: [RESET] => [GREEN]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{all_reset}Success to change color: [RESET] => [YELLOW]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{all_reset}Success to change color: [RESET] => [BLUE]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{all_reset}Success to change color: [RESET] => [MAGENTA]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{all_reset}Success to change color: [RESET] => [CYAN]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[white]', '\\clr[white]')
          print(f"{all_reset}Success to change color: [RESET] => [WHITE]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{all_reset}Success to change color: [RESET] => [ORANGE]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[black]', '\\clr[black]')
          print(f"{all_reset}Success to change color: [RESET] => [BLACK]{all_reset}")
        elif ("--clr[reset]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{all_reset}Success to change color: [RESET] => [GRAY]{all_reset}")

        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_gray}Success to change color: [GRAY] => [RED]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_gray}Success to change color: [GRAY] => [GREEN]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_gray}Success to change color: [GRAY] => [YELLOW]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_gray}Success to change color: [GRAY] => [BLUE]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_gray}Success to change color: [GRAY] => [MAGENTA]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_gray}Success to change color: [GRAY] => [CYAN]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_gray}Success to change color: [GRAY] => [WHITE]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_gray}Success to change color: [GRAY] => [ORANGE]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_gray}Success to change color: [GRAY] => [BLACK]{all_reset}")
        elif ("--clr[gray]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_gray = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_gray}Success to change color: [GRAY] => [GRAY]{all_reset}")

        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[red]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[red]', '\\clr[red]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [RED]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[green]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[green]', '\\clr[green]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [GREEN]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[yellow]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[yellow]', '\\clr[yellow]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [YELLOW]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[blue]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[blue]', '\\clr[blue]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [BLUE]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[magenta]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[magenta]', '\\clr[magenta]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [MAGENTA]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[cyan]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[cyan]', '\\clr[cyan]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [CYAN]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[white]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[white]', '\\clr[white]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [WHITE]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[orange]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[orange]', '\\clr[orange]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [ORANGE]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[black]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[black]', '\\clr[black]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [BLACK]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[gray]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\r[0]', '\\r[0]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [RESET]")
        elif ("--clr[*all]" in prompt_color) and ("--nw=clr[reset]" in prompt_color):
          clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_black, clr_gray, all_reset = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\clr[gray]', '\\clr[gray]')
          print(f"{clr_red}[RED] {clr_green}[GREEN] {clr_yellow}[YELLOW] {clr_blue}[BLUE] {clr_magenta}[MAGENTA] {clr_cyan}[CYAN] {clr_white}[WHITE] {clr_orange}[ORANGE] {clr_gray}[GRAY]\n{all_reset}Success to change colors => [RESET]")

        elif ("--clr[*all]" in prompt_color) and ("-r" in prompt_color):
          clr_black, clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_gray, bgclr_black, bgclr_red, bgclr_green, bgclr_yellow, bgclr_blue, bgclr_magenta, bgclr_cyan, bgclr_white, bgclr_orange, bgclr_gray, all_reset, style_bold, style_italic, style_strike, style_underline, style_none = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '\\clr[black]', '\\clr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '\\clr[red]', '\\clr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '\\clr[green]', '\\clr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '\\clr[yellow]', '\\clr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '\\clr[blue]', '\\clr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '\\clr[magenta]', '\\clr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '\\clr[cyan]', '\\clr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '\\clr[white]', '\\clr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '\\clr[orange]', '\\clr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '\\clr[gray]', '\\clr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_black.sc', '\\bgclr[black]', '\\bgclr[black]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_red.sc', '\\bgclr[red]', '\\bgclr[red]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_green.sc', '\\bgclr[green]', '\\bgclr[green]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_yellow.sc', '\\bgclr[yellow]', '\\bgclr[yellow]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_blue.sc', '\\bgclr[blue]', '\\bgclr[blue]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_magenta.sc', '\\bgclr[magenta]', '\\bgclr[magenta]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_cyan.sc', '\\bgclr[cyan]', '\\bgclr[cyan]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_white.sc', '\\bgclr[white]', '\\bgclr[white]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_orange.sc', '\\bgclr[orange]', '\\bgclr[orange]'), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_gray.sc', '\\bgclr[gray]', '\\bgclr[gray]'), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '\\r[0]', '\\r[0]'), FILECONFIGSTYLESYSTEM('File/System Config/style/style_bold.sc', '\\style[bold]', '\\style[bold]'), FILECONFIGSTYLESYSTEM('File/System Config/style/style_italic.sc', '\\style[italic]', '\\style[italic]'), FILECONFIGSTYLESYSTEM('File/System Config/style/style_strike.sc', '\\style[strike]', '\\style[strike]'), FILECONFIGSTYLESYSTEM('File/System Config/style/style_underline.sc', '\\style[undline]', '\\style[undline]'), FILECONFIGSTYLESYSTEM('File/System Config/style/style_none.sc', '\\style[none]', '\\style[none]')
          print(f"{clr_black}[BLACK]\033[0m {clr_red}[RED]\033[0m {clr_green}[GREEN]\033[0m {clr_yellow}[YELLOW]\033[0m {clr_blue}[BLUE]\033[0m {clr_magenta}[MAGENTA]\033[0m {clr_cyan}[CYAN]\033[0m {clr_white}[WHITE]\033[0m {clr_orange}[ORANGE]\033[0m {clr_gray}[GRAY]\033[0m \n{bgclr_black}[BG BLACK]\033[0m {bgclr_red}[BG RED]\033[0m {bgclr_green}[BG GREEN]\033[0m {bgclr_yellow}[BG YELLOW]\033[0m {bgclr_blue}[BG BLUE]\033[0m {bgclr_magenta}[BG MAGENTA]\033[0m {bgclr_cyan}[BG CYAN]\033[0m {bgclr_white}[BG WHITE]\033[0m {bgclr_orange}[BG ORANGE]\033[0m {bgclr_gray}[BG GRAY]\033[0m\n{style_bold}[BOLD]\033[0m {style_italic}[ITALIC]\033[0m {style_strike}[STRIKE]\033[0m {style_underline}[UNDERLINE]\033[0m\n{all_reset}Success to reset colors.")
        elif ("--clr[*all]" in prompt_color) and ("-n" in prompt_color):
          clr_black, clr_red, clr_green, clr_yellow, clr_blue, clr_magenta, clr_cyan, clr_white, clr_orange, clr_gray, bgclr_black, bgclr_red, bgclr_green, bgclr_yellow, bgclr_blue, bgclr_magenta, bgclr_cyan, bgclr_white, bgclr_orange, bgclr_gray, all_reset, style_bold, style_italic, style_strike, style_underline, style_none = FILECONFIGSTYLESYSTEM('File/System Config/style/clr_black.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_red.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_green.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_yellow.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_blue.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_magenta.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_cyan.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_white.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_orange.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_black.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_red.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_green.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_yellow.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_blue.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_magenta.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_cyan.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_white.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/bgclr_orange.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/clr_gray.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/all_reset.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/style_bold.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/style_italic.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/style_strike.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/style_underline.sc', '', ''), FILECONFIGSTYLESYSTEM('File/System Config/style/style_none.sc', '', '')
          print(f"{clr_black}[BLACK]\033[0m {clr_red}[RED]\033[0m {clr_green}[GREEN]\033[0m {clr_yellow}[YELLOW]\033[0m {clr_blue}[BLUE]\033[0m {clr_magenta}[MAGENTA]\033[0m {clr_cyan}[CYAN]\033[0m {clr_white}[WHITE]\033[0m {clr_orange}[ORANGE]\033[0m {clr_gray}[GRAY]\033[0m\n{bgclr_black}[BG BLACK]\033[0m {bgclr_red}[BG RED]\033[0m {bgclr_green}[BG GREEN]\033[0m {bgclr_yellow}[BG YELLOW]\033[0m {bgclr_blue}[BG BLUE]\033[0m {bgclr_magenta}[BG MAGENTA]\033[0m {bgclr_cyan}[BG CYAN]\033[0m {bgclr_white}[BG WHITE]\033[0m {bgclr_orange}[BG ORANGE]\033[0m {bgclr_gray}[BG GRAY]\033[0m\n{style_bold}[BOLD]\033[0m {style_italic}[ITALIC]\033[0m {style_strike}[STRIKE]\033[0m {style_underline}[UNDERLINE]\033[0m\n{all_reset}Success to make all none.")
        else:
          print(f"{clr_red}ERROR! idError: 6\nERROR! '{all_reset}{prompt_color}{clr_red}'\nColor error or colors not found.{all_reset}\nCommand: '{clr_yellow}--clr[<name color>] --nw=[<new color>]{all_reset}'. Reset all color: '{clr_cyan}--clr[*all] -r{all_reset}'. Default color: '{clr_green}--clr[*all] -n{all_reset}'.")
      elif "edit.color.console" == cmd_inp:
        print(f"{clr_red}ERROR! idError: 76\nNo colors have been edited.{all_reset}")
      elif cmd_inp:
        if "ccl=" in cmd_inp:
          index = cmd_inp.index("ccl=") + len("ccl=")
          expression = cmd_inp[index:].strip()
          try:
            result = eval(replace_rules_ansi(expression.replace('^', '**').replace('pi', '3.1415926535897932384626433832795').replace('e', '2.7182818284590452353602874713527').replace('ans', f'{calculate_ans}')))
            print(f'{result:_}')
            calculate_ans = result
          except ZeroDivisionError:
            print(f"{clr_red}ERROR! idError: 7\nERROR! '{all_reset}{expression}{clr_red}'\nCannot divide by zero.{all_reset}")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 8\nERROR! '{all_reset}{expression}{clr_red}'\nInvalid calculate.\n<{clr_yellow+str(e)+clr_red}>{all_reset}")

        elif "sqrt=" in cmd_inp:
          index = cmd_inp.index("sqrt=") + len("sqrt=")
          expression = cmd_inp[index:].strip()
          try:
            result = math.sqrt(eval(replace_rules_ansi(expression.replace('^', '**').replace('pi', '3.1415926535897932384626433832795').replace('e', '2.7182818284590452353602874713527').replace('ans', f'{calculate_ans}'))))
            print(f"{result:_}")
            calculate_ans = result
          except ZeroDivisionError:
            print(f"{clr_red}ERROR! idError: 89\nERROR! '{all_reset}{expression}{clr_red}'\nCannot divide by zero.{all_reset}")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 9\nERROR! '{all_reset}{expression}{clr_red}'\nInvalid sqrt.\n<{clr_yellow+str(e)+clr_red}>{all_reset}")

        elif "cbrt=" in cmd_inp:
          index = cmd_inp.index("cbrt=") + len("cbrt=")
          expression = cmd_inp[index:].strip()
          try:
            result = math.cbrt(eval(replace_rules_ansi(expression.replace('^', '**').replace('pi', '3.1415926535897932384626433832795').replace('e', '2.7182818284590452353602874713527').replace('ans', f'{calculate_ans}'))))
            print(f"{result:_}")
            calculate_ans = result
          except ZeroDivisionError:
            print(f"{clr_red}ERROR! idError: 90\nERROR! '{all_reset}{expression}{clr_red}'\nCannot divide by zero.{all_reset}")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 10\nERROR! '{all_reset}{expression}{clr_red}'\nInvalid cbrt.\n<{clr_yellow+str(e)+clr_red}>{all_reset}")

        elif "factorial=" in cmd_inp:
          index = cmd_inp.index("factorial=") + len("factorial=")
          expression = cmd_inp[index:].strip()
          try:
            result = math.factorial(eval(replace_rules_ansi(expression.replace('^', '**').replace('pi', '3.1415926535897932384626433832795').replace('e', '2.7182818284590452353602874713527').replace('ans', f'{calculate_ans}'))))
            print(f"{result:_}")
            calculate_ans = result
          except ZeroDivisionError:
            print(f"{clr_red}ERROR! idError: 99\nERROR! '{all_reset}{expression}{clr_red}'\nCannot divide by zero.{all_reset}")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 100\nERROR! '{all_reset}{expression}{clr_red}'\nInvalid factorial.\n<{clr_yellow+str(e)+clr_red}>{all_reset}")

        elif "text=" in command:
          index = cmd_inp.index("text=") + len("text=")
          LINEs = asciiGUI.terminal_size('y')
          COLUMNs = asciiGUI.terminal_size('x')
          SECONDS, MINUTES, HOURS, DATES, MOUNTS, YEARS = datetime.datetime.now().strftime("%S"), datetime.datetime.now().strftime("%M"), datetime.datetime.now().strftime("%H"), datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%m"), datetime.datetime.now().strftime("%Y")
          print(replace_rules_ansi((cmd_inp[index:])))

        elif "color.check" == cmd_inp:
          print(f"\033[0mcolors   : {clr_black}[BLACK] \033[0m{clr_red}[RED] \033[0m{clr_green}[GREEN] \033[0m{clr_yellow}[YELLOW] \033[0m{clr_blue}[BLUE] \033[0m{clr_magenta}[MAGENTA] \033[0m{clr_cyan}[CYAN] \033[0m{clr_orange}[ORANGE] \033[0m{clr_gray}[GRAY]\003[0m")
          print(f"\033[0mbg colors: {bgclr_black}[BG BLACK]\033[0m {bgclr_red}[BG RED]\033[0m {bgclr_green}[BG GREEN]\033[0m {bgclr_yellow}[BG YELLOW]\033[0m {bgclr_blue}[BG BLUE]\033[0m {bgclr_magenta}[BG MAGENTA]\033[0m {bgclr_cyan}[BG CYAN]\033[0m {bgclr_orange}[BG ORANGE] \033[0m{bgclr_gray}[BG GRAY]\033[0m")
          print(f"\033[0mstyle    : {style_bold}[BOLD] \033[0m{style_italic}[ITALIC] \033[0m{style_strike}[STRIKE]\033[0m {style_underline}[UNDERLINE]\033[0m")

        elif "text.typing.file=" in cmd_inp:
          try:
            index = cmd_inp.index("text.typing.file=") + len("text.typing.file=")
            text = replace_rules_ansi(cmd_inp[index:])
            speed_typing = input("\nSPEED TYPING (#s or 'enter' to use random speed): ")
            with open(f'{text}', 'r', encoding='utf8') as text_file:
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
                print(f"{clr_red}ERROR! idError: 67\nERROR! '{all_reset}{min_rdm_speed}{clr_red}', '{all_reset}{max_rdm_speed}{clr_red}'\nInvalid value.{all_reset}")
              except KeyboardInterrupt or EOFError:
                print(f"{clr_yellow}Typing stoped.{all_reset}")
          except ValueError:
           print(f"{clr_red}ERROR! idError: 68\nERROR! '{all_reset}{speed_typing}{clr_red}'\nInvalid value.{all_reset}")
          except FileNotFoundError:
            print(f"{clr_red}ERROR! idError: 69\nERROR! '{all_reset}{text}{clr_red}'\nFile or Directory not found. Please check again path file.{all_reset}")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 70\nInvalid input.\n<{clr_yellow+str(e)+clr_red}>{all_reset}"); continue
  
        elif "text.typing" in cmd_inp:
          try:
            if "text.typing => " in cmd_inp:
              text, speed_typing = '', ''
              text = replace_rules_ansi(text)
              try:
                index_argv = cmd_inp.index("text.typing => ") + len("text.typing => ")
                text, speed_typing = map(str, cmd_inp[index_argv:].split('\\,'))
                speed_typing = speed_typing.strip()
              except:
                print(f"{clr_red}ERROR! idError: 85\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 2 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'text.typing => <text>\\,<speed>'{all_reset}"); continue
            elif cmd_inp == "text.typing":
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
                print(f"{clr_red}ERROR! idError: 11\nERROR! '{all_reset}{min_rdm_speed}{clr_red}', '{all_reset}{max_rdm_speed}{clr_red}'\nInvalid value.{all_reset}")
              except KeyboardInterrupt or EOFError:
                print(f"{clr_yellow}Typing stoped.{all_reset}")
          except ValueError:
            print(f"{clr_red}ERROR! idError: 12\nERROR! '{all_reset}{speed_typing}{clr_red}'\nInvalid value.{all_reset}")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 13\nInvalid input.\n<{clr_yellow+str(e)+clr_red}>{all_reset}"); continue


        elif "input=" in command:
          index = cmd_inp.index("input=") + len("input=")
          LINEs = asciiGUI.terminal_size('y')
          COLUMNs = asciiGUI.terminal_size('x')
          SECONDS, MINUTES, HOURS, DATES, MOUNTS, YEARS = datetime.datetime.now().strftime("%S"), datetime.datetime.now().strftime("%M"), datetime.datetime.now().strftime("%H"), datetime.datetime.now().strftime("%d"), datetime.datetime.now().strftime("%m"), datetime.datetime.now().strftime("%Y")
          inp = input(replace_rules_ansi((cmd_inp[index:])))
          vars_input = inp

        elif "len=" in cmd_inp:
          index = cmd_inp.index("len=") + len("len=")
          print(f"length '{clr_cyan}{replace_rules_ansi(cmd_inp[index:])}{all_reset}': {clr_green}{len(replace_rules_ansi(cmd_inp[index:]))}{all_reset}")

        elif "dt=" in cmd_inp:
          try:
            timesdt = int(input("How much text to duplicate: "))
            index = cmd_inp.index("dt=") + len("dt=")
            resultdt = cmd_inp[index:] * timesdt
            print(resultdt)
          except ValueError:
            print(f"{clr_red}ERROR! idError: 14\nERROR! '{all_reset}{timesdt}{clr_red}'\nInvalid value.{all_reset}"); continue
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 101\nInvalid input.\n<{clr_yellow+str(e)+clr_red}>{all_reset}")

        elif "bnr=" in cmd_inp:
          index = cmd_inp.index("bnr=") + len("bnr=")
          def translate_binary(text):
            binary_text = ' '.join(format(ord(char), '08b') for char in text)
            return binary_text
          binary_output = translate_binary(replace_rules_ansi(cmd_inp[index:]))
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
            print(f"{clr_red}ERROR! idError: 15\nERROR! '{all_reset}{cmd_inp[index:]}{clr_red}'\nInvalid binary.{all_reset}"); continue

        elif "mrs=" in cmd_inp:
          index = cmd_inp.index("mrs=") + len("mrs=")
          morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'}
          def translate_to_morse(text):
            morse_text = ' '.join(morse_code.get(char.upper(), '[None]') for char in text)
            return morse_text
          morse_output = translate_to_morse(replace_rules_ansi(cmd_inp[index:]))
          print(morse_output)

        elif cmd_inp == "python.editor":
          programs = []
          num = 0
          space = "     "
          write = True
          if ascii_unicode_config:
            print(f"{clr_yellow}Type '#$more' for more information commands.{all_reset}\n{uc_1_horizontal * 5}{uc_1_horizontalCdown if python_editor_line_num_config else uc_1_horizontal}{uc_1_horizontal * (asciiGUI.terminal_size('x') - 6)}")
          else:
            print(f"{clr_yellow}Type '#$more' for more information commands.{all_reset}\n{'-' * 5}+{'-' * (asciiGUI.terminal_size('x') - 6)}")
          while write:
            try:
              if ascii_unicode_config:
                num += 1
                space1 = space[:-len(str(num))]
                if python_editor_line_num_config:
                  text_py = input(f"{clr_cyan}{space1}{num}{all_reset}{uc_1_vertical}").replace("\\ln", "\n").replace('exit()', 'pass').replace("os.system('kill -9 $$')", 'pass').replace("os.system('taskkill /F /PID {}'.format(os.getpid()))", 'pass').replace('os.system("kill -9 $$"")', 'pass').replace('os.system("taskkill /F /PID {}".format(os.getpid()))', 'pass')
                else:
                  text_py = input().replace("\\ln", "\n").replace('exit()', 'pass').replace("os.system('kill -9 $$')", 'pass').replace("os.system('taskkill /F /PID {}'.format(os.getpid()))", 'pass').replace('os.system("kill -9 $$"")', 'pass').replace('os.system("taskkill /F /PID {}".format(os.getpid()))', 'pass')
                if text_py == '#$exit':
                  write = False
                elif text_py == '#$clear':
                  clear_screen()
                  print(f'{uc_1_horizontal * 5}{uc_1_horizontalCdown if python_editor_line_num_config else uc_1_horizontal}{uc_1_horizontal * (asciiGUI.terminal_size("x") - 6)}')
                elif text_py == '#$more':
                  print(f"('#$exit' to exit; '#$run' ro run; '#$clear' to clear.)")
                else:
                  programs.append(text_py)
                  if text_py == '#$run':
                    print(f'{uc_1_horizontal * 5}{uc_1_horizontalCup if python_editor_line_num_config else uc_1_horizontal}{uc_1_horizontal * (asciiGUI.terminal_size("x") - 6)}\n{clr_orange}Shell\n{all_reset}{uc_1_horizontal * asciiGUI.terminal_size("x")}')
                    exec('\n'.join(programs))
                    print(f"\n{all_reset}{clr_yellow}[Program finished]{all_reset}")
                    print(f'{uc_1_horizontal * 5}{uc_1_horizontalCdown if python_editor_line_num_config else uc_1_horizontal}{uc_1_horizontal * (asciiGUI.terminal_size("x") - 6)}')
                    programs = []
                    num = 0
                    space = "     "
              else:
                num += 1
                space1 = space[:-len(str(num))]
                text_py = input(f"{clr_cyan}{space1}{num}{all_reset} ").replace("\\ln", "\n").replace('exit()', 'pass').replace("os.system('kill -9 $$')", 'pass').replace("os.system('taskkill /F /PID {}'.format(os.getpid()))", 'pass').replace('os.system("kill -9 $$"")', 'pass').replace('os.system("taskkill /F /PID {}".format(os.getpid()))', 'pass')
                if text_py == '#$exit':
                  write = False
                elif text_py == '#$clear':
                  clear_screen()
                  print(f'{"-" * 5}{"+" if python_editor_line_num_config else "-"}{"-" * (asciiGUI.terminal_size("x") - 6)}')
                elif text_py == '#$more':
                  print(f"('#$exit' to exit; '#$run' ro run; '#$clear' to clear.)")
                else:
                  programs.append(text_py)
                  if text_py == '#$run':
                    print(f'{"-" * 5}{"+" if python_editor_line_num_config else "-"}{"-" * (asciiGUI.terminal_size("x") - 6)}\n{clr_orange}Shell\n{all_reset}{"-" * asciiGUI.terminal_size("x")}')
                    exec('\n'.join(programs))
                    print(f"\n{all_reset}{clr_yellow}[Program finished]{all_reset}")
                    print(f'{"-" * 5}{"+" if python_editor_line_num_config else "-"}{"-" * (asciiGUI.terminal_size("x") - 6)}')
                    programs = []
                    num = 0
                    space = "     "
            except KeyboardInterrupt:
              programs = []
              num = 0
              space = "     "
              if ascii_unicode_config:
                print(f"\n{clr_magenta}[KeyboardInterrupt]{all_reset}\n{uc_1_horizontal * 5}{uc_1_horizontalCdown if python_editor_line_num_config else uc_1_horizontal}{uc_1_horizontal * (asciiGUI.terminal_size('x') - 6)}")
                continue
              else:
                print(f"\n{clr_magenta}[KeyboardInterrupt]{all_reset}\n{'-' * 5}{'+' if python_editor_line_num_config else '-'}{'-' * (asciiGUI.terminal_size('x') - 6)}")
                continue
            except EOFError:
              programs = []
              num = 0
              space = "     "
              if ascii_unicode_config:
                print(f"\n{clr_magenta}[EOFError]{all_reset}\n{uc_1_horizontal * 5}{uc_1_horizontalCdown if python_editor_line_num_config else uc_1_horizontal}{uc_1_horizontal * (asciiGUI.terminal_size('x') - 6)}")
                continue
              else:
                print(f"\n{clr_magenta}[EOFError]{all_reset}\n{'-' * 5}{'+' if python_editor_line_num_config else '-'}{'-' * (asciiGUI.terminal_size('x') - 6)}")
                continue
            except Exception as e:
              programs = []
              num = 0
              space = "     "
              if ascii_unicode_config:
                print(f"{clr_red}ERROR! idError: 16\nError Python dettected! {clr_green}('#$exit' to exit; '#$run' ro run; '#$clear' to clear.){all_reset}\n{e}\n{uc_1_horizontal * 5}{uc_1_horizontalCdown if python_editor_line_num_config else uc_1_horizontal}{uc_1_horizontal * (asciiGUI.terminal_size('x') - 6)}")
                continue
              else:
                print(f"{clr_red}ERROR! idError: 103\nError Python dettected! {clr_green}('#$exit' to exit; '#$run' ro run; '#$clear' to clear.){all_reset}\n{e}\n{'-' * 5}{'+' if python_editor_line_num_config else '-'}{'-' * (asciiGUI.terminal_size('x') - 6)}")
                continue

        elif cmd_inp == "trm.s.get":
          ts_row = asciiGUI.terminal_size('y')
          ts_col = asciiGUI.terminal_size('x')
          print(f"Terminal Size:\ncol: {clr_green}{ts_col}{all_reset}\nrow: {clr_green}{ts_row}{all_reset}")

        elif "text.ascii_generated" in cmd_inp:
          if "text.ascii_generated => " in cmd_inp:
            try:
              index_argv = cmd_inp.index("text.ascii_generated => ") + len("text.ascii_generated => ")
              text, font, auto = map(str, cmd_inp[index_argv:].split('\\,'))
              font, auto = font.strip(), auto.strip()
            except:
              print(f"{clr_red}ERROR! idError: 82\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 3 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'text.ascii_generated => <text>\\,<font>\\,<width>'{all_reset}")
              continue
          elif "text.ascii_generated" == cmd_inp:
            text = input("\nTEXT: ")
            font = input("FONT: ")
            auto = input("WIDTH: ")
          text = replace_rules_ansi(text)
          terminal_x = asciiGUI.terminal_size('x')
          try:
            if auto.isdigit():
              try:
                auto = int(auto)
                print("=" * terminal_x)
                ascii_generated = pyfiglet.figlet_format(text=text, font=font, width=auto)
                print(ascii_generated)
                print("=" * terminal_x)
              except pyfiglet.FontNotFound:
                print(f"{clr_red}ERROR! idError: 17\nERROR! '{all_reset}{font}{clr_red}'\nFont not found.{all_reset}"); continue
              except pyfiglet.CharNotPrinted:
                print(f"{clr_red}ERROR! idError: 71\nERROR! '{all_reset}{auto}{clr_red}'\nCharNotPrinted. Width size is too small.{all_reset}"); continue
              except Exception as e:
                print(f"{clr_red}ERROR! idError: 72\nAn unexpected Error occurred.\n{all_reset}Error Python:\n{e}"); continue
            else:
              try:
                print("=" * terminal_x)
                ascii_generated = pyfiglet.figlet_format(text=text, font=font, width=terminal_x)
                print(ascii_generated)
                print("=" * terminal_x)
              except pyfiglet.FontNotFound:
                print(f"{clr_red}ERROR! idError: 18\nERROR! '{all_reset}{font}{clr_red}'\nFont not found.{all_reset}"); continue
              except pyfiglet.CharNotPrinted:
                print(f"{clr_red}ERROR! idError: 73\nERROR! '{all_reset}{terminal_x}{clr_red}'\nCharNotPrinted. Width size is too small.{all_reset}"); continue
              except Exception as e:
                print(f"{clr_red}ERROR! idError: 74\nAn unexpected Error occurred.\n{all_reset}Error Python:\n{e}"); continue
          except:
            print(f"{clr_red}ERROR! idError: 83\nAn unexpected Error occurred.\n{clr_yellow}'text.ascii_generated => <text>\\,<font>\\,<width>'{all_reset}"); continue

        elif "dom.get.ip_address=" in cmd_inp:
          index = cmd_inp.index("dom.get.ip_address=") + len("dom.get.ip_address=")
          host_name = replace_rules_ansi(cmd_inp[index:].strip())
          try:
            address = socket.gethostbyname(host_name)
            print(f"Domain Name: '{clr_cyan}{host_name}{all_reset}'\nIP Address: '{clr_green}{address}{all_reset}'")
          except:
            print(f"{clr_red}ERROR! idError: 19\nERROR! '{all_reset}{host_name}{clr_red}'\nInvalid domain or no internet connection.{all_reset}")

        elif "python.exec.file=" in cmd_inp:
          index = cmd_inp.index("python.exec.file=") + len("python.exec.file=")
          dir_file = cmd_inp[index:].strip()
          try:
            with open(f"{dir_file}", "r", encoding="utf8") as exec_file:
              py_file = exec_file.read().replace('exit()', 'pass').replace("os.system('kill -9 $$')", 'pass').replace("os.system('taskkill /F /PID {}'.format(os.getpid()))", 'pass').replace('os.system("kill -9 $$")', 'pass').replace('os.system("taskkill /F /PID {}".format(os.getpid()))', 'pass')
              exec(py_file)
            print(f"exit()\n{clr_yellow}Python program '{clr_green}{dir_file}{clr_yellow}' Finished.")
            continue
          except FileNotFoundError:
            print(f"{clr_red}ERROR! idError: 20\nERROR! '{all_reset}{dir_file}{clr_red}'\nFile or Directory is not Found. Please check your location path file.{all_reset}")
          except KeyboardInterrupt or EOFError:
            print(f"{clr_red}ERROR! idError: 98\nInvalid input.{all_reset}")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 21\nERROR! '{all_reset}{dir_file}{clr_red}'\nAn unknown Error occurred while trying to locate the specified file or a Python Error occurred in the target file.{all_reset}\n{e}")

        elif "cat_read.file=" in cmd_inp:
          index = cmd_inp.index("cat_read.file=") + len("cat_read.file=")
          dir_file_cat = cmd_inp[index:].strip()
          try:
            with open(f'{dir_file_cat}', 'r', encoding="utf8") as cat_file:
              file = cat_file.read()
              print(file)
            print(f"{clr_green}READ FILE: '{clr_cyan}{dir_file_cat}{clr_green}'{all_reset}")
          except FileNotFoundError:
            print(f"{clr_red}ERROR! idError: 22\nERROR! '{all_reset}{dir_file_cat}{clr_red}'\nFile or Directory is not Found. Please check your location path file.{all_reset}")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 23\nERROR! '{all_reset}{dir_file_cat}{clr_red}'\nAn unknown Error occurred while trying to locate the specified file.{all_reset}\nError Python:\n{e}")

        elif cmd_inp == "num_box_text.empty":
          clear_screen()
          print(f"{clr_yellow}exit: in line box = break\nclear: in line box = clear\n{all_reset}")
          num = 0
          space = "     "
          while True:
            num += 1
            space1 = space[:-len(str(num))]
            if ascii_unicode_config:
              box1 = input(f"{space1}{num}{uc_1_vertical}")
            else:
              box1 = input(f"{space1}{num} ")
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
            if ("official" == letter_type.strip()) and ("english" == language_type.strip()):
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
              print(asciiGUI.justify(letterhead1_inp, 'center', space=' ', width=72))
              print(asciiGUI.justify(letterhead2_inp, 'center', space=' ', width=72))
              print(asciiGUI.justify(f'({letterfrom_inp})', 'center', space=' ', width=71))
              print(asciiGUI.justify(mailing_address_inp, 'center', space=' ', width=72))
              print("========================================================================")
              current_time_fortime = datetime.datetime.now().strftime("%A %d, %B %Y")
              current_time_fornumberletter = datetime.datetime.now().strftime("%Y")
              print(asciiGUI.justify(current_time_fortime, 'right', space=' ', width=72))
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
              print(f"{uc_1_horizontal * 72}\nLetter tester.")
            elif ("un_official" == letter_type.strip()) and ("english" == language_type.strip()):
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
              print(f"\nletter <?\n{uc_1_horizontal * 72}")
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
              print(f"{uc_1_horizontal * 72}\nLetter tester.")
            elif ("official" == letter_type.strip()) and ("indonesian" == language_type.strip()):
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
              print(f"\nletter < ?\n{uc_1_horizontal * 72}")
              print(asciiGUI.justify(letterhead1_inp, 'center', space=' ', width=72))
              print(asciiGUI.justify(letterhead2_inp, 'center', space=' ', width=72))
              print(asciiGUI.justify(f'({letterfrom_inp})', 'center', space=' ', width=71))
              print(asciiGUI.justify(mailing_address_inp, 'center', space=' ', width=72))
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
              print(asciiGUI.justify(output_time_in, 'right', space=' ', width=72))
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
              print(f"{uc_1_horizontal * 72}\nLetter tester.")
            elif ("un_official" == letter_type.strip()) and ("indonesian" == language_type.strip()):
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
              print(f"\nletter <?\n{uc_1_horizontal * 72}")
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
              print(f"{uc_1_horizontal * 72}\nLetter tester.")
            else:
              print(f"{clr_red}ERROR! idError: 24\nERROR! '{all_reset}{removeCMD}{clr_red}'\nCommand not found.{all_reset}")
          except ValueError:
            print(f"{clr_red}ERROR! idError: 75\nERROR! '{all_reset}{removeCMD}{clr_red}'\nThe value entered is more or less than the command (requires 2 values).{all_reset}")
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
              print(f"{clr_red}ERROR! idError: 26\nNo mudule named '{clr_magenta}{import_cmd}{clr_red}'{all_reset}")
          except ModuleNotFoundError:
            print(f"{clr_red}ERROR! idError: 27\nImported module or Python Directory or File not found. Please do not edit Console files or directories!\n{clr_yellow}If you find this error delete this old Console file. Then reinstall the latest Console file!{all_reset}")
          except KeyboardInterrupt:
            print(" [KeyboardInterrupt] ")
          except EOFError:
            print(" [EOFError] ")
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 28\nAn unexpected Error Occurred! Please do not change any of the 'IMPORT' directories or files in the Console.{all_reset}\nError Python:\n{e}")

        elif cmd_inp == "import":
          print(f"{clr_red}ERROR! idError: 29\nNo module to import.{all_reset}")

        elif cmd_inp == "import.list":
          print("Import list in Console.\n\nlink (cmd)>> link-feeldreams.github.io/aboutyou\nlink (cmd)>> link-cobabuka.htmlku.repl.co\nproject (cmd)>> project-testkecocokanpasangan.consolePy\nproject (cmd)>> project-pekerjaancocoknama.consolePy\nproject (cmd)>> project-artisifatnama.consolePy\nfake (cmd)>> fake-cmd.windows10\nfake (cmd)>> fake-kali.linux\nfake (cmd)>> fake-iMacPro.apple\nascii (cmd)>> ascii-windows10.logo\nascii (cmd)>> ascii-apple.logo\nascii (cmd)>> ascii-kalilinux.logo\nascii (cmd)>> ascii-python.logo\nascii (cmd)>> ascii-ubuntu.logo\nascii (cmd)>> ascii-android.logo\nascii (cmd)>> ascii-memerctichum.gif\nascii (cmd)>> ascii-rgbcolor.gif\nascii (cmd)>> ascii-clockdigital.gif\ngit (cmd)>> git-camhackers.hack\nhack (cmd)>> hack-ddos.hack\ngames (cmd)>> games-classicsnake.game")

        elif "forms-c=" in cmd_inp:
          index = cmd_inp.index("forms-c=") + len("forms-c=")
          choice_many = replace_rules_ansi(cmd_inp[index:].strip())
          if not choice_many.isdigit():
            print(f"{clr_red}ERROR! idError: 31\nERROR! '{all_reset}{choice_many}{clr_red}'\nInvalid value.{all_reset}")
            continue
          try:
            if int(choice_many) >= 15:
              print(f"{clr_red}ERROR! idError: 102\nERROR! '{all_reset}{choice_many}{clr_red}'\nThe choice of questions exceeds the limit. Max: 15.{all_reset}")
              continue
            print(f"{clr_cyan}\nForms {choice_many} coice\n{all_reset}")
            title = input("TITLE FORMS: ")
            questions = []
            choices = []
            correct_answers = []
            question_number = 1
            while True:
              reach_here = input("Is the next question the last question? [y/n]: ")
              if reach_here.lower().strip() == "y" or reach_here.lower().strip() == "n":
                break
              else:
                continue
            while True:
              question = input(f"[{clr_cyan}{question_number}{all_reset}]: ")
              choices.append([])
              for i in range(int(choice_many)):
                choice = input(f"  {chr(65+i)}: ")
                choices[-1].append(choice)
              while True:
                correct_answer = input("Correct answer: ")
                if correct_answer.strip() == '':
                  print(f'{clr_yellow}The correct answer cannot be empty.{all_reset}')
                  continue
                break
              questions.append(question)
              correct_answers.append(correct_answer)
              if reach_here.lower().strip() == "y":
                break
              elif reach_here.lower().strip() == "n":
                while True:
                  reach_here = input("Is the next question the last question? [y/n]: ")
                  if reach_here.lower().strip() == "y" or reach_here.lower().strip() == "n":
                    break
                  continue
                question_number += 1
              else:
                print(f"{clr_red}ERROR! idError: 30\nERROR! '{all_reset}{reach_here}{clr_red}'\nCommand not found.{all_reset}")
                break
            if reach_here.lower().strip() == "y":
              clear_screen()
              score = round(100 / len(questions), 1)
              correct_count = 0
              wrong_answers = []
              terminal_x = asciiGUI.terminal_size('x')
              print("=" * terminal_x)
              print(clr_cyan + asciiGUI.justify(title, 'center', space=' ', width=terminal_x) + all_reset)
              print("=" * terminal_x)
              while True:
                for i, question in enumerate(questions, start=1):
                  print(f"\n{clr_cyan}{i}{all_reset}. {question}")
                  for j, choice in enumerate(choices[i-1]):
                    print(f"  {chr(65+j)}. {choice}")
                  while True:
                    answer = input(f"{clr_yellow}= {all_reset}")
                    if answer.strip() == '':
                      continue
                    break
                  if answer.upper() == correct_answers[i-1].upper():
                    correct_count += 1
                  else:
                    wrong_answers.append((i, correct_answers[i-1]))
                ask_is_end = input(f"\nThis form has been completed.\n[{clr_green}y{all_reset}] Do you want to see the final result or ...\n[{clr_yellow}n{all_reset}] Want to refill answer?\n\n[y/n]: ")
                if ask_is_end.lower().strip() == 'y':
                  break
                else:
                  correct_count = 0
                  wrong_answers = []
                  continue
              print(f"Final score: {clr_green}{correct_count * score}{all_reset}/{100}")
              if wrong_answers:
                print("Wrong answer:", ", ".join([f"{num} ({choice})" for num, choice in wrong_answers]))
          except KeyboardInterrupt or EOFError:
            print()
          except Exception as e:
            print(f"{clr_red}ERROR! idError: 32\nInvalid input.\n<{clr_yellow+str(e)+clr_red}>{all_reset}")

        elif cmd_inp == "time.get":
          current_time = datetime.datetime.now().strftime("%H:%M:%S %A %d, %B %Y")
          print(current_time)

        elif "ccl.time.d=" in cmd_inp:
          index = cmd_inp.index("ccl.time.d=") + len("ccl.time.d=")
          day = replace_rules_ansi(cmd_inp[index:].strip())
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
            print(f"{clr_blue}" + "From today '{}', Past time from {} Day: '{}'".format(time_format(datetime.datetime.now()), Number_days, cD_formated))
            print(f"{clr_green}" + "From today '{}', Next time from {} Day: '{}'".format(time_format(datetime.datetime.now()), Number_days, cU_formated) + f"{all_reset}")

        elif "ccl.time.hms=" in cmd_inp:
          index = cmd_inp.index("ccl.time.hms=") + len("ccl.time.hms=")
          data_time_hms = replace_rules_ansi(cmd_inp[index:].strip())
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
            print(f"{clr_red}ERROR! idError: 77\nERROR! '{all_reset}{data_time_hms}{clr_red}'\nAn unexpected Error occurred. Maybe (value or in : or ,){all_reset}")


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
          timedown_inp = replace_rules_ansi(cmd_inp[index:].strip())
          if not timedown_inp.replace('.', '').isdigit():
            print(f"{clr_red}ERROR! idError: 36\nERROR! '{all_reset}{timedown_inp}{clr_red}'\nInvalid value.{all_reset}")
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
              print(f"{clr_red}ERROR! idError: 37\nERROR! '{all_reset}{timedown_inp}{clr_red}'\nInvalid input.{all_reset}")

        elif "time.down.dhms.tick" in cmd_inp:
          if "time.down.dhms.tick => " in cmd_inp:
            try:
              index_argv = cmd_inp.index("time.down.dhms.tick => ") + len("time.down.dhms.tick => ")
              day_input, hours_input, minutes_input, seconds_input, tick_input = map(str, cmd_inp[index_argv:].split('\\,'))
              day_input, hours_input, minutes_input, seconds_input, tick_input = replace_rules_ansi(day_input.strip()), replace_rules_ansi(hours_input.strip()), replace_rules_ansi(minutes_input.strip()), replace_rules_ansi(seconds_input.strip()), replace_rules_ansi(tick_input.strip())
            except:
              print(f"{clr_red}ERROR! idError: 106\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 5 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'time.down.dhms.tick => <set day>\\,<set hours>\\,<set minutes.\\,<set seconds>\\,<set tick>'{all_reset}"); continue
          elif cmd_inp == "time.down.dhms.tick":
            day_input = input("\nSET DAY: ")
            hours_input = input("SET HOURS: ")
            minutes_input = input("SET MINUTES: ")
            seconds_input = input("SET SECONDS: ")
            tick_input = input("SET TICK: ")
            day_input, hours_input, minutes_input, seconds_input, tick_input = replace_rules_ansi(day_input.strip()), replace_rules_ansi(hours_input.strip()), replace_rules_ansi(minutes_input.strip()), replace_rules_ansi(seconds_input.strip()), replace_rules_ansi(tick_input.strip())
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
            if set_hours < 0 or set_hours > 23:
              print(f"{clr_red}Hours must be entered between 0 - 23{all_reset}")
              continue
            if set_minutes < 0 or set_minutes > 59:
              print(f"{clr_red}Minutes must be entered between 0 - 59{all_reset}")
              continue
            if set_seconds < 0 or set_seconds > 59:
              print(f"{clr_red}Seconds must be entered between 0 - 59{all_reset}")
              continue
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

        elif "time.down.dhms" in cmd_inp:
          day_input = ''
          hours_input = ''
          minutes_input = ''
          seconds_input = ''
          if "time.down.dhms => " in cmd_inp:
            try:
              index_argv = cmd_inp.index("time.down.dhms => ") + len("time.down.dhms => ")
              day_input, hours_input, minutes_input, seconds_input = map(str, cmd_inp[index_argv:].split('\\,'))
              day_input, hours_input, minutes_input, seconds_input = replace_rules_ansi(day_input.strip()), replace_rules_ansi(hours_input.strip()), replace_rules_ansi(minutes_input.strip()), replace_rules_ansi(seconds_input.strip())
            except:
              print(f"{clr_red}ERROR! idError: 105\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 4 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'time.down.dhms => <set day>\\,<set hours>\\,<set minutes.\\,<set seconds>'{all_reset}"); continue
          elif cmd_inp == "time.down.dhms":
            day_input = input("\nSET DAY: ")
            hours_input = input("SET HOURS: ")
            minutes_input = input("SET MINUTES: ")
            seconds_input = input("SET SECONDS: ")
            day_input, hours_input, minutes_input, seconds_input = replace_rules_ansi(day_input.strip()), replace_rules_ansi(hours_input.strip()), replace_rules_ansi(minutes_input.strip()), replace_rules_ansi(seconds_input.strip())
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
            if set_hours < 0 or set_hours > 23:
              print(f"{clr_red}Hours must be entered between 0 - 23{all_reset}")
              continue
            if set_minutes < 0 or set_minutes > 59:
              print(f"{clr_red}Minutes must be entered between 0 - 59{all_reset}")
              continue
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
            print(f"{clr_red}ERROR! idError: 40\nERROR! '{all_reset}{timedown_inp}{clr_red}'\nInvalid value.{all_reset}")
          except KeyboardInterrupt or EOFError:
            print(f"{clr_red}ERROR! idError: 41\nInvalid input.{all_reset}")

        elif "time.down$[set]=" in cmd_inp:
          try:
            index = cmd_inp.index("time.down$[set]=") + len("time.down$[set]=")
            timedown_e_inp = replace_rules_ansi(cmd_inp[index:].strip())
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
            print(f"{clr_red}ERROR! idError: 42\nERROR! '{all_reset}{timedown_e_inp}{clr_red}'\nInvalid value.{all_reset}")
          except KeyboardInterrupt or EOFError:
            print(f"{clr_red}ERROR! idError: 43\nInvalid input.{all_reset}")

        elif "time.sleep=" in cmd_inp:
          try:
            index = cmd_inp.index("time.sleep=") + len("time.sleep=")
            time.sleep(float(replace_rules_ansi(cmd_inp[index:].strip())))
          except ValueError:
            print(f"{clr_red}ERROR! idError: 94\nERROR! '{all_reset}{cmd_inp[index:].strip()}{clr_red}'\nInvalid value.{all_reset}")
          except KeyboardInterrupt or EOFError:
            print(f"{clr_red}ERROR! idError: 95\nInvalid input.{all_reset}")

        elif "prompt" in cmd_inp:
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
                  if "prompt => " in cmd_inp:
                    index_argv = cmd_inp.index("prompt => ") + len("prompt => ")
                    os.system(cmd_inp[index_argv:])
                    break
                  else:
                    command_style = f"{clr_cyan}{uc_1_UpRight}{uc_1_horizontal * 2}({clr_blue}Console-py@{name}{clr_cyan})-[{all_reset}{dir}{clr_cyan}]\n{uc_1_DownRight}{uc_1_horizontal}{clr_green}$ {all_reset}"
                elif os_name == "nt":
                  if "prompt => " in cmd_inp:
                    index_argv = cmd_inp.index("prompt => ") + len("prompt => ")
                    os.system(cmd_inp[index_argv:])
                    break
                  else:
                    command_style = f"{clr_blue}{uc_1_UpRight}{uc_1_horizontal * 2}({clr_red}Console-py@{name}{clr_blue})-[{all_reset}{dir}{clr_blue}]\n{uc_1_DownRight}{uc_1_horizontal}{clr_green}> {all_reset}"
                else:
                  if "prompt => " in cmd_inp:
                    index_argv = cmd_inp.index("prompt => ") + len("prompt => ")
                    os.system(cmd_inp[index_argv:])
                    break
                  else:
                    command_style = f"Console-py@{name}:{dir} # "
              command = input(command_style)
              if command == "exit":
                break
              else:
                os.system(command)
            except KeyboardInterrupt or EOFError:
              print()
            except Exception as e:
              print(f"{clr_red}ERROR! idError: 78\nError: \n{all_reset}{e}")

        elif "rdm.[0,1]" in cmd_inp:
          if "rdm.[0,1] => " in cmd_inp:
            try:
              index_argv = cmd_inp.index("rdm.[0,1] => ") + len("rdm.[0,1] => ")
              tick_inp, timeout_inp = map(str, cmd_inp[index_argv:].split('\\,'))
              tick_inp, timeout_inp = replace_rules_ansi(tick_inp.strip()), replace_rules_ansi(timeout_inp.strip())
            except:
              print(f"{clr_red}ERROR! idError: 86\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 2 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'rdm.[0,1] => <tick>\\,<timeout>'{all_reset}"); continue
          elif cmd_inp == "rdm.[0,1]":
            tick_inp = input("\nTICK (#s): ")
            timeout_inp = input("TIMEOUT (#s): ")
            tick_inp, timeout_inp = replace_rules_ansi(tick_inp.strip()), replace_rules_ansi(timeout_inp.strip())
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
                terminal_x = asciiGUI.terminal_size('x')
                random_string = generate_random_string(terminal_x)
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

        elif "rdm.[n]" in cmd_inp:
          if "rdm.[n] => " in cmd_inp:
            try:
              index_argv = cmd_inp.index("rdm.[n] => ") + len("rdm.[n] => ")
              tick_inpN, timeout_inpN = map(str, cmd_inp[index_argv:].split('\\,'))
              tick_inpN, timeout_inpN = replace_rules_ansi(tick_inpN.strip()), replace_rules_ansi(timeout_inpN.strip())
            except:
              print(f"{clr_red}ERROR! idError: 87\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 2 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'rdm.[n] => <tick>\\,<timeout>'{all_reset}"); continue
          elif cmd_inp == "rdm.[n]":
            tick_inpN = input("\nTICK (#s): ")
            timeout_inpN = input("TIMEOUT (#s): ")
            tick_inpN, timeout_inpN = replace_rules_ansi(tick_inpN.strip()), replace_rules_ansi(timeout_inpN.strip())
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
                terminal_x = asciiGUI.terminal_size('x')
                random_string = generate_random_string(terminal_x)
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

        elif "rdm.[custom]" in cmd_inp:
          if "rdm.[custom] => " in cmd_inp:
            try:
              index_argv = cmd_inp.index("rdm.[custom] => ") + len("rdm.[custom] => ")
              characters_inp, tick_inp, timeout_inp = map(str, cmd_inp[index_argv:].split('\\,'))
              tick_inp, timeout_inp = replace_rules_ansi(tick_inp.strip()), replace_rules_ansi(timeout_inp.strip())
            except:
              print(f"{clr_red}ERROR! idError: 88\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 3 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'rdm.[custom] => <characters>\\,<tick>\\,<timeout>'{all_reset}"); continue
          elif cmd_inp == "rdm.[custom]":
            tick_inp = input("\nTICK (#s): ")
            timeout_inp = input("TIMEOUT (#s): ")
            characters_inp = input("CHARACTERS: ")
            tick_inp, timeout_inp = replace_rules_ansi(tick_inp.strip()), replace_rules_ansi(timeout_inp.strip())
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
                terminal_x = asciiGUI.terminal_size('x')
                random_string = generate_random_string(terminal_x)
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
            if "gs_th_num => " in game_inp.lower():
              try:
                index_argv = game_inp.index("gs_th_num => ") + len("gs_th_num => ")
                min, max, max_tebakan = map(str, game_inp[index_argv:].split('\\,'))
                min, max, max_tebakan = replace_rules_ansi(min.strip()), replace_rules_ansi(max.strip()), replace_rules_ansi(max_tebakan.strip())
              except:
                print(f"{clr_red}ERROR! idError: 91\nERROR! '{all_reset}{game_inp[index_argv:]}{clr_red}'\nNeed 3 arguments got " + str(len(game_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'games=gs_th_num => <min>\\,<max>\\,<tries>'{all_reset}"); continue
            elif "gs_th_num" in game_inp.lower():
              min = input("Minimum number: ")
              max = input("Maximum number: ")
              max_tebakan = input("Tries: ")
              min, max, max_tebakan = replace_rules_ansi(min.strip()), replace_rules_ansi(max.strip()), replace_rules_ansi(max_tebakan.strip())
            print(f"{clr_cyan}\nGuess The Numbers!\n{all_reset}")
            try:
              min = int(min)
              max = int(max)
              max_tebakan = int(max_tebakan)
            except ValueError:
              print(f"{clr_red}ERROR! idError: 50\nInvalid value.{all_reset}")
              continue
            except Exception as e:
              print(f"{clr_red}ERROR! idError: 51\nInvalid input.\n<{clr_yellow+str(e)+clr_red}>{all_reset}")
              continue
            def tebak_angka():
              if del_new_ln_config:
                clear_screen()
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
            print(f"\n{clr_cyan}Hangman!{all_reset}\n")
            if "hgmn => " in game_inp.lower():
              try:
                index_argv = cmd_inp.index("hgmn => ") + len("hgmn => ")
                language_game, difficulty_game = map(str, cmd_inp[index_argv:].split('\\,'))
                language_game, difficulty_game = language_game.strip(), difficulty_game.strip()
              except:
                print(f"{clr_red}ERROR! idError: 92\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 2 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'games=hgmn => <language>\\,<difficulty>'{all_reset}"); continue
            elif "hgmn" in game_inp.lower():
              print(f"\nSelect a language / Pilih bahasa\n1. English (Inggris)\n2. Indonesia")
              language_game = input("= ")[:1]
              print("\nSelect a difficulty")
              print(f"1. {clr_green}Easy{all_reset}      (3 letters) (have 15 tries)")
              print(f"2. {clr_blue}Normal{all_reset}    (4 letters) (have 10 tries)")
              print(f"3. {clr_yellow}Medium{all_reset}    (5 letters) (have 8 tries)")
              print(f"4. {clr_red}Hard{all_reset}      (6 letters) (have 6 tries)")
              print(f"5. {clr_magenta}Very hard{all_reset} (7 letters) (have 5 tries)")
              difficulty_game = input("= ")[:1]
            ascii_help_eng = "   ____\n  |/   |\n  |   (_) [Please help me :(]\n  |   \\|/ //\n  |    |\n  |   / \\\n  |\n__|__\n"
            ascii_win_eng = "   ____\n  |/   |\n  |\n  |\n  |   (_) [Thanks you for helping me :D]\n  |   \\|/ //\n  |    |\n__|__ / \\\n"
            ascii_lose_eng = "   ____\n  |/   |\n  |   (x) [*dead]\n  |   \\|/ //\n  |    |\n  |   / \\\n  |\n__|__"
            ascii_help_ind = "   ____\n  |/   |\n  |   (_) [Tolong bantu aku :(]\n  |   \\|/ //\n  |    |\n  |   / \\\n  |\n__|__\n"
            ascii_win_ind = "   ____\n  |/   |\n  |\n  |\n  |   (_) [Terima kasih telah membantuku :D]\n  |   \\|/ //\n  |    |\n__|__ / \\\n"
            ascii_lose_ind = "   ____\n  |/   |\n  |   (x) [*mati]\n  |   \\|/ //\n  |    |\n  |   / \\\n  |\n__|__"
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
              print(f"{clr_red}ERROR! idError: 53\nERROR! '{all_reset}{language_game}{clr_red}', '{all_reset}{difficulty_game}{clr_red}'\nCommand not found.{all_reset}")

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
              if del_new_ln_config:
                clear_screen()
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
                print(f"=====[ {clr_cyan}    Series!   {all_reset} ]=====\n\nSeries: {clr_cyan}{series_count}{all_reset} | Computer: {clr_yellow}{computer_count}{all_reset} | You: {clr_green}{player_count}{all_reset} | Played: {clr_magenta}{played}{all_reset}\n")
              elif result == 1:
                played += 1
                player_count += 1
                print(f"=====[ {clr_green}   You wins!  {all_reset} ]=====\n\nSeries: {clr_cyan}{series_count}{all_reset} | Computer: {clr_yellow}{computer_count}{all_reset} | You: {clr_green}{player_count}{all_reset} | Played: {clr_magenta}{played}{all_reset}\n")
              else:
                played += 1
                computer_count += 1
                print(f"=====[ {clr_yellow}Computer wins!{all_reset} ]=====\n\nSeries: {clr_cyan}{series_count}{all_reset} | Computer: {clr_yellow}{computer_count}{all_reset} | You: {clr_green}{player_count}{all_reset} | Played: {clr_magenta}{played}{all_reset}\n")

          elif "ti_ta_to-bot" in game_inp.lower():
            try:
              print(f"{clr_cyan}\nTic Tac Toe (bot)\n{all_reset}")
              def print_board(board):
                count_strip = 0
                if ascii_unicode_config:
                  print(f"{uc_1_UpRight}{(uc_1_horizontal * 3 + uc_1_horizontalCdown) * 2}{uc_1_horizontal * 3}{uc_1_UpLeft}")
                  for row in board:
                    print(f"{uc_1_vertical}", end=" ")
                    for cell in row:
                      if cell == "X":
                        print((f"{clr_red}{cell}{all_reset}"), end=f" {uc_1_vertical} ")
                      elif cell == "O":
                        print((f"{clr_cyan}{cell}{all_reset}"), end=f" {uc_1_vertical} ")
                      else:
                        print(cell, end=f" {uc_1_vertical} ")
                    count_strip += 1
                    if count_strip < 3:
                      print(f"\n{uc_1_verticalCright}{(uc_1_horizontal * 3 + uc_1_Plus) * 2}{uc_1_horizontal * 3}{uc_1_verticalCleft}")
                    else:
                      print(f"\n{uc_1_DownRight}{(uc_1_horizontal * 3 + uc_1_horizontalCup) * 2}{uc_1_horizontal * 3}{uc_1_DownLeft}")
                else:
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
                  if del_new_ln_config:
                    clear_screen()
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
            except Exception as e:
              print(f"{clr_red}ERROR! idError: 80\nAn unexpected error occurred.\n{all_reset}Error Python:\n{e}")
              continue
          elif "numpuz" in game_inp.lower():
            print(f"{clr_cyan}\nNumpuz\n{all_reset}")
            if "numpuz => " in game_inp.lower():
              index_argv = game_inp.index("numpuz => ") + len("numpuz => ")
              input_level = replace_rules_ansi(game_inp[index_argv:])
            elif "numpuz" in game_inp.lower():
              input_level = replace_rules_ansi(input("Input Level (3-10): "))
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
                    if ascii_unicode_config:
                      print(f'{uc_1_UpRight}' + f'{uc_1_horizontal * 4 + uc_1_horizontalCdown}' * (self.size - 1) + f'{uc_1_horizontal * 4 + uc_1_UpLeft}')
                      for i in range(self.size):
                        if i == 0:
                          pass
                        else:
                          print(f'{uc_1_verticalCright}' + f'{uc_1_horizontal * 4 + uc_1_Plus}' * (self.size - 1) + f'{uc_1_horizontal * 4 + uc_1_verticalCleft}')
                        for j in range(self.size):
                          print(f'{uc_1_vertical}{clr_cyan}' + '{:^4}'.format(self.board[i][j]) + f'{all_reset}', end='')
                        print(f'{uc_1_vertical}')
                      print(f'{uc_1_DownRight}' + f'{uc_1_horizontal * 4 + uc_1_horizontalCup}' * (self.size - 1) + f'{uc_1_horizontal * 4 + uc_1_DownLeft}')
                    else:
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
            try:
              print(f"{clr_cyan}\nMinesweeper\n{all_reset}")
              try:
                bombs_limit_min = {
                  6:5, 7:5, 8:5, 9:5, 10:5, 11:5, 12:5, 13:5, 14:5, 15:5, 16:5, 17:5, 18:5, 19:5, 20:5,
                  21:10, 22:10, 23:10,
                  24:15, 25:15, 26:15,
                  27:20, 28:20, 29:20, 30:20, 31:20, 32:20,
                  33:25, 34:25, 35:25
                }
                bombs_limit_max = {
                  6:30, 7:40, 8:60, 9:70, 10:90, 11:110, 12:130, 13:160, 14:190, 15:220, 16:250, 17:280, 18:310, 19:350, 20:390,
                  21:430, 22:470, 23:520,
                  24:570, 25:620, 26:670,
                  27:720, 28:770, 29:830, 30:890, 31:950, 32:1010,
                  33:1080, 34:1150, 35:1220
                }
                if "minswe => " in game_inp.lower():
                  try:
                    index_argv = game_inp.index("minswe => ") + len("minswe => ")
                    size, bomb = map(str, game_inp[index_argv:].split('\\,'))
                    size, bomb = int(replace_rules_ansi(size.strip())), int(replace_rules_ansi(bomb.strip()))
                  except:
                    print(f"{clr_red}ERROR! idError: 93\nERROR! '{all_reset}{game_inp[index_argv:]}{clr_red}'\nNeed 2 arguments got " + str(len(game_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'games=minswe => <size>\\,<bomb>'{all_reset}"); continue
                elif "minswe" in game_inp.lower():
                  size = replace_rules_ansi(input("Size (6-35): "))
                  size = int(size)
                  try:
                    bomb = replace_rules_ansi(input(f"Bomb ({bombs_limit_min[size]}-{bombs_limit_max[size]}): "))
                  except KeyError:
                    if size <= 6:
                      print(f"{clr_red}ERROR! idError: 104\nERROR! '{all_reset}{size}{clr_red}'\nSize too small!")
                      continue
                    elif size >= 35:
                      print(f"{clr_red}ERROR! idError: 97\nERROR! '{all_reset}{size}{clr_red}'\nSize too big!")
                      continue
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
                              visible_board[row][col] = f' {color_mapping[cell_value]}{cell_value}{all_reset} '
                        else:
                          visible_board[row][col] = ' '
                    string_rep = ''
                    if ascii_unicode_config:
                      indices_row = f'   {clr_cyan}' + ' '.join([f'{i:^3}' for i in range(self.dim_size)]) + f'{all_reset}\n'
                      separator_row = f'  {uc_1_verticalCright}' + f'{uc_1_horizontal * 3}{uc_1_Plus}' * ((remove_ansi_len(indices_row) - 5) // 4) + f'{uc_1_horizontal * 3}{uc_1_verticalCleft}\n'
                      border_board_top = f'  {uc_1_UpRight}' + f'{uc_1_horizontal * 3}{uc_1_horizontalCdown}' * ((remove_ansi_len(indices_row) - 5) // 4) + f'{uc_1_horizontal * 3}{uc_1_UpLeft}\n'
                      string_rep += indices_row + border_board_top
                      for i in range(len(visible_board)):
                        row = visible_board[i]
                        cells = [f'{cell:^3}' for cell in row]
                        add_space_string_rep = ' ' if len(f'{i}') == 1 else ''
                        string_rep += f'{clr_cyan}{i}{all_reset}{add_space_string_rep}{uc_1_vertical}' + f'{uc_1_vertical}'.join(cells) + f'{uc_1_vertical}\n'
                        if i < (len(visible_board) - 1):
                          string_rep += separator_row
                      string_rep += f'  {uc_1_DownRight}' + f'{uc_1_horizontal * 3}{uc_1_horizontalCup}' * ((remove_ansi_len(indices_row) - 5) // 4) + f'{uc_1_horizontal * 3}{uc_1_DownLeft}\n'
                    else:
                      indices_row = f'   {clr_cyan}' + ' '.join([f'{i:^3}' for i in range(self.dim_size)]) + f'{all_reset}\n'
                      separator_row = f'  +' + f'---+' * ((remove_ansi_len(indices_row) - 5) // 4) + f'---+\n'
                      border_board_top = f'  +' + f'---+' * ((remove_ansi_len(indices_row) - 5) // 4) + f'---+\n'
                      string_rep += indices_row + border_board_top
                      for i in range(len(visible_board)):
                        row = visible_board[i]
                        cells = [f'{cell:^3}' for cell in row]
                        add_space_string_rep = ' ' if len(f'{i}') == 1 else ''
                        string_rep += f'{clr_cyan}{i}{all_reset}{add_space_string_rep}|' + f'|'.join(cells) + f'|\n'
                        if i < (len(visible_board) - 1):
                          string_rep += separator_row
                      string_rep += f'  +' + f'---+' * ((remove_ansi_len(indices_row) - 5) // 4) + f'---+\n'
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
                    if user_input == "!":
                      pass
                    else:
                      print(board)
                      print(f"{clr_green}Congratulations! You won!{all_reset}")
                  else:
                    print(f"{clr_red}Sorry, You lose!{all_reset}")
                    board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
                    print(board)
                if bomb >= bombs_limit_min[size] and bomb <= bombs_limit_max[size]:
                  if __name__ == '__main__':
                    play(dim_size=size, num_bombs=bomb)
                else:
                  print(f"{clr_red}ERROR! idError: 60\nOver Size, Bomb!{all_reset}\n")
                  for i in range(30):
                    print(f'{i+6}: {bombs_limit_min[i+6]}-{bombs_limit_max[i+6]}')
              except ValueError:
                print(f"{clr_red}ERROR! idError: 61\nInvalid value.{all_reset}")
            except Exception as e:
              print(f"{clr_red}ERROR! idError: 81\nAn unexpected error occurred.\n{all_reset}Error Python:\n{e}")
              continue
          else:
            print(f"{clr_red}ERROR! idError: 62\nERROR! '{all_reset}{game_inp}{clr_red}'\nCommand not found.{all_reset}")

        elif "dupl.text" in cmd_inp:
          if "dupl.text => " in cmd_inp:
            try:
              index_argv = cmd_inp.index("dupl.text => ") + len("dupl.text => ")
              text_inp, tick_inp, timeout_inp = map(str, cmd_inp[index_argv:].split('\\,'))
              tick_inp, timeout_inp = tick_inp.strip(), timeout_inp.strip()
            except:
              print(f"{clr_red}ERROR! idError: 84\nERROR! '{all_reset}{cmd_inp[index_argv:]}{clr_red}'\nNeed 3 arguments got " + str(len(cmd_inp[index_argv:].split('\\,'))) + f".\n{clr_yellow}'dupl.text => <text>\\,<tick>\\,<timeout>'{all_reset}"); continue
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
          print(f"{clr_red}ERROR! Invalid-1\nERROR! '{all_reset}{cmd_inp}{clr_red}'\nInvalid command.{all_reset}")

  except EOFError:
    print(f"\nYou just press [Ctrl + Z or D ({clr_red}EOFError{all_reset})]")
    continue
  except KeyboardInterrupt:
    print(f"\nYou just press [Ctrl + C ({clr_red}KeyboardInterrupt{all_reset})]")
    continue
  except Exception as e:
    print(f"\033[31mERROR! idError: 65\nAn unexpected Fatal Error occurred while running \033[36mconsole.py\033[31m. Don't worry! We'll fix it soon.\033[0m\nError Python:\n{e}")
    con_ex = input("Press ENTER to exit or 'c' to continue...")
    if con_ex.lower() == "c":
      continue
    else:
      exit()
  except:
    print("\033[31mERROR! idError: 66\nOops! Something Error!\033[0m")
    clear_screen()
    exit()