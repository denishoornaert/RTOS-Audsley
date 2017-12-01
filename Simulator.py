from Task import *
from Configuration import *

EDGE = 30 # TODO replace 'EDGE' by OMax+(2xPMax)

class Simulator ():

    """docstring for Simulator."""

    def __init__(self):
        self.timeline = [];
        self.config = None;
        self.initList();

    def __str__(self):
        out = "";
        res = [" "*EDGE for i in range(len(self.config.tasks))];
        for i in range(len(self.timeline)):
            elem = self.timeline[i];
            if(elem != None):
                res[elem.priority] = res[elem.priority][:i]+str(elem.priority)+res[elem.priority][i:];
        res.reverse();
        for line in res:
            out += line+"\n";
        return out;

    def initList(self):
        self.timeline = [None for i in range(EDGE)];

    def setConfig(self, config):
        self.config = config;

    def schedule(self, task):
        counter = task.offset;
        cpuUsed = task.wcet;
        jobNb = 0;
        while(counter < EDGE):
            if(self.timeline[counter] == None):
                if(not cpuUsed): # cpuUsed == 0
                    jobNb += 1;
                    counter = task.offset+(jobNb*task.period);
                    cpuUsed = task.wcet;
                else:
                    self.timeline[counter] = task;
                    counter += 1;
                    cpuUsed -= 1;
            else:
                counter += 1;

    # Throw an error.
    def start(self):
        if(self.config != None):
            for task in self.config.tasks:
                self.schedule(task);
        else:
            print("Error ! Configuration not set.");
