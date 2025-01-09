from tkinter import Tk, BOTH, Canvas

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y     


class Line:
    def __init__(
            self,
            p1,
            p2
    ):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
            )


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Mazing")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height, bg="white")        
        self.__canvas.pack(fill=BOTH, expand=1)
        self.is_running = False


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")


    def draw_line(self, line: Line, color="black"):
        line.draw(self.__canvas, color)
 

    def close(self):
        self.__running = False





