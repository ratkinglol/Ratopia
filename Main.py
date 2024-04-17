"The Main Game"
import turtle
import requests
import socket


BRIGHT_YELLOW = "#FFE800"

SERVER_IP = "192.168.1.31"
SERVER_PORT = 60214

screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
screen.bgcolor("pink")
screen.title("Ratopia V0.0.0")




custom_selected = 0
coop_selected = 0
f4a_selected = 0

infinity_selected = 0
war_selected = 0
score_selected = 0

easy_selected = 0
medium_selected = 0
hard_selected = 0 


in_custom_menu = 0

bot_1_selected = 0
bot_2_selected = 0
bot_3_selected = 0
bot_4_selected = 0
bot_5_selected = 0

def f1_key():
  console_command()

def key_1():
  pass


def ctrl_key():
  print('ctrl pressed')

def esc_key():
  global custom_selected, f4a_selected, coop_selected, bot_1_selected, bot_2_selected, bot_3_selected, bot_4_selected, bot_5_selected, starting_screen_on, new_game_screen_on, settings_screen
  if settings_screen == 1:
    settings_text.clear()
    #
    starting_screen_on = 1
    settings_screen = 0
    #
    starting_screen()
  elif starting_screen_on == 1:
    print('no')
  elif new_game_screen_on == 1:
    new_game_screen_on = 0
    custom_selected = 0
    coop_selected = 0
    f4a_selected = 0
    bot_1_selected = 0
    bot_2_selected = 0
    bot_3_selected = 0
    bot_4_selected = 0
    bot_5_selected = 0
    starting_screen_on = 1
    #
    new_game_text.clear()
    #
    normal_clear()
    #
    selected_clear()
    #
    starting_screen()
    if starting_screen_on == 1:
      pass
    else:
      normal_clear()
      selected_clear()
      starting_screen()

def console_command():
  "The function that controls the console command logic"
  global useful_x_1, useful_y_1, write_console_command2, write_console_command3, custom_selected, coop_selected, easy_select_draw
  thingy = turtle.textinput("", "Console Command Terminal")
  if thingy.lower() == "write white arial" or thingy.lower() == "white arial write" or thingy.lower() == "0":
    write_console_command = turtle.textinput("", "x coordinate")
    write_console_command1 = turtle.textinput("", "y coordinate")
    #
    useful_x_1 = int(write_console_command)
    useful_y_1 = int(write_console_command1)
    #
    write_console_command2 = turtle.textinput("", "text to write")
    write_console_command3 = turtle.textinput("", "text size")
    write_console(useful_x_1, useful_y_1, write_console_command2, write_console_command3)
  elif thingy.lower() == "print" or thingy.lower() == "p" or thingy == "0":
    print_console_command = turtle.textinput("", "print:")
    if print_console_command == "custom_selected":
      try:
        print(custom_selected)
      except:
        print("Error, 'variable custom_selected' has no assigned value")
        pass
    elif print_console_command == "coop_selected":
      try:
        print(coop_selected)
      except:
        print("Error, variable 'coop_selected' has no assigned value")
  elif thingy.lower() == "server":
    server_console_command = turtle.textinput("", "Code to communicate with server")
    com_with_server(server_console_command)
    turtle.onkey(key_1, '1')
    turtle.onkey(ctrl_key, 'Control_L')
  elif thingy.lower() == "close" or thingy.lower() == "exit":
    exit()
  elif thingy.lower() == "todo list" or thingy.lower() == "to-do list" or thingy.lower() == "to do list":
    todo_list = turtle.textinput('', '1. Finish Custom Game Mode Creation | 2. Add the settings menu')
  elif thingy.lower() == 'easy.clear()':
    easy_select_draw.clear()
    turtle.onkey(f1_key, 'F1')
    turtle.listen()

def normal_clear():
  turtle.tracer(0, 0)
  try:
    coop_square.clear()
  except:
    pass
  print("DEBUG", "|", "normal_clear() past first clear")
  try:
    custom_square.clear()
  except:
    pass
  print("DEBUG", "|", "normal_clear() past second clear")
  try:
    freefor_all_square.clear()
  except:
    pass
  print("DEBUG", "|", "normal_clear() past third clear")
  try:
    bot_1_square.clear()
  except:
    pass
  print("DEBUG", "|", "normal_clear() past fourth clear")
  try:
    bot_2_square.clear()
  except:
    pass
  try:
    bot_3_square.clear()
  except:
    pass
  try:
    bot_4_square.clear()
  except:
    pass
  try:
    bot_5_square.clear()
  except:
    pass
  done1 = 'normal done'
  turtle.update()
  turtle.tracer(1, 10)
  return done1


def selected_clear():
  turtle.tracer(0, 0)
  try:
    coop_selected_square.clear()
  except:
    pass
  print("DEBUG", "|", "selected_clear() past first clear")
  try:
    custom_selected_square.clear()
  except:
    pass
  print("DEBUG", "|", "selected_clear() past second clear")
  try:
    free_selected_square.clear()
  except:
    pass
  print("DEBUG", "|", "selected_clear() past third clear")
  try:
    bot1selectedsquare.clear()
  except:
    pass
  print("DEBUG", "|", "selected_clear() past fourth clear")
  try:
    bot2selectedsquare.clear()
  except:
    pass
  try:
    bot3selectedsquare.clear()
  except:
    pass
  try:
    bot4selectedsquare.clear()
  except:
    pass
  try:
    bot5selectedsquare.clear()
  except:
    pass
  turtle.update()
  turtle.tracer(1, 10)
  done = 'done'
  return done

starting_screen_on = 1
new_game_screen_on = 0
settings_screen = 0

writing_tool = turtle.Turtle()
writing_tool.speed(0)
writing_tool.color('white')
writing_tool.penup()
writing_tool.hideturtle()
writing_tool.goto(0, 0)
writing_tool.hideturtle()



while True:
  if writing_tool.isvisible() == True:
    writing_tool.hideturtle()
  else:
    break

def com_with_server(code_for_server):
  """Function used to communicate with server, there are a few different codes for the server to process.
  
  CODES:

  code 'test x', just a test code.
  
  code 'server.closeconnection()', closes connection with server"""
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER_IP, SERVER_PORT))
    server_msg = s.recv(1024)
    print(server_msg)
    s.send(code_for_server.encode())
    server_msg = s.recv(1024)
    print(server_msg)
    if code_for_server.lower() == "server.closeconnection()" or code_for_server.lower() == "server.close()" or code_for_server == "server x":
      server_msg = s.recv(1024)
      print(server_msg)
  except socket.error:
    print("Error Communicating With Server")
    error_message = turtle.textinput("", "Error Communicating With Server")
    pass
  except:
    print("Unknown Error")
    error_message = turtle.textinput("", "Unknown Error")
    pass

def write_console(x_c : int, y_c : int, text, size : int):
  global writing_tool
  turtle.tracer(0, 0)
  writing_tool.goto(x_c, y_c)
  writing_tool.write(text, align="center", font=("Arial", size, "normal"))
  turtle.update()
  turtle.tracer(1, 10)

