# Drawing Shapes with Turtle Graphics

This Python script allows you to draw various shapes using the Turtle graphics library. You can choose to draw a pentagon, square, circle, or triangle, and customize the number of shapes drawn (for square, circle, and triangle).

## Features

- Draw a hollow pentagon with different colors for each side
- Draw a specified number of solid squares with random colors, sizes, and positions
- Draw a specified number of circles with random colors, radii, and positions
- Draw a specified number of triangles with random colors, sizes, and positions
- User input validation to ensure correct shape selection and positive number input

## Requirements

- Python 3.x
- Turtle graphics library (built-in with Python)

## Usage

1. Run the script by executing `python script_name.py` in your terminal or command prompt.
2. Follow the on-screen prompts to select the shape you want to draw.
3. For squares, circles, and triangles, you'll be prompted to enter the number of shapes to draw.
4. The shapes will be drawn in the Turtle graphics window.
5. To exit the program, enter "quit", "exit", or "q" when prompted.

## Functions

- `main()`: The main function that handles the user input and calls the appropriate drawing function.
- `hollow_pentagon(turtle: Turtle, colors: List[str])`: Draws a hollow pentagon with each side in a different color from the provided list.
- `solid_squares(turtle: Turtle, colors: List[str], number: int)`: Draws the specified number of solid squares with random colors, sizes, and positions.
- `draw_square(turtle: Turtle, color: str, size: int, x: int, y: int)`: Helper function to draw a single square.
- `circle_canvas(turtle: Turtle, colors: str, number: int)`: Draws the specified number of circles with random colors, radii, and positions.
- `draw_circle(turtle: Turtle, color: str, radius: int, x: int, y: int)`: Helper function to draw a single circle.
- `triangle_canvas(turtle: Turtle, colors: str, number: int)`: Draws the specified number of triangles with random colors, sizes, and positions.
- `draw_triangle(turtle: Turtle, color: str, size: int, x: int, y: int)`: Helper function to draw a single triangle.

## Note

- The script uses the `turtle` module, which provides a graphical user interface (GUI) for drawing shapes and animations.
- The shapes are drawn in a separate window, which will remain open until you click on it to exit.
- The script uses type hints for improved code readability and maintainability.
