import pandas as pd
import csv

lst_tuberclosis = []
lst_giardiasis = []
lst_influenza = []
lst_para = []
lst_malaria = []

with open('ratesbydisease2008_2018.csv', encoding="utf8", errors='ignore') as CSV_FILE2:
    HEALTH_DATA = csv.reader(CSV_FILE2)
    next(HEALTH_DATA)  # to skip the first row
    for row in HEALTH_DATA:
        if row[0] == 'Tuberculosis':
            for i in range(1, len(row) ):
                if i % 2 != 0:
                    lst_tuberclosis.append(row[i])

with open('ratesbydisease2008_2018.csv', encoding="utf8", errors='ignore') as CSV_FILE2:
    HEALTH_DATA = csv.reader(CSV_FILE2)
    next(HEALTH_DATA)  # to skip the first row
    for row in HEALTH_DATA:
        if row[0] == 'Influenza ':
           for i in range(1, len(row)):
                if i % 2 != 0:
                    lst_influenza.append(row[i])

with open('ratesbydisease2008_2018.csv', encoding="utf8", errors='ignore') as CSV_FILE2:
    HEALTH_DATA = csv.reader(CSV_FILE2)
    next(HEALTH_DATA)  # to skip the first row
    for row in HEALTH_DATA:
        if row[0] == 'Malaria':
            for i in range(1, len(row)):
                if i % 2 != 0:
                    lst_malaria.append(row[i])

with open('ratesbydisease2008_2018.csv', encoding="utf8", errors='ignore') as CSV_FILE2:
    HEALTH_DATA = csv.reader(CSV_FILE2)
    next(HEALTH_DATA)  # to skip the first row
    for row in HEALTH_DATA:
        if row[0] == 'Giardiasis':
            for i in range(1, len(row)):
                if i % 2 != 0:
                    lst_giardiasis.append(row[i])

with open('ratesbydisease2008_2018.csv', encoding="utf8", errors='ignore') as CSV_FILE2:
    HEALTH_DATA = csv.reader(CSV_FILE2)
    next(HEALTH_DATA)  # to skip the first row
    for row in HEALTH_DATA:
        if row[0] == 'Paratyphoid fever':
            for i in range(1, len(row)):
                if i % 2 != 0:
                    lst_para.append(row[i])



