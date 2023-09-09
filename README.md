# Thesis-NeRFs 🧩

##  Denoising 3D TEM tomography via Advanced Neural Radiance Fields(NeRF) 
#### Most Important paper for TEM -> [NerfMM](https://nerfmm.active.vision./) 📔 




## Usefull commands 👽

**Linux 🤸**
1. Cude Version `nvidia-smi` // 11.8
2. Python Version `python3 --version` // 3.8.15
3. Clear cmd `reset` 
4. Conda path setup [path](https://askubuntu.com/questions/849470/how-do-i-activate-a-conda-environment-in-my-bashrc)
5. ubuntu architecture `uname -m` // x86_64
6. ubunty version and machine id `hostnamectl`
7. nvcc version `nvcc -V`
8. to find or locate file `locate {nvcc}`
9. pytorch -v `pip3 show torch` // 1.12.1+cu113
10. linux background proccessing `htop`
11. Kill VS code server `Remote-SSH: kill VS Code Server on Host` [Documentation](https://github.com/microsoft/vscode-remote-release/issues/4307)
12. Installing stuff without `sudo` [Documentation](https://askubuntu.com/questions/339/how-can-i-install-a-package-without-root-access) 
13. Extract file `tar -xvf cmake-3.x.x.tar.gz`
14. Debian-based Linux Destribution: `cat /etc/os-release`
15. Change GPU `export CUDA_VISIBLE_DEVICES=1`
16. For building CMAKE `cmake . -B build -DCMAKE_CUDA_COMPILER:STRING="/usr/local/cuda-11.8/bin/nvcc"`

#### [NeRFstudio Documentation](https://docs.nerf.studio/en/latest/quickstart/installation.html) 📄 
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
4. Jupyter notebook password [setup](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)
5. Remove env `conda env remove -n ENV_NAME`
6. Remove all env `conda remove --name myenv --all`
7. Env list `conda env list`


## Usefull tools for Literature Review 🛠️

1. It provides an overview of any article and all related research with the assistance of AI -> [Paper Digest](https://www.paperdigest.org/review/). 
2. The AI Research Assistant -> [Elicit](https://elicit.org/)
3. An app that visualizes all of the related papers for a specific paper -> [Litmap](https://www.litmaps.com/)
4. Similar to Litmap, but using a different linked paper visualization website-> [Connected paper](https://www.connectedpapers.com/)
5. For improved writing efficiency -> [Writefull](https://www.writefull.com/)
6. For creating custom vectors or biologically themed graphics -> [Bio render](https://biorender.com/)
7. Similarly, litmap and connected paper provide another option -> [scite](https://scite.ai/)
8. Reference Manager -> [Zotero](https://www.zotero.org/)
9. Alternative Reference Manager -> [Mandele](https://www.mendeley.com/?interaction_required=true)
