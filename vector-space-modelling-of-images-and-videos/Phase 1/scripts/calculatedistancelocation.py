import extractinfolocation
import os
import pandas as pd
import numpy as np
from heapq import nlargest
import xml.etree.ElementTree as ET

count=0
filepath=input("Enter filename")
filedirectory="C:\\Users\\arpan\\Documents\\ASU\\"+filepath

locationnumber=int(input("enter location number"))
model=input("enter model(TF,DF or TFIDF)")
k=int(input("enter k value"))

#Read the xml to extract the location given the location id
xmlfilepath="C:\\Users\\arpan\\Documents\\ASU\\devset_topics.xml"
locationdocument = ET.parse(xmlfilepath)

number=locationdocument.findall('topic/number')
root=locationdocument.getroot()

for child in range(0,len(root)):
    if int(root[child][0].text) ==locationnumber:
        desiredlocation=root[child][1].text
        break

extractdata= extractinfolocation.DataExtractor()
#location="C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerPOI.wFolderNames.txt"
df=extractdata.openandextractdatalocation(filedirectory)
locations = df["Location"].unique()
terms = df["Term"].unique()
#extract dataframe and place in a matrix(User x Term) containing the model values
columns = list(terms)
#columns.insert(0, "imageid")
matrix = pd.DataFrame(columns = columns)
for location in locations:

    vector = []
    location_df = df[df['Location'] == location]
    location_terms = list(location_df["Term"].unique())
    for term in terms:
        if term not in location_terms:
            vector.append(0)
        else:
            new_df = location_df[location_df["Term"] == term]
            vector.append(new_df[model].iloc[0])
    matrix.loc[len(matrix.index)] = vector
colsumarray=[]
termmatrix=[]
#Calculate dot product of each matrix with chosen location
for location in range(0,len(locations)):
     colsum=0
     temptermrow = []
     for term in range(0,len(terms)):

        rowsum=(float(matrix.values[locationnumber][term])*float(matrix.values[location][term]))
        if matrix.values[locationnumber][term] == 0 and float(matrix.values[location][term]) == 0:
            temptermrow.append(float("-inf"))
        else:
            temptermrow.append(rowsum)
        colsum+=rowsum
     termmatrix.append(temptermrow)
     colsumarray.append(colsum)


klocations=nlargest(k, enumerate(colsumarray), key=lambda x:x[1])
saveindexes=[]
for i in range (0,k):
    saveindexes.append(klocations[i][0])

saveindexterms=[]
ktermsindexes=[]
for k in range(0,len(saveindexes)):
            ktermsindexes.append(nlargest(3, enumerate(termmatrix[saveindexes[k]]), key=lambda x:x[1]))


#printing k similar locations and top 3 terms
print("Most similar locations and matching scores  and 3 most similar terms are = ")
for i in range(0,len(saveindexes)):
    print("\n")
    print("%s %f"%(locations[saveindexes[i]],klocations[i][1]),end=" ")
    for j in range(0,3):
     print(terms[ktermsindexes[i][j][0]],end=" ")


