import subprocess
import pandas as pd
import numpy as np
import os

data=pd.read_csv("/home/user/Downloads/cross_section_longitudinal_new.csv", names=['Ind', 'Lon', 'Lat'])
data["Lat"] = data["Lat"].astype('float')
data["Lon"] = data["Lon"].astype('float')

data=pd.read_csv("/home/user/Downloads/input_RedBox.csv", dtype='str', header=None,names=['Lon', 'Lat'])
data["Lat"] = data["Lat"].astype('float')
data["Lon"] = data["Lon"].astype('float')

os.chdir('/home/user/geomodelgrids/geomodelgrids-1.0.0rc2-Linux_x86_64')

no_data=[]
for i in range(len(data)):
    a=subprocess.run('source /home/user/geomodelgrids/geomodelgrids-1.0.0rc2-Linux_x86_64/setup.sh; geomodelgrids_borehole --models=/home/user/geomodelgrids/geomodelgrids-1.0.0rc2-Linux_x86_64/src/tests/data/USGS.h5  --location=%f,%f --max-depth=1000 --dz=1 --output=./longitudinal_section/%s.out --values=Vs' %(data.Lat[i],data.Lon[i],str(data.Ind[i])),
                   shell=True, executable='/bin/bash', universal_newlines=True)
    if a.returncode!=0:
        no_data.append([i, str([i])])
        
a=subprocess.run('source /home/user/geomodelgrids/geomodelgrids-1.0.0rc2-Linux_x86_64/setup.sh; geomodelgrids_borehole --models=/home/user/geomodelgrids/geomodelgrids-1.0.0rc2-Linux_x86_64/src/tests/data/USGS.h5  --location=37.330560,-122.082500 --max-depth=1000 --dz=0.5 --output=./Profile_MAR.out --values=Vs', shell=True, executable='/bin/bash', universal_newlines=True)
