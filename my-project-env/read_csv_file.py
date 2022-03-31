#Q. read csv file, delete the last 2 rows and update to the new csv files?
import csv

#creating a csv file
#new_file = open("myfile_copied.csv", 'x')

file = open("/home/neosoft/Desktop/task/my-project-env/myfile.csv", "r")
file_write = open("/home/neosoft/Desktop/task/myfile_copied.csv", "w")


data = csv.reader(file)  #read the csv file
writer = csv.writer(file_write)

new_list = [] 

for row in data:
    #appending each row into a list
    new_list.append(row)
length = len(new_list)
print(length)
    

for i in range(length-2):    #iterate over the csv length
    writer.writerow(new_list[i]) #new_list.append(new_list[i])
file.close()
file_write.close()


