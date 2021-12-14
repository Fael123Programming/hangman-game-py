from word import Word

class Match:
    def __init__(self, word: Word, chances: int):
        self.__word = word  # Representa a palavra a ser descoberta.
        self.__symbols = list("*" * len(word))  # Representa uma lista de asteriscos que vão sendo, de acordo com os acertos do jogador, descobertos ou não. 
        self.__chances = chances  # Quantidade de erros que o jogador pode cometer.
        self.__hits = 0  # Quantidade de acertos do jogador.
        self.__errors = 0  # Quantidade de erros cometidos.
        self.__status = Status()  # Status da partida

    @property
    def word(self):
        return self.__word

    @property
    def chances(self):
        return self.__chances

    @property
    def hits(self):
        return self.__hits

    @property
    def errors(self):
        return self.__errors

    @property
    def symbols(self):
        return self.__symbols

    @property
    def status(self): 
        return self.__status
    
        
    def __analyse_charactere(self, charactere: str) -> str:
        if len(charactere) > 1:
            self.__errors += 1
            return "mais que um caractere digitado"
        elif len(charactere) == 0:
            self.__errors += 1
            return "nenhum caractere digitado"    
        elif not charactere.isalpha():
            self.__errors += 1
            return "caractere invalido"
        else: 
            hit = False
            for letter in range(len(self.__word)):
                if self.__word[letter] == charactere:
                    self.__symbols[letter] = charactere 
                    self.__hits += 1
                    hit = True
            if not hit:
                self.__errors += 1        
            return "caractere encontrado" if hit else "caractere nao encontrado"

    def play(self):
        from system import System
        from time import sleep
        sys = System() 
        sys.msg("Hangman Game", 50)
        print("Secret word: ", end="")
        sys.print_list(self.__symbols)
        print("\nErrors:", self.__errors)
        print("Hint:", self.__word.hint)
        sys.draw_gallows(self.__errors)
        won, lose = False, False
        while True:
            letter = input("Letter of your choice: ").lower()
            sys.clean_prompt()
            res = self.__analyse_charactere(letter)
            won, lose = res == Status.WON, res == Status.LOSE
            sys.msg(res.capitalize(), 50)
            sleep(2)
            sys.clean_prompt()
            sys.msg("Hangman Game", 50)
            print("Secret word: ", end="")
            sys.print_list(self.__symbols)
            print("\nErrors:", self.__errors)
            print("Hint:", self.__word.hint)
            sys.draw_gallows(self.__errors)
            if won or lose:
                return self.__status            


class Status:
   """
   Esta classe representa o status atual de uma partida e é utilizada para a contabilidade do desempenho
   do jogador ao final da partida.
   O status de uma partida pode ser:
   - Se o número de erros cometidos pelo jogador é igual à quantidade de chances: "jogador perdeu";
   - Senão se os acertos conseguidos pelo jogador são iguais ao tamanho de palavra secreta: "jogador venceu";
   - Senão, o status será: "em andamento".
   """ 
   LOSE = "jogador perdeu"
   WON = "jogador venceu"
   IN_PROGRESS = "em andamento"

   def __init__(self):
      self.__status = Status.IN_PROGRESS

   def update_status(self, match: Match):
      if match.erros == match.chances:
         self.__status = Status.LOSE
      elif match.acertos == len(match.palavra):
         self.__status = Status.WON
      else:
         self.__status = Status.IN_PROGRESS  

   @property
   def status(self):
      return self.__status