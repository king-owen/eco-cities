# Project Search Template #
# Ijaz Ryan Owen Varinder Taymoor #
import csv
from os import close, error
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
    
    df_traffic = pd.read_csv("LA_Traffic_Volume_With_Coordinates.csv")
    data_we_want["coordinates"] = df_traffic["coordinates"]
    data_we_want["volume"] = df_traffic["24 Hr. Total Vol."]


    df_air = pd.read_csv("Air_Quality__LA_.csv")
    data_we_want["count"] = df_air["Count"]

    data_we_want["Location"] = df_air["Location"]
    # print(data_we_want["Location"], data_we_want["coordinates"])
    close_enough = {}
    # df_air = pd.read_csv("Air_Quality__LA_.csv")
    # df_new = df_air.query("coordinates==33.9935686, -117.9274972")
    # print(df_new["Total"])
    #print(df)
    particle_and_traffic = {}
    particle_and_traffic["particles"] = []
    particle_and_traffic["traffic"] = []
    air_index = 0
    for location in data_we_want["Location"]:
        location = location[1:-1]
        location_list = location.split(", ")
        #print(location)
        loc_lat = float(location_list[0])
        loc_long = float(location_list[1])
        close_enough[location] = [[], []]
        close_enough[location][0].append(float(data_we_want["count"][air_index]))
        particle_and_traffic["particles"].append(float(data_we_want["count"][air_index]))
        traffic_index = 0
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
                    close_enough[location][1].append(int(data_we_want["volume"][traffic_index]))
                    

                traffic_index += 1
            except:
                # print(error)
                traffic_index+=1
        total = sum(close_enough[location][1])
        particle_and_traffic["traffic"].append(total)
        close_enough[location][1] = total
        air_index+=1
    print(close_enough)
    # part_and_traffic_df = pd.DataFrame(particle_and_traffic)
    part_and_traffic_df = pd.DataFrame(particle_and_traffic, columns = ["particles", "traffic"])
    corrMatrix = part_and_traffic_df.corr()
    sn.heatmap(corrMatrix, annot = True)
    plt.show()
    #getting average
    #look through close_enough and go key by key and make a new list

    # df_we_want = pd.DataFrame(data_we_want, columns = keywords)
    # corrMatrix = df_we_want.corr()

    # sn.heatmap(corrMatrix, annot=True)    
    # plt.show()

    # print(df_we_want)





def google_geo_finder(FILENAMES = "idk"):
  
    all_addresses = []
    gmaps = googlemaps.Client(key = "AIzaSyCUJSFnd_DZX2j04BnSiz22pr8Nb3xbKyY")
    df = pd.read_csv("Traffic NY Update.csv")
    for location in df["Spec Boroughs"] + " New York":
        count = 0
        current_address = "N/A"
        try:
            # print(location)
            geocode_result = gmaps.geocode(location)
            result_we_want = geocode_result.pop()
            address_components = result_we_want["address_components"]
            formatted_address = result_we_want["formatted_address"]
            if "Manhattan" in location:
                if count == 0:
                    current_address = "Manhattan"
                    all_addresses.append("Manhattan")
                    print(current_address)
                    count += 1
            elif "Brooklyn" in location:
                if count == 0:
                    current_address = "Brooklyn"
                    all_addresses.append("Brooklyn")
                    count += 1
                    print(current_address)

            elif "Staten Island" in location:
                if count == 0:
                    current_address = "Staten Island"
                    all_addresses.append("Staten Island")
                    print(current_address)
                    count += 1

            elif "Queens" in location:
                if count == 0:
                    current_address = "Queens"
                    all_addresses.append("Queens")
                    print(current_address)
                    count += 1

            elif "Bronx" in location:
                if count == 0:
                    current_address = "Bronx"
                    all_addresses.append("Bronx")
                    print(current_address)
                    count += 1

            elif "Manhattan" in formatted_address:
                if count == 0:
                    current_address = "Manhattan"
                    all_addresses.append("Manhattan")
                    print(current_address)
                    count += 1
            elif "Brooklyn" in formatted_address:
                if count == 0:
                    current_address = "Brooklyn"
                    all_addresses.append("Brooklyn")
                    print(current_address)
                    count += 1
            elif "Staten Island" in formatted_address:
                if count == 0:
                    current_address = "Staten Island"
                    all_addresses.append("Staten Island")
                    print(current_address)
                    count += 1
            elif "Queens" in formatted_address:
                if count == 0:
                    current_address = "Queens"
                    all_addresses.append("Queens")
                    print(current_address)
                    count += 1
            elif "Bronx" in formatted_address:
                if count == 0:
                    current_address = "Bronx"
                    all_addresses.append("Bronx")
                    print(current_address)
                    count += 1
            else:

                for list in address_components:
                    for inner_list in list:
                        if count == 0:
                            if "Manhattan" in list[inner_list]:
                                if count == 0:
                                    current_address = "Manhattan"
                                    all_addresses.append("Manhattan")
                                    count += 1
                                    print("Manhattan")
                                
                            elif "Brooklyn" in list[inner_list]:
                                if count == 0:
                                    current_address = "Brooklyn"
                                    all_addresses.append("Brooklyn")
                                    count += 1
                                    print("Brooklyn")
                                
                            elif "Staten Island" in list[inner_list]:
                                if count == 0:
                                    current_address = "Staten Island"
                                    all_addresses.append("Staten Island")
                                    count += 1
                                    print("Staten Island")
                            
                            elif "Queens" in list[inner_list]:
                                if count == 0:
                                    current_address = "Queens"
                                    all_addresses.append("Queens")
                                    count += 1
                                    print("Queens")
                            
                            elif "Bronx" in list[inner_list]:
                                if count == 0:
                                    current_address = "Bronx"
                                    all_addresses.append("Bronx")
                                    count += 1
                                    print("Bronx")
                if count == 0:
                    all_addresses.append("N/A")
                    count += 1
                    print("N/A")
                            

        except:
            if count == 0:
                all_addresses.append("N/A")
                print(":(")
                count += 1
    df["Even More Specific"] = all_addresses
    df.to_csv("Traffic New York Update2.csv")
    """
    for location in df["Spec Boroughs"] + " New York":
        try:
            print(location)
            geocode_result = gmaps.geocode(location)
            result_we_want = geocode_result.pop()
            address_components = result_we_want["address_components"]
            address_components = address_components[1]
            address_components = address_components["long_name"]
            formatted_address = result_we_want["formatted_address"]
            formatted_address = formatted_address.split(",")
            formatted_address = formatted_address[1]

            if "Manhattan" or "Brooklyn" or "Queens" or "Staten Island" or "Bronx" in address_components:
                geocode_result.append(address_components)
                print(address_components)
            else:
                geocode_result.append(formatted_address)
                print(formatted_address)
            # # result_we_want = result_we_want["long_name"]
            # print(result_we_want)
        except:
            geocode_result.append("N/A")
            print("N/A")
    
    
    # for location in str(df["Roadway Name"] + "from" + df["From"] + "to" + df["To"]):
    #     geocode_result = gmaps.geocode(location)
    #     result_we_want = geocode_result.pop()
    df["Even More Specific"] = geocode_result
    df.to_csv("Traffic New York Update2.csv")

 
    # print(geocode_result)
    print("wtf")
    # all_coordinates = []
    # for location in df["Location"]:
    """
    
  
    """For checking geocode in LA"""
    #     try:
