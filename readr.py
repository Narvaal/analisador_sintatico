import pandas as pd
# Básicamente altera a resposta dos resultados escrevendo
# se aquela combinação de caracteres é ou não valida 

#Lendo a tabela 
tabela = pd.read_excel("testes.xlsx",dtype="string")

# Lista com os valores da tabela
testes = list(tabela['Valor']) 
resultados = list(tabela['Resultado']) 

#Inico do programa

# Aqui onde a validação deve ser feita 

#  Exemplo de implementação 
#
#   if teste[i] == valido:
#       rultado[i] = "valido"
#   else: resultado[i] = "invalido"


#Escrevendo no arquivo testes com os resultados
dataFrame = pd.DataFrame(
    {
        "Valor": testes,
        "Resultado": resultados
    }
)
dataFrame.to_excel("testes.xlsx")  




