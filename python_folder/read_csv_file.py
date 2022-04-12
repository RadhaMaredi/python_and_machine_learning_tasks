#Q. read csv file, delete the last 2 rows and update to the new csv files?

import csv

#creating a csv file
new_file = open("myfile_copied.csv", 'x')

#open the files to to read and write purpose 
file = open("/home/neosoft/Desktop/task/my-project-env/myfile.csv", "r")
file_write = open("/home/neosoft/Desktop/task/myfile_copied.csv", "w")
data = csv.reader(file)  #reading the csv file
writer = csv.writer(file_write)

#crated empty list to store the rows and to know lenght of the file
new_list = []
for row in data:          #this loop iterate over the each row of the file
    new_list.append(row)  #appending each row into a list
length = len(new_list)    #finding the length of the file

for i in range(length-2):        #iterate over the csv length-2
    writer.writerow(new_list[i]) #store each row in or new csv file.
file.close()                     #close the file
file_write.close()


