import pandas as pd
# Básicamente altera a resposta dos resultados escrevendo
# se aquela combinação de caracteres é ou não valida 

class Pilha():
    pilha = []
    def __init__(self, inicial):
        self.pilha = [inicial]
        self.tamanho = 1
        
    def Topo(self):
        return self.pilha[0]
    
    def Insere(self, elemento):
        self.pilha.insert(0, elemento)
        self.tamanho += 1
        
    def Remover(self):
        self.pilha.pop(0)
        self.tamanho -= 1
        
    def Lista(self):
        for i in range(0, self.tamanho, 1):
            print(self.pilha[i])

Alfabeto = ['+', '-', '*', '/', '(', ')', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9']

NaoTerminais = ['I', 'S', 'K', 'T', 'Z', 'F', 'N', 'D']

Sinicial = 'I'

RegrasProducao = {'I1': 'S',
                  'S1': "TK",
                  'K1': "+TK",
                  'K2': "-TK",
                  'K3': '',
                  'T1': "FZ",
                  'Z1': "*FZ",
                  'Z2': "/FZ",
                  'Z3': '',
                  'F1': "(S)",
                  'F2': 'N',
                  'F3': "-N",
                  'N1': "1D",
                  'N2': "2D",
                  'N3': "3D",
                  'N4': "4D",
                  'N5': "5D",
                  'N6': "6D",
                  'N7': "7D",
                  'N8': "8D",
                  'N9': "9D",
                  'D1': "0D",
                  'D2': "1D",
                  'D3': "2D",
                  'D4': "3D",
                  'D5': "4D",
                  'D6': "5D",
                  'D7': "6D",
                  'D8': "7D",
                  'D9': "8D",
                  'D10': "9D",
                  'D11': ''
                  }

def Algo(cadeia, state, index, hist, deriv):
    alternate = 1
    while True:
        
        if state == "t":
            return "Válido"
        
        if state == "b":
            
            if (hist.Topo()[0] in Alfabeto):
                index -= 1
                
            else:
                temp = hist.Topo()
                hist.Remover()
                alternate = int( temp.replace(hist.Topo(), '')[1:])
                hist.Insere(temp)
                
            hist.Remover()
            deriv.Remover()
            
            if index == 1 and hist.Topo()[0]+str(alternate) not in RegrasProducao:
                return "Inválido"
            
            if  deriv.Topo()[0] in NaoTerminais:
                alternate += 1
                
                if ((deriv.Topo()[0] + str(alternate)) in RegrasProducao):
                    state = "q"
                else:
                    alternate = 1
      
        if state == "q":
            
            if index > len(cadeia):
                
                state = "t"
            
            else:
                
                if (len(deriv.Topo()) == 0):
                    state = "b"
                
                elif deriv.Topo()[0] in NaoTerminais:
                    
                    if ( (deriv.Topo()[0] + str(alternate)) in RegrasProducao):
                    
                        hist.Insere(deriv.Topo()[0] + str(alternate) + hist.Topo())
                        deriv.Insere( RegrasProducao[deriv.Topo()[0] + str(alternate)] + deriv.Topo()[1:] )
                        alternate = 1
    
                
                elif cadeia[index-1] != deriv.Topo()[0]: 
                    state = "b"
                    
                else:
                    hist.Insere(deriv.Topo()[0] + hist.Topo())
                    deriv.Insere(deriv.Topo()[1:])
                    index += 1

        print("({},{},{},{}$)".format(state,index,hist.Topo(),deriv.Topo()))


#Lendo a tabela 
tabela = pd.read_excel("testes.xlsx",dtype="string")

# Lista com os valores da tabela
testes = list(tabela['Valor']) 
resultados = list(tabela['Resultado']) 

#Inico do programa

# Aqui onde a validação deve ser feita 

#  Exemplo de implementação 




for i in range (0, len(testes),1):
    L1 = Pilha("I")
    L2 = Pilha("I")
    resultados[i] = Algo(testes[i], "q",1,L1,L2)
    print("TERMINOU {}".format(i))

#Escrevendo no arquivo testes com os resultados
dataFrame = pd.DataFrame(
    {
        "Valor": testes,
        "Resultado": resultados
    }
)
dataFrame.to_excel("testes.xlsx")  

#def TreeExpansion(prod, nTerm):
    #return RegrasProducao[nTerm + prod]

#def Match():


#def Conclusion():


#def Unmatch():


#def BackTrack():


#def TryNext():

