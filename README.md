
<h1>
MRI image to image translation
</h1>

## Description
<p>
CINE segmented images to target images translation
</p>

## Setup 
Get the code by either cloning this repository using git
>git@github.com:wiki-yu/MRI-img-to-img-translation.git

Open a new terminal window in the the root folder.

### Build virtual enviroment:

_For Windows:_

```bash
py -m venv env # Only run this if env folder does not exist
.\env\Scripts\activate
pip install -r requirements.txt
```

_For MacOS/Linux:_

```bash
python3 -m venv env # Only run this if env folder does not exist
source env/bin/activate
pip install -r requirements.txt
```
## Data
Put all the input**.npy files under the folder data/train/input-imgs
Put all the label**.npy files under the folder data/train/target-imgs

## Demo
### 
```
python main.py
```

```










