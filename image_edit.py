from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from kneed import KneeLocator

#Loading image
def load_img(path):
   image = Image.open(path)
   return image

#Finding optimal k
def optimal_k(t,range_k):

    distortions=[]

    for k in range_k:
      kmeans= KMeans(n_clusters=k)
      kmeans.fit(t)
      distortions.append(kmeans.inertia_)

    plt.figure(figsize=(10, 5))
    plt.plot(range_k, distortions, marker='o', label="Inertia (WCSS)")
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Inertia (WCSS)')
    plt.title('Optimal "k" Elbow Method')
    plt.savefig('elbow.png', dpi=300,  bbox_inches='tight')
    plt.show()

    kl = KneeLocator(range_k, distortions, curve="convex", direction="decreasing")
    #print(kmeans.cluster_centers_)
    #print(kmeans.labels_)
    return kl.elbow


def compress_img(img,k,img_array):
   kmeans = KMeans(n_clusters=k)
   kmeans.fit(img)

   cluster_centers = kmeans.cluster_centers_.astype('uint8')
   labels = kmeans.labels_
   #print(cluster_centers)
   #print(labels)

   compressed_img=cluster_centers[labels]
   compressed_img=compressed_img.reshape(img_array.shape)
   Image.fromarray(compressed_img).save("img1_done.png")
   return cluster_centers


def transform_img(img_flattened,img_array,cluster_centers):
   knn = KNeighborsClassifier(n_neighbors=1)
   knn.fit(cluster_centers,np.arange(len(cluster_centers)))

   labels=knn.predict(img_flattened)
   #print(labels)
   compressed_img = cluster_centers[labels]
   #print(img_array.shape)
   #print(compressed_img)
   compressed_img=compressed_img.reshape(img_array.shape)
   Image.fromarray(compressed_img).save("img2_done.png")
   return compressed_img



#Loading image 
img1=load_img("img1.png")
img2=load_img("img2.png")

#converting image to np array
img1_arr=np.array(img1)
img2_arr=np.array(img2)
#print(img1_arr)

#flattening the array
img1_flattened = img1_arr.reshape(-1,3)
img2_flattened = img2_arr.reshape(-1,3)
#print(img1_flattened)
#print(tensor1_reshaped) 

#finding optimal k through kneed package
ideal_k=optimal_k(img1_flattened,range(2,30))
print(f'The elbow for the graph is at k={ideal_k}')
#print(f'But for more vividty of the compression, we use the point where the graph is almost starting to tend to zero.')

#compress image1.png
cluster_centers=compress_img(img1_flattened,ideal_k,img1_arr)

#transform image2.png
transform_img(img2_flattened,img2_arr,cluster_centers)






