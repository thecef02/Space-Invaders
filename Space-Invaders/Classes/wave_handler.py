

class WaveHandler():
    """ This class parses arrays to interpret which enemies to send in a level

    Attributes:
    self.currentWave : the array used to spawn and display the current wave
    self.name : name of this wave (displayed)
    self.next : name of the next array variable
    """
    def __init__(self):
        """
        constructs The initial array
        Args:
            none
        """
        self.currentWave = ["Wave 1", "A", "B", "A", "LEVEL_2"]
        self.name = "Wave 1"
        self.next = "LEVEL_2"
    def nextWave(self, nextWave):
        """
        shifts to the next wave
        Args:
            next wave (array): the next array to be parsed
        """
        if nextWave == "end":
            self.name = "THE END"
        else:
            self.currentWave = nextWave
            self.name = nextWave[0]
            self.next = nextWave[len(nextWave)-1]
