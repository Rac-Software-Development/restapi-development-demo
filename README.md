# highscorer
A python server and client for a simple RESTful API implementation. This is demonstration code, not meant for general usage. 

This RESTful server app has a few components to play with: 
- A REST [server] in multiple implementations that registers high scores for a given game name. 
- A simple [client module](highscore.py) that contacts this server and can be imported in other classes. 
- A [demo program](demo.py) importing the client and showing how to use it
- A [demo web page](www/highscore.html) with a fancy star field showing a continually updated list of highscores 
- A [ReactJS based client](react_client)
- An incomplete [Ionic based client](react_ionic_client)
Note that you should start the server before trying to run the demos. 

# Highscore server
The highscore server comes in three flavors:
- highscorer_server_on_json_storages.py uses a json file as database medium, including some caching. 
- highscore_server_barebones_on_db.py is a basic SQLite with SQL based implementation
- highscore_server_barebones_on_sqlalch.py is a SQLAlchemy using SQLite implementation

## Installing
To start the server, first make sure the requirements are installed: 
```
pip install -r requirements.txt
```
..then start for example the SQL based server:
```
python highscore_server_barebones_on_db.py
```
(and leave the process running!)

By default we listen on **all interfaces** (ie. 0.0.0.0) and **port 8080**. To start with a different port or a specific listener IP, add these to the start command as following:
```
python highscore_server.py 127.0.0.1:5000
```

## Usage
The highscore server takes highscores based on a game name using a REST API approach. Scores are saved in a local file called "highscore.json". The following URLs are available:

| URI | HTTP Verb | Description | 
| --- | --- | --- | 
| /highscores | GET | Lists all games known to the highscore server | 
| /highscores/\<gamename\> | GET | Given a \<gamename\>, retrieve the highscores known for that game. | 
| /highscores/\<gamename\> | POST | Expects a \<gamename\> and a body containing a dictionary with a name and a score, Only the top 10 scores are retained. Return a ranking if the score is in the top 10 (and a list of scores) or a 0 if your score did not make the top 10. | 

The body for the POST / save score method should resemble the following structure:
```json
{
    "name": "Mark",
    "score": 99
}
```
There's also a [Postman](https://www.postman.com/) file ([postman_collection.json](postman_collection.json)) you can use to test your server from Postman, just import it and modify the URL where required.

# Highscore client module
This is a simple client class you can put in your code to save high scores. This contacts the high score server so make sure it is running. If not, the code will throw a HighScoreException explaining it could not reach the server. 

A very simple example: 
```python
from highscore import HighScore

hs = HighScore("lunarlander")

# Prints the rank your score reached, or 0 if it was outside of the top 10
print(hs.add_highscore("Mark", 10))

# Gets the top 10 scores 
print(hs.get_highscores())
```

In case your highscore server is listening on another address, add it to the create like so:
```python
from highscore import HighScore

hs = HighScore("lunarlander", server_url="http://127.0.0.1:8080", debug=True)
```
This also shows the debug function which will print your request and response after sending. 

# Demo.py
This very small program rolls a random score, then sends it to the highscore server using the highscore module. Run it with an extra parameter of "debug" to print the request and response send. 
```
c:\python demo.py debug
< POST /highscores/lunarlander HTTP/1.1
< Host: 127.0.0.1:8080
< User-Agent: python-requests/2.26.0
< Accept-Encoding: gzip, deflate
< Accept: */*
< Connection: keep-alive
< Content-Length: 28
< Content-Type: application/json
< 
< {"name": "Mark", "score": 8}
> HTTP/1.0 200 OK
> Content-Type: application/json
> Content-Length: 118
> Server: Werkzeug/2.0.2 Python/3.8.3
> Date: Thu, 04 Nov 2021 20:47:18 GMT
> 
{
    "scores": [
        {
            "name": "Mark",
            "score": 8
        }
    ],
    "score_rank": 1
}

YEAH! 8 SCORE! Ranking 1
```

# Demo web page
The demo page is a fancy scrolling star field (https://github.com/jakesgordon/javascript-starfield/) with a list of highscores. There are 2 variants:
- A Jquery based approach 
- An ES2017-ES2020 pure javascript variant

You can run this page from your web browser directly, no need for a webserver.

# ReactJS Based Client
This client is similar to the other clients in the www directory, but requires you to complete the setup and run it using NPM (Node Package Manager). If "npm" is not on your system, download and install the Node.js eocsystem from [here](https://nodejs.org/en/download/)

You will need to install all of the required libraries in the ReactJS directory, which will take quite some space. From the react_client directory, do: 
```
npm install 
npm start
```
This will start a development server you can use to view the result. 

# React on Ionic based mobile client
Similar to the ReactJS example, this client requires Node.js to be installed.

To install the required Ionic libraries:
```
npm install -g @ionic/cli
```

Next, start this client as following:
```
ionic start
```

To set up the deployment for the Android emulator on Android Developer Studio, consult the [documentation](https://ionicframework.com/docs/angular/your-first-app/deploying-mobile)