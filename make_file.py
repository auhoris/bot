import csv

def make_file(data):
    with open('info.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for key, value in data.items():
            writer.writerow([key, value])
