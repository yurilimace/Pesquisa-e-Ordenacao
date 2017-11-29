from tkinter import *
from Tkinterlp2 import *


class OP3:
    def __init__(self, raiz):
        self.raiz = raiz
        self.framecima = Frame(self.raiz)
        self.framecima.pack()
        self.frame1 = Frame(self.raiz)
        self.frame1.pack()
        self.frame2 = Frame(self.raiz)
        self.frame2.pack()
        self.frame3=Frame(self.raiz)
        self.frame3.pack()
        titulo1 = Label(self.framecima, text="Python Market", fg="green", bg="white", font=("Arial", "46", "bold"))
        titulo1.pack()
        titulo2 = Label(self.framecima, text="Repor Estoque", fg="green", bg="white", font=("Arial", "22", "bold"))
        titulo2.pack()

        titulo4=Label(self.framecima,text="cod  nome   preço venda  preço compra   quantidade")
        titulo4["width"]=100
        titulo4.pack()

        #barra de digitar
        titulo3=Label(self.frame2,text="Quantidade que deseja repor do produto mostrado:")
        titulo3.pack(side=LEFT)
        ent=Entry(self.frame2,bd=4,relief=GROOVE)
        ent.pack(side=LEFT)

        # criando quadrado
        s = Scrollbar(self.frame1)
        s.pack(side=RIGHT, fill=Y)
        l = Listbox(self.frame1, yscrollcommand=s.set,relief=GROOVE)
        l["width"] = 50
        for i in range(100):
            l.insert(END, "o numero da linha é" + str(i))
        l.pack(side=LEFT, fill=BOTH)
        s.config(command=l.yview)

        # criando botao
        self.botao1 = Button(self.frame3, command=self.fechar, text='voltar ao menu principal', fg='black', bg='grey',
                             font=("Arial", "10", "bold"))
        self.botao1["width"] = 20
        # self.botao1.bind("<Button-1>",self.teste)
        self.botao1.pack()
        self.botao1click = 0

    def fechar(self):
        self.framecima.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        m = Tkinterlp2.Menu(self.raiz)
        self.raiz.mainloop()