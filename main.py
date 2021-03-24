# Project Search Template #
# Ijaz Ryan Owen Varinder Taymoor #
import csv
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
_data = ["GEOID10", "PCT_POP_INC_UNDER_200_POVERTY", "PCT_ADULT_WITH_ASTHMA", "PCT_ADULT_WITH_DISABILITIES"]

def open_file(FILENAME):
    with open(FILENAME) as csv_file:
        data_search = []
        main_word = input("Please input data keyword: ")
        keyword = 1
        data_search.append(main_word)
       
        keyword = input("Please put correlating data keyword or enter 0 to exit: ")
        while keyword != "0":
            keyword = input("Please put correlating data keyword or enter 0 to exit: ")
            if keyword != 0:
                data_search.append(keyword)
            
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        imp_col_idx = {}
        relevant_health_data = {}
        data_point = input("Please enter what you are looking for (greater or lower) followed by a space and a number: ")
        data_point = data_point.split()
        print(data_point)

        for row in csv_reader:
            if line_count == 0:
                for idx, col in enumerate(row):
                    # if col == "GEOID10" or col == "PCT_POP_INC_UNDER_200_POVERTY" or col == "PCT_ADULT_WITH_ASTHMA" or col == "PCT_ADULT_WITH_DISABILITIES":
                    if col in data_search:
                        imp_col_idx[col] = idx
                print(imp_col_idx)
        
                line_count += 1

            else:
                try: 
                    if data_point[0] == ">":
                    
                        if row[imp_col_idx[main_word]] >= data_point[1]:
                            for word in data_search:
                                #Later want to put the keyword and a list of data into the dictionary
                                #Or somehow manipulate this data
                                print(row[imp_col_idx[word]])

                    elif data_point[0] == "<":
                        if row[imp_col_idx[main_word]] <= data_point[1]:
                            for word in data_search:
                                #Later want to put the keyword and a list of data into the dictionary
                                #Or somehow manipulate this data
                                print(row[imp_col_idx[word]])


                except:
                    continue


                    # try:
                    #     if float(row[imp_col_idx[0]]) >= data_point[1]:
                    #         print(row[imp_col_idx[]])
                # try:
                #     if float(row[imp_col_idx[0]]) >= 0.4:
                #         print(row[imp_col_idx["PCT_ADULT_WITH_ASTHMA"]])
                # except:
                #     continue
          
                # #     print(row[imp_col_idx["GEOID10"]])
                
                ####correlation calculation######
                # x = []
                # y = []
                # correlation, p_value = stats.pearsonr(x, y)





def main():
    FILENAME = input("Enter file name: ")
    open_file(FILENAME)



main()