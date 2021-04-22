from models.player import Player
from models.team_score import TeamScore
from models.team import Team
import sqlite3
import json

def get_players(filters):
    with sqlite3.connect("./flagons.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        players = {}

        if filters is None:
            db_cursor.execute("""
            SELECT
                p.id,
                p.firstName,
                p.lastName,
                p.teamId
            FROM Players p
            """)

            dataset = db_cursor.fetchall()

            players = []
            for row in dataset:
                player = Player(row['id'], row['firstName'], row['lastName'], row['teamId'])
                players.append(player.__dict__)

            return json.dumps(players)