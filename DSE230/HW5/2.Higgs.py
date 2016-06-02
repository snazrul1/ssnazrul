# Name: Syed Sadat Nazrul
# Email: ssnazrul@eng.ucsd.edu
# PID: A09771598
from pyspark import SparkContext
sc = SparkContext()

# coding: utf-8

# In[1]:

from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint

from string import split,strip

from pyspark.mllib.tree import GradientBoostedTrees, GradientBoostedTreesModel
from pyspark.mllib.tree import RandomForest, RandomForestModel

from pyspark.mllib.util import MLUtils


# ### Higgs data set
# * **URL:** http://archive.ics.uci.edu/ml/datasets/HIGGS#  
# * **Abstract:** This is a classification problem to distinguish between a signal process which produces Higgs bosons and a background process which does not.
# 
# **Data Set Information:**  
# The data has been produced using Monte Carlo simulations. The first 21 features (columns 2-22) are kinematic properties measured by the particle detectors in the accelerator. The last seven features are functions of the first 21 features; these are high-level features derived by physicists to help discriminate between the two classes. There is an interest in using deep learning methods to obviate the need for physicists to manually develop such features. Benchmark results using Bayesian Decision Trees from a standard physics package and 5-layer neural networks are presented in the original paper. The last 500,000 examples are used as a test set.
# 
# 


# In[3]:

# ### As done in previous notebook, create RDDs from raw data and build Gradient boosting and Random forests models. Consider doing 10% sampling since the dataset is too big for your local machine

# In[4]:

# Read the file into an RDD
# If doing this on a real cluster, you need the file to be available on all nodes, ideally in HDFS.
path='/HIGGS/HIGGS.csv'
inputRDD=sc.textFile(path)
# inputRDD.first()


# In[5]:

Data=inputRDD.map(lambda line: [float(strip(x)) for x in line.split(',')])     .map(lambda line: LabeledPoint(line[0], line[1:]))
# Data.first()


# ###Reducing data size
# In order to see the effects of overfitting more clearly, we reduce the size of the data by a factor of 100

# In[6]:

Data1=Data.sample(False,0.1, seed=255).cache()
(trainingData,testData)=Data1.randomSplit([0.7,0.3],seed=255)


# ###Gradient Boosted Trees

# In[7]:

from time import time
errors={}
for depth in [10]:
    model=GradientBoostedTrees.trainClassifier(Data1,
                                             categoricalFeaturesInfo={}, numIterations=10,
					     maxDepth=depth, learningRate=0.25, maxBins=35)
    #print model.toDebugString()
    errors[depth]={}
    dataSets={'train':trainingData,'test':testData}
    for name in dataSets.keys():  # Calculate errors on train and test sets
        data=dataSets[name]
        Predicted=model.predict(data.map(lambda x: x.features))
        LabelsAndPredictions=data.map(lambda lp: lp.label).zip(Predicted)
        Err = LabelsAndPredictions.filter(lambda (v,p):v != p).count()/float(data.count())
        errors[depth][name]=Err
    print depth,errors[depth]


# In[ ]:



