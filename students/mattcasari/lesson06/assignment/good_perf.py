"""
well performing, well written module

"""

import datetime
import csv
import pandas as pd

def _counter():
    idx = 0
    while True:
        yield idx
        idx += 1

def analyze(filename):
    start = datetime.datetime.now()
    year_2013 = _counter()
    year_2014 = _counter()
    year_2015 = _counter()
    year_2016 = _counter()
    year_2017 = _counter()
    year_2018 = _counter()
    found = _counter()

    year_count = {}
    field_names = ['uuid','idx1','idx2','idx3','idx4','date','extra']
    df = pd.read_csv(filename, delimiter=',',names=field_names)

    

    year_count["2013"] = sum(df['date'].str.contains('2013'))
    year_count["2014"] = sum(df['date'].str.contains('2014'))
    year_count["2015"] = sum(df['date'].str.contains('2015'))
    year_count["2016"] = sum(df['date'].str.contains('2016'))
    year_count["2017"] = sum(df['date'].str.contains('2017'))
    year_count["2018"] = sum(df['date'].str.contains('2018'))
    found = df['extra'].value_counts()['ao']
    # if df['date'][6:] == '2013':
    #     next(year_2013)
    # if df['date'][6:] == '2014':
    #     next(year_2014)
    # if df['date'][6:] == '2015':
    #     next(year_2015)
    # if df['date'][6:] == '2016':
    #     next(year_2016)
    # if df['date'][6:] == '2017':
    #     next(year_2017)
    # if df['date'][6:] == '2018':
    #     next(year_2018)
    # if "ao" in df['extra']:
    #     next(found)         
    # with open(filename,'r') as csvfile:
        # reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        # reader = csv.DictReader(csvfile, fieldnames=field_names)
        # for row in reader:
        #     print(row)
        #     if row[5][6:] == '2013':
        #         next(year_2013)
        #     if row['date'][6:] == '2014':
        #         next(year_2014)
        #     if row['date'][6:] == '2015':
        #         next(year_2015)
        #     if row['date'][6:] == '2016':
        #         next(year_2016)
        #     if row['date'][6:] == '2017':
        #         next(year_2017)
        #     if row['date'][6:] == '2018':
        #         next(year_2018)
        #     if "ao" in row['extra']:
        #         next(found)         


        # year_count["2013"] = next(year_2013)
        # year_count["2014"] = next(year_2014)
        # year_count["2015"] = next(year_2015)
        # year_count["2016"] = next(year_2016)
        # year_count["2017"] = next(year_2017)
        # year_count["2018"] = next(year_2018)
        # found = next(found)

    end = datetime.datetime.now()
        
    return (start, end, year_count, found)

def main():
    filename = "data/exercise.csv"
    analyze(filename)


if __name__ == "__main__":
    main()
