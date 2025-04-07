import csv
fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [['Nikhil', 'COE', '1', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SEI', '3', '9.5'],
        ['Prateek', 'MCE', '3', '7'],
        ['Sahil', 'EP', '2', '9.1']]

filename = "Pratice/FileHandling/CSVHandling/universityRecords.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)