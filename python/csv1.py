#pull in the csv file
import csv
#open the csv file
#identify the csv read as our_reader and tell it to read our csv fie that we've opened as csvfile
# with open('csvs/basic.csv', 'r') as csvfile:
#    our_reader = csv.reader(csvfile)
    #this organizes the data in a sensible way by taking each row in the csv file and turning it into a list. The whole file then becomes a list of lists

#    names = [row for row in our_reader]
# #prints whole list
# #print(names)
#
# #this print is a double index and selects the first row and the first column and spits that out.
# #print(names[1][2])
#
# #find length of names list
# #print(len(names))
#
# #find the length of each first name
# #for row in names:
#     #print(len(row[2]))
#
# #find the longest first name
# #if the length of row 2 is longer than the length of 'longest' (which = a space, or nothing), then longest then = row 2. when we print longest, it prints row 2 because we've told the computer longest = row 2.
# longest = ''
# for row in names:
#     if len(row[2]) > len(longest):
#         longest = row[2]
# #print(longest)
#
# #construct a new list consisting of only the first names we have in the csv file
# #setting new variable so that first_names = row 2 of csv file
# first_names = [row[2] for row in names]
# #reversing order of itmes in row 2, which are first_names
# first_names.reverse()
# #printing newly isolated and reversed row 2, or first_names
# #print(first_names)
#
# #this adds a new row to the original csv file consisting of the below list
# new_row = [2, 'wayne', 'graham','meh']
# names.append(new_row)
# #print(names)
#
# #this adds another row to the csv file but it doesn't print out like the last one.
# a_row = [3, 'fox', 'eliza', 'SO COOL']
# #print(names + a_row)
#
# #write something to the csv, this step is creating a new csv file and writing data to it
# with open('csvs/practice.csv', 'w', newline = '') as fout:
#     csvwriter = csv.writer(fout)
#     for i in range(0, 100, 10):
#         csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20, i + 25, i +30])
#
# #this step is printing out the data from the new csv using our csv reader. data is set as a variable for the entireity of the csv, or lsit of lists, so then we print the variable data
# with open('csvs/practice.csv', 'r') as fin:
#     our_reader = csv.reader(fin)
#     data = [row for row in our_reader]
# #print(data)
#
# #modifying particular elements in this new csv
# data[3][5] = 'Ethan'
# data[5][4] = 'Brandon'
# data[2][6] = 'Tony the cat'
#
# #this sets our new csv 'practice' as the output destination for the actions we're about to do
# with open('csvs/practice.csv', 'w', newline='') as fout:
#     #setting csvwriter as a variable for the csv writer we're using, which will act on the new csv file
#     csvwriter = csv.writer(fout)
#     #for each row in data apply the csv writer to that row. this will then be copied out to the new csv
#     for row in data:
#         csvwriter.writerow(row)
#print(data)

# #working with Dictwriter and Dictreader classes
# #create new list called groceries
# groceries = []
# #open the existing csv file 'shopping' as a csv file
# with open('csvs/shopping.csv', 'r') as csvfile:
#     #set a variable 'reader' as the output of the DictReader reading the csv file 'shopping'. AKA convert csv file to a DictReader object
#     reader = csv.DictReader(csvfile)
#     #for each row in the new variable 'reader', add 'row'
#     for row in reader:
#         groceries.append(row)
# print(groceries)

 #it wasn't the code that was the problem here, it was that somehow the contents of shopping.csv got deleted earlier and I had to re-download it
groceries = []
with open('csvs/shopping.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        groceries.append(row)

#print(groceries)

#querying by column to get a particular item
#print(groceries[2]['name'])

#pinting one column by looping over whole list
#for item in groceries:
    #print(item['name'])

#writing new data to our shooping.csv file. This is the data we want to add and the command to append the groceries list we already created and populated. Adding then formatting.
# tony = {'name': 'tony', 'nutritious': 'False', 'id': '5'}
# groceries.append(tony)
#
#  #creating a new csv file to write to and creating a new line that is currently empty and setting that as a variable. The creating a new varialbe that is a list of column names to be added. This then equals the variable fieldnames which is being written to the csv thru dictwriter
# with open ('csvs/updated_groceries.csv', 'w', newline= '') as fout:
#     column_names = ['id', 'name', 'nutritious']
#     #set dictwriter as a variable/action to make column_names as fieldnames in the csv we've designated
#     dictwriter = csv.DictWriter(fout, fieldnames=column_names)
#     #write column_names represented by variable dictwriter as headers in the fieldnames in the csv
#     dictwriter.writeheader()
#     #for every row in groderies, write the dictwriter variable which is each piece of info in {tony}, under the headers we've designated via the row above.
#     for row in groceries:
#         dictwriter.writerow(row)

tony = {'name': 'tony', 'nutritious': 'False', 'id': '5'}

groceries.append(tony)

with open('csvs/updated_groceries.csv', 'w', newline='') as fout:
    column_names = ['id', 'name', 'nutritious']
    dictwriter = csv.DictWriter(fout, fieldnames=column_names)
    dictwriter.writeheader()
    for row in groceries:
        dictwriter.writerow(row)
