class TictactoeaGameEngine:
    def  __init__(self):
        self.SIZE = 3
        self.board =list( '.'*self.SIZE * self.SIZE)#['.','.','.','.','.','.','.','.']
        self.turn = 'X'

    def show_board(self): #짤것
        print(self.board)

    def set(self, row, col):  #우리가 짤거
        self.board[7] = self.turn
        self.row =row
        self.col = col
        pass

    def set_winner(self): #1,2
        # - 3줄
        #/3 줄
        # \
        return self.turn
        # 비기는 조건: 디 채워졌을때 위의것에 해당안됬을때: self.board에 '.'이 없는 상태
        return 'd'

    def change_turn(self):
        #self.turn 'X' 면 '0', '0'면 'X'로 바꾸자
        pass

if __name__ == '__main__':
    game_engine  = TictactoeaGameEngine()
    game_engine.show_board()
    game_engine.set(3,2)
    game_engine.show_board()
    game_engine.set(3,1)
    game_engine.set(3,3)
    print(game_engine.set_winner())
    game_engine.change_turn()
    print(game_engine.turn)


