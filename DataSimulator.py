''' 

    Title: Data Simulator
    Author: Karl Roth
    Date: January 2019
    
'''


import numpy as np
import pandas as pd
import csv


# Define functions

def saveFile(output, file_name):
    file = open(file_name,'wrb')

    with file:
        writer = csv.writer(file)
        writer.writerows(output) 

# Set the Lat/Long boundaries

start_lat = 40.10902
start_lon = -88.230338

end_lat = 40.115616
end_lon = -88.223750


# Number of points in the simulation 

columns = 30
rows = 30

lat_unit = (end_lat - start_lat)/columns
lon_unit = (end_lon - start_lon)/rows


# Initialize list with header

output = [["Latitude","Longitude","Counts"]]


# Case B: Tent

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
    
        '''
        #For Rows = 10
        if x < rows/2:
            num = str(32+4*x)
            result = [lat, lon, num]
        else: 
            num = str(32 + 8*rows/2 - 4*x)
            result = [lat, lon, num]
        
        
        #For rows = 20
        if x < rows/2:
            num = str(32+2*x)
            result = [lat, lon, num]
        else: 
            num = str(32 + 4*rows/2 - 2*x)
            result = [lat, lon, num]
        
        '''
        #For rows = 30
        if x < rows/2:
            num = str(32+64*x/rows)
            result = [lat, lon, num]
        else: 
            num = str( 96 - 64*x/rows)
            result = [lat, lon, num]
        
        output.append(result)

saveFile(output, "SimData_Tent_900.csv")

    
# Case B': Random Tent

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
    
        #For rows = 30
        if x < rows/2:
            num = str(32+64*x/rows + np.random.randint(0,8)) 
            result = [lat, lon, num]
        else: 
            num = str(96-64*x/rows + np.random.randint(0,8))
            result = [lat, lon, num]
        
        output.append(result)
        
saveFile(output, "SimData_RandomTent_900.csv")   


# Case C: Pyramid

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
    
        #Bottom
        if y >= x and y <= rows - x:
            num = str(32+64*x/rows)
            result = [lat, lon, num]
        #Right
        if y > x and y > rows - x:
            num = str(96 - 64*y/columns)
            result = [lat, lon, num]
        #Top
        if y <= x and y >= rows - x:
            num = str(96 - 64*x/rows)
            result = [lat, lon, num]
        #Left
        if y < x and y < rows - x:
            num = str(32+64*y/columns)
            result = [lat, lon, num]
        
        output.append(result)
        
saveFile(output, "SimData_Pyramid_900.csv")

# Case C': Random Pyramid 

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
    
        #Bottom
        if y >= x and y <= rows - x:
            num = str(32+64*x/rows + np.random.randint(0,8))
            result = [lat, lon, num]
        #Right
        if y > x and y > rows - x:
            num = str(96 - 64*y/columns + np.random.randint(0,8))
            result = [lat, lon, num]
        #Top
        if y <= x and y >= rows - x:
            num = str(96 - 64*x/rows + np.random.randint(0,8))
            result = [lat, lon, num]
        #Left
        if y < x and y < rows - x:
            num = str(32+64*y/columns + np.random.randint(0,8))
            result = [lat, lon, num]
        
        output.append(result)
        
saveFile(output, "SimData_RandomPyramid_900.csv")


# Case D: Truncated Pyramid 

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
    
        # Plateau
        if x > rows/3 and x < 2*rows/3 and y > columns/3 and y < 2*columns/3:
            num = 64
            result = [lat, lon, num]
        #Bottom
        elif y >= x and y <= rows - x:
            num = str(32+96*x/rows)
            result = [lat, lon, num]
        #Right
        elif y > x and y > rows - x:
            num = str(128 - 96*y/columns)
            result = [lat, lon, num]
        #Top
        elif y <= x and y >= rows - x:
            num = str(128 - 96*x/rows)
            result = [lat, lon, num]
        #Left
        elif y < x and y < rows - x:
            num = str(32+96*y/columns)
            result = [lat, lon, num]
        
        
        output.append(result)
        
