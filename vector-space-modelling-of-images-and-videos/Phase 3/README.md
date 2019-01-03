PHASE III CSE 515
==================

This phase requires installation of MongoDB and Python.
Preprocessing of the devset and storing in it in the mongo database for easy access

SETUP
========

MongoDB installation version v4.0.2

  - Visit https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
  - Download and install mongoDB community edition.
  - Run command prompt as administrator and create data directory in the absolute path \data\db on the system
        "C:\Program Files\MongoDB\Server\4.0\bin\mongod.exe" --dbpath="c:\data\db"
  - Navigate to the path where mongodb is installed
  - Execute mongod.exe "C:\Program Files\MongoDB\Server\4.0\bin\mongod.exe" - this will connect you to the mongodb server
  - Execute mongo.exe
MongoDB is installed


Python installation version 3.7
  
   - Visit https://www.python.org/downloads/ and download and run the Python 3.7.0 for 64-bit
   - Add the file path of the installed python to the system environment variable path - C:\Users\Local\Programs\Python\Python37-32
   - Open command line and navigate to the location of where the python scripts are stored
   - Execute python -m pip install -U pip - Upgrade or install pip
   - Execute the following commands to install modules
                python -m pip install pymongo
                python -m pip install numpy
                python -m pip install scikit-learn
            python -m pip install scipy
            python -m pip install flask


Python is installed successfully



Preprocessing of the given dataset and storing it in MongoDB
===========================================================


- Download given dataset
- Extract 'desctxt', 'descvis' folders




To store the data to mongodb, run the below python scripts
----------------------------------------------------------




- Open command prompt and navigate to the location of the python scripts
-  Execute the following commands
                python transform_images.py -Enter the filepath of the extracted file 'devset_textTermsPerImage' C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_textTermsPerImage.txt
        python transform_locations.py 
                -Enter devset_topics file path C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_topics.xml
                -Enter devset_textTermsPerPOI.wFolderNames file path C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_textTermsPerPOI.wFolderNames.txt
        python transform_task4.py  
                -Enter devset_topics file path C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_topics.xml
                -Enter directory of the location of img folder in descvis extracted file C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\descvis\descvis\img
All the data is stored in monogdb


To run the python scripts for tasks
=====================================================




- Open command prompt and navigate to the location of the python scripts
- Execute the following commands


Task1:  python task1.py
Enter the value of k 
------------------------------------------------------------------------------------------------
Task2:  python task2.py 
Enter 1 for K means and 2 for spectral clustering
Enter the value of k
The output will be displayed on the webpage (http://127.0.0.1:5000/)

Task3:  python task3.py 
Enter the value of k
The output will be displayed on the webpage (http://127.0.0.1:5000/)

Task4:  python task4.py 
Enter the image ids
Enter the value of k
The output will be displayed on the webpage (http://127.0.0.1:5000/)

Task5:
A) python task5a.py <L> <K>
Creates LSH_index and LSH_bucket files which store the LSH index structure.

B) python task5b.py <query imageID> <T>
The output will be displayed on the webpage (http://127.0.0.1:5000/) 
Image IDs will also be displayed on the terminal along with the number of total unique candidates considered.

Task6:  
A)      python 6a.py
The output will be displayed on the webpage (http://127.0.0.1:5000/)


B)      python 6b.py
The output will be displayed on the webpage (http://127.0.0.1:5000/)


------------------------------------------------------------------------------------------------


Visualization
------------------------------
Copy all the images from all the locations(devset and testset) to a folder named ‘static’ where all the python files are present
