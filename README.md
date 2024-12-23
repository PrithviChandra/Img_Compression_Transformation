# Img_Compression_Transformation
Image compression and transformation using K-Means and KNN algorithms 

This project shows how KMeans and KNN algorithm can be used to compress and transform images based on the RGB distribution. We use KMeans to cluster the given image into similar clusters of k numbers, the value for which is found using the Elbow method. After finding the ideal k, we use KMeans to group the original RGB values to the closest RGB vale in the k values. This way we compress the image by reducing the pixel distribution. Using the associated k centroids, we try to cluster the pixels in the second image to the k clusters thereby transforming the image.

The elbow graph:
![image](https://github.com/user-attachments/assets/017a9dca-1148-4005-bfe3-16d3b41e6c72)
<img src="img2.png" alt="Image 1" width="300">

Original image 1:
![image](https://github.com/user-attachments/assets/63df61d3-0b73-4dff-8136-f003b039701e)

After compressing to k pixel values:
![image](https://github.com/user-attachments/assets/e668259d-e905-4788-b11b-1425a9fc4e9c)

Original image 2:
![image](https://github.com/user-attachments/assets/47e2216d-29a7-4d82-8131-29ab46babd82)

After transforming image 2 based on the k centroids: 
![image](https://github.com/user-attachments/assets/1ada1e04-0a06-4da9-9878-aece78507d61)



