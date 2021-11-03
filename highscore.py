import requests


class HighSCoreException(Exception):
    pass


def requester(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            raise HighSCoreException(f"Could not connect to HighScore server")
    return inner_function


class HighScore:
    def __init__(self, game, server_url="http://127.0.0.1:5000"):
        self.game = game
        self.server_url = server_url

    @requester
    def add_highscore(self, scorer, score):
        url = self.server_url + "/highscores/" + self.game
        score = {"name": scorer, "score": int(score)}
        resp = requests.post(url=url, json=score)
        json = resp.json()
        return json["score_rank"]

    @requester
    def get_highscores(self):
        url = self.server_url + "/highscores/" + self.game
        resp = requests.get(url=url)
        json = resp.json()
        return json["scores"]
