from partida import Partida
from time import sleep

def clear():
    from os import system,name
    system("cls" if name=="nt" else "clear")


palavra=input("Palavra a ser descoberta: ")
clear()    
p1=Partida(palavra,5)
venceu=False
while(True):
    p1.atualizarStatusPartida()
    print("---> "+p1.status.capitalize()+" <---")
    print(f"Palavra: {''.join(p1.simbolos)}")
    print(f"Chances: {p1.chances}")
    print(f"Acertos: {p1.acertos}")
    print(f"Erros: {p1.erros}")
    print("-----------------------------")
    if(p1.erros==p1.chances): break
    elif(p1.acertos==len(p1.palavra)): 
        venceu=True
        break
    carac=input("Caractere: ")
    resultado=p1.analisarCaractere(carac)
    if(resultado!= "analisado com sucesso"):
        clear()
        print(f"> {resultado.capitalize()} <")
        sleep(2)
    clear()
if(not venceu): print("Voce perdeu!")
else: print("Voce venceu!")