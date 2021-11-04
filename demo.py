import random
import sys

from highscore import HighScore

debug = len(sys.argv) > 1 and sys.argv[1] == 'debug'
hs = HighScore("lunarlander", debug=debug)
score = random.randint(0, 100)
rank = hs.add_highscore("Mark", score)
if rank > 0:
    print(f"YEAH! {score} SCORE! Ranking {rank}")
else:
    print(f"Oh no! {score} was not enough for making the highscore!")
