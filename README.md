# Masters Thesis

All Code written for processing D3S detector data collected from a mobile sensor network on February 16, 2016. This network consists of a small radiation detector that can easily fit in a pocket. This detector is paired via bluetooth to a Samsung Galaxy S6. The smartphone has an app created by our research group that sends the data into our Amazon Web Service Cloud where it is stored in S3. The header of the data is as follows:

Detector ID | Latitude | Longitude | Sigma (cps) | n (cps) | Time (ns) | channel 0 | channel 1 | ... | channel 4096

Detector ID is a unique identifcation number paired with each detector Latitude and Logitude are the GPS coordinates of the detector (within a few meters if outdoors) in degrees Sigma is the ionizing radiation counts per second measured by the D3S detector N is the neutron counts per second measured by the D3S detector Time is the unix time measured in nanoseconds Channels 0-4096 represent the energy spectrum measured from the detector

Additionally weather data was used from wunderground.com

GOAL: Sensor networks are increasingly being used for Nuclear Nonproliferation purposes in urban environments. The goal of this research is to take the gps and time-tagged radiation data and generate heat maps using various geostatistical techniques. Including MapReduce, Kriging, and Inverse Distance Weighting. By accurately characterizing background radiation we can improve outlier detection and find anomalous radioactive sources in our data set. This project required utilizing Elastic Map Reduce (EMR) clusters with Apache Spark pre-installed. All scripts were then run on subsets of the D3S data set. Some data cleaning and manipulation was required before processing.

## Simulations and Data Manipulations

For validation purposes, several simulations of background radiation were generated. Additionally, several subsets and manipulated versions of the original February 16, 2016, data were created in an attempt to improve the results of the final interpolations. 
