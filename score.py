import pickle
import os

class HighScore:
    def __init__(self) -> None:
        self.highscore = 0

    def update(self, score):
        if score > self.highscore: self.highscore = score

    def store(self):
        with open("score.pkl", "wb") as f:
            pickle.dump(self, f)

    def retrieve(filename):
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        else:
            return None