def starting_screen():
  global New_Game_Square, load_game_square, title_text
  turtle.tracer(0, 0)
  #
  New_Game_Square = turtle.Turtle()
  New_Game_Square.speed(0)
  New_Game_Square.color("black")
  New_Game_Square.penup()
  New_Game_Square.goto(-90, 200)
  New_Game_Square.pendown()
  New_Game_Square.begin_fill()
  for _ in range(2):
    New_Game_Square.forward(180)
    New_Game_Square.left(90)
    New_Game_Square.forward(40)
    New_Game_Square.left(90)
  New_Game_Square.color('blue')
  New_Game_Square.end_fill()
  New_Game_Square.hideturtle()
  New_Game_Square.penup()
  #
  load_game_square = turtle.Turtle()
  load_game_square.speed(0)
  load_game_square.color("black")
  load_game_square.penup()
  load_game_square.goto(-90, 0)
  load_game_square.pendown()
  load_game_square.begin_fill()
  for _ in range(2):
    load_game_square.forward(180)
    load_game_square.left(90)
    load_game_square.forward(40)
    load_game_square.left(90)
  load_game_square.color('blue')
  load_game_square.end_fill()
  load_game_square.hideturtle()
  load_game_square.penup()
  #
  load_game_square.goto(-90, -200)
  load_game_square.color('black')
  load_game_square.pendown()
  load_game_square.begin_fill()
  for _ in range(2):
    load_game_square.forward(180)
    load_game_square.left(90)
    load_game_square.forward(40)
    load_game_square.left(90)
  load_game_square.color('blue')
  load_game_square.end_fill()
  load_game_square.hideturtle()
  load_game_square.penup()
  #
  title_text = turtle.Turtle()
  title_text.speed(0)
  title_text.color("White")
  title_text.penup()
  title_text.hideturtle()
  title_text.goto(0, 400)
  title_text.write("Ratopia", align="center", font=("Arial", 30, "normal"))
  #
  title_text.goto(0, 200)
  title_text.write("New Game", align="center", font=("Arial", 25, "normal"))
  #
  title_text.goto(0, 0)
  title_text.write("Load Game", align="center", font=("Arial", 25, "normal"))
  #
  title_text.goto(0, -200)
  title_text.write("Settings", align="center", font=("Arial", 25, "normal"))
  #
  turtle.update()
  turtle.tracer(1, 10)

def start_clear():
  title_text.clear()
  New_Game_Square.clear()
  load_game_square.clear()

def settings():
  global settings_text, starting_screen_on, settings_screen
  turtle.tracer(0, 0)
  start_clear()
  starting_screen_on = 0
  settings_screen = 1
  #
  settings_text = turtle.Turtle()
  settings_text.speed(0)
  settings_text.color('black')
  settings_text.penup()
  settings_text.hideturtle()
  settings_text.goto(-400, 400)
  settings_text.write('Controls', align="center", font=("Arial", 20, "normal"))
  #
  settings_text.goto(-200, 400)
  settings_text.write("Graphics", align="center", font=("Arial", 20, "normal"))

def new_game():
  global custom_square, new_game_text, coop_square, bot_1_square, bot_2_square, bot_3_square, bot_4_square, bot_5_square, freefor_all_square
  turtle.tracer(0, 0)
  #
  start_clear()
  #
  custom_square = turtle.Turtle()
  custom_square.speed(0)
  custom_square.penup()
  custom_square.goto(-360, 300)
  custom_square.pendown()
  custom_square.color('black')
  custom_square.begin_fill()
  for _ in range(2):
    custom_square.forward(120)
    custom_square.left(90)
    custom_square.forward(30)
    custom_square.left(90)
  custom_square.color('blue')
  custom_square.end_fill()
  custom_square.hideturtle()
  custom_square.penup()
  #
  coop_square = turtle.Turtle()
  coop_square.speed(0)
  coop_square.color("black")
  coop_square.penup()
  coop_square.goto(-115, 300)
  coop_square.pendown()
  coop_square.begin_fill()
  for _ in range(2):
    coop_square.forward(225)
    coop_square.left(90)
    coop_square.forward(30)
    coop_square.left(90)
  coop_square.color('blue')
  coop_square.end_fill()
  coop_square.hideturtle()
  coop_square.penup()
  #
  freefor_all_square = turtle.Turtle()
  freefor_all_square.speed(0)
  freefor_all_square.color("black")
  freefor_all_square.penup()
  freefor_all_square.goto(185, 300)
  freefor_all_square.pendown()
  freefor_all_square.begin_fill()
  for _ in range(2):
    freefor_all_square.forward(225)
    freefor_all_square.left(90)
    freefor_all_square.forward(30)
    freefor_all_square.left(90)
  freefor_all_square.color('blue')
  freefor_all_square.end_fill()
  freefor_all_square.hideturtle()
  freefor_all_square.penup()
  #
  bot_1_square = turtle.Turtle()
  bot_1_square.speed(0)
  bot_1_square.color("black")
  bot_1_square.penup()
  bot_1_square.goto(-215, 0)
  bot_1_square.pendown()
  bot_1_square.begin_fill()
  for _ in range(2):
    bot_1_square.forward(25)
    bot_1_square.left(90)
    bot_1_square.forward(30)
    bot_1_square.left(90)
  bot_1_square.color('blue')
  bot_1_square.end_fill()
  bot_1_square.hideturtle()
  bot_1_square.penup()
  #
  bot_2_square = turtle.Turtle()
  bot_2_square.speed(0)
  bot_2_square.color('black')
  bot_2_square.penup()
  bot_2_square.goto(-115, 0)
  bot_2_square.pendown()
  bot_2_square.begin_fill()
  for _ in range(2):
    bot_2_square.forward(25)
    bot_2_square.left(90)
    bot_2_square.forward(30)
    bot_2_square.left(90)
  bot_2_square.color('blue')
  bot_2_square.end_fill()
  bot_2_square.hideturtle()
  bot_2_square.penup()
  #
  bot_3_square = turtle.Turtle()
  bot_3_square.speed(0)
  bot_3_square.color('black')
  bot_3_square.penup()
  bot_3_square.goto(-15, 0)
  bot_3_square.pendown()
  bot_3_square.begin_fill()
  for _ in range(2):
    bot_3_square.forward(25)
    bot_3_square.left(90)
    bot_3_square.forward(30)
    bot_3_square.left(90)
  bot_3_square.color('blue')
  bot_3_square.end_fill()
  bot_3_square.hideturtle()
  bot_3_square.penup()
  #
  bot_4_square = turtle.Turtle()
  bot_4_square.speed(0)
  bot_4_square.color('black')
  bot_4_square.penup()
  bot_4_square.goto(85, 0)
  bot_4_square.pendown()
  bot_4_square.begin_fill()
  for _ in range(2):
    bot_4_square.forward(25)
    bot_4_square.left(90)
    bot_4_square.forward(30)
    bot_4_square.left(90)
  bot_4_square.color('blue')
  bot_4_square.end_fill()
  bot_4_square.hideturtle()
  bot_4_square.penup()
  #
  bot_5_square = turtle.Turtle()
  bot_5_square.speed(0)
  bot_5_square.color('black')
  bot_5_square.penup()
  bot_5_square.goto(185, 0)
  bot_5_square.pendown()
  bot_5_square.begin_fill()
  for _ in range(2):
    bot_5_square.forward(25)
    bot_5_square.left(90)
    bot_5_square.forward(30)
    bot_5_square.left(90)
  bot_5_square.color('blue')
  bot_5_square.end_fill()
  bot_5_square.hideturtle()
  bot_5_square.penup()
  #
  new_game_text = turtle.Turtle()
  new_game_text.speed(0)
  new_game_text.color("white")
  new_game_text.penup()
  new_game_text.hideturtle()
  new_game_text.goto(0, 400)
  new_game_text.write("Game Mode:", align="center", font=("Arial", 30, "bold"))
  #
  new_game_text.goto(300, 300)
  new_game_text.write("Free For All", align="center", font=("Arial", 20, "bold"))
  #
  new_game_text.goto(0, 300)
  new_game_text.write("Co-Op Survival", align="center", font=("Arial", 20, "bold"))
  #
  new_game_text.goto(-300, 300)
  new_game_text.write("Custom", align="center", font=("Arial", 20, "bold"))
  #
  new_game_text.goto(0, 100)
  new_game_text.write("Bots:", align="center", font=("Arial", 30, "bold"))
  #
  new_game_text.goto(-200, 0)
  new_game_text.write("1", align="center", font=("Arial", 20, "bold"))
  #
  new_game_text.goto(-100, 0)
  new_game_text.write("2", align="center", font=("Arial", 20, "bold"))
  #
  new_game_text.goto(0, 0)
  new_game_text.write("3", align="center", font=("Arial", 20, "bold"))
  #
  new_game_text.goto(100, 0)
  new_game_text.write("4", align="center", font=("Arial", 20, "bold"))
  #
  new_game_text.goto(200, 0)
  new_game_text.write("5", align="center", font=("Arial", 20, "bold"))
  #
  turtle.update()
  turtle.tracer(1, 10)

