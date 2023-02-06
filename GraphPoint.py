import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df= pd.read_excel("Retail.xlsx")
df.info()
df.isnull().sum()

x=df.iloc[:,[0,6]].values

print(x)

# For Clustering 
wcss=[]
for i in range (1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
#for show the graph
sns.set()
plt.plot(range(1,11),wcss)
plt.title('Graph of Retail')
plt.xlabel('Number of Cluster')
plt.ylabel('Data Point')
plt.show()
