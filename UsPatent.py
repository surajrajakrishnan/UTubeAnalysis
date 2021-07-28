# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:12:47 2019

@author: NDH00360
"""

import pypatent
import pandas as pd

import time

Safety=['Airbag','ABS','Night Vision','ADAS','Brakes','NightVision','Tyre','SafetySystem','Lane Change Warning']
Infotianment=['UX','TouchScreen','Holographics','SmartPhone','CarPlay','Andriod Auto','Car Audio','VoiceControl']
Performance=['Torque','Battery Pack','Engine','Four Wheel Drive','motors']
Design=['Spoilers','Paint','Grille','MatteFinish','Trim Design','Alloy Wheels','Car Seat','Welcoming Lights']
Comfort=['Steering Mount Control','Cruise Control','Camera','KeyLess Entry','Climate Control','In-Car Payment']

competitors=['Lexus','Audi','Tesla','BMW','ACURA','Mercedes']
dfCompList=['Audi']
#Test=Safety
#dataframecompetitors=pd.DataFrame()



for word in dfCompList:
    try:
        dfComp=pd.DataFrame()
        print (word)
        dfComp=pypatent.Search('ttl/LIDAR and ttl/vehicle',results_limit=10).as_dataframe()
        time.sleep(1)
        if(len(dfComp) !=0):
            dfComp.to_csv(r"C:\Users\NDH00360\Desktop\Normalization\{}".format(word)+".csv") 
    except:
        print ("e")
        
        
#dfComp.to_csv(r'C:\Users\NDH00360\Desktop\Normalization\dfCompCarPlay.csv')  
