class TimeLine():
    """docstring for FTP."""

    def __init__(self, lowerBound, upperBound):
        self.history = dict()
        self.timeline = [None for _ in range(upperBound+1)] # '+1' includes the upper bound in the simulation output
        self.lowerBound = lowerBound
        self.upperBound = upperBound

    def __getitem__(self, index):
        return self.timeline[index]

    def __setitem__(self, index, value):
        self.timeline[index] = value

    def __len__(self):
        return len(self.timeline)

    def __str__(self):
        output = ""
        startTaskExec = None
        taskExec = None
        for time in range(self.lowerBound, self.upperBound+1): # '+1' includes the upper bound in the simulation output
            output += self.retrieveEvents(time)
            if taskExec != self.timeline[time]:
                if taskExec != None:
                    output += "{0}-{1}: T{2}J{3}\n".format(startTaskExec, time, taskExec[0]+1, taskExec[1]+1)
                startTaskExec = time
                taskExec = self.timeline[time]
        return output

    def retrieveEvents(self, time):
        output = ""
        events = self.history.get(time)
        if events != None:
            for event in events:
                output += event
        return output

    def addEvent(self, time, eventType, task, jobNb):
        s = ("{0}: {1} of job T{2}J{3}\n").format(time, eventType, task.priority+1, jobNb+1)
        self.history.setdefault(time, []);
        events = self.history.get(time)
        events.append(s)

    def addArrival(self, time, task, jobNb):
        self.addEvent(time, "Arrival", task, jobNb)

    def addDeadline(self, time, task, jobNb):
        self.addEvent(time, "Deadline", task, jobNb)

    def addDeadlineMiss(self, time, task, jobNb):
        s = ("{0}: job T{1}J{2} misses a deadline\n").format(time, task.priority+1, jobNb+1)
        self.history.setdefault(time, []);
        events = self.history.get(time)
        events.append(s)
        self.upperBound = time

    def applyTask(self, task):
        time = task.offset
        jobNb = 0
        while time < self.upperBound:
            self.addArrival(time, task, jobNb)
            deadline = time+task.period
            self.addDeadline(deadline, task, jobNb)
            jobNb += 1
            time += task.period
