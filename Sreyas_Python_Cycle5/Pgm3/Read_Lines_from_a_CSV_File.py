import csv

try:
    with open('testfile.csv') as file_obj:
        next(file_obj)
        read_obj = csv.reader(file_obj)

        [print(x) for x in read_obj]

except Exception:
    print(Exception)