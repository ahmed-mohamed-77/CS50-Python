import pytest
from unittest.mock import patch, call
from project.project import main, hollow_pentagon, solid_squares, circle_canvas, triangle_canvas

@pytest.fixture
def mock_turtle():
    with patch('project_turtle.project.Turtle') as mock_turtle:
        yield mock_turtle

@pytest.fixture
def mock_hollow_pentagon():
    with patch('project_turtle.project.hollow_pentagon') as mock_hollow_pentagon:
        yield mock_hollow_pentagon

@pytest.fixture
def mock_solid_squares():
    with patch('project_turtle.project.solid_squares') as mock_solid_squares:
        yield mock_solid_squares

@pytest.fixture
def mock_circle_canvas():
    with patch('project_turtle.project.circle_canvas') as mock_circle_canvas:
        yield mock_circle_canvas

@pytest.fixture
def mock_triangle_canvas():
    with patch('project_turtle.project.triangle_canvas') as mock_triangle_canvas:
        yield mock_triangle_canvas

@pytest.fixture
def mock_print():
    with patch('builtins.print') as mock_print:
        yield mock_print

def test_draw_pentagon(mock_hollow_pentagon):
    with patch('builtins.input', side_effect=['pentagon', 'exit']):
        main()
        mock_hollow_pentagon.assert_called_once()

def test_draw_squares(mock_solid_squares):
    with patch('builtins.input', side_effect=['square', '3', 'exit']):
        main()
        mock_solid_squares.assert_called_once()

def test_draw_circles(mock_circle_canvas):
    with patch('builtins.input', side_effect=['circle', '4', 'exit']):
        main()
        mock_circle_canvas.assert_called_once()

def test_draw_triangles(mock_triangle_canvas):
    with patch('builtins.input', side_effect=['triangle', '5', 'exit']):
        main()
        mock_triangle_canvas.assert_called_once()

def test_invalid_input(mock_print):
    with patch('builtins.input', side_effect=['hexagon', 'exit']):
        main()
        mock_print.assert_any_call("\nERROR PLEASE SELECT FROM THE GIVEN SHAPES\n")
        mock_print.assert_any_call("*" * 30)

