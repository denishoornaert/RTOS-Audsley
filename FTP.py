from TimeLine import *

class FTP:
    """docstring for FTP."""

    def __init__(self, lowerBound, upperBound):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.timeline = TimeLine(lowerBound, upperBound)
        self.config = None

    def __str__(self):
        out = "Schedule from: {0} to: {1}; {2} tasks\n"
        out = out.format(self.lowerBound, self.upperBound, len(self.config.tasks))
        out += self.timeline.__str__();
        return out

    def setConfig(self, config):
        self.config = config
        for task in self.config.tasks:
            self.timeline.applyTask(task)

    def schedule(self, soft, task):
        res = True
        counter = task.offset
        cpuUsed = task.wcet
        jobNb = 0
        while res and counter < self.upperBound:
            if self.timeline[counter] is None:
                if not cpuUsed:  # cpuUsed == 0
                    jobNb += 1
                    counter = task.offset + (jobNb * task.period)
                    cpuUsed = task.wcet
                else:
                    if soft or (counter < task.offset + (jobNb * task.period) + task.deadline):
                        self.timeline[counter] = (task.priority, jobNb)
                        counter += 1
                        cpuUsed -= 1
                    else:
                        if soft:
                            self.timeline.addDeadlineMiss(counter, task, jobNb);
                        res = False
            else:
                counter += 1
        return res

    def hardSchedule(self, task):
        return self.schedule(False, task)
