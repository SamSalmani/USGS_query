import os
import pandas as pd
import numpy as np

data=pd.read_excel("/home/user/Downloads/LatLon.xlsx", dtype='str')
data["Lat"] = data["Lat"].astype('float128')
data["Lon"] = data["Lon"].astype('float128')

fpath = r"geomodelgrids/geomodelgrids-1.0.0rc2-Linux_x86_64/src/tests/data"

os.chdir(fpath)
for i in range(len(data)):
    a = os.system(r"geomodelgrids/geomodelgrids-1.0.0rc2-Linux_x86_64/bin/geomodelgrids_borehole --models=USGS.h5  --location=%f,%f --max-depth=2000 --dz=100 --output=USGS/%s.out --values=Vs" %(data.Lat[i],data.Lon[i],str(data.Linux_name[i])))
    if a!=0:
        print(i,str(data.Linux_name[i]))
        
a=os.listdir(os.path.join(os.getcwd()+"/USGS"))
pd.DataFrame(a).to_excel("a.xlsx")

m=[]
n=[]
for j in range(len(data)):
    n.append(str(data.Linux_name[j]))
    for k in range(len(a)):
        if str(data.Linux_name[j]) == str(a[k][0:-4]):
            m.append(str(a[k][0:-4]))
        
b = list(set([str(data.Linux_name)])-set(m))
c= np.setdiff1d(n,m)
