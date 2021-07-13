class Partida:
    def __init__(self,palavra,chances):
        self.__palavra=palavra
        self.__simbolos=self.atribuirSimbolos()
        self.__chances=chances
        self.__acertos=0
        self.__erros=0
        self.__status=""

    @property
    def palavra(self):return self.__palavra

    @property
    def chances(self):return self.__chances

    @property
    def acertos(self):return self.__acertos

    @property
    def erros(self):return self.__erros

    @property
    def simbolos(self):return self.__simbolos

    @property
    def status(self): return self.__status
    
    def atualizarStatusPartida(self):
        if(self.__erros==self.__chances): self.__status="jogador perdeu"
        elif(self.__acertos==len(self.__palavra)): self.__status="jogador venceu"
        else: self.__status="em andamento"
        
    def analisarCaractere(self,caractere):
        acertou=False
        if(len(caractere)==0 or len(caractere)>1):
            self.__erros+=1
            return  "caractere invalido"
        elif caractere in self.__simbolos: 
            self.__erros+=1
            return "caractere ja digitado"
        for letra in range(len(self.__palavra)):
            if(self.__palavra[letra]==caractere):
                self.__simbolos[letra]=caractere 
                self.__acertos+=1
                acertou=True
        if(not acertou):self.__erros+=1
        return "analisado com sucesso"
        
    def atribuirSimbolos(self):
        qtdDeLetras=len(self.__palavra)
        simbolos=[]
        while(qtdDeLetras>0):
            simbolos.append("*")
            qtdDeLetras-=1
        return simbolos 