import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
datadir="/Users/suhaniagarwal/Desktop/ilgc_website_2/Map Maker/Maps"
rgb_files = sorted(os.listdir(datadir))

rgb_files.pop(0)
print(rgb_files)

for file in rgb_files:
    p=file.split('.')
    print('<option value="' + '/Map Maker/Maps/' +file + '">' + p[0] + '</option>')

# suhanidatadir="/Users/suhaniagarwal/Desktop/ilgc_website_2/Map Maker/Maps"
# os.chdir(datadir)
# z=next(os.walk(datadir))[1]
# for i in z:
#     print('<option value="'+suhanidatadir+'/punjab'+'/'+i+'/'+i+'_map.html"">'+i+'</option>')
# import sys
# os.chdir(".")
# sys.stdout = open('punjab.txt', 'w')
# for i in z:
#     print('<option value="'+suhanidatadir+'/punjab'+'/'+i+'/'+i+'_maphdhdha.html">'+i+'</option>')
 <option data-id="wrapperOne" value="/Map Maker/Maps/Amritsar.html">Amritsar</option>
<option value="/Map Maker/Maps/Amritsar.html">Amritsar</option>
<option value="/Map Maker/Maps/Barnala.html">Barnala</option>
<option value="/Map Maker/Maps/Bathinda.html">Bathinda</option>
<option value="/Map Maker/Maps/Chandgarh.html">Chandgarh</option>
<option value="/Map Maker/Maps/Faridkot.html">Faridkot</option>
<option value="/Map Maker/Maps/Fategarh_Sahib.html">Fategarh_Sahib</option>
<option value="/Map Maker/Maps/Fazilka.html">Fazilka</option>
<option value="/Map Maker/Maps/Firozpur.html">Firozpur</option>
<option value="/Map Maker/Maps/Gurdaspur.html">Gurdaspur</option>
<option value="/Map Maker/Maps/Hoshiarpur.html">Hoshiarpur</option>
<option value="/Map Maker/Maps/Jalandhar.html">Jalandhar</option>
<option value="/Map Maker/Maps/Kapurthala.html">Kapurthala</option>
<option value="/Map Maker/Maps/Ludhiana.html">Ludhiana</option>
<option value="/Map Maker/Maps/Mansa.html">Mansa</option>
<option value="/Map Maker/Maps/Moga.html">Moga</option>
<option value="/Map Maker/Maps/Muktsar.html">Muktsar</option>
<option value="/Map Maker/Maps/Pathankot.html">Pathankot</option>
<option value="/Map Maker/Maps/Patiala.html">Patiala</option>
<option value="/Map Maker/Maps/Rupnagar.html">Rupnagar</option>
<option value="/Map Maker/Maps/SAS_Nagar.html">SAS_Nagar</option>
<option value="/Map Maker/Maps/Sangrur.html">Sangrur</option>
<option value="/Map Maker/Maps/Shahid_Bhagat.html">Shahid_Bhagat</option>
<option value="/Map Maker/Maps/Tarn_Taran.html">Tarn_Taran</option>