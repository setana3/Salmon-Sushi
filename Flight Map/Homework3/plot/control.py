# -*- coding: utf-8 -*-

from modules import render_csv
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

data = render_csv.read('../Csv/Tallinn.csv','../Csv/geographical_coordinates.csv')

plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree()) #type of map.
ax.coastlines(resolution='50m') #resolution of image
ax.set_title('Tallina Lennujaama lennud 2020')
#ax.add_feauture() #Add some extra stuff here


tallinn_lon = data['TLL'][0]
tallinn_lat = data['TLL'][1]

print(tallinn_lat)

for key in data.keys():

    plt.plot([data[key][0], tallinn_lon], [data[key][1], tallinn_lat],
             color='blue', linewidth=0.25, marker='.',
             transform=ccrs.Geodetic(),
             )
    plt.text(data[key][0], data[key][1], key,
         horizontalalignment='right',
         transform=ccrs.Geodetic())

ax.add_feature(cfeature.LAND)
ax.coastlines(lw=0.5)
ax.gridlines(linestyle='-', color='gray')
plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')


plt.show()