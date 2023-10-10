import curses
from signal import signal, SIGTERM, pause
from collections import namedtuple
from threading import Thread
from time import sleep
from random import choice, randint

time_sleep_input = 0.1
fps = int(1 / time_sleep_input)
game_on = False
keyboard_on = True
point = namedtuple("point", "y x")
number = namedtuple("number", "value color")
directions = {curses.KEY_UP: point(-1, 0), curses.KEY_DOWN: point(1, 0), curses.KEY_RIGHT: point(0, 1), curses.KEY_LEFT: point(0, -1)}
colors = (curses.COLOR_BLUE, curses.COLOR_CYAN, curses.COLOR_GREEN, curses.COLOR_MAGENTA, curses.COLOR_RED, curses.COLOR_YELLOW)

def safe_exit():
  exit(1)

def grow_food():
  global food
  while True:
    location = point(randint(1, terminal_y-3), randint(1, terminal_x-2))
    if location not in snake and location not in food:
      value = randint(1, 9)
      color = choice(colors)
      food[location] = number(value, color)
      game_area.addstr(location.y, location.x, f"{value}", curses.color_pair(color))
      break

def start_game():
  global snake, game, game_on, bearing, food, score, color_bands
  game_area.clear()
  bearing = choice(list(directions))
  snake = [point(terminal_y//2, terminal_x//2)]
  color_bands = [number(1, choice(colors))]
  game_area.addstr(snake[0].y, snake[0].x, "\u2588", curses.color_pair(color_bands[0].color))
  score = 0
  show_score()
  food = {}
  for __ in range(terminal_y//2):
    grow_food()
  game_area.border()
  game_area.refresh()
  gameover_popup.addstr(1, 15, "Game Over!", curses.color_pair(curses.COLOR_YELLOW))
  gameover_popup.addstr(2, 5, "Press Space Bar to Play Again!", curses.color_pair(curses.COLOR_GREEN))
  gameover_popup.border()
  game_on = True
  game = Thread(target=play, daemon=True)
  game.start()

def show_score():
  global hi_score, fps
  if score > hi_score:
    hi_score = score
  score_board.addstr(0, terminal_x//2-5, f"P1: {score:06d}", curses.color_pair(curses.COLOR_BLUE))
  score_board.addstr(0, terminal_x-11, f"HI: {hi_score:06d}", curses.color_pair(curses.COLOR_RED))
  score_board.addstr(0, terminal_x//terminal_x, f"FPS: {fps:03d}", curses.color_pair(curses.COLOR_GREEN))
  score_board.refresh()

def play():
  global keyboard_on
  try:
    while game_on:
      move_snake()
    gameover_popup.refresh()
    if hi_score == score:
      with open("File/IMPORT/games/ClassicSnake/snake.hi", "w", encoding='utf8') as hi:
        hi.write(str(hi_score))
  except Exception as e:
    keyboard_on = False
    curses.endwin()
    print(f"UNEXPECTED ERROR: {e}")
def move_snake():
  global game_on, score, fps
  growth = [color_bands[0].color]
  while growth:
    if bearing in [curses.KEY_UP, curses.KEY_DOWN]:
      sleep_duration = time_sleep_input * 2
      fps = int(1 / (time_sleep_input * 2))
    else:
      sleep_duration = time_sleep_input
      fps = int(1 / time_sleep_input)
    sleep(sleep_duration)
    new_location = point(snake[0].y + directions[bearing].y, snake[0].x + directions[bearing].x)
    show_score()
    if new_location in food:
      grow_food()
      game_area.refresh()
      color = food[new_location].color
      growth[0] = color
      growth[:0] = [color] * food[new_location].value
      score += food[new_location].value
      color_bands.insert(0, number(score+1, color))
      show_score()
      food.pop(new_location)
    snake.insert(0, new_location)
    game_area.addstr(new_location.y, new_location.x, "\u2588", curses.color_pair(growth[-1]))
    if new_location.y in (0, terminal_y-2) or new_location.x in (0, terminal_x-1) or new_location in snake[4:]:
      game_on = False
      break
    growth.pop(-1)
  game_area.addstr(snake[-1].y, snake[-1].x, " ")
  snake.pop(-1)
  for band in color_bands[1:]:
    segment = len(snake) - band.value
    game_area.addstr(snake[segment].y, snake[segment].x, "\u2588", curses.color_pair(band.color))
  game_area.refresh()

def main():
  global game_on, game_area, terminal_y, terminal_x, hi_score, score_board, gameover_popup, bearing, time_sleep_input
  while True:
    try:
      time_sleep_input = float(input('time.sleep (Delay) = '))
      break
    except:
      print('Invalid time sleep!')
      continue
  try:
    signal(SIGTERM, safe_exit)
    terminal = curses.initscr()
    terminal_y, terminal_x = terminal.getmaxyx()
    if terminal_y < 20 or terminal_x < 50:
      raise RuntimeError
    curses.curs_set(0)
    curses.noecho()
    curses.start_color()
    curses.use_default_colors()
    for color in colors:
      curses.init_pair(color, color, -1)
    score_board = curses.newwin(1, terminal_x, 0, 0)
    game_area = curses.newwin(terminal_y-1, terminal_x, 1, 0)
    game_area.keypad(True)
    game_area.timeout(50)
    gameover_popup = curses.newwin(4, 40, terminal_y//2-2, terminal_x//2-20)
    score_board.bkgd(curses.A_BOLD)
    game_area.bkgd(curses.A_BOLD)
    gameover_popup.bkgd(curses.A_BOLD | curses.color_pair(curses.COLOR_RED))
    try:
      with open("File/IMPORT/games/ClassicSnake/snake.hi", "r", encoding='utf8') as hi:
        hi_score = int(hi.read())
    except FileNotFoundError:
      hi_score = 0
    start_game()
    while keyboard_on:
      key = game_area.getch()
      if key in directions:
        if (directions[bearing].y + directions[key].y, directions[bearing].x + directions[key].x) != (0, 0) or not score:
          bearing = key
      elif not game_on and key == 32:
        start_game()
  except KeyboardInterrupt:
    pass
  except RuntimeError:
    curses.endwin()
    print("ERROR: Terminal window too small!")
    print("At least 50x20 characters dimensions are required")
    print(f"Current terminal dimensions are: {terminal_x}x{terminal_y}")
  finally:
    if game_on:
      game_on = False
      game.join()
    if not curses.isendwin():
      curses.endwin()