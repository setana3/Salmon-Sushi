# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd


tal = pd.read_csv('/Users/setana/code/Python/Advanced-Python/Homework3/CSV/Tallinn.csv',
                         sep=';')

wlf = pd.read_csv('/Users/setana/code/Python/Advanced-Python/Homework3/CSV/geographical_coordinates.csv',
                         sep=',')

data = dict()

### Compare IATA and show the whole row with iloc[num]
for item1, frame1 in tal['IATA'].iteritems():
    # print(tal.iloc[item1])
    for item2, frame2 in wlf['IATA'].iteritems():
        if frame1 == frame2:
            #print(wlf.iloc[item2]['Country'] + " has longitude of " + str(wlf.iloc[item2]["Longitude"]) +
            #      " and latitude of " + str(wlf.iloc[item2]["Latitude"]))
            data[wlf.iloc[item2]['IATA']] = [wlf.iloc[item2]["Longitude"],wlf.iloc[item2]["Latitude"]]


tallinn_lon = data['TLL'][0]
tallinn_lat = data['TLL'][1]


#Create matplot
plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree()) #type of map.
ax.coastlines(resolution='50m') #resolution of image
ax.set_title('Tallina Lennujaama lennud 2020')
ax.add_feature(land_50m)
ax.add_feature(ocean_50m)
ax.add_feature(lakes_50m)
ax.add_feature(river_50m)


def map_plotting(arg_lon,arg_lat,name,tallinn_lon, tallinn_lat):

    #mapping
    plt.plot([arg_lon, tallinn_lon], [arg_lat, tallinn_lat],
             color='blue', linewidth=0.25, marker='.',
             transform=ccrs.Geodetic(),
             )

    plt.text(arg_lon-1, arg_lat, str(name),
         horizontalalignment='right',
         transform=ccrs.Geodetic())


for key in data.keys():
    map_plotting(data[key][0],data[key][1],key, tallinn_lon, tallinn_lat)


ax.add_feature(cfeature.LAND)
ax.coastlines(lw=0.5)
ax.gridlines(linestyle='-', color='gray')

plt.savefig('coastlines.pdf')
plt.savefig('coastlines.png')

plt.show()
