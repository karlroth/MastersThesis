'''

    Title: Point Injection
    Author: Karl Roth
    Date: January 2019

'''


get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import pandas as pd

import numpy as np
import csv


# Define functions

def plotCampusCounts(df, title):
    ax = df.plot.scatter(x='Longitude', y='Latitude', c='Counts', colormap='viridis', title=title, sharex=False)
    ax.set_ylim(40.108,40.116)
    ax.set_xlim(-88.231,-88.223)

    for label in ax.xaxis.get_ticklabels()[::2]:
        label.set_visible(False)
        

def mergeTrainTest(train, test):
    
    # Change column name for easier merge

    test.columns = ['Latitude','Longitude','testCounts','Time']
    merged = pd.merge(train, test, 'outer')


    # Change column name back for plotting

    test.columns = ['Latitude','Longitude','Counts','Time']
    merged['Counts'] = merged['Counts'].fillna(merged['testCounts'])
    merged.drop(merged.columns[len(merged.columns)-1], axis=1, inplace=True)
    merged.drop(merged.columns[len(merged.columns)-1], axis=1, inplace=True)
    
    return merged


def injectUniformBackground(df, train, test, dimension):

    header = ["Latitude","Longitude","Counts"]
    output = []
    
    # Set the Lat/Long boundaries

    columns, rows = dimension
    
    start_lat = 40.109028
    start_lon = -88.230338

    end_lat = 40.116430
    end_lon = -88.22375
    
    lat_unit = (end_lat - start_lat)/columns
    lon_unit = (end_lon - start_lon)/rows


    for x in range(1,rows):
        for y in range(1,columns):
            lat = str(start_lat + x*lat_unit)
            lon = str(start_lon + y*lon_unit)
    
            result = [lat, lon, "32"]
        
            output.append(result)
        
    inject = pd.DataFrame(output, columns = header).astype(float)
    inject_test = inject.sample(frac=0.2)
    inject_train = inject.sample(frac=0.8)

    injected = pd.merge(inject, df, "outer")

    train_result = pd.merge(inject_train, train, "outer")
    test_result = pd.merge(inject_test, test, "outer")
        
    return train_result, test_result, injected
        

# Retrieve training and testing sets (generated in Spark)

train = pd.read_csv("Feb16_1-30_training.csv")
test = pd.read_csv("Feb16_1-30_test.csv")
merged = mergeTrainTest(train, test)


# 100 points injected

dimension = 10
train100, test100, injected100 = injectUniformBackground(merged, train, test, dimension)

train100.to_csv("Feb16_1-30_train100.csv")
test100.to_csv("Feb16_1-30_test100.csv")


# 400 points injected

dimension = 20
train400, test400, injected400 = injectUniformBackground(merged, train, test, dimension)

train400.to_csv("Feb16_1-30_train400.csv")
test400.to_csv("Feb16_1-30_test400.csv")


# 900 points injected

dimension = 30
train900, test900, injected900 = injectUniformBackground(merged, train, test, dimension)

train900.to_csv("Feb16_1-30_train900.csv")
test900.to_csv("Feb16_1-30_test900.csv")


# Plot of the datasets

plotCampusCounts(merged, "Full Dataset")
plotCampusCounts(injected100, "100 Injected points")
plotCampusCounts(injected400, "400 Injected points")
plotCampusCounts(injected900, "900 Injected points")
plotCampusCounts(train900, "900 Injected points: Training")
plotCampusCounts(test900, "900 Injected points: Testing")