def redo_custom_text():
  global new_game_text
  new_game_text.goto(-300, 300)
  new_game_text.write("Custom", align="center", font=("Arial", 20, "bold"))

def redo_coop_text():
  global new_game_text
  new_game_text.goto(0, 300)
  new_game_text.write("Co-Op Survival", align="center", font=("Arial", 20, "bold"))

def redo_f4a_text():
  global new_game_text
  new_game_text.goto(300, 300)
  new_game_text.write("Free For All", align="center", font=("Arial", 20, "bold"))

def redo_bot_text(thing):
  global new_game_text
  if thing == 1:
    new_game_text.goto(-200, 0)
    new_game_text.write("1", align="center", font=("Arial", 20, "bold"))
  elif thing == 2:
    new_game_text.goto(-100, 0)
    new_game_text.write("2", align="center", font=("Arial", 20, "bold"))
  elif thing == 3:
    new_game_text.goto(0, 0)
    new_game_text.write("3", align="center", font=("Arial", 20, "bold"))
  elif thing == 4:
    new_game_text.goto(100, 0)
    new_game_text.write("4", align="center", font=("Arial", 20, "bold"))
  elif thing == 5:
    new_game_text.goto(200, 0)
    new_game_text.write("5", align="center", font=("Arial", 20, "bold"))

def coop_select():
  global coop_selected, custom_selected, coop_selected_square, f4a_selected
  coop_selected = 1
  coop_square.clear()
  turtle.tracer(0, 0)
  coop_selected_square = turtle.Turtle()
  coop_selected_square.speed(0)
  coop_selected_square.color('black')
  coop_selected_square.penup()
  coop_selected_square.goto(-115, 300)
  coop_selected_square.pendown()
  coop_selected_square.begin_fill()
  for _ in range(2):
    coop_selected_square.forward(225)
    coop_selected_square.left(90)
    coop_selected_square.forward(30)
    coop_selected_square.left(90)
  coop_selected_square.color(BRIGHT_YELLOW)
  coop_selected_square.end_fill()
  coop_selected_square.hideturtle()
  coop_selected_square.penup()
  redo_coop_text()
  if custom_selected == 1:
    #
    custom_selected = 0
    #
    custom_selected_square.clear()
    #
    custom_square = turtle.Turtle()
    custom_square.speed(0)
    custom_square.color('black')
    custom_square.penup()
    custom_square.goto(-360, 300)
    custom_square.pendown()
    custom_square.begin_fill()
    #
    for _ in range(2):
      custom_square.forward(120)
      custom_square.left(90)
      custom_square.forward(30)
      custom_square.left(90)
    #
    custom_square.color('blue')
    custom_square.end_fill()
    custom_square.hideturtle()
    custom_square.penup()
    redo_custom_text()
    turtle.update()
    turtle.tracer(1, 10)
  elif f4a_selected == 1:
    turtle.tracer(0, 0)
    free_selected_square.clear()
    freefor_all_square = turtle.Turtle()
    freefor_all_square.speed(0)
    freefor_all_square.color("black")
    freefor_all_square.penup()
    freefor_all_square.goto(185, 300)
    freefor_all_square.pendown()
    freefor_all_square.begin_fill()
    for _ in range(2):
      freefor_all_square.forward(225)
      freefor_all_square.left(90)
      freefor_all_square.forward(30)
      freefor_all_square.left(90)
    freefor_all_square.color('blue')
    freefor_all_square.end_fill()
    freefor_all_square.hideturtle()
    freefor_all_square.penup()
    redo_f4a_text()
    turtle.update()
    turtle.tracer(1, 10)

def custom_select():
  global coop_selected, custom_selected, custom_selected_square
  custom_selected = 1
  custom_square.clear()
  turtle.tracer(0, 0)
  custom_selected_square = turtle.Turtle()
  custom_selected_square.speed(0)
  custom_selected_square.color('black')
  custom_selected_square.penup()
  custom_selected_square.goto(-360, 300)
  custom_selected_square.pendown()
  custom_selected_square.begin_fill()
  for _ in range(2):
    custom_selected_square.forward(120)
    custom_selected_square.left(90)
    custom_selected_square.forward(30)
    custom_selected_square.left(90)
  custom_selected_square.color(BRIGHT_YELLOW)
  custom_selected_square.end_fill()
  custom_selected_square.penup()
  custom_selected_square.hideturtle()
  turtle.update()
  turtle.tracer(1, 10)
  redo_custom_text()
  if coop_selected == 1:
    #
    turtle.tracer(0, 0)
    #
    coop_selected = 0
    #
    coop_selected_square.clear()
    #
    coop_square.speed(0)
    coop_square.color("black")
    coop_square.penup()
    coop_square.goto(-115, 300)
    coop_square.pendown()
    coop_square.begin_fill()
    #
    for _ in range(2):
      coop_square.forward(225)
      coop_square.left(90)
      coop_square.forward(30)
      coop_square.left(90)
    #
    coop_square.color('blue')
    coop_square.end_fill()
    coop_square.hideturtle()
    coop_square.penup()
    redo_coop_text()
    turtle.update()
    turtle.tracer(1, 10)
  elif f4a_selected == 1:
    turtle.tracer(0, 0)
    free_selected_square.clear()
    freefor_all_square = turtle.Turtle()
    freefor_all_square.speed(0)
    freefor_all_square.color("black")
    freefor_all_square.penup()
    freefor_all_square.goto(185, 300)
    freefor_all_square.pendown()
    freefor_all_square.begin_fill()
    for _ in range(2):
      freefor_all_square.forward(225)
      freefor_all_square.left(90)
      freefor_all_square.forward(30)
      freefor_all_square.left(90)
    freefor_all_square.color('blue')
    freefor_all_square.end_fill()
    freefor_all_square.hideturtle()
    freefor_all_square.penup()
    redo_f4a_text()
  custom_select_1()
  turtle.update()
  turtle.tracer(1, 10)

