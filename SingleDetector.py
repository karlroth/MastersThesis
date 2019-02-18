'''
    
    Title: Individual Detectors
    Author: Karl Roth
    Date: January 2019
    
'''

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

import pandas as pd
import numpy as np
import csv
from sklearn.model_selection import train_test_split


# Define functions

def plotCampusCounts(df, title):
    ax = df.plot.scatter(x='Longitude', y='Latitude', c='Counts', colormap='viridis', title=title, sharex=False)
    ax.set_ylim(40.108,40.116)
    ax.set_xlim(-88.231,-88.223)

    for label in ax.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)
    


# ## Single Detector Data
# 
# This workbook takes the detector data from February 16, 2016 and creates seperate plots and csv files for each unique Detector ID. Training and testing sets are saved as csv for later interpolation in ArcGIS. 
# 
# Methodology:
# 1. Raw February 16, 2016 data is imported and plotted
# 2. Plot is generated for each unique detector
# 3. Each unique detector is split into training and testing sets
# 


# Import Data

raw = pd.read_csv("Feb16-2016.csv")
raw.columns = ['ID','Latitude','Longitude','Counts','Time']


# Print the detector count and plot campus

print("The raw dataset contains "+ str(raw.size) +" measurements")
plotCampusCounts(raw, "Februrary 16, 2016")


# Plot all unique Detectors

detectors = raw['ID'].unique()

for detector in detectors:
    unique = raw.loc[raw['ID'] == detector]
    
    message = detector+": {:,} measurements".format(unique.size)
    plotCampusCounts(unique, message)
    

# Save DataFrames to CSV for interpolation

for detector in detectors:
    result = raw.loc[raw['ID'] == detector]
    filename = "Feb16-2016_{:}".format(detector)
    result.to_csv(filename+".csv")
    print(filename+".csv")
    
    train, test = train_test_split(result, test_size=0.2)
    
    test.to_csv(filename+"_test.csv")
    train.to_csv(filename+"_train.csv")


# ## Merged Detectors
# Some detectors were put together to provide broader coverage
# 
# Included:
# - Detector A: D3-SGM100195
# - Detector B: D3-SGM100182
# - Detector C: D3-SGM100196
# - Detector D: D3-SGM100367
# 
# Removed:
# - Detector E: D3-120126
# - Detector F: D3-SGM100224
# - Detector G: D3-SGM100390
# - Detector H: D3-SGM100478
# 


# Create list of Detectors to be merged

dfs = []
for detector in detectors:
    name = str(detector)
    if (name != "D3-SGM100224") and (name != "D3-120126") and (name != "D3-SGM100478") and (name != "D3-SGM100312") and (name != "D3-SGM100390"):
        filename = "Feb16-2016_"+detector+".csv"
        print(filename)
        dfs.append(pd.read_csv(filename))


# Merge Detectors A through B and plot

for df in dfs:
    result = pd.merge(result, df, 'outer')
    
plotCampusCounts(result, 'Select Detectors: {:,} measurements'.format(result.size) )
train, test = train_test_split(result, test_size=0.2)

result.to_csv("Feb16-2016_SelectDetectors.csv")
train.to_csv("Feb16-2016_SelectDetectors_train.csv")
test.to_csv("Feb16-2016_SelectDetectors_test.csv")