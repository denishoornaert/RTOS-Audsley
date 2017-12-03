from random import randint
from Configuration import *
from Task import *

OFFSET_UPPERBOUND = 20;
PERIOD_UPPERBOUND = 20;

class Generator ():

    """docstring for Generator."""

    @staticmethod
    def task(remainingUtilisation, remainingTasks, utilisationLowerBound=1, offsetLowerBound=0):
        # wcet of '1' at least otherwise the task is useless
        wcet     = randint(utilisationLowerBound, (remainingUtilisation//remainingTasks));
        period   = randint(wcet, PERIOD_UPPERBOUND);
        deadline = randint(wcet, period);
        offset   = randint(offsetLowerBound, OFFSET_UPPERBOUND);
        return Task(offset, period, deadline, wcet, None);

    @staticmethod
    def configuration(tasksNumber, utilisation):
        config = Configuration();
        for i in range(0, tasksNumber-1):
            task = Generator.task(utilisation, tasksNumber);
            utilisation -= task.wcet;
            config.add(task);
        # the '1' ensure that even if the other tasks have been assigned an
        # offset of '0', the system is well asynchrnous.
        task = Generator.task(utilisation, 1, utilisation, 1);
        config.add(task);
        return config;
