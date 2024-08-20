import csv

lookingoutside = 16 
objects = 'person, unknown,'
Eyeblinking = 4
row_list = [["Looking outside of monitor", "Objects", "Eyeblinking"],
            [lookingoutside, objects, Eyeblinking],]

with open('results/result.csv', 'w', newline='') as file:
     writer = csv.writer(file)
     writer.writerows(row_list)
