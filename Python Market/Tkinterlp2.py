from tkinter import *
from OP1 import *
from OP2 import *
from OP3 import *
from OP4 import *




class Menu:
    def __init__(self,raiz):
        self.raiz=raiz
        self.framecima = Frame(self.raiz)
        self.framecima.pack()
        self.frame1 = Frame(self.raiz)
        self.frame1.pack()
        self.frame2 = Frame(self.raiz)
        self.frame2.pack()

        # criando Titulo
        self.titulo1 = Label(self.framecima, text="Python Market", fg="green", bg="white", font=("Arial", "72", "bold"))
        self.titulo1.pack()
        self.titulo2 = Label(self.framecima, text="Menu", fg="green", bg="white", font=("Arial", "46", "bold"))
        self.titulo2.pack()
        # foto=PhotoImage(file="carr.png")
        # titulo3=Label(framecima,image=foto)
        # titulo3.pack()

        # criando botoes
        self.botao1 = Button(self.frame1,command=self.op1, text="Mostrar Estoque", fg="black", bg="grey",
                             font=("Arial,14,bold"))
        #self.botao1.bind("<Button-1>", self.botao1clic)
        self.botao1["width"] = 20
        self.botao1.pack(side=LEFT)
        self.botao2 = Button(self.frame2,command=self.op2, text="Buscar", fg="black", bg="grey", font=("Arial,14,bold"))
        self.botao2["width"] = 20
        self.botao2.pack(side=LEFT)
        self.botao3 = Button(self.frame1,command=self.op3, text="Repor Estoque", fg="black", bg="grey", font=("Arial,14,bold"))
        self.botao3["width"] = 20
        self.botao3.pack(side=LEFT)
        self.botao4 = Button(self.frame2,command=self.op4 ,text="Incluir produto no estoque", fg="black", bg="grey", font=("Arial,14,bold"))
        self.botao4["width"] = 20
        self.botao4.pack(side=LEFT)
        self.botao5 = Button(self.frame1, text="Efetuar Venda", fg="black", bg="grey", font=("Arial,14,bold"))
        self.botao5["width"] = 20
        self.botao5.pack(side=LEFT)
        self.botao6 = Button(self.frame2, command=self.sair, text="Sair", fg="black", bg="grey", font=("Arial,14,bold"))
        self.botao6["width"] = 20
        self.botao6.pack(side=LEFT)

    def sair(self):
        self.raiz.destroy()
    def op1(self):
        self.framecima.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        m=OP1(self.raiz)
        self.raiz.mainloop()



    def op2(self):
        self.framecima.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        m = OP2(self.raiz)
        self.raiz.mainloop()

    def op3(self):
        self.framecima.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        m = OP3(self.raiz)
        self.raiz.mainloop()

    def op4(self):
        self.framecima.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        m = OP4(self.raiz)
        self.raiz.mainloop()






















