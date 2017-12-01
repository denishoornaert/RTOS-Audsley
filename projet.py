#!/usr/bin/python
# -*- coding:Utf8 -*-

import sys
from Configuration import *
from Simulator import *
from FileReader import *


class Main:

    def __init__(self, argv):

        # Set debug mode
        debug = False;

        # Remove program name
        if(len(argv) > 2):
            argv = argv[1:]
        else:
            raise AttributeError("Missing argument")

        config = FileReader.produceConfig(argv[1]);

        if(argv[0] == "interval"):
            print(config.feasibilityInterval());
        elif(argv[0] == "sim"):
            sim = Simulator();
            sim.setConfig(config);
            sim.start();
            print(sim);
        elif(argv[0] == "audsley"):
            pass
        elif(argv[0] == "gen"):
            pass
        else:
            raise AttributeError("Unknow argument: " + str(argv[0]))

        # ONLY FOR TEST [DEBUG]
        if(debug):
            print(config);
            print(argv)



if __name__ == '__main__':
    Main(sys.argv)
