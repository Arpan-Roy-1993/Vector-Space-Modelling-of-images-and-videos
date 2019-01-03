PHASE II CSE 515
==================


This phase requires installation of MongoDB and Python.
Preprocessing of the devset and storing in it in the mongo database for easy access


SETUP
========


MongoDB installation version v4.0.2


  - Visit hhttps://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
  - Download and install mongoDB community edition.
  - Run command prompt as administartor and create data directory in the absolute path \data\db on the system
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
                python -m pip install tensorly
                python -m pip install scikit-learn
		python -m pip install scipy
		python -m pip install OrderedDict


Python is installed successfully
Task 1 and 2 has been implemented using Anaconda 5.2 with Python 3.6 on the JetBrains PyCharm IDE.  
      At the IDE (Run the respective programs:  task 1: = extractinfo.py and phase 2 task 1.py task 2= extractinfoimage.py and phase 2 task 2.py)  


Preprocessing for task 1 and 2
==========================================================
Task 1 and 2 require the following files to be present as well.(need not be run) 
 
Task 1: extract_info.py phase 2 task 1.py 
Task 2: extractinfoimage.py  phase 2 task 2.py
 
IMPORTANT: For the file “devset_textTermsPerPOI.wFolderNames”, Please remove  commas(,) placed in double quoted strings. Using “Find and Replace”, replace all   “,”    with nothing and then run the the programs.  




Prepocessing of the given dataset and storing it in MongoDB
===========================================================


- Download given dataset
- Extract 'desctxt', 'descvis' folders


To store the data to mongodb, run the below python scripts
----------------------------------------------------------


- Open command prompt and navigate to the location of the python scripts
-  Execute the following commands
        python transform_users.py - Enter the filepath of the extracted file 'devset_textTermsPerUser' C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_textTermsPerUser.txt
        python transform_images.py -Enter the filepath of the extracted file 'devset_textTermsPerImage' C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_textTermsPerImage.txt
        python transform_locations.py 
                -Enter devset_topics file path C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_topics.xml
                -Enter devset_textTermsPerPOI.wFolderNames file path C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_textTermsPerPOI.wFolderNames.txt
        python transform_task4.py  
                -Enter devset_topics file path C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_topics.xml
                -Enter directory of the location of img folder in descvis extracted file C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\descvis\descvis\img
All the data is stored in monogdb






To run the python scripts for the seven tasks
=====================================================


- Open command prompt and navigate to the location of the python scripts
- Execute the following commands
        python task1.py - Runs the task one 
        python task2.py - Runs the task two
        python task3.py <k> <model> <reduction_algorithm> <imageid> - Runs the task three
        python task4.py - Runs the task four
        python task5.py - Runs the task five
        python task6.py - Runs the task six
        python create_tensor - Creates a tensor and stores it locally
        python task7.py - Runs the task seven