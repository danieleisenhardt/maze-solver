from tkinter import Tk, BOTH, Canvas
from cell import Cell
from line import Line
from maze import Maze
from point import Point
from window import Window

def main():
    win = Window(800,600)

    maze = Maze(50, 50, 10, 14, 50, 50, win)

    win.wait_for_close()

main()
