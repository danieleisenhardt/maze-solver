from tkinter import Tk, BOTH, Canvas
from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800,600)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(50, 50, 100, 100)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell2.draw(150, 50, 200, 100)

    cell3 = Cell(win)
    cell3.has_bottom_wall = False
    cell3.draw(250, 50, 300, 100)

    win.wait_for_close()

main()
