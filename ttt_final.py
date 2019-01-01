import tkinter as tk
import tkinter.messagebox as tm

class TTT:
    
    def __init__(self):
        self.root = tk.Tk()
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
        self.b1 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b1))
        self.b2 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b2))
        self.b3 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b3))
        self.b4 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b4))
        self.b5 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b5))
        self.b6 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b6))
        self.b7 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b7))
        self.b8 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b8))
        self.b9 = tk.Button(self.frame2,text=" ",bg='gray',fg='white',height = 2,width=8,command = lambda : self.button_click(self.b9))
        
        self.b1.grid(row=2,column=0)
        self.b2.grid(row=2,column=1)
        self.b3.grid(row=2,column=2)
        self.b4.grid(row=1,column=0)
        self.b5.grid(row=1,column=1)
        self.b6.grid(row=1,column=2)
        self.b7.grid(row=0,column=0)
        self.b8.grid(row=0,column=1)
        self.b9.grid(row=0,column=2)
        
        
        self.frame2.pack()
        
        print(tm.askyesno("Choose","Choose your character"))
        
    def button_click(self,obj):
        obj.configure(text = 'X')
        
        
        
t = TTT()
