import logging
import os
import pandas as pd
import io
import numpy

#Class to extract location information from given input file
class DataExtractor():
    def __init__(self):
        {}
    def openandextractdatalocation(self,file_name):

        df = pd.read_csv("C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerPOI.wFolderNames.txt",header=None,error_bad_lines=False)
        df2=pd.DataFrame(columns=['Location','Term','TF','DF','TFIDF'])
        count=0
        array={}
        for column in df:
            for row in df[column]:

                array = row.split(' ')
                #print(array)
                length = (int)(len(array)/20)
                if "_" in array[0]:
                    df2.loc[count,'Location']=array[0]
                    countunderscore=str(array[0]).count('_')
                else:
                    countunderscore=0
                flag = False
                for j in range(countunderscore + 2,length,4):
                    if j== length-1:
                        flag = True
                        break
                    df2.loc[count,'Location']=array[0]
                    df2.loc[count,'Term']=array[j]
                    # print(array[j])
                    df2.loc[count,'TF']=array[j+1]
                    df2.loc[count,'DF']=array[j+2]
                    df2.loc[count,'TFIDF']=array[j+3]
                    count+=1
                if flag == True:
                    continue



        return df2


if __name__ == "__main__":

    extractdata= DataExtractor()
    location="C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerPOI.wFolderNames.txt"
    df=extractdata.openandextractdatalocation(location)
#    print(df)
