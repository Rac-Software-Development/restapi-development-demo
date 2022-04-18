import sqlite3

from flask import Flask, send_from_directory, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path="/", static_folder="www")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scores2.db'
db = SQLAlchemy(app)

# moeilijke wijziging in main branch

def result_to_dict(sql_result):
    result_dict = []
    for row in sql_result:
        result_dict.append(({column.name: str(getattr(row, column.name)) for column in row.__table__.columns}))
    return result_dict


class Highscores(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    score = db.Column(db.String(80), nullable=False)
    game = db.Column(db.String(120), nullable=False)


@app.route("/highscores/<game>", methods=["GET", "POST"])
def handle_highscores(game):
    if request.method == "POST":
        body = request.json
        try:
            score = Highscores(name=body["name"], score=body["score"], game=game)
            db.session.add(score)
            db.session.commit()
            result = "ok"
            error = ""
        except Exception as e:
            result = "error"
            error = str(e)
        return jsonify({"result": result, "error": error})
    elif request.method == "GET":
        scores = Highscores.query.filter_by(game=game)
        scores_dict = {"scores": result_to_dict(scores)}
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


db.create_all()
app.run(debug=True, host="0.0.0.0", port=5001)


def joost_function(var1, var2):
    pass

joost_function("1", "2")

mylist = ["1", "2"]
joost_function(mylist)

mydict = {
    "var2": "2",
     "var1": "1",
 }
joost_function(**mydict)