from tkinter import Tk, BOTH, Canvas

from config import Color
from geometry import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        return

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
        return

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
        return

    def close(self) -> None:
        self.__running = False
        return
    
    def draw_line(self, line: Line, fill_color: Color) -> None:
        line.draw(self.__canvas, fill_color)
        return