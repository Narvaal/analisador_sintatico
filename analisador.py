from gramatica import Alfabeto, NaoTerminais, Sinicial, RegrasProducao


class Analisador:
    __estado = str()
    __cabeca = int()
    __L1 = list()
    __L2 = list()
    __cadeia = str()

    def __init__(self, cadeia) -> None:
        self.__estado = 'q'
        self.__cabeca = 1
        self.__L1.append('e')
        self.__L2.append("$")
        self.__L2.append(f"{Sinicial}")
        self.__cadeia = cadeia+'$'

    def __print__(self) -> None:
        self.__L2.reverse()
        print(f"({self.__estado}, {self.__cabeca}, {self.__L1}, {self.__L2})")
        self.__L2.reverse()

    def __expansao(self, Regra) -> None:
        self.__estado = 'q'
        self.__L2.pop()
        for i in RegrasProducao[Regra][::-1]:
            self.__L2.append(i)
        self.__L1.append(Regra)

    def __igual(self) -> None:
        self.__estado = 'q'
        self.__L1.append(self.__L2[-1])
        self.__L2.pop()
        self.__cabeca += 1

    def __conclusao(self) -> None:
        self.__estado = 't'
        self.__L2.pop()
        self.__L2.append('e')

    def __desfazer(self) -> None:

        while True:
            self.__print__()
            self.__estado = 'b'
            tempR = self.__L1[-1]
            if tempR in Alfabeto:
                self.__cabeca -= 1
            else:

                tempP = RegrasProducao[tempR]
                for i in tempP:
                    self.__L2.pop()

            self.__L1.pop()
            self.__L2.append(tempR[0])

            if self.__L1[-2] in Alfabeto or self.__L1[-2] == 'e':
                break

    def __deusébom(self) -> None:

        if Sinicial in self.__L1[-1]:
            if self.__cabeca == 1:
                print("Fudeu")
                exit(1)
                pass
        else:

            tempR = self.__L1[-1]
            nome = tempR[0]
            numero = int(str(tempR[1:-1] + tempR[-1])) + 1
            Nregra = (nome+str(numero))
            if Nregra in RegrasProducao:
                tempP = RegrasProducao[tempR]
                tempL = len(tempP)
                if tempL > 1:
                    for i in range(tempL-1):
                        self.__L2.pop()
                print("#Regra+1")

                self.__L1.pop()
                self.__expansao(Nregra)
            else:
                print("#Backtrack")
                self.__desfazer()
                self.__deusébom()
                self.__print__()
                pass

    def analisar(self) -> None:
        print(self.__cadeia)
        while self.__estado != 't':
            self.__print__()
            if self.__L2[-1] == '$':
                self.__conclusao()
            else:
                if self.__L2[-1] in Alfabeto:
                    if self.__L2[-1] == self.__cadeia[self.__cabeca-1]:
                        self.__igual()
                    else:
                        self.__deusébom()
                else:
                    if len(self.__L2[-1]) == 1:
                        self.__expansao(self.__L2[-1]+'1')
                    else:
                        self.__deusébom()
            #input()
        self.__print__()


teste = Analisador("(1+2(")
teste.analisar()
