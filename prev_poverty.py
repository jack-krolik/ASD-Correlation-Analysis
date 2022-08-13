

"""

Name: Meagan Tsou
Date: 4/10/22

Class: DS2000
File Name: prev_poverty.py
    
Description: A visualization of ASD prevalance as it correlates 
with poverty rate by state

"""

from utils import us_state_to_abbrev, state_party
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import MaxNLocator

POVERTY_NAME = "PovertyRates.csv"
ASD_PREV_NAME = "ASDPrevalences.csv"



def main():
    # Read the Autism Prevalence file
    # Format: Location,Denominator,Prevalence,Lower CI,Upper CI,Year,Source
    asd_data = {}
    with open(ASD_PREV_NAME, 'r') as infile:
        infile.readline()
        for line in infile:
            data = line.split(',')
            if "" in [data[0], data[2], data[5]] or data[0] not in us_state_to_abbrev.values():
                continue
            if data[0] in asd_data:
                asd_data[data[0]].append([float(data[2])/10, int(data[5])])
            else:
                asd_data[data[0]] = [[float(data[2])/10, int(data[5])]]
            
        
    # Read the Poverty Rate file
    # Format: STATE,Total,Below poverty,Standard error,Percent,Standard error
    pov_data = {}
    year = 0
    with open(POVERTY_NAME, 'r') as infile:
        infile.readline()
        infile.readline()
        
        for line in infile:
            
            data = line.split(',')
            if data[0].isnumeric():

                year = int(data[0])
                pov_data[year] = {}
                continue
            elif data[0] not in us_state_to_abbrev.keys():
                continue                
                
            state_name = us_state_to_abbrev[data[0]]
            pov_data[year][state_name] = float(data[-2])
            
    # Make a list of all the data points and label them Democratic or Republican
    data_points = []
    
    for state in asd_data:
        state_data = asd_data[state]
        for data_point in state_data:
            state_prev = data_point[0]
            year = data_point[1]
            # Get the poverty rate based on state and year
            pov_rate = pov_data[year][state]
            label = "Democratic" if state in state_party["Democratic"] else "Republican"
            
            data_points.append([state_prev, year, pov_rate, label])
            
    # Size of marker will be based on poverty rates
    min_pov = 100
    max_pov = 0
    for year in pov_data.keys():
        min_pov = min(min_pov, min(pov_data[year].values()))
        max_pov = max(max_pov, max(pov_data[year].values()))

    # Plot the data
    set_l_label = False
    set_c_label = False
    plt.figure(figsize=(7,5), dpi=100)
    for point in data_points:
        point_i = int((point[2] - min_pov) ** 2)
        
        point_color = 'blue' if point[3] == 'Democratic' else 'red'
        if not set_l_label and point_color == 'blue':
            plt.scatter(point[1], point[0], 
                        color=point_color,
                        s=point_i, alpha=0.3,
                        label=point[3])
            set_l_label = True
        elif not set_c_label and point_color == 'red':
            plt.scatter(point[1], point[0], 
                        color=point_color,
                        s=point_i, alpha=0.3,
                        label=point[3])
            set_c_label = True
        else:
            plt.scatter(point[1], point[0], 
                        color=point_color,
                        s=point_i, alpha=0.3)
    
    # Plot legend for 2020 election voting states
    plt.legend(loc="upper left", title="2020 Election Vote")
    
    # plt.scatter(2000, 3.5,s=min_pov, label="Relative Min % Poverty")
    # plt.scatter(2000, 3,s=max_pov, label="Relative Max % Poverty")
    # plt.scatter([], [], c='k', alpha=0.3, s=min_pov, label=min_pov+'% poverty rate')
    # plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Poverty Rate')
    
    # Plot ticks for x and y axis
    plt.ylim(0, 4.5)
    plt.xticks(range(min(pov_data.keys()) + 1, max(pov_data.keys()) + 1, 2))
    
    # Plot some annotations
    plt.annotate('\________________________/-IA', (2011.5, 0.10), color='black', size=10)
    plt.annotate('CA-', (2016.8, 3.9), color='black', size=10)
    plt.annotate('AL-', (2002.8, 1.90), color='black', size=10)
    plt.annotate('OR-', (2010.8, 3), color='black', size=10)
    plt.annotate('MA-', (2018.8, 3.95), color='black', size=10)
    plt.annotate(' * Markersize = Relative Poverty Rate', 
                 (1999, 3.4), color='black', size=10)

    
    plt.title("State Data of Autism Spectrum Disorder (ASD)")
    plt.xlabel("Year")
    plt.ylabel("Percent of ASD Diagnoses (%)")
    
    plt.show()

main()