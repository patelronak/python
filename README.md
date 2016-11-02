# Rest API for PS3 Metacritic Game and Score Reported

This application will parse the Top Playstation 3 Games (By Metascore) on Metacritic’s PS3 page: http://www.metacritic.com/game/playstation-3 and return an array of JSON elements which contain title and metascore as output.

Following endpoints are exposed

/games
Returns all the games on the page as array of json with title and metascore.

/games/TITLE_OF_GAME
Returns specific game on the page as array of json with title and metascore.

First step is to run the server.
# HTTP API Server
Run the Server
```
./server.py
```

Run a query against the server

```
curl http://127.0.0.1:5000/games/
```

```
curl http://127.0.0.1:5000/games/The%20Awakened%20Fate:%20Ultimatum
```

# Example Ouput
```
[
  {
    "title": "XCOM: Enemy Within",
    “score”: 88
   },
  {
    "title": "Assasin’s Creed IV: Black Flag",
    “score”: 88
  }
]
```
