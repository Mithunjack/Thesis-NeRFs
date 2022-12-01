# Thesis-NeRFs 🖼️

## NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis 😱
#### [Paper]( https://arxiv.org/pdf/2003.08934.pdf) 📔 
#### [NeRFstudio Documentation](https://docs.nerf.studio/en/latest/quickstart/installation.html) 📄 




## Usefull commands 👽

**Linux 🤸**
1. Cude Version `nvidia-smi` // 11.8
2. Python Version `python3 --version` // 3.9.13
3. Clear cmd `reset` 
4. Conda path setup [path](https://askubuntu.com/questions/849470/how-do-i-activate-a-conda-environment-in-my-bashrc)
5. ubuntu architecture `uname -m` // x86_64
6. ubunty version and machine id `hostnamectl`
7. nvcc version `nvcc -V`
8. to find or locate file `locate {nvcc}`
9. pytorch -v // 1.12.1+cu113
10.linux background proccessing `htop`


**NerfStudio ✈️**
1. check available model `ns-train --help`
2. torch version check in anaconda `pip3 show torch`
3. With a specified websocket port `ns-train nerfacto --vis viewer --viewer.websocket-port=7008`
4. Resume training from one certain point `ns-train nerfacto --data data/nerfstudio/poster --trainer.load-dir {outputs/.../nerfstudio_models}`
5. Pre processing custom data `ns-process-data images --data data/custom_data --output-dir outputs/custom_data_preprocessed --no-gpu`

**Anaconda 🐍**
1. Creating conda env `conda create --name nerfstudio -y python=3.8`
2. Activate env `conda activate nerfstudio`
3. active env `conda info -e`

