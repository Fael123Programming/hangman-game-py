from extra.menu.menus.abstract.menu import Menu


class MenuPlay(Menu):

    def __init__(self):
        super().__init__("Play", "Generate word", "Main menu")

    def display(self):
        from main import get_player_logged_in
        from extra.view.view import View
        from extra.match.match import Match
        view = View()
        player_logged_in = get_player_logged_in()
        generated_word = None
        word_domain = None
        while True:
            view.msg("Play")
            for option in range(len(self.options)):
                print(f"({option + 1}) - {self.options[option]}")
            view.row()
            if generated_word is None:
                print(f"Generated word: None")
            else:
                print(f"Generated word: {view.stringify_list(Match.get_asterisks(generated_word))}")
            print(f"Word Domain: {word_domain}")
            view.row()
            if player_logged_in != "None":
                opt = input(f"What do you want to do, {player_logged_in}? ")
            else:
                opt = input("What do you want to do? ")
            view.clean_prompt()
            if opt not in ["1", "2", "3"]:
                view.msg("Choose a valid option")
                view.stop()
            elif opt == "1":
                self._play(generated_word, player_logged_in)
            elif opt == "2":
                list_word_domain_generated_word = self.generate_word()
                word_domain = list_word_domain_generated_word[0]
                generated_word = list_word_domain_generated_word[1]
            else:
                return
            view.clean_prompt()

    @staticmethod
    def generate_word() -> list:  # Returns [word_domain, generated_word] if any
        from extra.view.view import View
        from extra.data_persistence.database_manager import DatabaseManager
        from extra.word_provider.word_provider import WordProvider
        view = View()
        db = DatabaseManager()
        view.msg("Choose a domain")
        domains = db.word_domains()
        word_domain, generated_word = None, None
        for domain in range(len(domains)):
            print(f"[{domain + 1}] - {domains[domain]}")
        view.row()
        try:
            chosen_domain = int(input("-> "))
            view.clean_prompt()
        except ValueError:
            view.clean_prompt()
            view.msg("Choose a valid domain")
            view.stop()
        else:
            if chosen_domain not in list(range(1, len(domains) + 1)):
                view.msg("Choose a valid domain")
                view.stop()
            else:
                view.msg(f"You have chosen {domains[chosen_domain - 1]}", show_lower_line=False)
                view.msg("Generate a random word from it [y/n]?", show_upper_line=False)
                resp = input("-> ")[0].lower()
                view.clean_prompt()
                if resp == "y":
                    word_domain = domains[chosen_domain - 1]
                    generated_word = WordProvider(db).random_word(word_domain)
                else:
                    view.msg("Canceled")
                    view.stop()
        finally:
            return [word_domain, generated_word]

    @staticmethod
    def _play(word, player):
        from extra.view.view import View
        from extra.match.match import Match
        from extra.data_persistence.database_manager import DatabaseManager
        view = View()
        if word is None:
            view.msg("You have to go into 'Generate word' first'")
            view.stop()
        else:
            if player != "None":
                player = DatabaseManager().select_player(player)
            match = Match(word, player)
            match.play()