def redo_custom_select_1_text(thing : str, selected : int):
  if thing == "x" and selected == 0:
    custom_select_1_draw_write_thing.color('white')
    custom_select_1_draw_write_thing.goto(-500, 400)
    custom_select_1_draw_write_thing.write("X", align="center", font=("Arial", 20, "normal"))
  elif thing == "infinity" and selected == 1:
    custom_select_1_draw_write_thing.color('black')
    custom_select_1_draw_write_thing.goto(-300, 350)
    custom_select_1_draw_write_thing.write("Infinity", align="center", font=("Arial", 20, "normal"))
    custom_select_1_draw_write_thing.color('white')
  elif thing == "war" and selected == 1:
    custom_select_1_draw_write_thing.color('black')
    custom_select_1_draw_write_thing.goto(0, 350)
    custom_select_1_draw_write_thing.write("War", align="center", font=("Arial", 20, "normal"))
    custom_select_1_draw_write_thing.color('white')
  elif thing == "score" and selected == 1:
    custom_select_1_draw_write_thing.color('black')
    custom_select_1_draw_write_thing.goto(300, 350)
    custom_select_1_draw_write_thing.write("Score", align="center", font=("Arial", 20, "normal"))
    custom_select_1_draw_write_thing.color('white')
  elif thing == "infinity" and selected == 0:
    custom_select_1_draw_write_thing.color('white')
    custom_select_1_draw_write_thing.goto(-300, 350)
    custom_select_1_draw_write_thing.write("Infinity", align="center", font=("Arial", 20, "normal"))
  elif thing == "war" and selected == 0:
    custom_select_1_draw_write_thing.color('white')
    custom_select_1_draw_write_thing.goto(0, 350)
    custom_select_1_draw_write_thing.write("War", align="center", font=("Arial", 20, "normal"))
  elif thing == "score" and selected == 0:
    custom_select_1_draw_write_thing.color('white')
    custom_select_1_draw_write_thing.goto(300, 350)
    custom_select_1_draw_write_thing.write('Score', align="center", font=("Arial", 20, "normal"))
  elif thing == "easy" and selected == 1:
    custom_select_1_draw_write_thing.color('black')
    custom_select_1_draw_write_thing.goto(-300, 150)
    custom_select_1_draw_write_thing.write("Easy", align="center", font=("Arial", 20, "normal"))
    custom_select_1_draw_write_thing.color('white')
  elif thing == "medium" and selected == 1:
    custom_select_1_draw_write_thing.color('black')
    custom_select_1_draw_write_thing.goto(0, 150)
    custom_select_1_draw_write_thing.write("Medium", align="center", font=("Arial", 20, "normal"))
    custom_select_1_draw_write_thing.color('white')
  elif thing == "hard" and selected == 1:
    custom_select_1_draw_write_thing.color('black')
    custom_select_1_draw_write_thing.goto(300, 150)
    custom_select_1_draw_write_thing.write("Hard", align="center", font=("Arial", 20, "normal"))
    custom_select_1_draw_write_thing.color('white')
  elif thing == "easy" and selected == 0:
    custom_select_1_draw_write_thing.color('white')
    custom_select_1_draw_write_thing.goto(-300, 150)
    custom_select_1_draw_write_thing.write("Easy", align="center", font=("Arial", 20, "normal"))
  elif thing == "medium" and selected == 0:
    custom_select_1_draw_write_thing.color('white')
    custom_select_1_draw_write_thing.goto(0, 150)
    custom_select_1_draw_write_thing.write("Medium", align="center", font=("Arial", 20, "normal"))
  elif thing == "hard" and selected == 0:
    custom_select_1_draw_write_thing.color('white')
    custom_select_1_draw_write_thing.goto(300, 150)
    custom_select_1_draw_write_thing.write("Hard", align="center", font=("Arial", 20, "normal"))

def custom_select_1():
  turtle.tracer(0, 0)
  global custom_select_1_draw_write_thing, in_custom_menu, new_game_screen_on
  #
  in_custom_menu = 1
  new_game_screen_on = 0
  #
  custom_select_1_draw_write_thing = turtle.Turtle()
  custom_select_1_draw_write_thing.speed(0)
  custom_select_1_draw_write_thing.color('white')
  custom_select_1_draw_write_thing.penup()
  custom_select_1_draw_write_thing.hideturtle()
  #
  custom_select_1_draw_write_thing.goto(-500, 400)
  custom_select_1_draw_write_thing.write("X", align="center", font=("Arial", 20, "normal"))
  #
  custom_select_1_draw_write_thing.color('black')
  custom_select_1_draw_write_thing.goto(-500, 385)
  custom_select_1_draw_write_thing.pendown()
  custom_select_1_draw_write_thing.begin_fill()
  custom_select_1_draw_write_thing.circle(30)
  custom_select_1_draw_write_thing.end_fill()
  custom_select_1_draw_write_thing.penup()
  redo_custom_select_1_text("x", 0)
  #
  custom_select_1_draw_write_thing.color('white')
  custom_select_1_draw_write_thing.goto(-425, 450)
  custom_select_1_draw_write_thing.pendown()
  custom_select_1_draw_write_thing.begin_fill()
  for _ in range(2):
    custom_select_1_draw_write_thing.forward(850)
    custom_select_1_draw_write_thing.right(90)
    custom_select_1_draw_write_thing.forward(900)
    custom_select_1_draw_write_thing.right(90)
  custom_select_1_draw_write_thing.color('black')
  custom_select_1_draw_write_thing.end_fill()
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.color('white')
  custom_select_1_draw_write_thing.goto(0, 400)
  custom_select_1_draw_write_thing.write('Custom Game Mode', align="center", font=("Arial", 20, "bold"))
  #
  custom_select_1_draw_write_thing.goto(-350, 390)
  custom_select_1_draw_write_thing.pendown()
  custom_select_1_draw_write_thing.goto(350, 390)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(350, 290)
  custom_select_1_draw_write_thing.pendown()
  custom_select_1_draw_write_thing.goto(-350, 290)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(350, 190)
  custom_select_1_draw_write_thing.pendown()
  custom_select_1_draw_write_thing.goto(-350, 190)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(350, 90)
  custom_select_1_draw_write_thing.pendown()
  custom_select_1_draw_write_thing.goto(-350, 90)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(350, -10)
  custom_select_1_draw_write_thing.pendown()
  custom_select_1_draw_write_thing.goto(-350, -10)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(-300, 350)
  custom_select_1_draw_write_thing.write("Infinity", align="center", font=("Arial", 20, "normal"))
  #
  custom_select_1_draw_write_thing.goto(-350, 350)
  custom_select_1_draw_write_thing.pendown()
  for _ in range(2):
    custom_select_1_draw_write_thing.forward(100)
    custom_select_1_draw_write_thing.left(90)
    custom_select_1_draw_write_thing.forward(30)
    custom_select_1_draw_write_thing.left(90)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(0, 350)
  custom_select_1_draw_write_thing.write('War', align="center", font=("Arial", 20, "normal"))
  #
  custom_select_1_draw_write_thing.goto(-40, 350)
  custom_select_1_draw_write_thing.pendown()
  for _ in range(2):
    custom_select_1_draw_write_thing.forward(80)
    custom_select_1_draw_write_thing.left(90)
    custom_select_1_draw_write_thing.forward(30)
    custom_select_1_draw_write_thing.left(90)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(300, 350)
  custom_select_1_draw_write_thing.write('Score', align="center", font=("Arial", 20, "normal"))
  #
  custom_select_1_draw_write_thing.goto(250, 350)
  custom_select_1_draw_write_thing.pendown()
  for _ in range(2):
    custom_select_1_draw_write_thing.forward(100)
    custom_select_1_draw_write_thing.left(90)
    custom_select_1_draw_write_thing.forward(30)
    custom_select_1_draw_write_thing.left(90)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(0, 300)
  custom_select_1_draw_write_thing.write('Nations Allowed', align="center", font=('Arial', 20, 'bold'))
  #
  custom_select_1_draw_write_thing.goto(0, 200)
  custom_select_1_draw_write_thing.write('Difficulty', align="center", font=("Arial", 20, 'bold'))
  #
  custom_select_1_draw_write_thing.goto(-300, 150)
  custom_select_1_draw_write_thing.write('Easy', align='center', font=('Arial', 20, 'normal'))
  #
  custom_select_1_draw_write_thing.goto(-340, 150)
  custom_select_1_draw_write_thing.pendown()
  for _ in range(2):
    custom_select_1_draw_write_thing.forward(80)
    custom_select_1_draw_write_thing.left(90)
    custom_select_1_draw_write_thing.forward(30)
    custom_select_1_draw_write_thing.left(90)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(0, 150)
  custom_select_1_draw_write_thing.write('Medium', align='center', font=('Arial', 20, 'normal'))
  #
  custom_select_1_draw_write_thing.goto(-60, 150)
  custom_select_1_draw_write_thing.pendown()
  for _ in range(2):
    custom_select_1_draw_write_thing.forward(120)
    custom_select_1_draw_write_thing.left(90)
    custom_select_1_draw_write_thing.forward(30)
    custom_select_1_draw_write_thing.left(90)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(300, 150)
  custom_select_1_draw_write_thing.write('Hard', align='center', font=('Arial', 20, 'normal'))
  #
  custom_select_1_draw_write_thing.goto(260, 150)
  custom_select_1_draw_write_thing.pendown()
  for _ in range(2):
    custom_select_1_draw_write_thing.forward(80)
    custom_select_1_draw_write_thing.left(90)
    custom_select_1_draw_write_thing.forward(30)
    custom_select_1_draw_write_thing.left(90)
  custom_select_1_draw_write_thing.penup()
  #
  custom_select_1_draw_write_thing.goto(0, 100)
  custom_select_1_draw_write_thing.write('Map Type', align="center", font=("Arial", 20, "bold"))
  #
  custom_select_1_draw_write_thing.goto(0, 0)
  custom_select_1_draw_write_thing.write('Map Size', align='center', font=('Arial', 20, 'bold'))
  #
  turtle.update()
  turtle.tracer(1, 10)

