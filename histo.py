from Configuration import *
from Generator import *
import numpy
import matplotlib.pyplot as plt

histogram=plt.figure()

x = [];
for i in range(0, 10000):
    config = Generator.configuration(3, 70);
    x.append(config.getUtilisation());

bins = numpy.linspace(min(x), max(x), 100);

plt.hist(x, bins, alpha=0.5);
plt.show();