geocode_result = gmaps.geocode(location)
result_we_want = geocode_result.pop()
coordinates = (str(result_we_want["geometry"]["location"]))[1:-1]
coordinates = coordinates.replace("'lat': ", "")
coordinates = coordinates.replace("'lng': ", "")
all_coordinates.append(coordinates)
print(coordinates)
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



def new_york():
    specific_borough = []
    traffic_new_york_df = pd.read_csv("NY_Traffic_Vol_2014-2019(3).csv")
    for borough in traffic_new_york_df["Boroughs"]:
        # print(borough)
        if "Bronx" or "Laconia" or "Canal" or "Fordham" or "Van Cortland" or "Pelham" or "Netherland" or "University Heights" or "East 153" or "East 156" or "Concourse" or "Bartow" in str(borough):
            borough = "Bronx"
            # print(borough)
        elif "Harlem" or "Adam Clayton" or "East 46th A" in str(borough):
            borough = "Manhattan"
            # print(borough)
        elif "Manhattan" in str(borough):
            borough = "Manhattan"
        elif "Brooklyn" in str(borough):
            borough = "Brooklyn"
        elif "Queens" or "Auburndale" or "Jamaica" in str(borough):
            borough = "Queens"
        elif "Staten" in str(borough):
            borough = "Staten Island"
        
        specific_borough.append(borough)
    traffic_new_york_df["Spec Boroughs"] = specific_borough
    traffic_new_york_df.to_csv("Traffic NY Update.csv")
# def google_geo_finder(FILENAMES = "idk"):
  
  
  
#     gmaps = googlemaps.Client(key = "AIzaSyAZIWy7l39FrbssxdhBnuDXr9OtAhm5NV0")
#     df = pd.read_csv("NY_Traffic_Vol_2014-2019.csv")
#     for location in str(df["Roadway Name"] + "from" + df["From"] + "to" + df["To"]):
#         try:
#             geocode_result = gmaps.geocode(location)
#             result_we_want = geocode_result.pop()
#             result_we_want = result_we_want["address_components"]
#             result_we_want = result_we_want[1]
#             result_we_want = result_we_want["long_name"]
#             print(result_we_want)
#         except:
#             geocode_result.append("N/A")
#     # for location in str(df["Roadway Name"] + "from" + df["From"] + "to" + df["To"]):
#     #     geocode_result = gmaps.geocode(location)
#     #     result_we_want = geocode_result.pop()
        
#     # print(geocode_result)
#     print("wtf")
#     # all_coordinates = []
#     # for location in df["Location"]:
  






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



# main()
# new_york()

#play()
google_geo_finder()