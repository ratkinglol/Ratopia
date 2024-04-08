import turtle
import time

BRIGHT_YELLOW = "#FFE800"

screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("pink")

ctrl_key_press = 1


custom_selected = 0
coop_selected = 0
f4a_selected = 0

def key_1_1():
  pass

def key_1():
  global ctrl_key_press
  if ctrl_key_press == 1:
    print("DEBUG", "|", "Console Command")
    console_command()
  elif ctrl_key_press == 0:
    print("DEBUG", "|", "Control Not Pressed While 1 Pressed")

def ctrl_key1():
  global ctrl_key_press
  ctrl_key_press = 0

def ctrl_key():
  global ctrl_key_press
  ctrl_key_press = 1


def console_command():
  global useful_x_1, useful_y_1, write_console_command2, write_console_command3, custom_selected, coop_selected
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

starting_screen_on = 1
new_game_screen_on = 0

writing_tool = turtle.Turtle()
writing_tool.speed(0)
writing_tool.color('white')
writing_tool.penup()
writing_tool.hideturtle()
writing_tool.goto(0, 0)
writing_tool.hideturtle()

while writing_tool.isvisible() == True:
  writing_tool.hideturtle()
  if writing_tool.isvisible() == False:
    break

def write_console(x_c, y_c, text, size):
  global writing_tool
  writing_tool.goto(x_c, y_c)
  writing_tool.write(text, align="center", font=("Arial", size, "normal"))

def starting_screen():
  global New_Game_Square, load_game_square, title_text
  turtle.tracer(0, 0)
  #
  New_Game_Square = turtle.Turtle()
  New_Game_Square.speed(0)
  New_Game_Square.color("blue")
  New_Game_Square.penup()
  New_Game_Square.goto(-90, 200)
  New_Game_Square.pendown()
  New_Game_Square.begin_fill()
  for _ in range(2):
    New_Game_Square.forward(180)
    New_Game_Square.left(90)
    New_Game_Square.forward(40)
    New_Game_Square.left(90)
  New_Game_Square.end_fill()
  New_Game_Square.hideturtle()
  New_Game_Square.penup()
  #
  load_game_square = turtle.Turtle()
  load_game_square.speed(0)
  load_game_square.color("blue")
  load_game_square.penup()
  load_game_square.goto(-90, 0)
  load_game_square.pendown()
  load_game_square.begin_fill()
  for _ in range(2):
    load_game_square.forward(180)
    load_game_square.left(90)
    load_game_square.forward(40)
    load_game_square.left(90)
  load_game_square.end_fill()
  load_game_square.hideturtle()
  load_game_square.penup()
  #
  load_game_square.goto(-90, -200)
  load_game_square.pendown()
  load_game_square.begin_fill()
  for _ in range(2):
    load_game_square.forward(180)
    load_game_square.left(90)
    load_game_square.forward(40)
    load_game_square.left(90)
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

def new_game():
  global custom_square, new_game_text, coop_square
  turtle.tracer(0, 0)
  #
  start_clear()
  #
  custom_square = turtle.Turtle()
  custom_square.speed(0)
  custom_square.color('blue')
  custom_square.penup()
  custom_square.goto(-350, 300)
  custom_square.pendown()
  custom_square.begin_fill()
  for _ in range(2):
    custom_square.forward(100)
    custom_square.left(90)
    custom_square.forward(30)
    custom_square.left(90)
  custom_square.end_fill()
  custom_square.hideturtle()
  custom_square.penup()
  #
  coop_square = turtle.Turtle()
  coop_square.speed(0)
  coop_square.color("blue")
  coop_square.penup()
  coop_square.goto(-115, 300)
  coop_square.pendown()
  coop_square.begin_fill()
  for _ in range(2):
    coop_square.forward(225)
    coop_square.left(90)
    coop_square.forward(30)
    coop_square.left(90)
  coop_square.end_fill()
  coop_square.hideturtle()
  coop_square.penup()
  #
  freefor_all_square = turtle.Turtle()
  freefor_all_square.speed(0)
  freefor_all_square.color("blue")
  freefor_all_square.penup()
  freefor_all_square.goto(185, 300)
  freefor_all_square.pendown()
  freefor_all_square.begin_fill()
  for _ in range(2):
    freefor_all_square.forward(225)
    freefor_all_square.left(90)
    freefor_all_square.forward(30)
    freefor_all_square.left(90)
  freefor_all_square.end_fill()
  freefor_all_square.hideturtle()
  freefor_all_square.penup()
  #
  new_game_text = turtle.Turtle()
  new_game_text.speed(0)
  new_game_text.color("white")
  new_game_text.penup()
  new_game_text.hideturtle()
  new_game_text.goto(0, 400)
  new_game_text.write("Game Mode:", align="center", font=("Arial", 30, "normal"))
  #
  new_game_text.goto(300, 300)
  new_game_text.write("Free For All", align="center", font=("Arial", 20, "normal"))
  #
  new_game_text.goto(0, 300)
  new_game_text.write("Co-Op Survival", align="center", font=("Arial", 20, "normal"))
  #
  new_game_text.goto(-300, 300)
  new_game_text.write("Custom", align="center", font=("Arial", 20, "normal"))
  #
  new_game_text.goto(0, 100)
  new_game_text.write("Bots:", align="center", font=("Arial", 30, "normal"))
  #
  new_game_text.goto(-200, 0)
  new_game_text.write("1", align="center", font=("Arial", 20, "normal"))
  #
  new_game_text.goto(-100, 0)
  new_game_text.write("2", align="center", font=("Arial", 20, "normal"))
  #
  new_game_text.goto(0, 0)
  new_game_text.write("3", align="center", font=("Arial", 20, "normal"))
  #
  new_game_text.goto(100, 0)
  new_game_text.write("4", align="center", font=("Arial", 20, "normal"))
  #
  new_game_text.goto(200, 0)
  new_game_text.write("5", align="center", font=("Arial", 20, "normal"))
  #
  turtle.update()
  turtle.tracer(1, 10)

