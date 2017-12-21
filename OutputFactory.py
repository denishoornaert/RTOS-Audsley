import numpy


class OutputFactory:
    """docstring for OutputFactory."""

    @staticmethod
    def toMatrix(simulator):
        res = [[0 for _ in range(len(simulator.timeline))] for _ in range(len(simulator.config.tasks))]
        for i in range(len(simulator.timeline)):
            elem = simulator.timeline[i]
            if elem is not None:
                res[elem[0]][i] = elem[0] + 1
        res.reverse()
        return numpy.matrix(res)

    # There is an import in this method because otherwise the import is every
    # time executed but it is not garanteed that the module 'matplotlib' is installed.
    @staticmethod
    def generateFigure(matrix, filePath):
        import matplotlib.pylab as plt
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.set_aspect('equal')
        plt.yticks(range(0, len(matrix)))
        plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.get_cmap('hot_r'))
        plt.xlabel('Time slots')
        plt.ylabel('Tasks')
        plt.savefig(filePath, bbox_inches='tight')

    @staticmethod
    def produce(simulator, filePath):
        matrix = OutputFactory.toMatrix(simulator)
        OutputFactory.generateFigure(matrix, filePath)
