import logging
import os
import pandas as pd
import io
import math

#class to extract data from file and enter into a dataframe
class DataExtractor():
    def __init__(self):
        {}
    # def openandextractdata(self,file_name):
    # #Parsing each row in an array and assigning to a new dataframe
    #     df = pd.read_csv(file_name,header=None,error_bad_lines=False)
    #     df2=pd.DataFrame(columns=['Userid','Term','TF','DF','TFIDF'])
    #     count=0
    #     for column in df:
    #         for row in df[column]:
    #             array = row.split(' ')
    #             length = (int)(len(array)/5)
    #             for i in range(2,length,4):
    #                  df2.loc[count,'Userid']=array[0]
    #                  df2.loc[count,'Term']=array[i-1]
    #                  df2.loc[count,'TF']=array[i]
    #                  df2.loc[count,'DF']=array[i+1]
    #                  df2.loc[count,'TFIDF']=array[i+2]
    #                  count+=1
    #
    #     return df2

    def openandextractdata(self, file_name):
        file_outputuser=open("useroutputfile.txt","w",encoding="utf8")
        file_user=open("C:\\ASU\\MWDB\\Project\\phase2_testdata\\devset\\desctxt\\devset_textTermsPerUser.txt",encoding="utf8")
        for line in file_user:
	        line = line.rstrip()
	        data     = line.split(" ")
	        userid   = data[0]
	        data     = data[1:]
	        no_terms = len(data)/4        # no. of terms for each userid
	        index    = 0
	        while index < no_terms:
		        term_data  = data[4 * index: (4 * index)+4]
		        term_data  = ','.join(term_data)
		        write_data = userid + ',' + term_data + '\n'
		        file_outputuser.write(write_data)
		        index = index + 1
        file_outputuser.close()
        file_outputuser=open("useroutputfile.txt","r",encoding="utf8")
        df = pd.read_csv(file_outputuser, header=None, error_bad_lines=False, sep=",")
        df.columns = ['Userid', 'Term', 'TF', 'DF', 'TFIDF']
        return df
if __name__ == "__main__":

    extractdata= DataExtractor()
    location="C:\\ASU\\MWDB\\Project\\phase2_testdata\\devset\\desctxt\\devset_textTermsPerUser.txt"
    df=extractdata.openandextractdata(location)
    print(df)
