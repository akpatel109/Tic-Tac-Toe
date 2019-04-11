import tkinter as tk
import tkinter.messagebox as tm
import random

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = 'X'
   # The first element in the list is the player's letter; the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def makeMove(board, letter, move):
    board[move] = letter

def getBoardCopy(board):
    # Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def getPlayerMove(board):
    # Let the player enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
   # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Here is the algorithm for our Tic-Tac-Toe AI:
    # First, check if we can win in the next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    # Check if the player could win on their next move and block them.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise, return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

class TTT:
    letter = ['X','Y']
    turn = ''
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.tk_strictMotif()
        self.root.resizable(False,False)
        self.root.title("Tic Tac Toe")
        self.create_main_menu()
        tk.mainloop()
        
        
    def create_main_menu(self):
        self.frame1 = tk.Frame(self.root,height = 300, width = 300,background='gray')
        btn1 = tk.Button(self.frame1,text = 'New Game',command = self.create_game,height = 2,width = 12,padx = 10,pady = 10)
        btn1.grid(row=0)
        btn2 = tk.Button(self.frame1,text = 'Quit',command = self.root.destroy,height = 2,width = 12,padx = 10,pady = 10)
        btn2.grid(row=1)
        self.frame1.pack(fill="both",padx=50,pady=50)
        
        
    def create_game(self):
        self.frame1.destroy()
        self.frame2 = tk.Frame(self.root,height = 300,width = 300)
        print(dir(self.frame2),self.frame2.winfo_id())
        print(self.frame2.winfo_children())
        self.b1 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b1))
        self.b2 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b2))
        self.b3 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b3))
        self.b4 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b4))
        self.b5 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b5))
        self.b6 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b6))
        self.b7 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b7))
        self.b8 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b8))
        self.b9 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b9))
        
        self.status_bar = tk.Label(self.frame2,text = " ",bg = 'gray',fg = 'white',height = 1,width = 24)

        self.b1.grid(row=2,column=0)
        self.b2.grid(row=2,column=1)
        self.b3.grid(row=2,column=2)
        self.b4.grid(row=1,column=0)
        self.b5.grid(row=1,column=1)
        self.b6.grid(row=1,column=2)
        self.b7.grid(row=0,column=0)
        self.b8.grid(row=0,column=1)
        self.b9.grid(row=0,column=2)
        self.status = tk.Label(self.frame2,text="",bg='gray',fg='white',width=28)
        self.status.grid(row=3,columnspan=3)
        self.random_turn()
        self.frame2.pack()
        Popup()
        if TTT.turn == 'computer':
            self.comp_turn()
        else:
            self.status.configure(text = 'take your turn')
        
    def comp_turn(self):
        all_btns = [self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]
        for i in range(9):
            if all_btns[i]['text'] != " ":
                all_btns[i].configure(text = TTT.letter[1])
                if self.is_winner(TTT.letter[1]):
                    self.status.configure(text = "Sorry, You lose the game")
                    msg = tk.messagebox.askyesno("Play Again","Wanna Play Again?")
                    if msg:
                        self.frame2.destroy()
                        self.create_game()
                    else:
                        self.root.destroy()
                else:
                    all_btns[i].configure(text = " ")

        for i in range(9):
            if all_btns[i]['text'] != " ":
                all_btns[i].configure(text = TTT.letter[0])
                if self.is_winner(TTT.letter[0]):
                    all_btns[i].configure(text = TTT.letter[1])

        self.change_turn(TTT.turn)
        return
        


        
        
    def button_click(self,obj):
        if obj['text'] !=  " ":
            self.status.configure(text = 'Space already filled, choose another one')
            return
        #if TTT.turn == 'player':
        #    obj.configure(text = TTT.letter[0])
        #else:
        #    obj.configure(text = TTT.letter[1])
        obj.configure(text = TTT.letter[0])

        if self.is_winner(TTT.letter[0]):
            self.status.configure(text = 'congrats, You won the Game')
            msg = tk.messagebox.askyesno("Play Again","Wanna Play Again?")
            if msg:
                self.frame2.destroy()
                self.create_game()
            else:
                self.root.destroy()
        elif self.is_winner(TTT.letter[1]):
            self.status.configure(text = 'Sorry, You lose the game')
            msg = tk.messagebox.askyesno("Play Again","Wanna Play Again?")
            if msg:
                self.frame2.destroy()
                self.create_game()
            else:
                self.root.destroy()
                
        else:
            TTT.turn = self.change_turn(TTT.turn)
            self.comp_turn()
    
    
    def change_turn(self,text):
        if text == 'computer':
            return 'player'
        return 'computer'

    def random_turn(self):
        if random.randint(0, 1) == 0:
            TTT.turn = 'computer'
        else:
            TTT.turn = 'player'
    
    def is_winner(self,text):
        return ((self.b7['text'] == text and self.b8['text'] == text and self.b9['text'] == text) or # Across the top
    (self.b4['text'] == text and self.b5['text'] == text and self.b6['text'] == text) or # Across the middle
    (self.b1['text'] == text and self.b2['text'] == text and self.b3['text'] == text) or # Across the bottom
    (self.b7['text'] == text and self.b4['text'] == text and self.b1['text'] == text) or # Down the left side
    (self.b8['text'] == text and self.b5['text'] == text and self.b2['text'] == text) or # Down the middle
    (self.b9['text'] == text and self.b6['text'] == text and self.b3['text'] == text) or # Down the right side
    (self.b7['text'] == text and self.b5['text'] == text and self.b3['text'] == text) or # Diagonal
    (self.b9['text'] == text and self.b5['text'] == text and self.b1['text'] == text)) # Diagonal

    def start_game(self):
        while True:
            # Reset the board.
            playerLetter, computerLetter = inputPlayerLetter()
            self.random_turn()
            
            gameIsPlaying = True
            while gameIsPlaying:
                if TTT.turn == 'player':
                    # Player's turn
                    pass
            print('Do you want to play again? (yes or no)')
            if not input().lower().startswith('y'):
                break
                
class Popup:
    root = None
    def __init__(self):
        self.root = tk.Toplevel(Popup.root)
        self.root.resizable(False,False)
        self.root.title("choose your Character")
        self.frame1 = tk.Frame(self.root,height = 300, width = 300,background='gray',borderwidth=4, relief='ridge')
        label = tk.Label(self.frame1, text="chose character",height = 2,width = 20)
        label.grid(columnspan = 2,rowspan = 2)
        btn1 = tk.Button(self.frame1,text = 'X',command = lambda:self.set_letters('X','Y'),height = 1,width = 6,padx = 10,pady = 10)
        btn1.grid(row=2,column=0)
        btn2 = tk.Button(self.frame1,text = 'Y',command = lambda:self.set_letters('Y','X'),height = 1,width = 6,padx = 10,pady = 10)
        btn2.grid(row=2,column=1)
        self.frame1.pack(fill="both")

    def set_letters(self,a,b):
        TTT.letter = [a,b]
        self.root.destroy()
        
t = TTT()
