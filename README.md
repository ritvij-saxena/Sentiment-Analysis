#Sentinment Analysis Project

The main goals are to:
1. **Collect** raw data from some online social networking site (Twitter, Facebook, Reddit, Instagram, etc.)
2. Perform **community detection** to cluster users into communities.
3. Perform **supervised classification** to annotate messages and/or users according to some criterion. Manual Labelling can be done
4. Analyze the results and **summarize** your conclusions.

- `collect.py`: This file collects data used for analysis. 
- `cluster.py`: This file reads the data collected in the previous step and uses any Girvan Newman community detection algorithm to cluster users into communities.
- `classify.py`: This file classifies the data by sentiment. You can use a labelled data file to perform supervised learning.
- `summarize.py`: This file reads the output of the previous methods and writes it to a text file called `summary.txt` containing the following entries:
  - Number of users collected:
  - Number of messages collected:
  - Number of communities discovered:
  - Average number of users per community:
  - Number of instances per class found:
  - One example from each class:

'description.txt' contains a brief summary of what the code does and the conclusions.
