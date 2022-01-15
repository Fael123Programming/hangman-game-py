from extra.menu.menus.abstract.menu import Menu
from extra.view.view import View


class MenuChallenge(Menu):
    from extra.player.player import Player

    def __init__(self):
        super().__init__("Defy a player", "Received challenges", "Main menu")

    def display(self):
        from extra.data_persistence.database_manager import DatabaseManager
        from main import get_player_logged_in
        view = View()
        db = DatabaseManager()
        player = db.select_player(get_player_logged_in())
        while True:
            view.msg("Challenges")
            for option in range(len(self.options)):
                print(f"({option + 1}) - {self.options[option]}")
            view.row()
            opt = input(f"What do you want to do, {player.nickname}? ")
            view.clean_prompt()
            if opt not in ["1", "2", "3"]:
                view.msg("Choose a valid option")
            elif opt == "1":
                self._defy_player(player)
            elif opt == "2":
                self._received_challenges(player)
            else:
                return
            view.stop()
            view.clean_prompt()

    @staticmethod
    def _defy_player(player: Player):
        from extra.data_persistence.database_manager import DatabaseManager
        db = DatabaseManager()
        view = View()
        view.msg("Defy a player")
        player_nickname = input("Player nickname: ")
        view.clean_prompt()
        if player_nickname.isspace() or len(player_nickname) == 0:
            view.msg("Invalid nickname")
        elif player_nickname == player.nickname:
            view.msg(f"{player_nickname} is yourself")
        else:
            view.msg(f"Checking database for player {player_nickname}...")
            view.stop(2)
            view.clean_prompt()
            player_to_defy = db.select_player(player_nickname)
            if player_to_defy is None:
                view.msg(f"{player_nickname} seems to be nonexistent")
            else:
                from extra.menu.menus.concrete.other.menu_play import MenuPlay
                domain_and_word = MenuPlay.generate_word()
                view.clean_prompt()
                if None not in domain_and_word:
                    view.msg(f"Random word: {domain_and_word[1].word}", show_lower_line=False)
                    view.msg(f"Word domain: {domain_and_word[0]}", show_upper_line=False, show_lower_line=False)
                    view.msg(f"Receiver: {player_nickname}")
                    view.msg("Send challenge [y/n]?", show_upper_line=False)
                    resp = input("-> ")[0].lower()
                    view.clean_prompt()
                    if resp == "y":
                        from extra.challenge.challenge import Challenge
                        ch = Challenge(domain_and_word[1], player_to_defy, player)
                        db.insert_data("challenges", ch.__str__())
                        view.msg(f"Challenge sent from {player.nickname} to {player_to_defy.nickname} successfully")
                    else:
                        view.msg("Canceled")

    @staticmethod
    def _received_challenges(player: Player):
        from extra.view.view import View
        from extra.data_persistence.database_manager import DatabaseManager
        from extra.match.match import Match
        db = DatabaseManager()
        view = View()
        challenges = db.challenges_of_player(player.nickname)
        while True:
            if len(challenges) == 0:
                view.msg("No challenges found")
                view.stop()
                return
            view.msg(f"Received challenges: {player.nickname}")
            for counter in range(len(challenges)):
                view.msg(str(counter + 1), show_upper_line=False)
                print(f"Sender: {challenges[counter].sender.nickname}")
                print(f"Word: {view.stringify_list(Match.get_asterisks(challenges[counter].word))}")
                print(f"Word domain: {challenges[counter].word.domain}")
                print(f"Timestamp: {challenges[counter].timestamp}")
                view.row()
            try:
                resp = int(input("Choose a challenge to play or reject\ntyping its index or -1 to get back: "))
                view.clean_prompt()
            except ValueError:
                view.clean_prompt()
                view.msg("Choose a valid challenge index or -1")
            else:
                if resp not in range(1, len(challenges) + 1) and resp != -1:
                    view.msg("Choose a valid challenge index or -1")
                    view.stop()
                elif resp == -1:
                    return
                else:
                    while True:
                        view.msg(f"Received challenges: {player.nickname}")
                        print(f"Sender: {challenges[resp - 1].sender.nickname}")
                        print(f"Word: {view.stringify_list(Match.get_asterisks(challenges[resp - 1].word))}")
                        print(f"Word domain: {challenges[resp - 1].word.domain}")
                        print(f"Timestamp: {challenges[resp - 1].timestamp}")
                        view.row()
                        print("(1) - Play\n(2) - Reject\n(3) - Get back")
                        view.row()
                        answer = input("What do you want to do? ")
                        view.clean_prompt()
                        if answer not in ["1", "2", "3"]:
                            view.msg("Choose a valid option")
                        elif answer == "1":
                            challenges[resp - 1].play()
                            challenges.remove(challenges[resp - 1])
                            break
                        elif answer == "2":
                            view.msg("If you reject a challenge, it is considered a defeat", show_lower_line=False)
                            view.msg("Are you sure [y/n]?", show_upper_line=False)
                            confirmation = input("-> ")[0].lower()
                            view.clean_prompt()
                            if confirmation == "y":
                                from extra.match.status import Status
                                challenges[resp - 1].status.status = Status.defeat()
                                challenges[resp - 1].hand_results()
                                view.msg(f"Challenge from {challenges[resp - 1].sender.nickname} rejected")
                                challenges.remove(challenges[resp - 1])
                                break
                            else:
                                view.msg("Canceled")
                        else:
                            break
                        view.stop()
                        view.clean_prompt()
            finally:
                view.stop()
                view.clean_prompt()
