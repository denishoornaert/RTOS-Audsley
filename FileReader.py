from Task import *
from Configuration import *

class FileReader ():

    """docstring for FileReader."""

    @staticmethod
    def openFile(filePath):
        f = open(filePath);
        lines = f.readlines();
        f.close();
        return lines;

    @staticmethod
    def extractData(lines):
        return [(line.strip()).split() for line in lines];

    @staticmethod
    def convertToTasks(data):
        return [Task(int(r[0]), int(r[3]), int(r[2]), int(r[1])) for r in data];

    @staticmethod
    def createConfiguration(tasks):
        config = Configuration();
        for task in tasks:
            config.add(task);
        return config;

    @staticmethod
    def produceConfig(filePath):
        lines = FileReader.openFile(filePath);
        data  = FileReader.extractData(lines);
        tasks = FileReader.convertToTasks(data);
        return  FileReader.createConfiguration(tasks);
