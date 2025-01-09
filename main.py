from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(100, 100, 200, 200)
    

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(200, 100, 300, 200)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(100, 200, 200, 300)
              
    win.wait_for_close()


main()
