# cichlid-tracking
Package for recording and tracking. This only works for Windows not Mac computers

Download python 3.7 for Windows from  website (Spinnaker only currently supports up to 3.7)
Python-3.7.6-amd64.exe
https://www.python.org/downloads/

Make sure to add Python 3.7 to Path
e.g. C:\Users\nichol0000\AppData\Local\Programs\Python\Python37![image](https://user-images.githubusercontent.com/6535283/205022707-6b1efd33-df01-44bc-85fe-e39f4a00c8ce.png)

Clone this package (cichlid-tracking), open in PyCharm. Set the python interpreter as the venv environment of this project. 

Install all packages with pip, except for PySpin which needs to be installed by a whl.

Pyspin is the FLIR Library.

First you need to instal Spinnaker:
https://flir.app.boxcn.net/v/SpinnakerSDK/folder/109034499134?page=2
Download:
SpinnakerSDK_FULL_1.27.0.48_x64.exe
and
spinnaker_python-1.27.0.48-cp37-cp37m-win_amd64

Follow the instructions to install SpinnakerSDK_FULL_1.27.0.48_x64.exe 

Then install the PySpin package from the whl in the command prompt (use the spinnaker_python-1.27.0.48-cp37-cp37m-win_amd64 README.txt)
e.g.:
python -m pip install H:\Desktop\spinnaker_python-1.27.0.48-cp37-cp37m-win_amd64\spinnaker_python-1.27.0.48-cp37-cp37m-win_amd64.whl
