
from turtle import Screen, Turtle
from pixart import initialization,draw_grid,draw_shape_from_file,draw_shape_from_string

"""Calling of functions in main are made into comments to avoid all functions running on the same canvas,
They require to be uncommented to be tested"""
# Main function and script
def main():
    screen = Screen()
    turta = Turtle()
  
    initialization(turta)
    
    # Uncomment to test drawing from a string:
    # draw_shape_from_string(turta)

    # Uncomment to test drawing from a file:
    # draw_shape_from_file(turta)

    # Uncomment to test drawing a grid:
    # draw_grid(turta)

    screen.exitonclick() 


if __name__ == "__main__":
    main()