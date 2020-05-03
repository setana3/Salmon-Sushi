import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def map_plotting(dict_data):

    try:

        tallinn_lon = dict_data['TLL'][0]
        tallinn_lat = data['TLL'][1]

        for key in dict_data.keys():

            plt.plot([dict_data[key][0], tallinn_lon], [dict_data[key][1], tallinn_lat],
                     color='blue', linewidth=0.25, marker='.',
                     transform=ccrs.Geodetic(),
                     )

            plt.text(dict_data[key][0]-1, dict_data[key][1], key,
                 horizontalalignment='right',
                 transform=ccrs.Geodetic())

    except Exception as e:
        return e
