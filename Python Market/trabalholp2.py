import pickle

class Produto:
    #construtor
    def __init__(self):
        self.nome=input("digite o nome do produto\n")
        self.codigo=0
        self.desc=input("descricao do produto\n")
        self.precoc=float(input("digite o preoço de compra do produto\n"))
        self.precov=float(input("digite o preoço de venda do produto\n"))
        self.quantidade=int(input("digite a quantidade do produto\n"))
    def __str__(self):
        return "  "+str(self.codigo) + "    " + str(self.nome)+ "   " + str(self.desc) + "   " + str(self.precoc) + "   " + str(self.precov) + "   " + str(self.quantidade)+"\n"


     
    
        
        

def Gera():
    pro=Produto()
    return pro

def menu():
    print(10*"*"+"menu"+10*"*")
    print("1 mostrar estoque")
    print("2 buscar")
    print("3 repor estoque")
    print("4 incluir produto no estoque")
    print("5 Efetuar uma venda")
    print("0 Sair do Aplicativo")
    return int(input("\ndigite sua opção\n"))    
          



def Principal():
    #estoque=[]
    f = open('estoque.arq','rb')
    estoque = pickle.load(f)
    f.close()
    while(True):
            op=menu()
            if(op==0):
                  f=open("estoque.arq","wb")
                  pickle.dump(estoque,f)
                  f.close()
                  break
            elif(op==1):
                   #imprime o estoque
                   print("codigo  nome   desc  precocompra  precovenda  quant")
                   for i in estoque:
                       print (i)


            elif(op==2):
                bus=input("Digite o nome do produto: \n")
                for i in estoque:
                    if(bus==i.nome):
                        print(i)
                    else:
                        print("Produto nao cadastrado")
                        


            elif(op==3):
                quantmin=2
                for i in estoque:
                    if(i.quantidade<=2):
                        print (i)
                        repor=int(input("\ndigite quanto deseja repor:\n"))
                        i.quantidade+=repor
                print("Estoque Reposto")
                        


            elif(op==4):
                  pro=Produto()
                  estoque.append(pro)
                  cod=estoque.index(pro)
                  pro.codigo=cod+1

            elif(op==5):
                venda=[]
                total=0
                #busca produto pelo nome
                bus=input("Nome do Produto:\n")
                for i in estoque:
                    if(bus==pro.nome):
                        print(i)
                        ven=int(input("quantidade de produtos levados:"))
                        pro=i
                        i.quantidade-=ven
                        pro.quantidade=ven
                        total+=pro.precov*pro.quantidade
                        venda.append(pro)
                    else:
                        print("Produto nao encontrado")
                #imprimindo na nota fiscal        
                print("cod    Nome    Desc   Preco")
                for i in venda:
                    print(str(i.codigo)+" "+str(i.nome) +" "+ str(i.desc)+" "+str(i.precov))

                print(total)
              
            else:
                print("opcao invalida")
                    
  
        
               
            
Principal()
   
    


    
