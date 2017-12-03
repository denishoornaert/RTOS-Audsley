#!/usr/bin/python
# -*- coding:Utf8 -*-

import sys
from Configuration import *
from Simulator import *
from Audsley import *
from FileController import *
from OutputFactory import *
from Generator import *


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
            config = FileController.produceConfig(argv[1]);
            print(config.feasibilityInterval());
        elif(argv[0] == "sim"):
            config = FileController.produceConfig(argv[3]);
            sim = Simulator(int(argv[1]), int(argv[2]));
            sim.setConfig(config);
            sim.start();
            print(sim);
            OutputFactory.produce(sim, "schedule1.png");
        elif(argv[0] == "audsley"):
            config = FileController.produceConfig(argv[3]);
            aud = Audsley(int(argv[1]), int(argv[2]));
            aud.setConfig(config);
            aud.start();
            print(aud);
        elif(argv[0] == "gen"):
            # Generation of the system
            config = Generator.configuration(int(argv[1]), int(argv[2]));
            # Determine feasibility interval (used by Audsley algorithm)
            interval = config.feasibilityInterval();
            # Find the priority and thus the order to which write the task in the file
            aud = Audsley(interval[0], interval[1]);
            aud.setConfig(config);
            aud.start();
            print(aud)
            print(config)
            FileController.writeConfig(config, argv[3]);
        else:
            raise AttributeError("Unknow argument: " + str(argv[0]))

        # ONLY FOR TEST [DEBUG]
        if(debug):
            print(config);
            print(argv)



if __name__ == '__main__':
    Main(sys.argv)
