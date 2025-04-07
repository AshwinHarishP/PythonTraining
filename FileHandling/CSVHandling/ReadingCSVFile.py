import csv
filename = "Pratice/FileHandling/CSVHandling/universityRecords.csv"
rows, fields = [], []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append (row)
        
# Print total row count correctly
print(f"Total no. of rows: {len(rows)}")

print('Field names are:', ', '.join(fields))

for row in rows[:5]:
    for col in row: 
        print(f"{col:10}", end=" ")  
    print('/n')