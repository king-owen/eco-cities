# Project Search Template #
# Ijaz Ryan Owen Varinder Taymoor #
import csv
import numpy as np
import pandas as pd
import glob
import seaborn as sn
import matplotlib.pyplot as plt
# import geocoder
import googlemaps
from datetime import datetime
"""
This program uses Pandas to correlate between different variables in different files, if need be. Visualized with maptplotlib and seaborn
"""


def panda_open_file2(list_FILENAME):
    list_FILENAME = ["LA_Traffic_Volume_With_Coordinates.csv", "Air_Quality__LA_.csv"]
    data_we_want = {}
    keywords = []

    # for filename in list_FILENAME:
    #     temp_words = []
    #     df = pd.read_csv(filename)
    #     keyword  = "idk"
    #     while keyword != "":
    #         keyword = input(f'keyword for {filename}: ')
    #         if keyword != "":
    #            keywords.append(keyword)
    #            temp_words.append(keyword)
        
    #     for word in temp_words:
    #         data_we_want[word] = df[word]
    
    df = pd.read_csv("LA_Traffic_Volume_With_Coordinates.csv")
    data_we_want["coordinates"] = df["coordinates"]

    df = pd.read_csv("Air_Quality__LA_.csv")
    data_we_want["Location"] = df["Location"]
    # print(data_we_want["Location"], data_we_want["coordinates"])
    close_enough = {}
    df = pd.read_csv("Air_Quality__LA_.csv")
    #print(df)
    for location in data_we_want["Location"]:
        location = location[1:-1]
        location_list = location.split(", ")
        #print(location)
        loc_lat = float(location_list[0])
        loc_long = float(location_list[1])
        close_enough[location] = []
        for coordinate in data_we_want["coordinates"]:
            #print(coordinate)
            #reak
            try:
                #coordinate = coordinate[1:-1]
                coordinates_list = coordinate.split(", ")
                #print(coordinate)
                coord_lat = float(coordinates_list[0])
                coord_long = float(coordinates_list[1])
                #print(type(loc_lat))
                #print(type(loc_long))
                #print(type(coord_lat))
                #print(type(coord_long))
                if coord_lat == loc_lat or coord_lat < (loc_lat + 0.01) and coord_lat > (loc_lat - 0.01):
                    close_enough[location].append(coordinate)
            except:
                pass
    print(close_enough)

    # df_we_want = pd.DataFrame(data_we_want, columns = keywords)
    # corrMatrix = df_we_want.corr()

    # sn.heatmap(corrMatrix, annot=True)    
    # plt.show()

    # print(df_we_want)





def google_geo_finder(FILENAMES = "idk"):
  
  
  
    gmaps = googlemaps.Client(key = "AIzaSyAZIWy7l39FrbssxdhBnuDXr9OtAhm5NV0")
    df = pd.read_csv("NY_Traffic_Vol_2014-2019.csv")
    for location in str(df["Roadway Name"] + "from" + df["From"] + "to" + df["To"]):
        try:
            geocode_result = gmaps.geocode(location)
            result_we_want = geocode_result.pop()
            result_we_want = result_we_want["address_components"]
            result_we_want = result_we_want[1]
            result_we_want = result_we_want["long_name"]
            print(result_we_want)
        except:
            geocode_result.append("N/A")
    # for location in str(df["Roadway Name"] + "from" + df["From"] + "to" + df["To"]):
    #     geocode_result = gmaps.geocode(location)
    #     result_we_want = geocode_result.pop()
        
    # print(geocode_result)
    print("wtf")
    # all_coordinates = []
    # for location in df["Location"]:
  
  
  
    """For checking geocode in LA"""
    #     try:
    #         geocode_result = gmaps.geocode(location)
    #         # print(geocode_result)
    #         result_we_want = geocode_result.pop()
    #         coordinates = (str(result_we_want["geometry"]["location"]))[1:-1]
    #         coordinates = coordinates.replace("'lat': ", "")
    #         coordinates = coordinates.replace("'lng': ", "")
    #         all_coordinates.append(coordinates)
    #         print(coordinates)
    #     except:
    #         all_coordinates.append("N/A")
    # df["coordinates"] = all_coordinates
    # df.to_csv("LA_Traffic_Volume_With_Coordinates2.csv")
    
 
    # reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    # now = datetime.now()
    # directions_result = gmaps.directions("Sydney Town Hall",
    #                                  "Parramatta, NSW",
    #                                  mode="transit",
    #                                  departure_time=now)


def play():
    df = pd.read_csv("NY_Traffic_Vol_2014-2019.csv")
    # totals = []
    # print(df)
    # print(df["0"])
    # print("wtf")
    sum_column = str(df["Roadway Name"]) + "from" + str(df["From"]) + "to" + str(df["To"])
    # print(sum_column[1])
    df["full"] = sum_column
    print(sum_column)
    # print(df["full"][1])
    # print(df["Roadway Name"])
    # print(df)
    # df["full address"] = sum_column
    # df.to_csv("NY_Traffic_Vol_2014-2019(3).csv")

def main():
    name_input = "idk"
    FILENAMES = []
    while name_input != "":
        name_input = input("Enter file name: ")
        if name_input != "":
            FILENAMES.append(name_input)
        
    # google_geo_finder()
    # coordinates = geo_finder(FILENAMES)
    value = panda_open_file2(FILENAMES)

    # value = panda_open_file(FILENAME)
    # open_file(FILENAME)
    # something = algorithm(value)



main()

#play()
# google_geo_finder()