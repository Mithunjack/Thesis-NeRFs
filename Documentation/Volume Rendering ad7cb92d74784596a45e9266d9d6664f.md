# Volume Rendering

Volume rendering enables you to create a 2D projection of a 3D discretely sampled dataset.

For a given camera position, a volume rendering algorithm obtains the RGBα (Red, Green, Blue, and Alpha channel) for every voxels in the space through which rays from the camera are casted.  The RGBα color is converted to an RGB color and recorded in the corresponding pixel of the 2D image. The process is repeated for every pixel until the entire 2D image is rendered.

![Untitled](Volume%20Rendering%20ad7cb92d74784596a45e9266d9d6664f/Untitled.png)

[Neural Radiance Field (NeRF): A Gentle Introduction](https://datagen.tech/guides/synthetic-data/neural-radiance-field-nerf/)