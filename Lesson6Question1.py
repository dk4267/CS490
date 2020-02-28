import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import preprocessing

#read in data set
dataset = pd.read_csv('CC.csv')
xdata = dataset.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
# ydata = dataset.iloc[:, -1]

#handle null values
newx = xdata.apply(lambda x: x.fillna(x.mean()), axis=0)

#elbow method to find optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(newx)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()
#optimal number of clusters is 5 or 6 - use 6

#build kmeans model
from sklearn.cluster import KMeans
nclusters = 6
km = KMeans(n_clusters=nclusters)
km.fit(newx)

# calculate silhouette score
y_cluster_kmeans = km.predict(newx)
from sklearn import metrics
score = metrics.silhouette_score(newx, y_cluster_kmeans)
print('Silhouette score: ' + str(score))

#feature scaling
scaler = preprocessing.StandardScaler()
scaler.fit(newx)
X_scaled_array = scaler.transform(newx)
X_scaled = pd.DataFrame(X_scaled_array, columns=newx.columns)

#kmeans after feature scaling
km2 = KMeans(n_clusters=nclusters)
km2.fit(X_scaled)

#silhouette score after feature scaling
y_cluster_kmeans2 = km2.predict(X_scaled_array)
score = metrics.silhouette_score(X_scaled_array, y_cluster_kmeans2)
print('Silhouette score after feature scaling: ' + str(score))
#score actually decreased

#PCA
pca = PCA(2)
X_pca = pca.fit_transform(X_scaled_array)

#kmeans after PCA
km3 = KMeans(n_clusters=nclusters)
km3.fit(X_pca)

#silhouette score after PCA
y_cluster_kmeans3 = km3.predict(X_pca)
score = metrics.silhouette_score(X_pca, y_cluster_kmeans3)
print('Silhouette score after PCA: ' + str(score))
#better score than the previous 2
