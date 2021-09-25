import csv


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