# Project Search Template #
# Ijaz Ryan Owen Varinder Taymoor #
import csv

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
_data = []

def open_file(FILENAME):
    with open(FILENAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        imp_col_idx = {}
        relevant_health_data = {}

        for row in csv_reader:
            if line_count == 0:
                for idx, col in enumerate(row):
                    if col == "GEOID10" or col == "PCT_POP_INC_UNDER_200_POVERTY" or col == "PCT_ADULT_WITH_ASTHMA" or col == "PCT_ADULT_WITH_DISABILITIES":
                        imp_col_idx[col] = idx
        
                line_count += 1
            else:
                try:
                    if float(row[imp_col_idx["PCT_POP_INC_UNDER_200_POVERTY"]]) >= 0.4:
                        print(row[imp_col_idx["PCT_ADULT_WITH_ASTHMA"]])
                except:
                    continue
          
                #     print(row[imp_col_idx["GEOID10"]])





def main():
    FILENAME = input("Enter file name: ")
    open_file(FILENAME)



main()