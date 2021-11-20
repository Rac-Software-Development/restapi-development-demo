# highscorer
A python server and client for a simple RESTful API implementation. This is demonstration code, not meant for general usage. 

This RESTful server app has a few components to play with: 
- A REST [server](highscorer_awecwe.py) that registers high scores for a given game name. 
- A simple [client module](highscore.py) that contacts this server and can be imported in other classes. 
- A [demo program](demo.py) importing the client and showing how to use it
- A [demo web page](www/highscore.html) with a fancy star field showing a continually updated list of highscores 

Note that you should start the server before trying to run the demo. 

# Highscore server

## Installing
To start the server, first make sure the requirements are installed: 
```
pip install -r requirements.txt
```
..then start the server
```
python highscore_server.py
```
(and leave the window open)

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