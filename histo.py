from Configuration import *
from Generator import *
import numpy
import matplotlib.pyplot as plt
import threading


NB_THREADS = 6;
class struct ():

    def __init__(self):
        self.list = [];
        self.minimum = 0;
        self.maximum = 0;
        self.average = 0;

results = [struct() for i in range(NB_THREADS)];
threads = [];

def gen(struct):
    for i in range(0, 1000):
        config = Generator.configuration(6, 70);
        struct.list.append(config.getUtilisation());
    struct.minimum = min(struct.list);
    struct.minimum = max(struct.list);
    struct.minimum = sum(struct.list)/10000;

for i in range(NB_THREADS):
    thread = threading.Thread(name='gen', target=gen, args=[results[i]]);
    thread.start();
    threads.append(thread);

for thread in threads:
    thread.join();
    print("+", end="");
print("");

histogram=plt.figure()

res = [];
for r in results:
    res.extend(r.list);

print(len(res));
bins = numpy.linspace(min(res), max(res), 200);

plt.hist(res, bins, alpha=0.5);
plt.show();
