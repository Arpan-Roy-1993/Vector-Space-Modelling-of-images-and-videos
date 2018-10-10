import extract_info
import os
import pandas as pd
import numpy as np
from heapq import nsmallest
from collections import defaultdict
import math
from heapq import nlargest

filepath=input("Enter filename")
filedirectory="C:\\Users\\arpan\\Documents\\ASU\\"+filepath

userid=(input("enter userid"))
model=input("enter model(TF,DF or TFIDF)")
k=int(input("enter k value"))


extractdata= extract_info.DataExtractor()
#location="C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerUser.txt"
df=extractdata.openandextractdata(filedirectory)

users = df["Userid"].unique()
terms = df["Term"].unique()
count=0
for i in users:
  if(i==userid):
    break
  count+=1
count=3
columns = list(terms)
#extract dataframe and place in a matrix(User x Term) containing the model values
matrix = pd.DataFrame(columns = columns)
for user in users:

    vector = []
    user_df = df[df["Userid"] == user]
    user_terms = list(user_df["Term"].unique())
    for term in terms:
        if term not in user_terms:
            vector.append(0)
        else:
            new_df = user_df[user_df["Term"] == term]
            vector.append(new_df[model].iloc[0])
    matrix.loc[len(matrix.index)] = vector
###############################################Dotproduct#################################################
#Calculate dot product of each matrix with chosen image

colsumarray=[]
termmatrix=[]

for user in range(0,len(users)):
     colsum=0
     temptermrow = []
     for term in range(0,len(terms)):
        rowsum=(float(matrix.values[count][term])*float(matrix.values[user][term]))
        if matrix.values[count][term] == 0 and float(matrix.values[user][term]) == 0:
            temptermrow.append(float("-inf"))
        else:
            temptermrow.append(rowsum)
        colsum+=rowsum
     termmatrix.append(temptermrow)
     colsumarray.append(colsum)

k=8

kusers=nlargest(k, enumerate(colsumarray), key=lambda x:x[1])
saveindexes=[]
for i in range (0,k):
    saveindexes.append(kusers[i][0])

saveindexterms=[]
ktermsindexes=[]
for k in range(0,len(saveindexes)):
            ktermsindexes.append(nlargest(3, enumerate(termmatrix[saveindexes[k]]), key=lambda x:x[1]))

#printing k similar users and top 3 terms


print("Most similar users and matching scores  and 3 most similar terms are = ")
for i in range(0,len(saveindexes)):
    print("\n")
    print("%s %f"%(users[saveindexes[i]],kusers[i][1]),end=" ")
    for j in range(0,3):
     print(terms[ktermsindexes[i][j][0]],end=" ")

