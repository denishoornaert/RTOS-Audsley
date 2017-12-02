from Task import *
from Configuration import *

class FTP ():

    """docstring for FTP."""

    def __init__(self, lowerBound, upperBound):
        self.lowerBound = lowerBound;
        self.upperBound = upperBound;
        self.timeline = [];
        self.config = None;
        self.initList();

    def __str__(self):
        out = "";
        res = [" "*self.upperBound for i in range(len(self.config.tasks))];
        for i in range(len(self.timeline)):
            elem = self.timeline[i];
            if(elem != None):
                res[elem.priority] = res[elem.priority][:i]+str(elem.priority)+res[elem.priority][i:];
        res.reverse();
        for line in res:
            out += line+"\n";
        return out;

    def initList(self):
        self.timeline = [None for i in range(self.upperBound)];

    def setConfig(self, config):
        self.config = config;

    def schedule(self, soft, task):
        res = True;
        counter = task.offset;
        cpuUsed = task.wcet;
        jobNb = 0;
        while(res and counter < self.upperBound):
            if(self.timeline[counter] == None):
                if(not cpuUsed): # cpuUsed == 0
                    jobNb += 1;
                    counter = task.offset+(jobNb*task.period);
                    cpuUsed = task.wcet;
                else:
                    if(soft or counter < task.offset+(jobNb*task.period)+task.deadline):
                        self.timeline[counter] = task;
                        counter += 1;
                        cpuUsed -= 1;
                    else:
                        if(soft):
                            s = "{0}: Job T{1}J{2} misses a deadline";
                            print(s.format(counter, task.priority, jobNb));
                        res = False;
            else:
                counter += 1;
        return res;

    def hardSchedule(self, task):
        return self.schedule(False, task);
