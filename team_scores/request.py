from models.player import Player
from models.team_score import TeamScore
from models.team import Team
import sqlite3
import json

def get_scores(filters):
    with sqlite3.connect("./flagons.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        scores = {}

        if filters is None:
            db_cursor.execute("""
            SELECT
                s.id,
                s.teamId,
                s.score,
                s.timestamp
            FROM TeamScore s
            """)

            dataset = db_cursor.fetchall()

            teams = []
            for row in dataset:
                team = TeamScore(row['id'], row['teamId'], row['score'], row['timestamp'])
                teams.append(team.__dict__)

            return json.dumps(teams)