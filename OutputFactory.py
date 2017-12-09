import matplotlib.pylab as plt
import numpy


class OutputFactory:
    """docstring for OutputFactory."""

    @staticmethod
    def toFile(plt, filePath):
        plt.savefig(filePath, bbox_inches='tight')

    @staticmethod
    def toMatrix(simulator):
        res = [[0 for i in range(len(simulator.timeline))] for j in range(len(simulator.config.tasks))]
        for i in range(len(simulator.timeline)):
            elem = simulator.timeline[i]
            if elem is not None:
                res[elem.priority][i] = elem.priority + 1
        res.reverse()
        return numpy.matrix(res)

    @staticmethod
    def generateFigure(matrix):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_aspect('equal')
        plt.yticks(range(0, len(matrix)))
        plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.get_cmap('hot_r'))
        plt.xlabel('Time slots')
        plt.ylabel('Tasks')
        return plt

    @staticmethod
    def produce(simulator, filePath):
        matrix = OutputFactory.toMatrix(simulator)
        fig = OutputFactory.generateFigure(matrix)
        OutputFactory.toFile(fig, filePath)
