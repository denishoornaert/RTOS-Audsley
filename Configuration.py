from Task import *

class Configuration ():

    """docstring for Configuration."""

    def __init__(self):
        self.tasks = [];

    def __str__(self):
        res = "";
        for task in self.tasks:
            res += task.__str__();
        res += "Utilisation : "+str(self.getUtilisation());
        return res;

    def getOMax(self):
        return max([task.offset for task in self.tasks]);

    def getPMax(self):
        return max([task.period for task in self.tasks]);

    def getUtilisation(self):
        return sum([task.wcet/task.period for task in self.tasks])*100;

    def add(self, task):
        self.tasks.append(task);

    def feasibilityInterval(self):
        OMax = self.getOMax();
        PMax = self.getPMax();
        return (OMax, OMax+(2*PMax));
