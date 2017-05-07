# LabExplatoryWork
**Objectives:** 

1)Determine underlying research themes in scientific literature   
2)Create a model for predicting how these research themes will evolve over time 

**Task 1: Convergence and Divergence of Topics in Scientific Literature**
***Input:*** ArXiv Papers in High Energy Physics (KDD 2003 Dataset)
	This dataset contains abstracts from 1992-2003 in LaTeX. (hep-Th)

***Output:*** Topic clusters per period (period = 2 years)
**To do:**
Extract relevant entities (usually nouns)  from each paper using Part of Speech Tagging (NLTK POS Tagger). These entities will comprise the vocabulary of this corpus. 
Extract word2vec representation (CBOW architecture) for the words in the vocabulary for a given period. For each period, there would be a different set of word vectors. Word2Vec extraction can be done using Gensim. (Just use the default parameters)
Perform clustering (K-means or DBSCan) on the word vectors per period. 
***K-means:*** determine the right k 
***DBScan:*** determine the right parameters 
You can tell how good a clustering is based on silhouette coefficient; Tweak parameters until silhouette coefficient is maximized.


**Task 1: Convergence and Divergence of Topics in Scientific Literature**

**For clusters of size >= n:**
M1: Determine the diameter (maximum distance between points  in the cluster)
M2: Determine the average distance between points in the cluster
Experiment between cosine similarity or euclidean distance as distance metrics for M1 and M2 
M3: Calculate the centroid of each topic cluster
Create an intercluster distance matrix for a given period. 

**Task 1: Convergence and Divergence of Topics in Scientific Literature**
Given our initial set of clusters from Period 1(1992 - 1993), we need to find their corresponding clusters in the subsequent periods (Period 2: 1994-1995, Period 3: 1996-1997.. and so on). We do the matching based on normalized mutual information. 

For example, if NMI(Cluster 1 in Period 1, Cluster 3 in Period 2) > ϴ, then they are matching clusters. Some clusters from Period n may not have any match in Period n+1. In this case, these clusters have dissolved. Meanwhile, clusters in Period n+1 that do not have any match from Period n are newborn clusters. Experiment on the value of ϴ. 

We are only concerned with clusters that are persistent over time. 

**DETECTING CONVERGENCE**

Convergence occurs when the intercluster distance between 2 clusters decrease over time. 

**DETECTING DIVERGENCE**

Divergence occurs when the diameter and/or the average distance between points of a topic cluster increases over time. 
