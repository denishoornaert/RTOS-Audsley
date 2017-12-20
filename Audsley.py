from FTP import *


class Audsley(FTP):
    """docstring for Audsley."""

    def __init__(self, lowerBound, upperBound):
        super(Audsley, self).__init__(lowerBound, upperBound)
        self.log = ""

    def __str__(self):
        return self.log

    def softSchedule(self, task):
        return self.schedule(True, task)

    def lpv(self, lowestPriorityTask):
        again = True
        i = 0
        while again and i < len(self.config.tasks):
            task = self.config.tasks[i]
            if not (task is lowestPriorityTask):
                again = self.softSchedule(task)
            i += 1
        return self.hardSchedule(lowestPriorityTask)

    def audsley(self, recursion, tasksSubSet):
        if len(tasksSubSet):
            s = (" " * recursion) + "Task {0} is {1}lowest priority viable"
            lpvTask = None
            for task in tasksSubSet:
                tmpStr = ""
                self.timeline = TimeLine(self.lowerBound, self.upperBound)
                isLpv = self.lpv(task)
                if isLpv:
                    lpvTask = task
                else:
                    tmpStr = "not "
                self.log += s.format(task.priority, tmpStr) + "\n"
            if lpvTask is None:
                self.log = "No priority assignment found"
            else:
                tasksSubSet.remove(lpvTask)
                self.audsley(recursion + 1, tasksSubSet)

    def start(self):
        if self.config is not None:
            self.audsley(0, self.config.tasks)
        else:
            print("Error ! Configuration not set.")
