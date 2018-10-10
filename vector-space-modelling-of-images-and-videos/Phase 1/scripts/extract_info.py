import logging
import os
import pandas as pd
import io


#class to extract data from file and enter into a dataframe
class DataExtractor():
    def __init__(self):
        {}
    def openandextractdata(self,file_name):
    #Parsing each row in an array and assigning to a new dataframe
        df = pd.read_csv("C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerUser.txt",header=None,error_bad_lines=False)
        df2=pd.DataFrame(columns=['Userid','Term','TF','DF','TFIDF'])
        count=0
        for column in df:
            for row in df[column]:
                array = row.split(' ')
                length = (int)(len(array)/50)
                for i in range(2,length,4):
                     df2.loc[count,'Userid']=array[0]
                     df2.loc[count,'Term']=array[i-1]
                     df2.loc[count,'TF']=array[i]
                     df2.loc[count,'DF']=array[i+1]
                     df2.loc[count,'TFIDF']=array[i+2]
                     count+=1

        return df2



if __name__ == "__main__":

    extractdata= DataExtractor()
    location="C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerUser.txt"
    df=extractdata.openandextractdata(location)
#    print(df)














