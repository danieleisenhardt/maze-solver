from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
    
    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self.draw_cell(i,j)
    
    def draw_cell(self, i, j):
        if self._win is None:
            return
        cell = self._cells[i][j]
        x = self._x1 + self._cell_size_x * i
        y = self._y1 + self._cell_size_y * j
        cell.draw(x, y, x + self._cell_size_x, y + self._cell_size_y)
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        # time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self.draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self.draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, i, j):
        current = self._get_cell(i, j)
        current.visited = True

        while True:
            options = []

            left = self._get_cell(i - 1, j)
            if (left is not None and left.visited == False):
                options.append([i -1, j])
            right = self._get_cell(i + 1, j)
            if (right is not None and right.visited == False):
                options.append([i + 1, j])
            top = self._get_cell(i, j - 1)
            if (top is not None and top.visited == False):
                options.append([i, j - 1])
            bottom = self._get_cell(i, j + 1)
            if (bottom is not None and bottom.visited == False):
                options.append([i, j + 1])
            
            if len(options) == 0:
                break

            next = options[random.randrange(len(options))]
            next_cell = self._get_cell(next[0], next[1])
            if (next[0] < i):
                current.has_left_wall = False
                next_cell.has_right_wall = False
            if (next[0] > i):
                current.has_right_wall = False
                next_cell.has_left_wall = False
            if (next[1] < j):
                current.has_top_wall = False
                next_cell.has_bottom_wall = False
            if (next[1] > j):
                current.has_bottom_wall = False
                next_cell.has_top_wall = False
            
            self.draw_cell(i, j)
            self.draw_cell(next[0], next[1])

            self._break_walls_r(next[0], next[1])

    
    def _get_cell(self, i, j):
        if i < 0 or i >= self._num_cols or j < 0 or j >= self._num_rows:
            return None
        return self._cells[i][j]
