from extra.singleton_meta.singleton_meta import SingletonMeta


class CharAnalyzer(metaclass=SingletonMeta):
    from extra.match.match import Match

    @staticmethod
    def analyse_char(match: Match, char: str) -> str:
        if len(char) > 1:
            match.errors += 1
            match.update_status()
            return "more than a single character typed"
        elif len(char) == 0:
            match.errors += 1
            match.update_status()
            return "no character typed"
        elif not char.isalpha():
            match.errors += 1
            match.update_status()
            return "invalid character"
        else:
            hit = False
            for letter in range(len(match.word.word)):
                if match.word.word[letter].lower() == char:
                    match.symbols[letter] = match.word.word[letter]
                    match.hits += 1
                    hit = True
            if not hit:
                match.errors += 1
            match.update_status()
            return "character found" if hit else "character not found"
