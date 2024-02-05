import pathlib
import os
import numpy as np
import rasterio

import pandas as pd

#root = pathlib.Path(__file__).parent

MEDIAN = rasterio.open(r'C:\Users\user\Desktop\Thesis\VsProfiles\Willis15_Vs30_model\data\California_vs30_Wills15_hybrid_7p5c.tif')
STD = rasterio.open(r'C:\Users\user\Desktop\Thesis\VsProfiles\Willis15_Vs30_model\data/California_vs30_Wills15_hybrid_7p5c_sd.tif')


def lookup(lonlats):
    return (
        np.fromiter(MEDIAN.sample(lonlats, 1), np.float),
        np.fromiter(STD.sample(lonlats, 1), np.float)
    )


def test_lookup():
    medians, stds = list(lookup([(-122.258, 37.875), (-122.295, 37.895)]))

    np.testing.assert_allclose(medians, [733.4, 351.9], rtol=0.01)
    np.testing.assert_allclose(stds, [0.432, 0.219], rtol=0.01)
    
    
fname_latlon = r'C:\Users\user\Desktop\Thesis\VsProfiles\New Datasets\New_sections\input_RedBox_longitudinal.csv'
data_latlon = pd.read_csv(fname_latlon, header=None)
npt = len(data_latlon)

#initialize Vs30med, Vs30sigma
data_latlon['Vs30med'] = [np.nan]*npt
data_latlon['Vs30sig'] = [np.nan]*npt
data_latlon = data_latlon.copy(deep=False)

for k, pt_info in enumerate(data_latlon.iterrows()):

    pt_lonlat = [(pt_info[1][0], pt_info[1][1])]
    vs30med, vs30sig = lookup(pt_lonlat)
    
    data_latlon['Vs30med'][k] = vs30med
    data_latlon['Vs30sig'][k] = vs30sig
    
data_latlon.to_csv(os.path.join(r"C:\Users\user\Desktop\Thesis\VsProfiles\New Datasets\New_sections\longitudinal_section_new.csv"), sep=",", index = False, index_label= False)

    
