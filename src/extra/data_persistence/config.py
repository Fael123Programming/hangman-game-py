import sqlite3

"""
    This hangman game works with only one database that affords the game
    all data it needs. This database has the following tables:
    -> players: with the following fields (nickname text, password text, matches_played integer, match_victories integer
    , match_defeats integer, challenges_played integer, challenge_victories integer, challenge_defeats integer, 
    challenges_made integer, yield_coefficient real);
    -> challenges: with the following fields (word text, chances integer, receiver_nickname text, sender_nickname text) 
    where receiver_nickname and sender_nickname are nicknames of real players and hence, primary keys of table players;
    -> words: with the following fields (word text, hint text, domain text);
    -> domains: with the following fields (domain_name text).
"""
# The code below was already run and hence should not be executed once again!

if __name__ == "__main__":
    from database_manager import DataBaseManager
    from sys import path
    db = DataBaseManager("database")
    print(db.domains())
#     print(db.inspect_table("players", "*", "nickname"))
#     player_fields = {
#                 "nickname": "text", PK
#                 "password": "text",
#                 "matches_played": "integer",
#                 "match_victories": "integer",
#                 "match_defeats": "integer",
#                 "challenges_played": "integer",
#                 "challenge_victories": "integer",
#                 "challenge_defeats": "integer",
#                 "challenges_made": "integer",
#                 "yield_coefficient": "real"
#         }
#     db.create_table("players", player_fields)
#     challenges_fields = {
#                     "word": "text",
#                     "chances": "integer",
#                     "receiver_nickname": "text", PK
#                     "sender_nickname": "text",
#     }
#     db.create_table("challenges", challenges_fields)
#     words_fields = {
#                 "word": "text", PK
#                 "hint": "text",
#                 "domain": "text"
#     }
#     db.create_table("words", words_fields)
