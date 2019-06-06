import csv

# with open('csvs/ripper.csv', 'r') as csvfile:
#     our_reader = csv.reader(csvfile)
#     names = [row for row in our_reader]
#     #print(names)


#so basically, we want to open our csv file and set it as an object or variable (i.e. with open csv... as "fin"), then we want to set the action of reading "fin" as a varialbel, so "reader", then we want to point this process to what we want it to read, so "results = ...", and set it as a variable ("results"). Then we want to print only one slice of "results", in this case the first column in row 4, so we ask to print results[0] (because we're already only looking at row 4).


# first line calls the csv we want, opens it as 'fin', and sets it to be read as our input
# with open('csvs/ripper.csv', 'r') as fin:
#
# # #this sets a variable that is the reader reading the csv file we have now called 'fin'
#     reader = csv.reader(fin)
#
# # #setting a variale called 'results' that points to row 4 in the csv being read by the variable/action 'reader'
#
#     results = [row[4] for row in reader]
#
# #saves only the text content from row 4 (which actually means column) in one variable "all_texts"
# all_texts = results


#What is the earliest date an article was published? So the first step for all of these has been opening the csv as an object/variable and then setting up a variable that reads the object we've just designated via the reader method, then setting a results variable so we can define the results we're looking at
# with open('csvs/ripper.csv', 'r') as fin:
#     reader = csv.reader(fin)
#     results = [row for row in reader]

# #this points the function above to column 3 in the csv, which contains the date content
# dates = [row[3] for row in results]

# #now we want to use a method to (min)print the earliest date
# print(min(dates))


#Now we want to create a new csv file that has all the same content but with lower case letters for all the text content in column 4. First we have to open it to be read as an object like before.
# with open('csvs/ripper.csv', 'r') as fin:
#     reader = csv.reader(fin)
#     results = [row for row in reader]
#
# #now we want to change all the upper case letters in row 4 to lowercase. This points to the rows in the results version of the csv we've opened using reader. Then it looks at row[4] and performs the method 'lower' on all of row 4 to make everything lowercase.
# for row in results:
#     row[4] = row[4].lower()
#
# #Now that things are changed we have to re-write to a new file, which we're calling ripper_texts.csv and which will be created in this process. Now we're treating the csv as the object we're writing out to instead of reading from. The writer is defines as the write action applied to the csv and operating on the fout object.
# with open('csvs/ripper_texts.csv', 'w') as fout:
#     writer = csv.writer(fout)
# #now, for each row in row we're writing to the csv, except because of the above action row 4 will be all lowercase.
#     for row in results:
#         writer.writerow(row)
