import fractions

class Configuration:
    """docstring for Configuration."""

    def __init__(self):
        self.tasks = []

    def __str__(self):
        res = ""
        for task in self.tasks:
            res += task.__str__()
        res += "Utilisation : " + str(self.getUtilisation())
        return res

    def lcm(self, value1, value2):
        res = 0
        if(value1 and value2):
            res = abs(value1*value2)/fractions.gcd(value1, value2)
        return int(res)

    def getOMax(self):
        return max([task.offset for task in self.tasks])

    # Actually not really optimal in case of a huge configuration
    def getPMax(self):
        return max([self.lcm(task1.period, task2.period) for task1 in self.tasks for task2 in self.tasks])

    def getUtilisation(self):
        return sum([task.utilisation() for task in self.tasks]) * 100

    def isSynchronous(self):
        return all(self.tasks[0].offset == task.offset for task in self.tasks)

    def add(self, task):
        self.tasks.append(task)

    def feasibilityInterval(self):
        OMax = self.getOMax()
        PMax = self.getPMax()
        return OMax, OMax + (2 * PMax)
