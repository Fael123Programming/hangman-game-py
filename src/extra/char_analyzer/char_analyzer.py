class CharAnalyzer:

    @staticmethod
    def analyse_char(match, char: str) -> str:
        if len(char) > 1:
            match.errors += 1
            match.update_status()
            return "mais que um caractere digitado"
        elif len(char) == 0:
            match.errors += 1
            match.update_status()
            return "nenhum caractere digitado"
        elif not char.isalpha():
            match.errors += 1
            match.update_status()
            return "caractere invalido"
        else:
            hit = False
            for letter in range(len(match.word.word)):
                if match.word.word[letter] == char:
                    match.symbols[letter] = char
                    match.hits += 1
                    hit = True
            if not hit:
                match.errors += 1
            match.update_status()
            return "caractere encontrado" if hit else "caractere nao encontrado"
