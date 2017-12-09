from FTP import *


class Simulator(FTP):
    """docstring for Simulator."""

    def __init__(self, lowerBound, upperBound):
        super(Simulator, self).__init__(lowerBound, upperBound)

    # Throw an error.
    def start(self):
        if self.config is not None:
            for task in self.config.tasks:
                self.hardSchedule(task)
        else:
            print("Error ! Configuration not set.")
