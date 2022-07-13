#=========================================================================
'''
Racial diversity in ASD research and State Partisanship
Melissa Rejuan
'''
#=========================================================================
    
"""
Purpose: How well is race/ethnicity  diversity being represented in
autism research by research institution in conservative vs. 
liberal voting states?   
"""
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import math


DATA = 'diversity.csv'

LEFT_LEANING = ['California', 'Colorado', 'Connecticut',
                'Delaware', 'District of Columbia', 'Hawaii',
                'Illinois', 'Maryland', 'Massachusetts', 
                'Nevada', 'New Jersey', 'New York',
                'Oregon', 'Rhode Island', 'Vermont', 
                'Washington', 'New Mexico']
                
RIGHT_LEANING = ['Alabama', 'Alaska', 'Arizona',
                'Arkansas', 'Florida', 'Georgia',
                'Idaho', 'Indiana', 'Iowa', 'Kansas',
                'Kentucky', 'Louisiana', 'Maine',
                'Michigan', 'Minnesota', 'Mississippi',
                'Missouri', 'Montana', 'Nebraska',
                'New Hampshire', 'North Carolina', 
                'North Dakota', 'Ohio', 'Oklahoma',
                'Pennsylvania', 'South Carolina', 
                'South Dakota', 'Tennessee', 'Texas',
                'Utah', 'Virginia', 'West Virginia',
                'Wisconsin', 'Wyoming']


RACES = ['White', 'Hispanic', 'Black', 'Asian', 'Native Hawaiian/Other Pacific Islander',
'American Indian/Alaska Native','Other', 'Bi - or multiracial', 'Unknown']

RESEARCH_STATES = ['Massachusetts', 'Georgia', 'Connecticut', 'Pennsylvania',
                    'Colorado', 'California', 'Wisconsin', 'Florida', 'New York',
                    'North Carolina', 'Illinois', 'Ohio', 'Missouri',
                    'Texas', 'Michigan', 'Washington', 'Tennessee']

 
def find_pct(race, total_size):
    percent = (race / total_size) * 100
    return int(percent) 