def free_4_all_select():
  """The function called when free for all is selected in the new game menu.
  #
  Dev Notes: For some reason unbeknownst to me, it is not cooperating to make the black outline around the selected box like the other functions
  #
  Dev Notes: The reason was because the .pendown() function was not called lmao"""
  global coop_selected, custom_selected, f4a_selected, free_selected_square
  turtle.tracer(0, 0)
  f4a_selected = 1
  free_selected_square = turtle.Turtle()
  free_selected_square.speed(0)
  free_selected_square.color('black')
  free_selected_square.penup()
  free_selected_square.goto(185, 298)
  free_selected_square.pendown()
  free_selected_square.begin_fill()
  #
  for _ in range(2):
    free_selected_square.forward(227)
    free_selected_square.left(90)
    free_selected_square.forward(35)
    free_selected_square.left(90)
  free_selected_square.color(BRIGHT_YELLOW)
  free_selected_square.end_fill()
  free_selected_square.penup()
  free_selected_square.hideturtle()
  redo_f4a_text()
  turtle.update()
  turtle.tracer(1, 10)
  if coop_selected == 1:
    #
    turtle.tracer(0, 0)
    #
    coop_selected = 0
    #
    coop_selected_square.clear()
    #
    coop_square.speed(0)
    coop_square.color("black")
    coop_square.penup()
    coop_square.goto(-115, 300)
    coop_square.pendown()
    coop_square.begin_fill()
    #
    for _ in range(2):
      coop_square.forward(225)
      coop_square.left(90)
      coop_square.forward(30)
      coop_square.left(90)
    #
    coop_square.color('blue')
    coop_square.end_fill()
    coop_square.hideturtle()
    coop_square.penup()
    redo_coop_text()
    turtle.update()
    turtle.tracer(1, 10)
  elif custom_selected == 1:
    turtle.tracer(0, 0)
    custom_selected = 0
    #
    custom_selected_square.clear()
    #
    custom_square = turtle.Turtle()
    custom_square.speed(0)
    custom_square.color('black')
    custom_square.penup()
    custom_square.goto(-360, 300)
    custom_square.pendown()
    custom_square.begin_fill()
    #
    for _ in range(2):
      custom_square.forward(120)
      custom_square.left(90)
      custom_square.forward(30)
      custom_square.left(90)
    #
    custom_square.color('blue')
    custom_square.end_fill()
    custom_square.hideturtle()
    custom_square.penup()
    redo_custom_text()
    turtle.update()
    turtle.tracer(1, 10)

def bot_1_select():
  global bot_1_selected, bot_2_selected, bot_3_selected, bot_4_selected, bot_5_selected, bot1selectedsquare
  turtle.tracer(0, 0)
  #
  bot_1_selected = 1
  bot_1_square.clear()
  #
  bot1selectedsquare = turtle.Turtle()
  bot1selectedsquare.speed(0)
  bot1selectedsquare.color('black')
  bot1selectedsquare.penup()
  bot1selectedsquare.goto(-215, 0)
  bot1selectedsquare.pendown()
  bot1selectedsquare.begin_fill()
  for _ in range(2):
    bot1selectedsquare.forward(25)
    bot1selectedsquare.left(90)
    bot1selectedsquare.forward(30)
    bot1selectedsquare.left(90)
  bot1selectedsquare.color(BRIGHT_YELLOW)
  bot1selectedsquare.end_fill()
  bot1selectedsquare.hideturtle()
  bot1selectedsquare.penup()
  redo_bot_text(1)
  if bot_2_selected == 1:
    bot_2_selected = 0
    bot2selectedsquare.clear()
    bot_2_square = turtle.Turtle()
    bot_2_square.speed(0)
    bot_2_square.color('black')
    bot_2_square.penup()
    bot_2_square.goto(-115, 0)
    bot_2_square.pendown()
    bot_2_square.begin_fill()
    for _ in range(2):
      bot_2_square.forward(25)
      bot_2_square.left(90)
      bot_2_square.forward(30)
      bot_2_square.left(90)
    bot_2_square.color('blue')
    bot_2_square.end_fill()
    bot_2_square.penup()
    bot_2_square.hideturtle()
    redo_bot_text(2)
  elif bot_3_selected == 1:
    bot_3_selected = 0
    bot3selectedsquare.clear()
    bot_3_square = turtle.Turtle()
    bot_3_square.speed(0)
    bot_3_square.color('black')
    bot_3_square.penup()
    bot_3_square.goto(-15, 0)
    bot_3_square.pendown()
    bot_3_square.begin_fill()
    for _ in range(2):
      bot_3_square.forward(25)
      bot_3_square.left(90)
      bot_3_square.forward(30)
      bot_3_square.left(90)
    bot_3_square.color('blue')
    bot_3_square.end_fill()
    bot_3_square.hideturtle()
    bot_3_square.penup()
    redo_bot_text(3)
  elif bot_4_selected == 1:
    bot_4_selected = 0
    bot4selectedsquare.clear()
    bot_4_square = turtle.Turtle()
    bot_4_square.speed(0)
    bot_4_square.color('black')
    bot_4_square.penup()
    bot_4_square.goto(85, 0)
    bot_4_square.pendown()
    bot_4_square.begin_fill()
    for _ in range(2):
      bot_4_square.forward(25)
      bot_4_square.left(90)
      bot_4_square.forward(30)
      bot_4_square.left(90)
    bot_4_square.color('blue')
    bot_4_square.end_fill()
    bot_4_square.hideturtle()
    bot_4_square.penup()
    redo_bot_text(4)
  elif bot_5_selected == 1:
    bot_5_selected = 0
    bot5selectedsquare.clear()
    bot_5_square = turtle.Turtle()
    bot_5_square.speed(0)
    bot_5_square.color('black')
    bot_5_square.penup()
    bot_5_square.goto(185, 0)
    bot_5_square.pendown()
    bot_5_square.begin_fill()
    for _ in range(2):
      bot_5_square.forward(25)
      bot_5_square.left(90)
      bot_5_square.forward(30)
      bot_5_square.left(90)
    bot_5_square.color('blue')
    bot_5_square.end_fill()
    bot_5_square.hideturtle()
    bot_5_square.penup()
    redo_bot_text(5)
  turtle.update()
  turtle.tracer(1, 10)

