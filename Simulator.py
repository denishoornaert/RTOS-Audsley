from Task import *
from Configuration import *

class Simulator ():

    """docstring for Simulator."""

    def __init__(self):
        self.timeline = [];
        self.config = None;
        self.initList();

    def __str__(self):
        res = "";
        for elem in self.timeline:
            res += " " if (elem == None) else str(elem.priority);
        return res+"|";

    def initList(self):
        self.timeline = [None for i in range(210)];

    def setConfig(self, config):
        self.config = config;

    def schedule(self, task):
        counter = task.offset;
        cpuUsed = task.wcet;
        jobNb = 0;
        while(counter < 210):
            if(not cpuUsed): # cpuUsed == 0
                jobNb += 1;
                counter = task.offset+(jobNb*task.period);
                cpuUsed = task.wcet;
            else:
                self.timeline[counter] = task;
                counter += 1;
                cpuUsed -= 1;

    # Throw an error.
    def start(self):
        if(self.config != None):
            for task in self.config.tasks:
                self.schedule(task);
        else:
            print("Error ! Configuration not set.");
