from Classes.enemy import Enemy

class WaveHandler():
    def __init__(self):
        self.currentWave = ["Wave 1", "A", "B", "A", "LEVEL_2"]
        self.name = "Wave 1"
        self.next = "LEVEL_2"
    def nextWave(self, nextWave):
        if nextWave == "end":
            self.name = "THE END"
        else:
            self.currentWave = nextWave
            self.name = nextWave[0]
            self.next = nextWave[len(nextWave)-1]
