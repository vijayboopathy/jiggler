"""
Scope:
  1. Activate script when the shortcut is triggered.
  2. Stop script when the shortcut is tirggered again.
  3. Move mouse pointer by 5 pixel every 5 second
"""

from pyautogui import size, position, move, moveTo
import random
import time

move_by = 5 # pixels to move
frequency = 12 # how often should move

resolution = size()
width=resolution[0]
height=resolution[1]

def get_mouse_cur_pos():
  cur_mouse_pos_x = position()[0]
  cur_mouse_pos_y = position()[1]
  return cur_mouse_pos_x, cur_mouse_pos_y

def define_x_and_y():
  x, y = get_mouse_cur_pos()
  operation = random.choice('+-')
  if operation == '+':
    random_x = abs(x + random.randint(1, width - move_by))
    random_y = abs(y + random.randint(1, height - move_by))
  elif operation == '-':
    random_x = abs(x - random.randint(1, width - move_by))
    random_y = abs(y - random.randint(1, height - move_by))
  return random_x, random_y

def move_mouse_cur():
  random_x, random_y = define_x_and_y()
  if random_x < width and random_y < height:
    print('moving randomly')
    moveTo(random_x,random_y)
  else:
    print('moving by default')
    move()

def main():
  while True:
    time.sleep(frequency)
    move_mouse_cur()

if __name__ == "__main__":
  main()
