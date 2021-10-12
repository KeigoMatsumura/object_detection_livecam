## Installation

### Requirements
The code in this repository requires Python 3.7.6. I advise you to run the code inside an Anaconda environment:

```
conda create -n od-livecam python=3.7.6
conda activate od-livecam
```

Next, clone the repository and install the requirements:

```
cd $HOME
git clone https://github.com/KeigoMatsumura/object_detection_simplified.git
cd object_detection_livecam
pip install -r requirements.txt
pip install git+https://github.com/AmbientDataInc/ambient-python-lib.git
```
### Model
The model used in this repo can be downloaded as follows:
```
mkdir models
cd models/
wget https://github.com/fizyr/keras-retinanet/releases/download/0.5.1/resnet50_coco_best_v2.1.0.h5
```
