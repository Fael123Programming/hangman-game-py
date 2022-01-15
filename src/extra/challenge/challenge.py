from extra.match.match import Match


class Challenge(Match):
    from extra.word.word import Word
    from extra.player.player import Player

    __slots__ = ["_sender", "_timestamp"]

    def __init__(self, word: Word, receiver: Player, sender: Player, chances=5, timestamp=None):
        from datetime import datetime
        assert chances > 0, f"Chances {chances} must be non-negative"
        super().__init__(word, receiver, chances)  # receiver is the player.
        self._sender = sender
        if timestamp is None:
            self._timestamp = datetime.now().__str__()  # Timestamp
        else:
            self._timestamp = timestamp

    @property
    def sender(self):
        return self._sender

    @property
    def timestamp(self):
        return self._timestamp

    # Overridden method!
    def hand_results(self):
        from extra.match.status import Status
        from extra.data_persistence.database_manager import DatabaseManager
        self._sender.performance.challenges_made += 1
        self.player.performance.challenges_played += 1
        sender_data = {"challenges_made": self._sender.performance.challenges_made}
        player_data = {"challenges_played": self.player.performance.challenges_played}
        if self.status.status == Status.victory():
            self._sender.performance.challenge_defeats += 1
            self.player.performance.challenge_victories += 1
            sender_data["challenge_defeats"] = self._sender.performance.challenge_defeats
            player_data["challenge_victories"] = self.player.performance.challenge_victories
        else:
            self._sender.performance.challenge_victories += 1
            self.player.performance.challenge_defeats += 1
            sender_data["challenge_victories"] = self._sender.performance.challenge_victories
            player_data["challenge_defeats"] = self.player.performance.challenge_defeats
        self._sender.performance.calculate_new_yield_coe()
        self.player.performance.calculate_new_yield_coe()
        sender_data["yield_coefficient"] = self._sender.performance.yield_coefficient
        player_data["yield_coefficient"] = self.player.performance.yield_coefficient
        db = DatabaseManager()
        db.update_record("players", sender_data, {"nickname": self._sender.nickname})
        db.update_record("players", player_data, {"nickname": self.player.nickname})
        db.delete_record("challenges", {"receiver_nickname": self.player.nickname,
                                        "sender_nickname": self._sender.nickname, "timestamp": self._timestamp})

    def __str__(self):
        data = (
            self._word.word,
            self._chances,
            self.player.nickname,
            self._sender.nickname,
            self._timestamp
        )
        return data.__str__()

    @classmethod
    def instantiate(cls, data: tuple):
        assert len(data) == 5, "Data is invalid"
        from extra.data_persistence.database_manager import DatabaseManager
        from extra.word.word import Word
        db = DatabaseManager()
        receiver_player = db.select_player(data[2])
        sender_player = db.select_player(data[3])
        word_tuple = db.inspect_table("words", "*", {"word": data[0]}, "word")[0]
        assert len(word_tuple) == 3, "Word tuple is invalid"
        word = Word(word_tuple[0], word_tuple[1], word_tuple[2])
        return cls(word, receiver_player, sender_player, data[1], data[4])


