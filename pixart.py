

PIXEL_SIZE = 30
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'


def initialization(turta):
    '''Function which sets the speed, pencolor and the starting point of the turtle to start drawing'''
    turta.speed(0)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2)  # initial coordinate of the turtle to begin drawing
    turta.setheading(0)
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)


"""The get_color(color) function returns the color based on the following values"""

def get_color(color):
    if color == "0":
        return "black"
    elif color == "1":
        return "white"
    elif color == "2":
        return "red"
    elif color == "3":
        return "yellow"
    elif color == "4":
        return "orange"
    elif color == "5":
        return "green"
    elif color == "6":
        return "yellowgreen"
    elif color == "7":
        return "sienna"
    elif color == "8":
        return "tan"
    elif color == "9":
        return "gray"
    elif color == "A":
        return "darkgray"
    else:
        return None

"""The draw_color_pixel(color_string, turta) function draws a pixel using the color returned from the get_color function, it also validates it"""
def draw_color_pixel(color_string, turta):
    color = get_color(color_string)
    if color != None:
        turta.fillcolor(color)
        turta.begin_fill()
        for i in range(4):
            turta.forward(PIXEL_SIZE)
            turta.left(90)
        turta.end_fill()
        turta.forward(PIXEL_SIZE)

"""The draw_pixel(color_string, turta) function uses draw_color_pixel(color_string, turta) to draw a single pixel"""
def draw_pixel(color_string, turta):
    draw_color_pixel(color_string, turta)

"""The draw_line_from_string(color_string, turta) function draws a line of pixels and uses the color_string to obtain the color from each character in the string
Checks if invalid color is found and stops executing once color is invalid, however executes the previous valid colors from the same string"""
def draw_line_from_string(color_string, turta):
    for color in color_string:
        if get_color(color) is None:
            return False
        draw_pixel(color,turta)
    return True


"""The draw_shape_from_string(turta) function repeatedly takes a string of colors from user input and uses 
that string to draw a line of pixels using the colors from that string until an invalid color is entered or enter is pressed without inputting anything
Uses PIXEL_SIZE constant"""
def draw_shape_from_string(turta):
    while True:
        color_string = input("Enter string of colors (or press Enter to exit) (ALSO give repeating digit 1212 or 2121 for surprise >:D):")
        # Stop loop if an empty string is entered
       
        if color_string == "":
            print("Empty string. bye bye...")
            break
        if draw_line_from_string(color_string, turta):

            # Move to start of next row
            turta.penup()
            turta.setheading(270)  # face down
            turta.forward(PIXEL_SIZE)
            turta.setheading(180)  # face left to move back
            turta.forward(len(color_string) * PIXEL_SIZE)
            turta.setheading(0)  # face right to start new row
            turta.pendown()
        else:
            print("Invalid color string entered. Stopping...")
            break

"""The draw_grid(turta) function draws a 20x20 grid in red and black using constants"""
def draw_grid(turta):
    # This makes the 20x20 chessboard
    for row in range( ROWS):
        if row % 2 == 0:
            color_string = "02" * (COLUMNS // 2)
        else:
            color_string = "20" * (COLUMNS // 2)
        draw_line_from_string(color_string, turta)
        turta.penup()
        turta.setheading(270)  # move down a row
        turta.forward(PIXEL_SIZE)
        turta.setheading(180)  # move back to start of the row
        turta.forward(COLUMNS * PIXEL_SIZE)
        turta.setheading(0)
        turta.pendown()

"""The draw_shape_from_file(turta) takes a file path as input from user and reads each line in the file, which is a color string
and draws a line of pixels according to that string until an invalid color is detected or end of file has been reached
File is closed after reading"""
#Add function to draw shapes from a file
def draw_shape_from_file(turta):
    file_path = input("Enter the path of the file you want to read: ")
    
    file = open(file_path, 'r')  # Open the file (assumes the path is valid)
    for line in file:
        line = line.strip()  # Remove any leading/trailing whitespace
        if draw_line_from_string(line, turta):
            # Move to start of next row
            turta.penup()
            turta.setheading(270)  # face down
            turta.forward(PIXEL_SIZE)
            turta.setheading(180)  # face left to move back
            turta.forward(len(line) * PIXEL_SIZE)
            turta.setheading(0)  # face right to start new row
            turta.pendown()
        else:
            print("Invalid color string in file. Stopping...")
            break
    file.close()  # Close the file after reading

