class Task ():

    """docstring for Task."""

    def __init__(self):
        self.__init__(0, 0, 0, 0);

    def __init__(self, offset, period, deadline, wcet):
        self.offset = offset;
        self.period = period;
        self.deadline = deadline;
        self.wcet = wcet;

    def __str__(self):
        t = "Offset : {0}\tPeriod : {1}\tDeadline : {2}WCET : \t{3}\n";
        return t.format(self.offset, self.period, self.deadline, self.wcet);
