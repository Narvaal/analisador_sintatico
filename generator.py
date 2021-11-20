import random   
import pandas as pd

# Gera testes de entrada para o programa em .xlsx

#Parametros para criação dos valores
values = ['+', '-', '*', '/', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   #Caracteres usados
numValuesList =  10000               #Numero de testes 
sizeMin = 3                      #Tamanho minimo de cada teste
sizeMax = 10                      #Tamanho maximo de cada teste   

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

