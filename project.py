#!/usr/bin/python
# -*- coding:Utf8 -*-

import sys

from Audsley import *
from FileController import *
from Generator import *
from OutputFactory import *
from Simulator import *


class Main:
    def __init__(self, argv):

        # Set debug mode
        debug = False

        # Remove program name
        if len(argv) > 2:
            argv = argv[1:]
        else:
            raise AttributeError("Missing argument")

        if argv[0] == "interval":
            config = FileController.produceConfig(argv[1])
            fi = config.feasibilityInterval()
            print("{0},{1}".format(fi[0], fi[1]))
        elif argv[0] == "sim":
            config = FileController.produceConfig(argv[3])
            sim = Simulator(int(argv[1]), int(argv[2]))
            sim.setConfig(config)
            sim.start()
            print(sim)
            if len(argv) == 5:
                OutputFactory.produce(sim, argv[4])
        elif argv[0] == "audsley":
            config = FileController.produceConfig(argv[3])
            aud = Audsley(int(argv[1]), int(argv[2]))
            aud.setConfig(config)
            aud.start()
            print(aud)
        elif argv[0] == "gen":
            config = Generator.configuration(int(argv[1]), int(argv[2]))
            FileController.writeConfig(config, argv[3])
        else:
            raise AttributeError("Unknow argument: " + str(argv[0]))

        # ONLY FOR TEST [DEBUG]
        if debug:
            print(config)
            print(argv)


if __name__ == '__main__':
    Main(sys.argv)