def bot_2_select():
  global bot_1_selected, bot_2_selected, bot_3_selected, bot_4_selected, bot_5_selected, bot2selectedsquare
  turtle.tracer(0, 0)
  #
  bot_2_selected = 1
  bot_2_square.clear()
  #
  bot2selectedsquare = turtle.Turtle()
  bot2selectedsquare.speed(0)
  bot2selectedsquare.color('black')
  bot2selectedsquare.penup()
  bot2selectedsquare.goto(-115, 0)
  bot2selectedsquare.pendown()
  bot2selectedsquare.begin_fill()
  for _ in range(2):
    bot2selectedsquare.forward(25)
    bot2selectedsquare.left(90)
    bot2selectedsquare.forward(30)
    bot2selectedsquare.left(90)
  bot2selectedsquare.color(BRIGHT_YELLOW)
  bot2selectedsquare.end_fill()
  bot2selectedsquare.penup()
  bot2selectedsquare.hideturtle()
  redo_bot_text(2)
  if bot_1_selected == 1:
    bot_1_selected = 0
    bot1selectedsquare.clear()
    bot_1_square = turtle.Turtle()
    bot_1_square.speed(0)
    bot_1_square.color("black")
    bot_1_square.penup()
    bot_1_square.goto(-215, 0)
    bot_1_square.pendown()
    bot_1_square.begin_fill()
    for _ in range(2):
      bot_1_square.forward(25)
      bot_1_square.left(90)
      bot_1_square.forward(30)
      bot_1_square.left(90)
    bot_1_square.color('blue')
    bot_1_square.end_fill()
    bot_1_square.hideturtle()
    bot_1_square.penup()
    redo_bot_text(1)
  elif bot_3_selected == 1:
    bot_3_selected = 0
    bot3selectedsquare.clear()
    bot_3_square = turtle.Turtle()
    bot_3_square.speed(0)
    bot_3_square.color('black')
    bot_3_square.penup()
    bot_3_square.goto(-15, 0)
    bot_3_square.pendown()
    bot_3_square.begin_fill()
    for _ in range(2):
      bot_3_square.forward(25)
      bot_3_square.left(90)
      bot_3_square.forward(30)
      bot_3_square.left(90)
    bot_3_square.color('blue')
    bot_3_square.end_fill()
    bot_3_square.hideturtle()
    bot_3_square.penup()
    redo_bot_text(3)
  elif bot_4_selected == 1:
    bot_4_selected = 0
    bot4selectedsquare.clear()
    bot_4_square = turtle.Turtle()
    bot_4_square.speed(0)
    bot_4_square.color('black')
    bot_4_square.penup()
    bot_4_square.goto(85, 0)
    bot_4_square.pendown()
    bot_4_square.begin_fill()
    for _ in range(2):
      bot_4_square.forward(25)
      bot_4_square.left(90)
      bot_4_square.forward(30)
      bot_4_square.left(90)
    bot_4_square.color('blue')
    bot_4_square.end_fill()
    bot_4_square.hideturtle()
    bot_4_square.penup()
    redo_bot_text(4)
  elif bot_5_selected == 1:
    bot_5_selected = 0
    bot5selectedsquare.clear()
    bot_5_square = turtle.Turtle()
    bot_5_square.speed(0)
    bot_5_square.color('black')
    bot_5_square.penup()
    bot_5_square.goto(185, 0)
    bot_5_square.pendown()
    bot_5_square.begin_fill()
    for _ in range(2):
      bot_5_square.forward(25)
      bot_5_square.left(90)
      bot_5_square.forward(30)
      bot_5_square.left(90)
    bot_5_square.color('blue')
    bot_5_square.end_fill()
    bot_5_square.hideturtle()
    bot_5_square.penup()
    redo_bot_text(5)
  turtle.update()
  turtle.tracer(1, 10)

def bot_3_select():
  global bot_1_selected, bot_2_selected, bot_3_selected, bot_4_selected, bot_5_selected, bot3selectedsquare
  turtle.tracer(0, 0)
  bot_3_selected = 1
  bot_3_square.clear()
  bot3selectedsquare = turtle.Turtle()
  bot3selectedsquare.speed(0)
  bot3selectedsquare.color('black')
  bot3selectedsquare.penup()
  bot3selectedsquare.goto(-15, 0)
  bot3selectedsquare.pendown()
  bot3selectedsquare.begin_fill()
  for _ in range(2):
    bot3selectedsquare.forward(25)
    bot3selectedsquare.left(90)
    bot3selectedsquare.forward(30)
    bot3selectedsquare.left(90)
  bot3selectedsquare.color(BRIGHT_YELLOW)
  bot3selectedsquare.end_fill()
  bot3selectedsquare.hideturtle()
  bot3selectedsquare.penup()
  redo_bot_text(3)
  if bot_1_selected == 1:
    bot_1_selected = 0
    bot1selectedsquare.clear()
    bot_1_square = turtle.Turtle()
    bot_1_square.speed(0)
    bot_1_square.color("black")
    bot_1_square.penup()
    bot_1_square.goto(-215, 0)
    bot_1_square.pendown()
    bot_1_square.begin_fill()
    for _ in range(2):
      bot_1_square.forward(25)
      bot_1_square.left(90)
      bot_1_square.forward(30)
      bot_1_square.left(90)
    bot_1_square.color('blue')
    bot_1_square.end_fill()
    bot_1_square.hideturtle()
    bot_1_square.penup()
    redo_bot_text(1)
  elif bot_2_selected == 1:
    bot_2_selected = 0
    bot2selectedsquare.clear()
    bot_2_square = turtle.Turtle()
    bot_2_square.speed(0)
    bot_2_square.color('black')
    bot_2_square.penup()
    bot_2_square.goto(-115, 0)
    bot_2_square.pendown()
    bot_2_square.begin_fill()
    for _ in range(2):
      bot_2_square.forward(25)
      bot_2_square.left(90)
      bot_2_square.forward(30)
      bot_2_square.left(90)
    bot_2_square.color('blue')
    bot_2_square.end_fill()
    bot_2_square.penup()
    bot_2_square.hideturtle()
    redo_bot_text(2)
  elif bot_4_selected == 1:
    bot_4_selected = 0
    bot4selectedsquare.clear()
    bot_4_square = turtle.Turtle()
    bot_4_square.speed(0)
    bot_4_square.color('black')
    bot_4_square.penup()
    bot_4_square.goto(85, 0)
    bot_4_square.pendown()
    bot_4_square.begin_fill()
    for _ in range(2):
      bot_4_square.forward(25)
      bot_4_square.left(90)
      bot_4_square.forward(30)
      bot_4_square.left(90)
    bot_4_square.color('blue')
    bot_4_square.end_fill()
    bot_4_square.hideturtle()
    bot_4_square.penup()
    redo_bot_text(4)
  elif bot_5_selected == 1:
    bot_5_selected = 0
    bot5selectedsquare.clear()
    bot_5_square = turtle.Turtle()
    bot_5_square.speed(0)
    bot_5_square.color('black')
    bot_5_square.penup()
    bot_5_square.goto(185, 0)
    bot_5_square.pendown()
    bot_5_square.begin_fill()
    for _ in range(2):
      bot_5_square.forward(25)
      bot_5_square.left(90)
      bot_5_square.forward(30)
      bot_5_square.left(90)
    bot_5_square.color('blue')
    bot_5_square.end_fill()
    bot_5_square.hideturtle()
    bot_5_square.penup()
    redo_bot_text(5)
  turtle.update()
  turtle.tracer(1, 10)

