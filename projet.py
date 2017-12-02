#!/usr/bin/python
# -*- coding:Utf8 -*-

import sys
from Configuration import *
from Simulator import *
from Audsley import *
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

        if(argv[0] == "interval"):
            config = FileReader.produceConfig(argv[1]);
            print(config.feasibilityInterval());
        elif(argv[0] == "sim"):
            config = FileReader.produceConfig(argv[3]);
            sim = Simulator(int(argv[1]), int(argv[2]));
            sim.setConfig(config);
            sim.start();
            print(sim);
        elif(argv[0] == "audsley"):
            config = FileReader.produceConfig(argv[3]);
            aud = Audsley(int(argv[1]), int(argv[2]));
            aud.setConfig(config);
            aud.start();
            print(aud);
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
