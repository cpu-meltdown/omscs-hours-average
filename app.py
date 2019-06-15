import csv

with open('hours.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    hours_per_week = {}
    week = 0
    for row in csv_reader:
        if row[0] != '':
            week = week + 1
            hours_per_week[str(week)] = float(row[2])
        else:
            hours_per_week[str(week)] = hours_per_week.get(str(week)) + float(row[2])
    
    print(float(sum(hours_per_week.values()) / len(hours_per_week)))
