import random

from highscore import HighScore


hs = HighScore("lunarlander")
score = random.randint(0, 100)
rank = hs.add_highscore("Mark", score)
if rank > 0:
    print(f"YEAH! {score} SCORE! Ranking {rank}")
else:
    print(f"Oh no! {score} was not enough for making the highscore!")
