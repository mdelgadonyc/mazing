from graphics import Window, Line, Points


def main():
    win = Window(800, 600)
    l = Line(Points(100, 100), Points(400, 400))
    win.draw_line(l, "black")
    win.wait_for_close()

main()
