# Project Search Template #
# Ijaz Ryan Owen Varinder Taymoor #
import csv
import numpy as np
import pandas as pd
import glob
import seaborn as sn
import matplotlib.pyplot as plt
# from scipy import stats

# def open_file(FILENAME):
#     with open(FILENAME) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter = ',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#     print(f'Processed {line_count} lines.')


############################### just trying things out ############################
# _data = ["GEOID10", "PCT_POP_INC_UNDER_200_POVERTY", "PCT_ADULT_WITH_ASTHMA", "PCT_ADULT_WITH_DISABILITIES"]

# def open_file(FILENAME):
#     with open(FILENAME) as csv_file:
#         data_search = []
#         keyword1 = input("Please input data keyword: ")
#         data_search.append(keyword1)
#         keyword2 = input("Please put correlating data keyword or enter 0 to exit: ")
#         data_search.append(keyword2)
#         # keyword = "randoooom"
#         # while keyword != "0":
#         #     keyword = input("Please put correlating data keyword or enter 0 to exit: ")
#         #     if keyword != "0":
#         #         data_search.append(keyword)
            
#         csv_reader = csv.reader(csv_file, delimiter = ',')
#         line_count = 0
#         imp_col_idx = {}
#         word_1_data = []
#         word_2_data = []
#         # data_point = input("Please enter what you are looking for (greater or lower) followed by a space and a number: ")
#         # data_point = data_point.split()
#         # print(data_point)

#         for row in csv_reader:
#             if line_count == 0:
#                 for idx, col in enumerate(row):
#                     # if col == "GEOID10" or col == "PCT_POP_INC_UNDER_200_POVERTY" or col == "PCT_ADULT_WITH_ASTHMA" or col == "PCT_ADULT_WITH_DISABILITIES":
#                     if col in data_search:
#                         imp_col_idx[col] = idx
#                 print(imp_col_idx)
        
#                 line_count += 1

#             else:
#                 try:
#                     for word in data_search:
#                         if word == keyword1:
#                             word_1_data.append(float(row[imp_col_idx[word]]))
#                         else:
#                             word_2_data.append(float(row[imp_col_idx[word]]))
                



#                 #     if row[imp_col_idx[main_word]] >= 0.4:
#                 #         for word in data_search:
#                 #             print(row[imp_col_idx[word]])
#                     # if data_point[0] == ">":
                    
#                     #     if row[imp_col_idx[main_word]] >= data_point[1]:
#                     #         for word in data_search:
#                     #             #Later want to put the keyword and a list of data into the dictionary
#                     #             #Or somehow manipulate this data
#                     #             print(row[imp_col_idx[word]])

#                     # elif data_point[0] == "<":
#                     #     if row[imp_col_idx[main_word]] <= data_point[1]:
#                     #         for word in data_search:
#                     #             #Later want to put the keyword and a list of data into the dictionary
#                     #             #Or somehow manipulate this data
#                     #             print(row[imp_col_idx[word]])


#                 except:
#                     continue
#         # print(word_1_data)
#         # print(word_2_data)
#         result = np.corrcoef(word_1_data, word_2_data)
#         print(result)


def panda_open_file(FILENAME):
    df = pd.read_csv(FILENAME)
    list_1 = []
    list_2 = []
    """ Print Column Names """
    # print(df.columns)

    """ Read Each Column """
    # print(df[['PCT_POP_INC_UNDER_200_POVERTY', ...]])

    """ Read Each Row """
    # print(df.iloc[row_range])

    """ Look for specifics """
    #  df.loc[df['Name'] == Conditional value]

    """ Sort by col name """
    #df.sort_values(['Name', 'Name2'], ascending = TrueorFalse)

    """ number of rows and columns in the data frame """
    #df.shape

    """ Iterate through Rows """
    #for index, row in df.iterrows():
        ## Can also get row name with index
        #print(index, row['Name'])
    keyword1 = input('keyword1 ')
    keyword2 = input('keyword2 ')
    for idx, row in df.iterrows():
        ## Can also get row name with index
        #print(index, row['Name'])
        list_1.append(float(row[keyword1]))
        list_2.append(float(row[keyword2]))
    
    if type(list_1[-1] is not float):
        list_1.pop()
    if type(list_2[-1] is not float):
        list_2.pop()
    
    print(list_1)
    print(list_2)
    
    result = np.corrcoef(list_1, list_2)
    print(result)

    return result




def algorithm(value):
    #IDEK
    pass


def main():
    FILENAME = input("Enter file name: ")
    value = panda_open_file(FILENAME)
    # open_file(FILENAME)
    something = algorithm(value)



main()