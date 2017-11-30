#!/usr/bin/python
# -*- coding:Utf8 -*-

import sys

class Task:

    def __init__(self, offset, period, deadline, wcet):
        self._offset = offset
        self._period = period
        self._deadline = deadline
        self._wcet = wcet

    def __str__(self):
        return "Offset: " + str(self._offset) + " - Period: " + str(self._period) + \
                " - Deadline: " + str(self._deadline) + " - WCET: " + str(self._wcet)


class Main:

    def __init__(self, argv):

        # Remove program name
        if(len(argv) > 2):
            argv = argv[1:]
        else:
            raise AttributeError("Missing argument")

        if(argv[0] == "interval"):
            pass
        elif(argv[0] == "sim"):
            pass
        elif(argv[0] == "audsley"):
            pass
        elif(argv[0] == "gen"):
            pass
        else:
            raise AttributeError("Unknow argument: " + str(argv[0]))

        # ONLY FOR TEST [DEBUG]
        taskList = self.readTaskFile(argv[1])
        for task in taskList:
            print(task)

        print(argv)
    

    def readTaskFile(self, fileName):
        """
            Read the Task File and create a python list of Task

            :param fileName name of the file
            :return list of Task
        """
        listOfTask = []

        with open(fileName, "r") as f:
            lineIndex = 0
            for line in f:
                strTask = line.strip()
                splitTask = strTask.split()
                if(len(splitTask) != 4):
                    print("Error in line " + str(lineIndex))
                else:
                    listOfTask.append(Task(splitTask[0], splitTask[1], splitTask[2], splitTask[3]))

                lineIndex += 1

        f.close()
        return listOfTask



if __name__ == '__main__':
    Main(sys.argv)