saveFile(output, "SimData_TruncPyramid_900.csv")


# Case D': Random Truncated Pyramid 

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
    
        #Square
        if x > rows/3 and x < 2*rows/3 and y > columns/3 and y < 2*columns/3:
            num = 64 + np.random.randint(0,16) 
            result = [lat, lon, num]
        #Bottom
        elif y >= x and y <= rows - x:
            num = str(32+96*x/rows + np.random.randint(0,8))
            result = [lat, lon, num]
        #Right
        elif y > x and y > rows - x:
            num = str(128 - 96*y/columns + np.random.randint(0,8))
            result = [lat, lon, num]
        #Top
        elif y <= x and y >= rows - x:
            num = str(128 - 96*x/rows + np.random.randint(0,8))
            result = [lat, lon, num]
        #Left
        elif y < x and y < rows - x:
            num = str(32+96*y/columns + np.random.randint(0,8))
            result = [lat, lon, num]
        
        
        output.append(result)
    
saveFile(output, "SimData_RandomTruncPyramid_900.csv")  
    

# Case E: Hot spot square in center

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
        
        if x >= rows/3 and x <= 2*rows/3 and y >= columns/3 and y <= 2*columns/3:
            num = "64"
            result = [lat, lon, num]
        else: 
            num = "32"
            result = [lat, lon, num]
        
        output.append(result)
        
saveFile(output, "SimData_HotSpot_900.csv")  

    
#Case E': Random Hot spot square in center

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
        
        if x >= rows/3 and x <= 2*rows/3 and y >= columns/3 and y <= 2*columns/3:
            num = str(64 + np.random.randint(-8, 8))
            result = [lat, lon, num]
        else: 
            num = "32"
            result = [lat, lon, num]
        
        output.append(result)

saveFile(output, "SimData_RandomHotSpot_900.csv")   


# Case E'': Random, Sparse hotspot square in center

caseE_random = pd.read_csv("SimData_RandomHotspot_900.csv")
caseE_sparse = caseE_random.sample(frac=0.2)
caseE_sparse.to_csv("SimData_RandomHotSpotSparse_900.csv")


# Case F: Simple Campus

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
        
        if x > rows/8 and x < rows/4 and y > columns/8 and y < columns/4:
            result = [lat, lon, "64"]
        elif x > 3*rows/8 and x < rows/2 and y > 3*columns/4 and y < 7*columns/8:
            result = [lat, lon, "64"]
        elif x < 3*rows/16 and y > columns/2:
            result = [lat, lon, "64"]
        else: 
            result = [lat, lon, "32"]
        
        output.append(result)
        
saveFile(output, "SimData_Campus_900.csv")


#Case F': Simple Campus, Random hotspots

output = [["Latitude","Longitude","Counts"]]

for x in range(1,columns):
    for y in range(1,rows):
        lat = str(start_lat + x*lat_unit)
        lon = str(start_lon + y*lon_unit)
        
        if x > rows/8 and x < rows/4 and y > columns/8 and y < columns/4:
            num = str(64 + np.random.randint(-8,8))
            result = [lat, lon, num]
        elif x > 3*rows/8 and x < rows/2 and y > 3*columns/4 and y < 7*columns/8:
            num = str(64 + np.random.randint(-8,8))
            result = [lat, lon, num]
        elif x < 3*rows/16 and y > columns/2:
            num = str(64 + np.random.randint(-8,8))
            result = [lat, lon, num]
        else: 
            result = [lat, lon, "32"]
        
        output.append(result)
        
saveFile(output, nb"SimData_RandomCampus_900.csv")     


# Case F'': Sparse Simple Campus, Random hotspots 

caseF_random = pd.read_csv("SimData_RandomCampus_900.csv")
case_sparse = case_random.sample(frac=0.2)
case_sparse.to_csv("SimData_RandomCampusSparse_900.csv")
