import extractinfolocation
import os
import math
import pandas as pd
import numpy as np
from heapq import nlargest
from heapq import nsmallest
import xml.etree.ElementTree as ET


location_id = int(input("Enter location ID"))
n=input("Enter model")
model = " "+n
k=int(input("Enter value of k"))

xmlfilepath = "C:\\Users\\arpan\\Documents\\ASU\\devset_topics.xml"
locationdocument = ET.parse(xmlfilepath)

number = locationdocument.findall('topic/number')
root = locationdocument.getroot()
all_locations = []
for child in range(0, len(root)):
    if int(root[child][0].text) == location_id:
        userlocation = root[child][1].text
    all_locations.append(root[child][1].text)

locationfile = "C:/Users/arpan/Documents/ASU/img/"
model_values = []
for location in all_locations:
    df = pd.read_csv("C:/Users/arpan/Documents/ASU/img/" + location + model + ".csv", header=None)
    del df[0]
    model_values.append(df.values.sum())

ksimilarlocationsmode = nsmallest(k+1, enumerate(model_values), lambda x: math.fabs(x[1] - model_values[all_locations.index(userlocation)]))
del ksimilarlocationsmode[0]
desired_locations = []
for item in ksimilarlocationsmode:
    desired_locations.append(all_locations[item[0]])

for location in desired_locations:
    df = pd.read_csv("C:/Users/arpan/Documents/ASU/img/" + location + model + ".csv", header=None)
    photo_ids = list(df[0].unique())
    del df[0]
    df = df.sum(axis=0)
    k_max_photo_ids = nlargest(3, enumerate(list(df)), lambda x: x[1])
    print("Location %s Score: %f"%(location, model_values[all_locations.index(location)]))
    for item in k_max_photo_ids:
        print("Photo Id - %d" % (photo_ids[item[0]]))
    print("\n")
