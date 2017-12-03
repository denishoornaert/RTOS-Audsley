from random import randint
from math import floor, ceil
from Configuration import *
from Task import *


class Generator ():

    """docstring for Generator."""

    taskId = 0;

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
        return Task(offset, period, deadline, wcet, Generator.taskId);

    @staticmethod
    def configuration(tasksNumber, utilisation):
        config = Configuration();
        utilisations = Generator.initUtilisations(tasksNumber, utilisation/100);
        for u in utilisations:
            Generator.taskId += 1;
            config.add(Generator.task(u));
        if(config.isSynchronous()):
            config.tasks[0].offset += 1;
        Generator.taskId = 0;
        return config;
