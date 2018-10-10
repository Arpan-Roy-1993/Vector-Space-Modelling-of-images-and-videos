import extractinfoimage
import os
import pandas as pd
import numpy as np
from heapq import nlargest
from collections import defaultdict


filepath=input("Enter filename")
filedirectory="C:\\Users\\arpan\\Documents\\ASU\\"+filepath

imageid=(input("enter imageid"))
model=input("enter model(TF,DF or TFIDF)")
k=int(input("enter k value"))



extractdata= extractinfoimage.DataExtractor()

#location="C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerImage.txt"

df=extractdata.openandextractdataimage(filedirectory)
#print(df)
images = df["Imageid"].unique()
terms = df["Term"].unique()
count=0
for i in images:
  if(i== imageid):
    break
  count+=1
#extract dataframe and place in a matrix(User x Term) containing the model values
columns = list(terms)
matrix = pd.DataFrame(columns = columns)
for image in images:

    vector = []
    image_df = df[df["Imageid"] == image]
    image_terms = list(image_df["Term"].unique())
    for term in terms:
        if term not in image_terms:
            vector.append(0)
        else:
            new_df = image_df[image_df["Term"] == term]
            vector.append(new_df[model].iloc[0])
    matrix.loc[len(matrix.index)] = vector
#Calculate dot product of each matrix with chosen image
colsumarray=[]
termmatrix=[]

for image in range(0,len(images)):
     if image==count:
       continue
     colsum=0
     temptermrow = []
     for term in range(0,len(terms)):
        rowsum=(float(matrix.values[count][term])*float(matrix.values[image][term]))
        if matrix.values[count][term] == 0 and float(matrix.values[image][term]) == 0:
            temptermrow.append(float("-inf"))
        else:
            temptermrow.append(rowsum)
        colsum+=rowsum
     termmatrix.append(temptermrow)
     colsumarray.append(colsum)


#printing k similar images and top 3 terms
kimages=nlargest(k, enumerate(colsumarray), key=lambda x:x[1])
saveindexes=[]
for i in range (0,k):
    saveindexes.append(kimages[i][0])

saveindexterms=[]
ktermsindexes=[]
for i in range(0,len(saveindexes)):
            ktermsindexes.append(nlargest(3, enumerate(termmatrix[saveindexes[i]]), key=lambda x:x[1]))


print("Most similar images and matching scores  and 3 most similar terms are = ")
for i in range(0,len(saveindexes)):
    print("\n")
    print("%s %f"%(images[saveindexes[i]],kimages[i][1]),end=" ")
    for j in range(0,3):
     print(terms[ktermsindexes[i][j][0]],end=" ")