def main():
    
    ###################### LOAD SHAPEFILE & PLOT MAP #########################
    
    states = gpd.read_file('cb_2014_us_state_20m.shp')
    states.head()
    states = states.to_crs("EPSG:3395")
    # print(states.crs)
    states = states[states['NAME'] != 'Puerto Rico']
    states = states[states['NAME'] != 'Alaska']
    states = states[states['NAME'] != 'Hawaii']
    ax2 = states.plot(edgecolor=u'gray', cmap = 'Pastel1', figsize = (8, 8), legend = True)       
    plt.title("Map of USA - Left Wing Leaning (Blue) and Right Wing Leaning (Red) States")

       
   ############# ASSIGN CONSERVATIVE AND LIBERAL STATES COLORS ###############
    
    # blue = left leaning, red = right leaning
    
    left_leaning = states[states['NAME'].isin(LEFT_LEANING)]
    
    right_leaning = states[states['NAME'].isin(RIGHT_LEANING)]
    
    
    # fig, ax = plt.subplots(1,1)
    
    left_leaning.plot(color='blue', ax = ax2, edgecolor=u'gray', legend = True)
    right_leaning.plot(color='red', ax = ax2, edgecolor=u'gray', legend = True)
    ax2.legend()
    
    # label each state
    states.apply(lambda x: ax2.annotate(s=x.STUSPS, xy=x.geometry.centroid.coords[0],
                                       ha='center', fontsize=8),axis=1)
    
   
    ############################# PIE CHARTS #################################

    # read diversity.csv file
    df = pd.read_csv(DATA, sep = ",")
    
    # look at what the columns are
    # print(df.columns)
    
    # Keep columns for map 
    col_df = df[['Location (State)', 'Sample Size', 'Total White', 
             'Total Hispanic/Latinx','Total Black', 'Total Asian',
             'Native Hawaiian/other Pacific Islander', 
             'American Indian/Alaska Native', 'Total Other', 
             ' Bi- or multiracial',' Unknown	']]
    

    # list of states in diversity.csv file 
    states_research = col_df['Location (State)']
    print(states_research)
    
    # MASSACHUSETTS
    ma_sizes = []
    mass = col_df[(col_df['Location (State)'] == 'Massachusetts')]
    mass_size = sum(mass['Sample Size'])
   
    # white
    mass_white = sum(mass['Total White'])
    mass_white_pct = find_pct(mass_white, mass_size)
    ma_sizes.append(mass_white_pct)

    # hispanic
    mass_his = sum(mass['Total Hispanic/Latinx'])
    mass_his_pct = find_pct(mass_his, mass_size)
    ma_sizes.append(mass_his_pct)
    
    # black
    mass_blk = sum(mass['Total Black'])
    mass_blk_pct = find_pct(mass_blk, mass_size)
    ma_sizes.append(mass_blk_pct)
    
    # asian
    mass_asian = sum(mass['Total Asian'])
    mass_asian_pct = find_pct(mass_asian, mass_size)
    ma_sizes.append(mass_asian_pct)

    
    # other
    mass_other = sum(mass['Total Other'])
    mass_other_pct = find_pct(mass_other, mass_size)
    ma_sizes.append(mass_other_pct)
    
    # multiracial
    mass_multi = sum(mass[' Bi- or multiracial'])
    mass_multi_pct = find_pct(mass_multi, mass_size)
    ma_sizes.append(mass_multi_pct) 
    
    # unknown
    mass_unknown = sum(mass[' Unknown	'])
    mass_unknown_pct = find_pct(mass_unknown, mass_size)
    ma_sizes.append(mass_unknown_pct)
    
    # print(ma_sizes)
    
    # pie chart
    plt.figure(0)
    races = ['White','Hispanic', 'Black', 'Asian',
    'Other', 'Bi - or multiracial', 'Unknown']   
    sizes = ma_sizes
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=races)
    ax1.axis('equal')  
    plt.title("Massachusetts", color = 'blue')
    plt.show()
    
    
    # GEORGIA
    ga_sizes = []
    ga = col_df[(col_df['Location (State)'] == 'Georgia')]
    ga_size = sum(ga['Sample Size'])
   
    # white
    ga_white = sum(ga['Total White'])
    ga_white_pct = find_pct(ga_white, ga_size)
    ga_sizes.append(ga_white_pct)

    # hispanic
    ga_his = sum(ga['Total Hispanic/Latinx'])
    ga_his_pct = find_pct(ga_his, ga_size)
    ga_sizes.append(ga_his_pct)
    
    # black
    ga_blk = sum(ga['Total Black'])
    ga_blk_pct = find_pct(ga_blk, ga_size)
    ga_sizes.append(ga_blk_pct)
    
    # asian
    ga_asian = sum(ga['Total Asian'])
    ga_asian_pct = find_pct(ga_asian, ga_size)
    ga_sizes.append(ga_asian_pct)

    # other
    ga_other = sum(ga['Total Other'])
    ga_other_pct = find_pct(ga_other, ga_size)
    ga_sizes.append(ga_other_pct)
    
    # multiracial
    ga_multi = sum(ga[' Bi- or multiracial'])
    ga_multi_pct = find_pct(ga_multi, ga_size)
    ga_sizes.append(ga_multi_pct) 
    
    # unknown
    ga_unknown = sum(ga[' Unknown	'])
    ga_unknown_pct = find_pct(ga_unknown, ga_size)
    ga_sizes.append(ga_unknown_pct)
    
    # pie chart
    races2 = ['White','Hispanic', 'Black', 'Asian',
    'Other', 'Bi - or multiracial', 'Unknown']      
    sizes2 = ga_sizes
    fig2, ax2 = plt.subplots()
    ax2.pie(sizes2, labels=races2)
    ax2.axis('equal')  
    plt.title("Georgia", color = 'red')
    plt.show()
    
    # CONNECTICUT
    ct_sizes = []
    ct = col_df[(col_df['Location (State)'] == 'Connecticut')]
    ct_size = sum(ct['Sample Size'])

    # white
    ct_white = sum(ct['Total White'])
    ct_white_pct = find_pct(ct_white, ct_size)
    ct_sizes.append(ct_white_pct)

    # hispanic
    ct_his = sum(ct['Total Hispanic/Latinx'])
    ct_his_pct = find_pct(ct_his, ct_size)
    ct_sizes.append(ct_his_pct)
    
    # black
    ct_blk = sum(ct['Total Black'])
    ct_blk_pct = find_pct(ct_blk, ct_size)
    ct_sizes.append(ct_blk_pct)
    
    # asian
    ct_asian = sum(ct['Total Asian'])
    ct_asian_pct = find_pct(ct_asian, ct_size)
    ct_sizes.append(ct_asian_pct)

    # pacific
    ct_pac = sum(ct['Native Hawaiian/other Pacific Islander'])
    ct_pac_pct = find_pct(ct_pac, ct_size)
    ct_sizes.append(ct_pac_pct)
    
    # american indian/alaska native
    ct_nat = sum(ct['American Indian/Alaska Native'])
    ct_nat_pct = find_pct(ct_nat, ct_size)
    ct_sizes.append(ct_nat_pct)
    
    # other
    ct_other = sum(ct['Total Other'])
    ct_other_pct = find_pct(ct_other, ct_size)
    ct_sizes.append(ct_other_pct)
    
    # multiracial
    ct_multi = sum(ct[' Bi- or multiracial'])
    ct_multi_pct = find_pct(ct_multi, ct_size)
    ct_sizes.append(ct_multi_pct) 
    
    # unknown
    ct_unknown = sum(ct[' Unknown	'])
    ct_unknown_pct = find_pct(ct_unknown, ct_size)
    ct_sizes.append(ct_unknown_pct)
      
    # pie chart
    races3 = ['White', 'Hispanic', 'Black', 'Asian', 'Native Hawaiian/Other Pacific Islander\n\n',
    'American Indian/Alaska Native','Other', 'Bi - or multiracial', 'Unknown']   
    sizes3 = ct_sizes
    fig3, ax3 = plt.subplots()
    ax3.pie(sizes3, labels=races3)
    ax3.axis('equal')  
    plt.title("Connecticut", color = 'blue')
    plt.show()
    
    # PENNSYLVANIA 
    pa_sizes = []
    pa = col_df[(col_df['Location (State)'] == 'Pennsylvania')]
    pa_size = sum(pa['Sample Size'])

    # white
    pa_white = sum(pa['Total White'])
    pa_white_pct = find_pct(pa_white, pa_size)
    pa_sizes.append(pa_white_pct)

    # hispanic
    pa_his = sum(pa['Total Hispanic/Latinx'])
    pa_his_pct = find_pct(pa_his, pa_size)
    pa_sizes.append(pa_his_pct)
    
    # black
    pa_blk = sum(pa['Total Black'])
    pa_blk_pct = find_pct(pa_blk, pa_size)
    pa_sizes.append(pa_blk_pct)
    
    # asian
    pa_asian = sum(pa['Total Asian'])
    pa_asian_pct = find_pct(pa_asian, pa_size)
    pa_sizes.append(pa_asian_pct)

    # pacific
    pa_pac = sum(pa['Native Hawaiian/other Pacific Islander'])
    pa_pac_pct = find_pct(pa_pac, pa_size)
    pa_sizes.append(pa_pac_pct)
    
    # american indian/alaska native
    pa_nat = sum(pa['American Indian/Alaska Native'])
    pa_nat_pct = find_pct(pa_nat, pa_size)
    pa_sizes.append(pa_nat_pct)
    
    # other
    pa_other = sum(pa['Total Other'])
    pa_other_pct = find_pct(pa_other, pa_size)
    pa_sizes.append(pa_other_pct)
    
    # multiracial
    pa_multi = sum(pa[' Bi- or multiracial'])
    pa_multi_pct = find_pct(pa_multi, pa_size)
    pa_sizes.append(pa_multi_pct) 
    
    # unknown
    pa_unknown = sum(pa[' Unknown	'])
    pa_unknown_pct = find_pct(pa_unknown, pa_size)
    pa_sizes.append(pa_unknown_pct)
    
    # pie chart
    races4 = ['White', 'Hispanic', 'Black', 'Asian', 'Native Hawaiian/Other Pacific Islander\n\n',
    'American Indian/Alaska Native','Other', 'Bi - or multiracial', 'Unknown']   
    sizes4 = ct_sizes
    fig4, ax4 = plt.subplots()
    ax4.pie(sizes4, labels=races4)
    ax4.axis('equal')  
    plt.title("Pennsylvania", color = 'red')
    plt.show()
    
    # COLORADO
    co_sizes = []
    co = col_df[(col_df['Location (State)'] == 'Colorado')]
    co_size = sum(co['Sample Size'])

    # white
    co_white = sum(co['Total White'])
    co_white_pct = find_pct(co_white, co_size)
    co_sizes.append(co_white_pct)

    # hispanic
    co_his = sum(co['Total Hispanic/Latinx'])
    co_his_pct = find_pct(co_his, co_size)
    co_sizes.append(co_his_pct)
    
    # black
    co_blk = sum(co['Total Black'])
    co_blk_pct = find_pct(co_blk, co_size)
    co_sizes.append(co_blk_pct)
    
    # other
    co_other = sum(co['Total Other'])
    co_other_pct = find_pct(co_other, co_size)
    co_sizes.append(co_other_pct)
    
    # pie chart
    races5 = ['White', 'Hispanic', 'Black', 
    'Other']   
    sizes5 = co_sizes
    fig5, ax5 = plt.subplots()
    ax5.pie(sizes5, labels=races5)
    ax5.axis('equal')  
    plt.title("Colorado", color = 'blue')
    plt.show()
    
    
    # CALIFORNIA
    ca_sizes = []
    ca = col_df[(col_df['Location (State)'] == 'California')]
    ca_size = sum(ca['Sample Size'])

    # white
    ca_white = sum(ca['Total White'])
    ca_white_pct = find_pct(ca_white, ca_size)
    ca_sizes.append(ca_white_pct)

    # hispanic
    ca_his = sum(ca['Total Hispanic/Latinx'])
    ca_his_pct = find_pct(ca_his, ca_size)
    ca_sizes.append(ca_his_pct)
    
    # black
    ca_blk = sum(ca['Total Black'])
    ca_blk_pct = find_pct(ca_blk, ca_size)
    ca_sizes.append(ca_blk_pct)
    
    # asian
    ca_asian = sum(ca['Total Asian'])
    ca_asian_pct = find_pct(ca_asian, ca_size)
    ca_sizes.append(ca_asian_pct)

    # pacific
    ca_pac = sum(ca['Native Hawaiian/other Pacific Islander'])
    ca_pac_pct = find_pct(ca_pac, ca_size)
    ca_sizes.append(ca_pac_pct)
    
    # american indian/alaska native
    ca_nat = sum(ca['American Indian/Alaska Native'])
    ca_nat_pct = find_pct(ca_nat, ca_size)
    ca_sizes.append(ca_nat_pct)
    
    # other
    ca_other = sum(ca['Total Other'])
    ca_other_pct = find_pct(ca_other, ca_size)
    ca_sizes.append(ca_other_pct)
    
    # multiracial
    ca_multi = sum(ca[' Bi- or multiracial'])
    ca_multi_pct = find_pct(ca_multi, ca_size)
    ca_sizes.append(ca_multi_pct) 
    
    # unknown
    ca_unknown = sum(ca[' Unknown	'])
    ca_unknown_pct = find_pct(ca_unknown, ca_size)
    ca_sizes.append(ca_unknown_pct)
    
    print(ca_sizes)
    
    # pie chart
    races6 = ['White', 'Hispanic', 'Black', 'Asian', 
              'Native Hawaiian/Other Pacific Islander',
              'American Indian/Alaska Native\n\n','Other\n', 'Bi - or multiracial', 
              'Unknown']  
    sizes6 = ca_sizes
    fig6, ax6 = plt.subplots()
    ax6.pie(sizes6, labels=races6)
    ax6.axis('equal')  
    plt.title("California", color = 'blue')
    plt.show()
    
    
    # WISCONSIN
    wi_sizes = []
    wi = col_df[(col_df['Location (State)'] == 'Wisconsin')]
    wi_size = sum(wi['Sample Size'])

    # white
    wi_white = sum(wi['Total White'])
    wi_white_pct = find_pct(wi_white, wi_size)
    wi_sizes.append(wi_white_pct)
    
    # pie chart
    races7 = ['White']
    sizes7 = wi_sizes
    fig7, ax7 = plt.subplots()
    ax7.pie(sizes7, labels=races7)
    ax7.axis('equal')  
    plt.title("Wisconsin", color = 'red')
    plt.show()
    
    
    # FLORIDA
    fl_sizes = []
    fl = col_df[(col_df['Location (State)'] == 'Florida')]
    fl_size = sum(fl['Sample Size'])

    # white
    fl_white = sum(fl['Total White'])
    fl_white_pct = find_pct(fl_white, fl_size)
    fl_sizes.append(fl_white_pct)

    # hispanic
    fl_his = sum(fl['Total Hispanic/Latinx'])
    fl_his_pct = find_pct(fl_his, fl_size)
    fl_sizes.append(fl_his_pct)
    
    # black
    fl_blk = sum(fl['Total Black'])
    fl_blk_pct = find_pct(fl_blk, fl_size)
    fl_sizes.append(fl_blk_pct)
    
    # asian
    fl_asian = sum(fl['Total Asian'])
    fl_asian_pct = find_pct(fl_asian, fl_size)
    fl_sizes.append(fl_asian_pct)
    
    # american indian/alaska native
    fl_nat = sum(fl['American Indian/Alaska Native'])
    fl_nat_pct = find_pct(fl_nat, fl_size)
    fl_sizes.append(fl_nat_pct)

    
    # multiracial
    fl_multi = sum(fl[' Bi- or multiracial'])
    fl_multi_pct = find_pct(fl_multi, fl_size)
    fl_sizes.append(fl_multi_pct) 
    
    
    # pie chart
    races8 = ['White', 'Hispanic', 'Black', 'Asian', 
              'American Indian/Alaska Native', 'Bi - or multiracial'] 
    sizes8 = fl_sizes
    fig8, ax8 = plt.subplots()
    ax8.pie(sizes8, labels=races8)
    ax8.axis('equal')  
    plt.title("Florida", color = 'red')
    plt.show()
    
    
    # NEW YORK
    ny_sizes = []
    ny = col_df[(col_df['Location (State)'] == 'New York')]
    ny_size = sum(ny['Sample Size'])

    # white
    ny_white = sum(ny['Total White'])
    ny_white_pct = find_pct(ny_white, ny_size)
    ny_sizes.append(ny_white_pct)

    # pie chart
    races9 = ['White']
    sizes9 = ny_sizes
    fig9, ax9 = plt.subplots()
    ax9.pie(sizes9, labels=races9)
    ax9.axis('equal')  
    plt.title("New York", color = 'blue')
    plt.show()
        
    # TEXAS
    tx_sizes = []
    tx = col_df[(col_df['Location (State)'] == 'Texas')]
    tx_size = sum(tx['Sample Size'])

    # white
    tx_white = sum(tx['Total White'])
    tx_white_pct = find_pct(tx_white, tx_size)
    tx_sizes.append(tx_white_pct)

    # hispanic
    tx_his = sum(tx['Total Hispanic/Latinx'])
    tx_his_pct = find_pct(tx_his, tx_size)
    tx_sizes.append(tx_his_pct)
    
    # other
    tx_other = sum(tx['Total Other'])
    tx_other_pct = find_pct(tx_other, tx_size)
    tx_sizes.append(tx_other_pct)
    
    
    # pie chart
    races9 = ['White', 'Hispanic', 'Other']  
    sizes9 = tx_sizes
    fig9, ax9 = plt.subplots()
    ax9.pie(sizes9, labels=races9)
    ax9.axis('equal')  
    plt.title("Texas", color = 'red')
    plt.show()
    
main()    