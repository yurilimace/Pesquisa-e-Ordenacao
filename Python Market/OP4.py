from tkinter import *
import Tkinterlp2

class OP4:
     def __init__(self, raiz):
        self.raiz = raiz
        self.framecima = Frame(self.raiz)
        self.framecima.pack(side=TOP)
        self.frame1 = Frame(self.raiz)
        self.frame1.pack(side=TOP)
        self.frame2 = Frame(self.raiz)
        self.frame2.pack()
        self.frame3=Frame(self.raiz)
        self.frame3.pack()
        titulo1 = Label(self.framecima, text="Python Market", fg="green", bg="white", font=("Arial", "46", "bold"))
        titulo1.pack()
        titulo2 = Label(self.framecima, text="Estoque", fg="green", bg="white", font=("Arial", "22", "bold"))
        titulo2.pack()
        titulo8=Label(self.frame2)
        titulo8.pack()

        #nome
        titulo3=Label(self.framecima,text="Nome do Produto:")
        titulo3.pack()
        ent=Entry(self.framecima,bd=4,relief=GROOVE)
        ent.pack()

        #descriçao do prodtuo
        titulo4=Label(self.framecima,text="Descrição do Produto:")
        titulo4.pack()
        ent=Entry(self.framecima,bd=4,relief=GROOVE)
        ent.pack()

        #preço de compra
        titulo5=Label(self.framecima,text="Preço de Compra")
        titulo5.pack()
        ent=Entry(self.framecima,bd=4,relief=GROOVE)
        ent.pack()

        #preço venda
        titulo6=Label(self.framecima,text="Preço de Venda")
        titulo6.pack()
        ent=Entry(self.framecima,bd=4,relief=GROOVE)
        ent.pack()

        #quantidade
        titulo7=Label(self.framecima,text="Quantidade estocada:")
        titulo7.pack()
        ent=Entry(self.framecima,bd=4,relief=GROOVE)
        ent.pack()

        self.botao1=Button(self.frame1, command=self.fechar, text='Confirmar', fg='black', bg='dark grey',
                             font=("Arial", "10", "bold"))
        self.botao1["width"]=15
        self.botao1.pack(side=LEFT)


        # criando botao
        self.botao3 = Button(self.frame3, command=self.fechar, text='voltar ao menu principal', fg='black', bg='grey',
                             font=("Arial", "10", "bold"))
        self.botao3["width"] = 20
        # self.botao1.bind("<Button-1>",self.teste)
        self.botao3.pack()
        self.botao1click = 0

     def fechar(self):
        self.framecima.destroy()
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        m = Tkinterlp2.Menu(self.raiz)
        self.raiz.mainloop()