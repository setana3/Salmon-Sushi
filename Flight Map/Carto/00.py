import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
import matplotlib.path as mpath
import numpy as np



plt.figure()
ax = plt.axes(projection=ccrs.PlateCarree())

#Setting the longtitude and latitude of NewYork
ny_lon, ny_lat = -75, 43

#Setting the longtitude and lattitude of delhi
delhi_lon, delhi_lat = 77.23, 28.61


plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='blue', linewidth=1, marker='o',
         transform=ccrs.Geodetic(),
         )




ax.add_feature(cfeature.LAND)
ax.coastlines(lw=0.5)
ax.gridlines(linestyle='-', color='gray')
plt.show()