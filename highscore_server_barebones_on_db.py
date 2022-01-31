import sqlite3

from flask import Flask, send_from_directory, jsonify, request, render_template

app = Flask(__name__, static_url_path="/", static_folder="www")

class HighScores:
    def __init__(self, database_file_name):
        self.database_file_name = database_file_name
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.database_file_name)
        cur = conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS highscores " \
              "(name TEXT NOT NULL, score TEXT NOT NULL, game TEXT NOT NULL)"
        cur.execute(sql)
        conn.commit()

    def get(self, game):
        conn = sqlite3.connect(self.database_file_name)
        cur = conn.cursor()
        sql = "SELECT * FROM highscores where game = ? " \
              "ORDER BY score DESC LIMIT 10"
        result = cur.execute(sql, [game])
        scores = []
        for score in result:
            scores.append({"name": score[0], "score": score[1]})
        return scores

    def insert_score(self, name, score, game):
        conn = sqlite3.connect(self.database_file_name)
        cur = conn.cursor()
        sql = "INSERT INTO highscores VALUES (?, ?, ?)"
        cur.execute(sql, [name, score, game])
        conn.commit()


@app.route("/highscores/<game>", methods=["GET", "POST"])
def handle_highscores(game):
    if request.method == "POST":
        body = request.json
        try:
            highscores.insert_score(body["name"], body["score"], game)
            result = "ok"
            error = ""
        except HighScores as e:
            highscores.error_message()
            result = "error"
            error = f"Missing required field ({e})"
        except Exception as e:
            result = "error"
            error = str(e)
        return jsonify({"result": result, "error": error})
    elif request.method == "GET":
        scores = highscores.get(game)
        scores_dict = {"scores": scores}
        return jsonify(scores_dict)


@app.route("/")
def hello_from_the_other_side():
    return send_from_directory("www", "highscore_jquery.html")

@app.route("/jinja/<game>")
def hello_from_jinja(game):
    params = {
        "name": game
    }
    return render_template("highscore_jquery.j2", **params)


highscores = HighScores("scores.db")
app.run(debug=True, host="127.0.0.1", port=5001)
