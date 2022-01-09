class Performance:
    __slots__ = ["_challenges_played", "_challenge_victories", "_challenge_defeats", "_challenges_made",
                 "_matches_played", "_match_victories", "_match_defeats", "_yield_coefficient"]
    # yield = (challenges_won + matches_won) / (challenges_played + matches_played + challenges_made).

    def __init__(self):
        # A performance of a novice is empty.
        self._challenges_played = self._matches_played = self._challenge_victories = self._match_victories = 0
        self._challenge_defeats = self._match_defeats = self._yield_coefficient = self._challenges_made = 0

    @property
    def challenges_played(self):
        return self._challenges_played

    @property
    def challenge_victories(self):
        return self._challenge_victories

    @property
    def challenge_defeats(self):
        return self._challenge_defeats

    @property
    def challenges_made(self):
        return self._challenges_made

    @property
    def matches_played(self):
        return self._matches_played

    @property
    def match_victories(self):
        return self._match_victories

    @property
    def match_defeats(self):
        return self._match_defeats

    @property
    def yield_coefficient(self):
        return self._yield_coefficient

    @challenges_played.setter
    def challenges_played(self, challenges_played):
        self._challenges_played = challenges_played

    @challenge_victories.setter
    def challenge_victories(self, challenge_victories):
        self._challenge_victories = challenge_victories

    @challenge_defeats.setter
    def challenge_defeats(self, challenge_defeats):
        self._challenge_defeats = challenge_defeats

    @challenges_made.setter
    def challenges_made(self, challenges_made):
        self._challenges_made = challenges_made

    @matches_played.setter
    def matches_played(self, matches_played):
        self._matches_played = matches_played

    @match_victories.setter
    def match_victories(self, match_victories):
        self._match_victories = match_victories

    @match_defeats.setter
    def match_defeats(self, match_defeats):
        self._match_defeats = match_defeats

    def calculate_new_yield_coe(self):
        self._yield_coefficient = (self._match_victories + self._challenge_victories) / \
                                  (self._matches_played + self._challenges_played + self._challenges_made)
