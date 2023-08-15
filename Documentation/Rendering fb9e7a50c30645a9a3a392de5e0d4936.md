# Rendering

Rendering is the process of creating an image from a 3D model. The model will contain features such as textures, shading, shadows, lighting, and viewpoints, and the role of the rendering engine is to process these features to create a realistic image.

Three common types of rendering algorithms are rasterization, which projects objects geometrically based on information in the model, without optical effects; ray casting, which calculates an image from a specific point of view using basic optical laws of reflection; and ray tracing, which uses Monte Carlo techniques to achieve a realistic image in a far shorter time. Ray tracing is used to improve rendering performance in NVIDIA GPUs.

![Untitled](Rendering%20fb9e7a50c30645a9a3a392de5e0d4936/Untitled.png)

[Neural Radiance Field (NeRF): A Gentle Introduction](https://datagen.tech/guides/synthetic-data/neural-radiance-field-nerf/#:~:text=A%20neural%20radiance%20field%20(NeRF,input%20views%20of%20a%20scene.)