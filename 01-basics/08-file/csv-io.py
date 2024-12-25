import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Chicago']
]

# Write the file
with open('data/output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # Write multiple rows

with open('data/output.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)