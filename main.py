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

    data_we_want = {}
    keywords = []

    for filename in list_FILENAME:
        temp_words = []
        df = pd.read_csv(filename)
        keyword  = "idk"
        while keyword != "":
            keyword = input(f'keyword for {filename}: ')
            if keyword != "":
               keywords.append(keyword)
               temp_words.append(keyword)
        
        for word in temp_words:
            data_we_want[word] = df[word]
    
    df_we_want = pd.DataFrame(data_we_want, columns = keywords)
    corrMatrix = df_we_want.corr()

    sn.heatmap(corrMatrix, annot=True)    
    plt.show()

    print(df_we_want)





def google_geo_finder(FILENAMES = "idk"):
    gmaps = googlemaps.Client(key = "AIzaSyAZIWy7l39FrbssxdhBnuDXr9OtAhm5NV0")
    df = pd.read_csv("LA_Traffic_Volume.csv")
    all_coordinates = []
    for location in df["Location"]:
        try:
            geocode_result = gmaps.geocode(location)
            # print(geocode_result)
            result_we_want = geocode_result.pop()
            coordinates = (str(result_we_want["geometry"]["location"]))[1:-1]
            coordinates = coordinates.replace("'lat': ", "")
            coordinates = coordinates.replace("'lng': ", "")
            all_coordinates.append(coordinates)
            print(coordinates)
        except:
            all_coordinates.append("N/A")
    df["coordinates"] = all_coordinates
    df.to_csv("LA_Traffic_Volume_With_Coordinates2.csv")
    
 
    # reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    # now = datetime.now()
    # directions_result = gmaps.directions("Sydney Town Hall",
    #                                  "Parramatta, NSW",
    #                                  mode="transit",
    #                                  departure_time=now)


def main():
    name_input = "idk"
    FILENAMES = []
    while name_input != "":
        name_input = input("Enter file name: ")
        if name_input != "":
            FILENAMES.append(name_input)
    
    google_geo_finder()
    # coordinates = geo_finder(FILENAMES)
    # value = panda_open_file2(FILENAMES)

    # value = panda_open_file(FILENAME)
    # open_file(FILENAME)
    # something = algorithm(value)



main()