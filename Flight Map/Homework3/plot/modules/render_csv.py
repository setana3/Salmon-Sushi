def read(a, b):
    try:

        import pandas as pd

        Base = pd.read_csv(a, sep=';') #Tallin.csv
        Data = pd.read_csv(b, sep=',') #geographical_coordinates

        _ret = dict()

        ### Compare IATA and show the whole row with iloc[num]
        for row_i, row_i_IATA in Base['IATA'].iteritems():
            # print(Base.iloc[row_i])
            for row_j, row_j_IATA in Data['IATA'].iteritems():
                if row_i_IATA == row_j_IATA:
                    #print(Data.iloc[row_j]['Country'] + " has longitude of " + str(Data.iloc[row_j]["Longitude"]) +
                    #      " and latitude of " + str(Data.iloc[row_j]["Latitude"]))
                    _ret[Data.iloc[row_j]['IATA']] = [Data.iloc[row_j]["Longitude"],Data.iloc[row_j]["Latitude"]]


        return _ret

    except Exception as e:
        return

if __name__ == '__main__':
    test = read('../../Csv/Tallinn.csv','../../Csv/geographical_coordinates.csv')
    print(test)