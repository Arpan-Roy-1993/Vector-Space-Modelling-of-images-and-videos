import logging
import os
import pandas as pd
import io

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
#Class to extract image information( image id, term,tf, df, tfidf)
class DataExtractor():
    def __init__(self):
        {}
    def openandextractdataimage(self,file_name):

        df = pd.read_csv("C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerImage.txt",header=None,error_bad_lines=False)
        df2=pd.DataFrame(columns=['Imageid','Term','TF','DF','TFIDF'])
        count=0
        for column in df:
            for row in df[column]:
                array = row.split(' ')
                length = (int)(len(array)/40)
                for i in range(2,length,4):
                     df2.loc[count,'Imageid']=array[0]
                     df2.loc[count,'Term']=array[i-1]
                     df2.loc[count,'TF']=array[i]
                     df2.loc[count,'DF']=array[i+1]
                     df2.loc[count,'TFIDF']=array[i+2]
                     count+=1

        return df2


if __name__ == "__main__":

    extractdata= DataExtractor()
    location="C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerImage.txt"
    df=extractdata.openandextractdataimage(location)
#    print(df)














