class Task ():

    """docstring for Task."""

    def __init__(self):
        self.__init__(0, 0, 0, 0, 0);

    def __init__(self, offset, period, deadline, wcet, priority):
        self.offset = offset;
        self.period = period;
        self.deadline = deadline;
        self.wcet = wcet;
        self.priority = priority;

    def __str__(self):
        t = "Offset : {0}\tPeriod : {1}\tDeadline : {2}\tWCET : {3}\tPriority : {4}\n";
        return t.format(self.offset, self.period, self.deadline, self.wcet, self.priority);
