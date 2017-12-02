import numpy
import toyplot
import toyplot.png

class OutputFactory ():

    """docstring for OutputFactory."""

    @staticmethod
    def toFile(canvas, filePath):
        toyplot.png.render(canvas, filePath)

    @staticmethod
    def toMatrix(simulator):
        res = [[0 for i in range(len(simulator.timeline))] for j in range(len(simulator.config.tasks))];
        for i in range(len(simulator.timeline)):
            elem = simulator.timeline[i];
            if(elem != None):
                res[elem.priority][i] = elem.priority+1;
        res.reverse();
        return res;

    @staticmethod
    def setColors(matrix):
        canvas, mark = toyplot.matrix(matrix, label="Scheduling", tlabel="Time slots",  llabel="Tasks");
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]):
                    mark.body.cell[i, j].style = {"fill":"black"};
                else:
                    mark.body.cell[i, j].style = {"fill":"white"};
        return canvas, mark;

    @staticmethod
    def produce(simulator, filePath):
        matrix = OutputFactory.toMatrix(simulator);
        canvas, mark = OutputFactory.setColors(matrix);
        OutputFactory.toFile(canvas, filePath);
