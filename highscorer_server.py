import json
import sys

from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


"""
    Highscore data looks like:
    {
        "gamename":[
            {"name: "scorer", "score": scoreint},
            {"name: "scorer", "score": scoreint},
            {"name: "scorer", "score": scoreint},
        ]
    }
"""
class HighScoreResource(Resource):
    FILENAME = "highscores.json"
    MAX_SCORES_PER_GAME = 10

    def __init__(self):
        self.data = None

    def _get_data(self):
        if not self.data:
            try:
                with open(HighScoreResource.FILENAME, "r") as jsonfile:
                    self.data = json.load(jsonfile)
            except FileNotFoundError:
                self.data = {}
        return self.data

    def _write_data(self, json_dict):
        with open(HighScoreResource.FILENAME, 'w') as jsonfile:
            json.dump(json_dict, jsonfile)
        self.data = json_dict


class GamesList(HighScoreResource):
    def get(self):
        if keys := self._get_data().keys():
            return list(keys)
        return []


class HighScores(HighScoreResource):
    def get(self, game):
        scores = self._get_data().get(game, {})
        return {"scores": scores}

    def post(self, game):
        # Validate input
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help="Name of the player that scored")
        parser.add_argument('score', type=int, help="Score put down by this player")
        params = parser.parse_args()

        # Add game if it was new
        highscores = self._get_data()
        if game not in highscores:
            highscores[game] = []

        # Add the new high score
        scores = highscores[game]
        new_score = {"name": params["name"], "score": params["score"]}
        scores.append(new_score)

        # Sort the score and cut off at the max
        scores.sort(key=lambda x: x["score"], reverse=True)
        highscores[game] = scores[:HighScoreResource.MAX_SCORES_PER_GAME]

        # Write the new data
        self._write_data(highscores)

        # See if this score made the list!
        response = {"scores": scores, "score_rank": 0}
        try:
            response["score_rank"] = highscores[game].index(new_score) + 1
        except ValueError:
            pass

        # Return the current list of high scores
        return response


api.add_resource(GamesList, '/highscores')
api.add_resource(HighScores, '/highscores/<game>')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = sys.argv[1].split(":")
        host = args[0]
        port = int(args[1])
    else:
        host = "0.0.0.0"
        port = 8080
    app.run(debug=True, host=host, port=port)
