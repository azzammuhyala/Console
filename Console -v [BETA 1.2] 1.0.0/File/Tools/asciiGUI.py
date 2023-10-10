"""
======================= file_name: 'asciiGUI.py' =======================
======================= import_name : 'asciiGUI' =======================

Last Update: 10/10/2023
Description: This is a library of tools for you to use with your needs
               for an attractive type of terminal (console) display.
"""

# -- importing: time, os -- #
import time, os

# -- func: get terminal size | return True -- #
def terminal_size(get):
  if 'x' in get.lower():
    return os.get_terminal_size().columns
  elif 'y' in get.lower():
    return os.get_terminal_size().lines

# -- func: make color text terminal | return True -- #
def colored(text="colored(<Your text>, <color or style>, <add style1>, <add style2>)", style="white", style_parameters1="", style_parameters2=""):
  style, style_parameters1, style_parameters2 = style.strip(), style_parameters1.strip(), style_parameters2.strip()
  ansi_key = {
    # - STYLE - #
    "bold": "\033[1m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "strike": "\033[9m",
    # - COLOR - #
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "orange": "\033[38;5;208m",
    "gray": "\033[90m",
    # - BACKGROUND COLOR  - #
    "bg black": "\033[40m",
    "bg red": "\033[41m",
    "bg green": "\033[42m",
    "bg yellow": "\033[43m",
    "bg blue": "\033[44m",
    "bg magenta": "\033[45m",
    "bg cyan": "\033[46m",
    "bg white": "\033[47m",
    "bg orange": "\033[48;5;208m"
  }
  try:
    if style_parameters1:
      return f"{ansi_key[style] + ansi_key[style_parameters1]}{text}\033[0m"
    elif style_parameters2:
      return f"{ansi_key[style] + ansi_key[style_parameters2]}{text}\033[0m"
    elif style_parameters1 and style_parameters2:
      return f"{ansi_key[style] + ansi_key[style_parameters1] + ansi_key[style_parameters2]}{text}\033[0m"
    else:
      return f"{ansi_key[style]}{text}\033[0m"
  except:
    if style == "":
      return "CodeAnsiEmptyError: The ansi code is empty."
    else:
      return f"CodeAnsiNotFoundError: '{style}' The ansi code is not found."

# -- func: make a table ascii for terminal | return False -- #
def table(headers=(['headers']), data=([['data']]), using_unicode=True):
  table_main = ''
  column_widths = [max(len(str(item)) for item in column) for column in zip(headers, *data)]
  header_line =  "\u250c" + "\u252c".join("\u2500" * (width + 2) for width in column_widths) + "\u2510\n" if using_unicode else "+" + "+".join("-" * (width + 2) for width in column_widths) + "+\n"
  header = "\u2502" + "\u2502".join(f" {header.center(width)} " for header, width in zip(headers, column_widths)) + "\u2502\n" if using_unicode else "|" + "|".join(f" {header.center(width)} " for header, width in zip(headers, column_widths)) + "|\n"
  table_main += header_line
  table_main += header
  for row in data:
    row_line = "\u251c" + "\u253c".join("\u2500" * (width + 2) for width in column_widths) + "\u2524\n" if using_unicode else "+" + "+".join("-" * (width + 2) for width in column_widths) + "+\n"
    row_line_down = "\u2514" + "\u2534".join("\u2500" * (width + 2) for width in column_widths) + "\u2518" if using_unicode else "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
    row_content = "\u2502" + "\u2502".join(f" {str(item).ljust(width)} " for item, width in zip(row, column_widths)) + "\u2502\n" if using_unicode else "|" + "|".join(f" {str(item).ljust(width)} " for item, width in zip(row, column_widths)) + "|\n"
    table_main += row_line
    table_main += row_content
  table_main += row_line_down
  return table_main

# -- func: make animation typing text terminal | return False -- #
def typing(text="Hello World! - asciiGUI", speed=0.1):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(speed)
  print()

# -- func: make progress bar ascii terminal | return False -- #
def progress_bar(type='line', speed=0.1, width=50, clear=True, max=100, bar_progress="#", bar_space=".", bar_start_end="[]", text="Hello World! - asciiGUI", isdone=" "):
  if 'line' in type.lower():
    total = 100
    progress = 0
    bar_start = bar_start_end[:1]
    bar_end = bar_start_end[1:]
    max = int(max)
    width = int(width)
    speed = float(speed)
    width = width - len(str(max)) - 6
    for i in range(max * 10):
      progress += 1
      percent = total * (progress / float(total) / 10)
      filled_width = int(width * (progress // 10) // max)
      bar = f'{bar_progress}' * filled_width + f'{bar_space}' * (width - filled_width)
      print(f"\r{bar_start}{bar}{bar_end} {percent:.1f}%", end="\r") if clear else print(f"{bar_start}{bar}{bar_end} {percent:.1f}%")
      time.sleep(speed / 10)
  elif 'circle' in type.lower():
    circle_keys = {0: '-', 1:'\\', 2: '|', 3: '/'}
    count = 0
    while max >= 0:
      print(text + circle_keys[count], end='\r') if clear else print(text + circle_keys[count])
      count += 1
      max -= 1
      time.sleep(speed / 10)
      if count >= 4:
        count = 0
    print(text + isdone)

# -- func: make justify func for text | return True -- #
def justify(content='Hello World! - asciiGUI', make='center', width=50, space=' ', minus=0):
  content_pieces = []
  content_end = ''
  contents = ''
  if len(content) >= width:
    content_end = str(content[(len(content) // width) * width:])
    start_index = 0
    while start_index < len(content):
      if start_index + width <= len(content):
        content_pieces.append(content[start_index:start_index + width])
      start_index += width
  if 'center' in make.lower():
    if len(content) <= width:
      contents += space[:1] * ((width - len(content) - minus) // 2) + content + space[:1] * ((width - len(content) - minus) // 2)
    elif len(content) >= width:
      for item in content_pieces:
        contents += item
      contents += space[:1] * ((width - len(content_end) - minus) // 2) + content_end + space[:1] * ((width - len(content_end) - minus) // 2)
    return contents
  elif 'right' in make.lower():
    if len(content) <= width:
      contents += space[:1] * (width - len(content) - minus) + content
    elif len(content) >= width:
      for item in content_pieces:
        contents += item
      contents += space[:1] * (width - len(content_end) - minus) + content_end
    return contents