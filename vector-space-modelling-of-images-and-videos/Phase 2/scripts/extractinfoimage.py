import logging
import os
import math
import pandas as pd
import io

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


# Class to extract image information( image id, term,tf, df, tfidf)
class DataExtractor():
    def __init__(self):
        {}
    def openandextractdataimage(self,file_name):

        df = pd.read_csv(file_name,header=None,error_bad_lines=False)
        df2=pd.DataFrame(columns=['Imageid','Term','TF','DF','TFIDF'])
        count=0
        for column in df:
            for row in df[column]:
                array = row.split(' ')
                length = (int)(len(array)/19)
                for i in range(2,length,4):
                     df2.loc[count,'Imageid']=array[0]
                     df2.loc[count,'Term']=array[i-1]
                     df2.loc[count,'TF']=array[i]
                     df2.loc[count,'DF']=array[i+1]
                     df2.loc[count,'TFIDF']=array[i+2]
                     count+=1

        return df2


    # def openandextractdataimage(self, file_name):
    #     df = pd.read_csv(file_name, header=None, error_bad_lines=False, sep=" ")
    #     df2 = pd.DataFrame(columns=['Imageid', 'Term', 'TF', 'DF', 'TFIDF'])
    #
    #     count = 0
    #     for index, row in df.iterrows():
    #         for i in range(1, len(row), 4):
    #             if not isinstance(row[i], str) and math.isnan(row[i]):
    #                 break
    #
    #             df2.loc[count, 'Imageid'] = row[0]
    #             df2.loc[count, 'Term'] = row[i]
    #             df2.loc[count, 'TF'] = row[i + 1]
    #             df2.loc[count, 'DF'] = row[i + 2]
    #             df2.loc[count, 'TFIDF'] = row[i + 3]
    #             count += 1
    #
    #     return df2


if __name__ == "__main__":
    extractdata = DataExtractor()
    location="C:\\Users\\arpan\\Documents\\ASU\\devset_textTermsPerImage.txt"
    # location = input("Enter directory location with file path:(with double slashes)")
    df = extractdata.openandextractdataimage(location)
    print(df)
