import tkinter

from ticatactoe_game_engine import TictactoeGameEngine

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.Tk()
        self.root.title('틱택토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}') #'300x300'
        self.root.resizable(width=False, height=False)

        self.canvas = tkinter.Canvas(self.root, bg ='white', width=self.CANVAS_SIZE, height=self.CANVAS_SIZE)
        self.canvas.pack()

        self.images= {}
        self.images['X'] = tkinter.PhotoImage(file='X.gif')
        self.images['O'] = tkinter.PhotoImage(file='O.gif')

        self.canvas.bind('<Button-1>', self.click_handler)#*** click_handler에 괄호가 없다. 지금 실행하는게 아니다.

        self.root.mainloop()

    def click_handler(self, event):
        print('click')

    def draw_board(self):
        pass


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()
