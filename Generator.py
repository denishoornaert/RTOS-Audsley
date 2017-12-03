from random import uniform
from math import floor
from Configuration import *
from Task import *


class Generator ():

    """docstring for Generator."""

    @staticmethod
    def initUtilisations(tasksNumber, totalUtilisation):
        utilisations = [uniform(1, 100)/100 for i in range(tasksNumber)];
        factor = sum(utilisations)/totalUtilisation;
        utilisations = [utilisation/factor for utilisation in utilisations];
        return utilisations;

    @staticmethod
    def task(utilisation):
        # wcet of '1' at least otherwise the task is useless
        wcet     = uniform(1, 10);
        period   = floor(wcet/utilisation);
        deadline = uniform(wcet, period);
        offset   = uniform(0, 30);
        return Task(offset, period, deadline, wcet, None);

    @staticmethod
    def configuration(tasksNumber, utilisation):
        config = Configuration();
        utilisations = Generator.initUtilisations(tasksNumber, utilisation/100);
        for u in utilisations:
            task = Generator.task(u);
            config.add(task);
        if(config.isSynchronous()):
            pass;
        return config;
