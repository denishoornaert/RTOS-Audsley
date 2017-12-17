from Configuration import *
from Task import *


class FileController:
    """docstring for FileController."""

    @staticmethod
    def openFile(filePath):
        f = open(filePath)
        lines = f.readlines()
        f.close()
        return lines

    @staticmethod
    def extractData(lines):
        return [(line.strip()).split() for line in lines]

    @staticmethod
    def convertToTasks(data):
        res = []
        for i in range(len(data)):
            r = data[i]
            res.append(Task(int(r[0]), int(r[1]), int(r[2]), int(r[3]), i))
        return res

    @staticmethod
    def createConfiguration(tasks):
        config = Configuration()
        for task in tasks:
            config.add(task)
        return config

    @staticmethod
    def produceConfig(filePath):
        lines = FileController.openFile(filePath)
        data = FileController.extractData(lines)
        tasks = FileController.convertToTasks(data)
        return FileController.createConfiguration(tasks)

    @staticmethod
    def writeFile(filePath, data):
        f = open(filePath, "w")
        f.write(data)
        f.close()

    @staticmethod
    def taskToString(task):
        s = "{0} {1} {2} {3}"
        return s.format(task.offset, task.period, task.deadline, task.wcet)

    @staticmethod
    def configToString(config):
        res = ""
        for task in config.tasks:
            res += FileController.taskToString(task)
            res += "\n"
        return res

    @staticmethod
    def writeConfig(config, filePath):
        data = FileController.configToString(config)
        FileController.writeFile(filePath, data)
