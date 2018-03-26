# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 13:20:05 2016

@author: aanas / anasLearn / Anas Aamoum
"""

from ps2 import *
import pylab




#Visualize some simulations:
    
#runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type, visualizeSimulation = False)
#runSimulation(3, 1.0, 15, 15, 1, 1, StandardRobot, True)
#runSimulation(2, 1.0, 15, 15, 1, 1, RandomWalkRobot, True)
#
#runSimulation(10, 1.0, 15, 15, 0.7, 1, StandardRobot, True)
#runSimulation(10, 1.0, 15, 15, 0.7, 1, RandomWalkRobot, True)



#Show Plots
showPlot1("Time It Takes 1 - 10 Robots To Clean 80% Of A Room", "number of robots", 
"time steps")


showPlot2("Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms", "aspect ratio", 
"time steps")