def redo_custom_text():
  global new_game_text
  new_game_text.goto(-300, 300)
  new_game_text.write("Custom", align="center", font=("Arial", 20, "normal"))

def redo_coop_text():
  global new_game_text
  new_game_text.goto(0, 300)
  new_game_text.write("Co-Op Survival", align="center", font=("Arial", 20, "normal"))

def redo_f4a_text():
  global new_game_text
  new_game_text.goto(300, 300)
  new_game_text.write("Free For All", align="center", font=("Arial", 20, "normal"))

def coop_select():
  global coop_selected, custom_selected, coop_selected_square, f4a_selected
  coop_selected = 1
  coop_square.clear()
  turtle.tracer(0, 0)
  coop_selected_square = turtle.Turtle()
  coop_selected_square.speed(0)
  coop_selected_square.color(BRIGHT_YELLOW)
  coop_selected_square.penup()
  coop_selected_square.goto(-115, 300)
  coop_selected_square.pendown()
  coop_selected_square.begin_fill()
  for _ in range(2):
    coop_selected_square.forward(225)
    coop_selected_square.left(90)
    coop_selected_square.forward(30)
    coop_selected_square.left(90)
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
    custom_square.color('blue')
    custom_square.penup()
    custom_square.goto(-350, 300)
    custom_square.pendown()
    custom_square.begin_fill()
    #
    for _ in range(2):
      custom_square.forward(100)
      custom_square.left(90)
      custom_square.forward(30)
      custom_square.left(90)
    #
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
    freefor_all_square.color("blue")
    freefor_all_square.penup()
    freefor_all_square.goto(185, 300)
    freefor_all_square.pendown()
    freefor_all_square.begin_fill()
    for _ in range(2):
      freefor_all_square.forward(225)
      freefor_all_square.left(90)
      freefor_all_square.forward(30)
      freefor_all_square.left(90)
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
  custom_selected_square.color(BRIGHT_YELLOW)
  custom_selected_square.penup()
  custom_selected_square.goto(-350, 300)
  custom_selected_square.pendown()
  custom_selected_square.begin_fill()
  for _ in range(2):
    custom_selected_square.forward(100)
    custom_selected_square.left(90)
    custom_selected_square.forward(30)
    custom_selected_square.left(90)
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
    coop_square.color("blue")
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
    freefor_all_square.color("blue")
    freefor_all_square.penup()
    freefor_all_square.goto(185, 300)
    freefor_all_square.pendown()
    freefor_all_square.begin_fill()
    for _ in range(2):
      freefor_all_square.forward(225)
      freefor_all_square.left(90)
      freefor_all_square.forward(30)
      freefor_all_square.left(90)
    freefor_all_square.end_fill()
    freefor_all_square.hideturtle()
    freefor_all_square.penup()
    redo_f4a_text()
    turtle.update()
    turtle.tracer(1, 10)


def free_4_all_select():
  global coop_selected, custom_selected, f4a_selected, free_selected_square
  turtle.tracer(0, 0)
  f4a_selected = 1
  free_selected_square = turtle.Turtle()
  free_selected_square.speed(0)
  free_selected_square.color(BRIGHT_YELLOW)
  free_selected_square.penup()
  free_selected_square.goto(185, 298)
  free_selected_square.begin_fill()
  #
  for _ in range(2):
    free_selected_square.forward(227)
    free_selected_square.left(90)
    free_selected_square.forward(35)
    free_selected_square.left(90)
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
    coop_square.color("blue")
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
    custom_square.color('blue')
    custom_square.penup()
    custom_square.goto(-350, 300)
    custom_square.pendown()
    custom_square.begin_fill()
    #
    for _ in range(2):
      custom_square.forward(100)
      custom_square.left(90)
      custom_square.forward(30)
      custom_square.left(90)
    #
    custom_square.end_fill()
    custom_square.hideturtle()
    custom_square.penup()
    redo_custom_text()
    turtle.update()
    turtle.tracer(1, 10)

def click_thing(x, y):
  global starting_screen_on, new_game_screen_on #1
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


DEBUG 188.0 328.0
DEBUG 411.0 327.0
DEBUG 187.0 300.0
DEBUG 413.0 300.0

starting_screen()

screen.onscreenclick(click_thing)

turtle.onkey(key_1, "1")

turtle.onkeypress(ctrl_key, "Control_L")
turtle.onkeyrelease(ctrl_key1, "Control_L")

turtle.listen()

turtle.mainloop()
