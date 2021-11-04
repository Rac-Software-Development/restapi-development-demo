import requests
from requests_toolbelt.utils import dump


class HighScoreException(Exception):
    pass


class HighScore:
    def __init__(self, game, server_url="http://127.0.0.1:8080", debug=False):
        self.game = game
        self.server_url = server_url
        self.debug = debug

    def add_highscore(self, scorer, score):
        uri = "/highscores/" + self.game
        score = {"name": scorer, "score": int(score)}
        json = self.__handle_request(requests.post, uri, json=score)
        return json["score_rank"]

    def get_highscores(self):
        uri = "/highscores/" + self.game
        json = self.__handle_request(requests.get, uri)
        return json["scores"]

    def __handle_request(self, requests_function, uri, json=None):
        url = self.server_url + uri
        try:
            resp = requests_function(url=url, json=json)
        except requests.exceptions.ConnectionError:
            raise HighScoreException(f"Could not connect to HighScore server at {self.server_url}")
        if self.debug:
            print(dump.dump_all(resp).decode('utf-8'))
        return resp.json()
