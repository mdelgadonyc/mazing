from graphics import Line, Point

class Cell:    
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(line, color=color)
        
        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(line, color=color)

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(line, color=color)

        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            color = "black"
        else:
            color = "white"
        self._win.draw_line(line, color=color)


    def draw_move(self, to_cell, undo=False):
        x_half1 = (self._x1 + self._x2) /2
        y_half1 = (self._y1 + self._y2) /2
        x_half2 = (to_cell._x1 + to_cell._x2) /2
        y_half2 = (to_cell._y1 + to_cell._y2) /2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_half1, y_half1), Point(x_half2, y_half2))
        self._win.draw_line(line, fill_color)

        