def bot_4_select():
  global bot_1_selected, bot_2_selected, bot_3_selected, bot_4_selected, bot_5_selected, bot4selectedsquare
  turtle.tracer(0, 0)
  bot_4_selected = 1
  bot_4_square.clear()
  bot4selectedsquare = turtle.Turtle()
  bot4selectedsquare.speed(0)
  bot4selectedsquare.color('black')
  bot4selectedsquare.penup()
  bot4selectedsquare.goto(85, 0)
  bot4selectedsquare.pendown()
  bot4selectedsquare.begin_fill()
  for _ in range(2):
    bot4selectedsquare.forward(25)
    bot4selectedsquare.left(90)
    bot4selectedsquare.forward(30)
    bot4selectedsquare.left(90)
  bot4selectedsquare.color(BRIGHT_YELLOW)
  bot4selectedsquare.end_fill()
  bot4selectedsquare.hideturtle()
  bot4selectedsquare.penup()
  redo_bot_text(4)
  if bot_1_selected == 1:
    bot_1_selected = 0
    bot1selectedsquare.clear()
    bot_1_square = turtle.Turtle()
    bot_1_square.speed(0)
    bot_1_square.color("black")
    bot_1_square.penup()
    bot_1_square.goto(-215, 0)
    bot_1_square.pendown()
    bot_1_square.begin_fill()
    for _ in range(2):
      bot_1_square.forward(25)
      bot_1_square.left(90)
      bot_1_square.forward(30)
      bot_1_square.left(90)
    bot_1_square.color('blue')
    bot_1_square.end_fill()
    bot_1_square.hideturtle()
    bot_1_square.penup()
    redo_bot_text(1)
  elif bot_2_selected == 1:
    bot_2_selected = 0
    bot2selectedsquare.clear()
    bot_2_square = turtle.Turtle()
    bot_2_square.speed(0)
    bot_2_square.color('black')
    bot_2_square.penup()
    bot_2_square.goto(-115, 0)
    bot_2_square.pendown()
    bot_2_square.begin_fill()
    for _ in range(2):
      bot_2_square.forward(25)
      bot_2_square.left(90)
      bot_2_square.forward(30)
      bot_2_square.left(90)
    bot_2_square.color('blue')
    bot_2_square.end_fill()
    bot_2_square.penup()
    bot_2_square.hideturtle()
    redo_bot_text(2)
  elif bot_3_selected == 1:
    bot_3_selected = 0
    bot3selectedsquare.clear()
    bot_3_square = turtle.Turtle()
    bot_3_square.speed(0)
    bot_3_square.color('black')
    bot_3_square.penup()
    bot_3_square.goto(-15, 0)
    bot_3_square.pendown()
    bot_3_square.begin_fill()
    for _ in range(2):
      bot_3_square.forward(25)
      bot_3_square.left(90)
      bot_3_square.forward(30)
      bot_3_square.left(90)
    bot_3_square.color('blue')
    bot_3_square.end_fill()
    bot_3_square.hideturtle()
    bot_3_square.penup()
    redo_bot_text(3)
  elif bot_5_selected == 1:
    bot_5_selected = 0
    bot5selectedsquare.clear()
    bot_5_square = turtle.Turtle()
    bot_5_square.speed(0)
    bot_5_square.color('black')
    bot_5_square.penup()
    bot_5_square.goto(185, 0)
    bot_5_square.pendown()
    bot_5_square.begin_fill()
    for _ in range(2):
      bot_5_square.forward(25)
      bot_5_square.left(90)
      bot_5_square.forward(30)
      bot_5_square.left(90)
    bot_5_square.color('blue')
    bot_5_square.end_fill()
    bot_5_square.hideturtle()
    bot_5_square.penup()
    redo_bot_text(5)
  turtle.update()
  turtle.tracer(1, 10)

def bot_5_select():
  global bot_1_selected, bot_2_selected, bot_3_selected, bot_4_selected, bot_5_selected, bot5selectedsquare
  turtle.tracer(0, 0)
  bot_5_selected = 1
  bot_5_square.clear()
  bot5selectedsquare = turtle.Turtle()
  bot5selectedsquare.speed(0)
  bot5selectedsquare.color('black')
  bot5selectedsquare.penup()
  bot5selectedsquare.goto(185, 0)
  bot5selectedsquare.pendown()
  bot5selectedsquare.begin_fill()
  for _ in range(2):
    bot5selectedsquare.forward(25)
    bot5selectedsquare.left(90)
    bot5selectedsquare.forward(30)
    bot5selectedsquare.left(90)
  bot5selectedsquare.color(BRIGHT_YELLOW)
  bot5selectedsquare.end_fill()
  bot5selectedsquare.hideturtle()
  bot5selectedsquare.penup()
  redo_bot_text(5)
  if bot_1_selected == 1:
    bot_1_selected = 0
    bot1selectedsquare.clear()
    bot_1_square = turtle.Turtle()
    bot_1_square.speed(0)
    bot_1_square.color("black")
    bot_1_square.penup()
    bot_1_square.goto(-215, 0)
    bot_1_square.pendown()
    bot_1_square.begin_fill()
    for _ in range(2):
      bot_1_square.forward(25)
      bot_1_square.left(90)
      bot_1_square.forward(30)
      bot_1_square.left(90)
    bot_1_square.color('blue')
    bot_1_square.end_fill()
    bot_1_square.hideturtle()
    bot_1_square.penup()
    redo_bot_text(1)
  elif bot_2_selected == 1:
    bot_2_selected = 0
    bot2selectedsquare.clear()
    bot_2_square = turtle.Turtle()
    bot_2_square.speed(0)
    bot_2_square.color('black')
    bot_2_square.penup()
    bot_2_square.goto(-115, 0)
    bot_2_square.pendown()
    bot_2_square.begin_fill()
    for _ in range(2):
      bot_2_square.forward(25)
      bot_2_square.left(90)
      bot_2_square.forward(30)
      bot_2_square.left(90)
    bot_2_square.color('blue')
    bot_2_square.end_fill()
    bot_2_square.penup()
    bot_2_square.hideturtle()
    redo_bot_text(2)
  elif bot_3_selected == 1:
    bot_3_selected = 0
    bot3selectedsquare.clear()
    bot_3_square = turtle.Turtle()
    bot_3_square.speed(0)
    bot_3_square.color('black')
    bot_3_square.penup()
    bot_3_square.goto(-15, 0)
    bot_3_square.pendown()
    bot_3_square.begin_fill()
    for _ in range(2):
      bot_3_square.forward(25)
      bot_3_square.left(90)
      bot_3_square.forward(30)
      bot_3_square.left(90)
    bot_3_square.color('blue')
    bot_3_square.end_fill()
    bot_3_square.hideturtle()
    bot_3_square.penup()
    redo_bot_text(3)
  elif bot_4_selected == 1:
    bot_4_selected = 0
    bot4selectedsquare.clear()
    bot_4_square = turtle.Turtle()
    bot_4_square.speed(0)
    bot_4_square.color('black')
    bot_4_square.penup()
    bot_4_square.goto(85, 0)
    bot_4_square.pendown()
    bot_4_square.begin_fill()
    for _ in range(2):
      bot_4_square.forward(25)
      bot_4_square.left(90)
      bot_4_square.forward(30)
      bot_4_square.left(90)
    bot_4_square.color('blue')
    bot_4_square.end_fill()
    bot_4_square.hideturtle()
    bot_4_square.penup()
    redo_bot_text(4)

def check_custom_logic(thing : str):
  global war_selected, infinity_selected, score_selected, easy_selected, medium_selected, hard_selected
  if thing.lower() == "war":
    if war_selected == 1:
      war_select_draw.clear()
      war_selected = 0
      redo_custom_select_1_text('war', 0)
  elif thing.lower() == "infinity":
    if infinity_selected == 1:
      infinity_select_draw.clear()
      infinity_selected = 0
      redo_custom_select_1_text('infinity', 0)
  elif thing.lower() == "score":
    if score_selected == 1:
      score_select_draw.clear()
      score_selected = 0
      redo_custom_select_1_text('score', 0)
  elif thing.lower() == "easy":
    if easy_selected == 1:
      easy_select_draw.clear()
      easy_selected = 0
      redo_custom_select_1_text('easy', 0)
  elif thing.lower() == "medium":
    if medium_selected == 1:
      medium_select_draw.clear()
      medium_selected = 0
      redo_custom_select_1_text('medium', 0)
  elif thing.lower() == "hard":
    if hard_selected == 1:
      hard_select_draw.clear()
      hard_selected = 0
      redo_custom_select_1_text('hard', 0)

def infinity_select():
  #elif -350 <= x <= -250 and 350 <= y <= 380:
  global infinity_select_draw, infinity_selected
  turtle.tracer(0, 0)
  #
  infinity_selected = 1
  #
  infinity_select_draw = turtle.Turtle()
  infinity_select_draw.speed(0)
  infinity_select_draw.color('white')
  infinity_select_draw.penup()
  infinity_select_draw.hideturtle()
  infinity_select_draw.goto(-350, 350)
  infinity_select_draw.pendown()
  infinity_select_draw.begin_fill()
  #
  for _ in range(2):
    infinity_select_draw.forward(100)
    infinity_select_draw.left(90)
    infinity_select_draw.forward(30)
    infinity_select_draw.left(90)
  #
  infinity_select_draw.color(BRIGHT_YELLOW)
  infinity_select_draw.end_fill()
  infinity_select_draw.penup()
  redo_custom_select_1_text('infinity', 1)
  #
  check_custom_logic('war')
  check_custom_logic('score')
  #
  turtle.update()
  turtle.tracer(1, 10)

