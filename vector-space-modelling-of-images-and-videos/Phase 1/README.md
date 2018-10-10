# Vector space modeling of images and video data - Phase 1

#### Introduction:
The tasks involve representing relationships between different entities of the data set given by “B. Ionescu, A. Popescu, M. Lupu, A.L. Ginsca, H. Muller, Retrieving Diverse Social Images at MediaEval 2014: Challenge, Dataset and Evaluation, MediaEval Benchmarking Initiative for Multimedia Evaluation, vol. 1263, CEUR-WS.org, ISSN: 1613-0073, October 1617, Barcelona, Spain, 2014.”. The data set contains information pertaining to images, videos and users associated through text files.

#### Software requirements:
Python 3.6 (64 bit) :: Anaconda 5.2 (64-bit) 

#### Directory Structure:
The project directory structure has the following directories:
	
	1. "resources" - contains the text files that constitute the data set. 
	2. "scripts" - contains supporting scripts needed for the successful execution of the project.

#### Execution Steps:
```
Task 1:
Files: extractinfo.py, calculatedistances.py

Task 2:
Files: extractinfoimage.py, calculatedistanceimage.py

Task 3:
Files: extractinfolocation.py, calculatedistancelocation.py

Task 4:
Files: extract and calculate task 4

Task 5:
Files: extract and calculate task 5

```

#### Troubleshooting:
1. The k most similar users/images/locations are displayed dynamically whenever the input is asked from the user. Also, this project uses in-memory data frames (via python pandas library) for storage and retrieval. You may observe delay due to large amount of data being parsed at the interface based on the input. Please be patient.
2. Please ensure the data set (text files) have the same names and column descriptors as the sample data set for correct execution.
3. Ensure you are running the correct python interpreter. The correct interpreter will give the following output on the command line:
	python --version
	Python 3.6 (64 bit) :: Anaconda 5.2 (64-bit)
