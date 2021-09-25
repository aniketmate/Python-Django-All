import csv

# with open(C) as file:
#     reader = csv.reader(file)
#     # print(reader)
#     c=0
#     for row in reader:
#         # print(row)
#         if c == 0:
#             print(f"Headers are {row[0]}, {row[1]}, {row[2]}")

#         else:
#             print(f"ID:- {row[0]}, Name:- {row[1]}, Age:- {row[2]}")
#         c+=1
import csv
# with open(r"E:\aniket mate\test_csv_123.csv", "w",newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Movie", "Protagonist"])
#     writer.writerow([1, "Batman", "Bruce Wayne"])
#     writer.writerow ([2, "Superman", "Clark Kent"])

# csv_rowlist = [["SN", "Movie", "Protagonist"],
#                 [1, "Batman", "Bruce Wayne"],
#                 [2, "Superman", "Clark Kent"]]

# with open(r"E:\aniket mate\test_csv_456.csv", "w",newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(csv_rowlist)

# import csv
# with open(r"E:\aniket mate\test_csv_789.csv", "w") as file:
#     writer = csv.writer(file,delimiter = '\t')
#     writer.writerow(["SN", "Movie", "Protagonist"])
#     writer.writerow([1, "Batman", "Bruce Wayne"])
#     writer.writerow ([2, "Superman", "Clark Kent"])

# with open(r"E:\aniket mate\annual-enterprise-survey-2020-financial-year-provisional-size-bands-csv.csv", "r") as file:
#     csv_file = csv.DictReader(file)
#     c=0
#     for row in csv_file:
#         print(row)
#         if c == 5:
#             break
#         c+=1

import csv

# with open(r"E:\aniket mate\test_csv_111.csv", "w", newline='') as file:
#     fieldnames = ['player_name', 'fide_rating']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'player_name':'Magnus Carlsen', 'fide_rating': 2870})
#     writer.writerow({'player_name':'Fabian Caruana', 'fide_rating': 2822})
#     writer.writerow({'player_name':'Ding Liren', 'fide_rating': 2801})
# import csv
# with open(r"E:\aniket mate\test_csv_111.csv", "r") as file:
#    csv_reader = csv.reader(file, delimiter= ',')
#    line_count = 0
#    for row in csv_reader:
#         if line_count == 0:
#            print(f"Column names are{','.join(row)}")
#         else:
#             print(f"{row[0]} works in the {row[1]} department, was born in{row[3]}")
#             line_count+=1
#    print(f"Processed {line_count} lines.")     
# 
# import csv
# with open(r"E:\aniket mate\test_csv_111.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')
#    csv_reader = csv.DictReader(csv_file, delimiter= ',')
#    line_count = 0
#    for row in csv_reader:
#         if line_count == 0:
#            print(f'Column names are{",".join(row)}')
#            print("-----------------------------")
#            line_count+=1
#         try:
#             print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#             # print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#         except KeyError as msg:
#             print("Key does not exist:- ", msg)
#             break
#         line_count += 1


# with open(r"E:\aniket mate\B5\business-operations-survey-2020-covid-19-csv.csv","r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ',')
#     no = 0 
#     total_value = 0
#     for row in csv_reader:
#         if no > 0:
#             total_value += int(row[5])
#         no += 1
#     print (total_value)

def total_avg_value_Acc_Food():
    """Accomodation and Food services total and average value"""
with open(r"E:\aniket mate\B5\business-operations-survey-2020-covid-19-csv.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    counter = 0
    no = 0 
    total_value_Acc_Food = 0
    for row in csv_reader:
        if row[1] == "Accommodation & food services":
            total_value_Acc_Food += int(row[5])
            counter +=1
            # print(a) # gives the exact row no the "Accommodation & food services" is found
        no += 1           
    print (f"Value of Accomodation and food services--{total_value_Acc_Food}")
    print(f"Average Value--{total_value_Acc_Food//counter}")


# OUTPUT
# Value of Accomodation and food services--175986
# Average Value--1660