import csv
import xml.etree.ElementTree
import os
import numpy as np
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import minmax_scale
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.decomposition import LatentDirichletAllocation

###########################################################################
##GET INPUT
XMLMappingFile=input("Enter XML file path for location id to name mapping")
CSV_folder= input("Enter the directory path for CSV files ")
query= input("Enter query(Location ID, Visual Descriptor Model, K)")
DimensionalityRedAlgo= input("Select and Enter Dimensionality Reduction Algorithm(PCA/ SVD/ LDA)")

##Global variables
allReducedLocs= []
QfileIndex=0

##PARSE QUERY
queryFields=query.split(" ")
QLoc=queryFields[0]
QModel=queryFields[1]
KValue=int(queryFields[2])

##GET QUERY LOCATION FILE NAME FROM XML FILE
e = xml.etree.ElementTree.parse(XMLMappingFile).getroot()
searchQ="topic[number='"+ QLoc+"']"
item=e.find(searchQ)
name=item[1].text
QFileName= name+" "+QModel+".csv"

##Create Matrix from file
def WriteFileToMatrix(filename):
    ListOfLists=[]
    with open(CSV_folder+"\\"+filename,"r",) as file:
        reader = csv.reader(file)
        for row in reader:
            TemList=[]
            for element in row:
               TemList.append(float(element))
            TemList.pop(0)
            ListOfLists.append(TemList)
    return ListOfLists

##Get all files of GIVEN visual descriptor model
def GetAllFilesByModel(modelName):
    filenames=[]
    for filename in os.listdir(CSV_folder):
        if(filename.endswith(modelName+".csv")):
            filenames.append(filename)
    return filenames

##Get all matricies of a model
def GetAllMatriciesOfModel(model):
    global QfileIndex
    allMatricies=[]
    allFiles=GetAllFilesByModel(model)
    i=0
    for item in allFiles:
        allMatricies.append(WriteFileToMatrix(item))
        if(item==QFileName):
            QfileIndex=i
        i=i+1
    return allMatricies

#################################################################################
#PCA

def ApplyPCA(train_data, test_data):
    ##Standardizing the Data
    scaler = StandardScaler()
    scaler.fit(train_data)
    train_data = scaler.transform(train_data)

    ##PCA
    pca=decomposition.PCA(n_components=KValue)
    pca.fit(train_data)     
    
    ##Transform all locations
    for loc in test_data:
        std_loc= scaler.transform(loc)
        allReducedLocs.append(pca.transform(std_loc))


    ##Latent semantics
    S= np.diag(pca.singular_values_)
    VT=pca.components_
    latentSemantics= (np.dot(S,VT)).transpose()

    return latentSemantics

##################################################################################
#SVD

def ApplySVD(train_data, test_data):
    svd= TruncatedSVD(n_components=KValue)
    svd.fit(train_data) 

    ##Transform all locations
    for loc in test_data:
        allReducedLocs.append(svd.transform(loc))
    
    ##Latent semantics
    S= np.diag(svd.singular_values_)
    VT=svd.components_
    latentSemantics= (np.dot(S,VT)).transpose()

    return latentSemantics

##################################################################################
#LDA

def ApplyLDA(train_data, test_data):
    lda = LatentDirichletAllocation(n_components=KValue)
    lda.fit(train_data)     
    
    for loc in test_data:
        allReducedLocs.append(lda.transform(loc))
    
    return lda.components_

##################################################################################
#apply Dimensionality Reduction

qMatrix= WriteFileToMatrix(QFileName)
allMatricies= GetAllMatriciesOfModel(QModel)

if(DimensionalityRedAlgo=="PCA"):
    LatentSematics = ApplyPCA(qMatrix, allMatricies)

if(DimensionalityRedAlgo=="SVD"):
    LatentSematics = ApplySVD(qMatrix, allMatricies)

if(DimensionalityRedAlgo=="LDA"):
    scaled_train_data = minmax_scale(qMatrix, feature_range = (0,5), axis = 1)
    allScaled_testmatrices=[]
    for matrix in allMatricies:
        allScaled_testmatrices.append( minmax_scale(matrix, feature_range = (0,5), axis = 1))

    LatentSematics = ApplyLDA(scaled_train_data, allScaled_testmatrices)

ReducedQueryLoc=allReducedLocs[QfileIndex]

####Print PCA latent sematics
print("Latent semantics:")
print("-----------------------------------------------------")
print(LatentSematics)
print("dimensions: ")
print(LatentSematics.shape)
print("------------------------------------------------------")


###################################################################################
#Similar 5 Locations

loclocM= None
i=0
first=True
for loc in allReducedLocs:
    if(i!=QfileIndex):
        distMatrix=euclidean_distances(ReducedQueryLoc,loc)
        minDist= distMatrix.min(1)
        if(first):
            loclocM=minDist
            first=False
        else:
            loclocM=np.column_stack((loclocM, minDist))
    i=i+1

minDistIndex= np.argmin(loclocM,axis=1)

length=len(allReducedLocs)
similarityMatrix=np.zeros(length)
for item in minDistIndex:
    if(item<QfileIndex):
        similarityMatrix[item]=similarityMatrix[item]+1
    else:
        similarityMatrix[item+1]=similarityMatrix[item+1]+1
    

x=np.argsort(similarityMatrix)

##top 5 names
print("TOP 5 SIMILAR LOCATIONS TO "+ QFileName.split(" ")[0])
allNames=GetAllFilesByModel(QModel)
i=1
while(i<=5):
    print("------------------------")
    print(allNames[x[length-i]].split(" ")[0])
    print("score:  " )
    print(similarityMatrix[x[length-i]])
    i=i+1