def war_select():
  #elif -40 <= x <= 40 and 350 <= y <= 380:
  global war_select_draw, war_selected
  turtle.tracer(0, 0)
  #
  war_selected = 1
  #
  war_select_draw = turtle.Turtle()
  war_select_draw.speed(0)
  war_select_draw.color('white')
  war_select_draw.penup()
  war_select_draw.hideturtle()
  war_select_draw.goto(-40, 350)
  war_select_draw.pendown()
  war_select_draw.begin_fill()
  for _ in range(2):
    war_select_draw.forward(80)
    war_select_draw.left(90)
    war_select_draw.forward(30)
    war_select_draw.left(90)
  #
  war_select_draw.color(BRIGHT_YELLOW)
  war_select_draw.end_fill()
  war_select_draw.penup()
  redo_custom_select_1_text('war', 1)
  #
  check_custom_logic('infinity')
  check_custom_logic('score')
  #
  turtle.update()
  turtle.tracer(1, 10)

def score_select():
  global score_select_draw, score_selected
  turtle.tracer(0, 0)
  score_selected = 1
  score_select_draw = turtle.Turtle()
  score_select_draw.speed(0)
  score_select_draw.color('white')
  score_select_draw.penup()
  score_select_draw.hideturtle()
  score_select_draw.goto(250, 350)
  score_select_draw.pendown()
  score_select_draw.begin_fill()
  for _ in range(2):
    score_select_draw.forward(100)
    score_select_draw.left(90)
    score_select_draw.forward(30)
    score_select_draw.left(90)
  score_select_draw.color(BRIGHT_YELLOW)
  score_select_draw.end_fill()
  score_select_draw.penup()
  redo_custom_select_1_text('score', 1)
  #
  check_custom_logic('infinity')
  check_custom_logic('war')
  #
  turtle.update()
  turtle.tracer(1, 10)

def easy_select():
  global easy_selected, easy_select_draw
  turtle.tracer(0, 0)
  easy_selected = 1
  easy_select_draw = turtle.Turtle()
  easy_select_draw.speed(0)
  easy_select_draw.color('white')
  easy_select_draw.penup()
  easy_select_draw.hideturtle()
  easy_select_draw.goto(-340, 150)
  easy_select_draw.pendown()
  easy_select_draw.begin_fill()
  for _ in range(2):
    easy_select_draw.forward(80)
    easy_select_draw.left(90)
    easy_select_draw.forward(30)
    easy_select_draw.left(90)
  easy_select_draw.color(BRIGHT_YELLOW)
  easy_select_draw.end_fill()
  redo_custom_select_1_text('easy', 1)
  check_custom_logic('medium')
  check_custom_logic('hard')
  turtle.update()
  turtle.tracer(1, 10)

def medium_select():
  global medium_selected, medium_select_draw
  turtle.tracer(0, 0)
  medium_selected = 1
  medium_select_draw = turtle.Turtle()
  medium_select_draw.speed(0)
  medium_select_draw.color('white')
  medium_select_draw.penup()
  medium_select_draw.hideturtle()
  medium_select_draw.goto(-60, 150)
  medium_select_draw.pendown()
  medium_select_draw.begin_fill()
  for _ in range(2):
    medium_select_draw.forward(120)
    medium_select_draw.left(90)
    medium_select_draw.forward(30)
    medium_select_draw.left(90)
  medium_select_draw.color(BRIGHT_YELLOW)
  medium_select_draw.end_fill()
  redo_custom_select_1_text('medium', 1)
  check_custom_logic('easy')
  check_custom_logic('hard')
  turtle.update()
  turtle.tracer(1, 10)

def hard_select():
  global hard_selected, hard_select_draw
  turtle.tracer(0, 0)
  hard_selected = 1
  hard_select_draw = turtle.Turtle()
  hard_select_draw.speed(0)
  hard_select_draw.color('white')
  hard_select_draw.penup()
  hard_select_draw.hideturtle()
  hard_select_draw.goto(260, 150)
  hard_select_draw.pendown()
  hard_select_draw.begin_fill()
  for _ in range(2):
    hard_select_draw.forward(80)
    hard_select_draw.left(90)
    hard_select_draw.forward(30)
    hard_select_draw.left(90)
  hard_select_draw.color(BRIGHT_YELLOW)
  hard_select_draw.end_fill()
  redo_custom_select_1_text('hard', 1)
  check_custom_logic('easy')
  check_custom_logic('medium')
  turtle.update()
  turtle.tracer(1, 10)

def click_thing(x, y):
  global starting_screen_on, new_game_screen_on, in_custom_menu #1
  print("DEBUG", x, y) #2
  if starting_screen_on == 1: #3
    if -88 <= x <= 90 and 200 <= y <= 238: #4
      print("DEBUG", "|", "New Game") #5
      starting_screen_on = 0 #6
      new_game_screen_on = 1
      new_game() #8
    elif -88 <= x <= 90 and 0 <= y <= 37:
      print("DEBUG", "|", "Load Game") #10
    elif -88 <= x <= 90 and -199 <= y <= -161:
      print("DEBUG", "|", "Settings")
      settings()
  elif starting_screen_on == 0 and new_game_screen_on == 1:
    if -348 <= x <= -252 and 303 <= y <= 328:
      print("DEBUG", "|", "Custom") #15
      custom_select()
    elif -112 <= x <= 112 and 301 <= y <= 327: #17
      print("DEBUG", "|", "CO-OP")
      coop_select()
    elif 187 <= x <= 412 and 300 <= y <= 328:
      print("DEBUG", "|", "FREE 4 ALL")
      free_4_all_select()
    elif -214 <= x <= -189 and -1 <= y <= 28:
      print("DEBUG", "|", "1 BOT")
      bot_1_select()
    elif -113 <= x <= -88 and -1 <= y <= 28:
      print("DEBUG", "|", "2 BOTS")
      bot_2_select()
    elif -14 <= x <= 10 and -1 <= y <= 28:
      print("DEBUG", "|", "3 BOTS")
      bot_3_select()
    elif 86 <= x <= 110 and -1 <= y <= 28:
      print("DEBUG", "|", "4 BOTS")
      bot_4_select()
    elif 187 <= x <= 210 and -1 <= y <= 28:
      print("DEBUG", "|", "5 BOTS")
      bot_5_select()
  elif new_game_screen_on == 0 and in_custom_menu == 1:
    if -533 <= x <= -472 and 385 <= y <= 446:
      print("DEBUG", "|", "Exiting Custom Menu")
      custom_select_1_draw_write_thing.clear()
      in_custom_menu = 0
      new_game_screen_on = 1
      if war_selected == 1:
        war_select_draw.clear()
      elif infinity_selected == 1:
        infinity_select_draw.clear()
      elif score_selected == 1:
        score_select_draw.clear()
      #
      if easy_selected == 1:
        easy_select_draw.clear()
      elif medium_selected == 1:
        medium_select_draw.clear()
      elif hard_selected == 1:
        hard_select_draw.clear()
    elif -350 <= x <= -250 and 350 <= y <= 380:
      print("DEBUG", "|", "Infinity Selected In Custom Menu")
      infinity_select()
    elif -40 <= x <= 40 and 350 <= y <= 380:
      print("DEBUG", "|", "War Selected In Custom Menu")
      war_select()
    elif 250 <= x <= 350 and 350 <= y <= 380:
      print("DEBUG", "|", "Score Selected In Custom Menu")
      score_select()
    elif -340 <= x <= -260 and 150 <= y <= 180:
      print("DEBUG", "|", "Easy Selected")
      easy_select()
    elif -60 <= x <= 60 and 150 <= y <= 180:
      print("DEBUG", "|", "Medium Selected")
      medium_select()
    elif 260 <= x <= 340 and 150 <= y <= 180:
      print("DEBUG", "|", "Hard Selected")
      hard_select()



starting_screen()


screen.onscreenclick(click_thing)



turtle.onkey(f1_key, 'F1')
turtle.onkey(key_1, '1')
turtle.onkey(ctrl_key, 'Control_L')
turtle.onkey(esc_key, 'Escape')
turtle.listen()

screen.mainloop()
