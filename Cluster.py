
import pandas as pd
from ydata_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df= pd.read_excel("Retail.xlsx")

x=df.iloc[:,[0,6]].values

# For Clustering................. 
wcss=[]
for i in range (1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

#training the kmeans clustering model.................
kmeans=KMeans(n_clusters=8,init='k-means++',random_state=0)
y=kmeans.fit_predict(x)
print(y)
    
#Show the point 
plt.figure(figsize=(20,10))
plt.scatter(x[y==0,0],x[y==0,1],s=50,c='green',label='Cluster 1')
plt.scatter(x[y==1,0],x[y==1,1],s=50,c='yellow',label='Cluster 2')
plt.scatter(x[y==2,0],x[y==2,1],s=50,c='red',label='Cluster 3')
plt.scatter(x[y==3,0],x[y==3,1],s=50,c='blue',label='Cluster 4')
plt.scatter(x[y==4,0],x[y==4,1],s=50,c='black',label='Cluster 5')
plt.scatter(x[y==5,0],x[y==5,1],s=50,c='violet',label='Cluster 6')
plt.scatter(x[y==6,0],x[y==6,1],s=50,c='purple',label='Cluster 7')
plt.scatter(x[y==7,0],x[y==7,1],s=50,c='maroon',label='Cluster 8')

#plt.scatter(kmeans.cluster_centers_[:0],kmeans.cluster_centers_[:1], s=100, c='cyan', label='Centroids')

plt.title("Show The Retail Data")
plt.xlabel("Invoice No.")
plt.ylabel("Customer Id")
plt.show()





