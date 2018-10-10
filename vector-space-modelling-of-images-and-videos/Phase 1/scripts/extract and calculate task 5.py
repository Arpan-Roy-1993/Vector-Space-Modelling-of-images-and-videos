import extractinfolocation
import os
import math
import pandas as pd
import numpy as np
from heapq import nlargest
from heapq import nsmallest
import xml.etree.ElementTree as ET

location_id = int(input("enter loation id"))
models = [ " CM"," CM3x3"," CN"," CN3x3"," CSD"," GLRLM"," GLRLM3x3", " HOG"," LBP"," LBP3x3"]
k = int(input("enter value of k:"))

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
location_to_scores_dict = {}
for location in all_locations:
    model_scores = []
    for model in range(0,len(models)):
        df = pd.read_csv("C:/Users/arpan/Documents/ASU/img/" + location + models[model] + ".csv", header=None)
        del df[0]
        model_scores.append(df.values.sum())
    location_to_scores_dict[location] = model_scores

cumulative_sum = []
for location in all_locations:
    cumulative_sum.append(sum(location_to_scores_dict[location]))

ksimilarlocationsmode = nsmallest(k+1, enumerate(cumulative_sum), lambda x: math.fabs(x[1] - cumulative_sum[all_locations.index(userlocation)]))
del ksimilarlocationsmode[0]

desired_locations = []
for item in ksimilarlocationsmode:
    desired_locations.append(all_locations[item[0]])

for location in range(0,len(desired_locations)):
    print("Location - %s Matching score - %f" % (all_locations[location],cumulative_sum[location]))
    for model in models:

        print("Model - %s, Score - %d" % (model, location_to_scores_dict[all_locations[location]][models.index(model)]))
    print("\n")
