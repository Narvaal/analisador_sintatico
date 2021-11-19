import random   
import pandas as pd

# Gera testes de entrada para o programa em .xlsx

#Parametros para criação dos valores
values = ['1','2','3','+','-']   #Caracteres usados
numValuesList =  100             #Numero de testes 
sizeMin = 5                      #Tamanho minimo de cada teste
sizeMax = 8                      #Tamanho maximo de cada teste   

#Gerando valores
lines = []
for i in range(numValuesList):
    line = ""
    for i in range(random.randint(sizeMin,sizeMax)):
        line += random.choice(values)
    lines.append(line)

#Gerando Excel 
dataFrame = pd.DataFrame(
    {
        "Valor": lines,
        "Resultado": "Não testado" 
    }
)
dataFrame.to_excel("testes.xlsx")  

