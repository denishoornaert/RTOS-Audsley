from random import randint
from math import floor, ceil
from Configuration import *
from Task import *


class Generator ():

    """docstring for Generator."""

    @staticmethod
    def initUtilisations(tasksNumber, totalUtilisation):
        utilisations = [randint(10, 100) for i in range(tasksNumber)];
        factor = sum(utilisations)/totalUtilisation;
        utilisations = [round(utilisation/factor,2) for utilisation in utilisations];
        return utilisations;

    @staticmethod
    def task(utilisation):
        # wcet of '1' at least otherwise the task is useless
        wcet     = randint(1, 10);
        period   = ceil(wcet/utilisation);
        deadline = randint(wcet, period);
        offset   = randint(0, 30);
        return Task(offset, period, deadline, wcet, None);

    @staticmethod
    def configuration(tasksNumber, utilisation):
        config = Configuration();
        utilisations = Generator.initUtilisations(tasksNumber, utilisation/100);
        for u in utilisations:
            task = Generator.task(u);
            config.add(task);
        if(config.isSynchronous()):
            print("sync");
        else:
            print("async");
        return config;
