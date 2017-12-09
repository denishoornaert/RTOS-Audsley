class Task:
    """docstring for Task."""

    def __init__(self, offset=0, period=0, deadline=0, wcet=0, priority=0):
        self.offset = offset
        self.period = period
        self.deadline = deadline
        self.wcet = wcet
        self.priority = priority

    def __str__(self):
        t = "Offset : {0}\tPeriod : {1}\tDeadline : {2}\tWCET : {3}\tPriority : {4}\n"
        return t.format(self.offset, self.period, self.deadline, self.wcet, self.priority)

    def utilisation(self):
        return self.wcet / self.period
