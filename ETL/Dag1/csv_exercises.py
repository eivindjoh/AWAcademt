# CSV Exercises
# 1. Write a function read_csv that accepts filename as a parameter and prints each line
# in the file given by filename. Try to use both csv.reader() and csv.DictReader
# Create your own CSV files to test, both with and without a header!

import csv
import os

# def read_csv(file):
#     with open(file, 'r', encoding='utf-8') as csv_file:
#         myfile = csv.reader(csv_file, delimiter=' ')
#         for line in myfile:
#             print(line)

# read_csv('test.txt')


# 2. Add a parameter n_lines to the function that only prints the n_lines first rows of the
# file. If n_lines is None it should print all lines in the file

# def read_csv(file, n_lines=None):
#     with open(file, 'r', encoding='utf-8') as csv_file:
#         myfile = csv.reader(csv_file, delimiter=' ')
#         for count, line in enumerate(myfile):
#             if n_lines==None:
#                     print(line)           
#             elif n_lines>=count+1:
#                     print(line)  
#             else:
#                 pass


# read_csv('test.txt', 2)


# 3. Add a new parameter to the function read_csv named filename_out. If filename_out
# is not None, the function should write each line to the file specified by filename_out
# instead of printing it.
# Example: read_csv(filename=“test.csv”, n_lines=10, filename_out=“out.csv”) should
# write the 10 first lines of test.csv to the file out.csv
# read_csv(filename=“test.csv”, n_lines=10, filename_out=None) should print the first
# 10 lines.

# def read_csv(file, n_lines=None, filename_out=None):
#     lines = []
#     with open(file, 'r', encoding='utf-8') as csv_file:
#         myfile = csv.reader(csv_file, delimiter=' ')
#         for count, line in enumerate(myfile):
#             if n_lines==None:
#                  pass        
#             elif n_lines>=count+1:
#                  lines.append(line) 
#             else:
#                 pass
#         if filename_out:
#             with open(filename_out, 'w', encoding='utf-8') as new_file:
#                     new_file = csv.writer(new_file, delimiter=',')
#                     new_file.writerows(lines)
#         else:
#             pass

# read_csv('test.txt', 4, filename_out='csv_exercises3.csv')

# 4. Expand the function to check if the filename_out already exists. If it does, it should
# append the rows (without the header) to the file instead of overwriting it.

# def read_csv(file, n_lines=None, filename_out=None):
#     lines = []
#     with open(file, 'r', encoding='utf-8') as csv_file:
#         myfile = csv.reader(csv_file, delimiter=' ')
#         for count, line in enumerate(myfile):
#             if n_lines==None:
#                  pass        
#             elif n_lines>=count+1:
#                  lines.append(line) 
#             else:
#                 pass
#         if filename_out != None:
#             if os.path.isfile(filename_out):
#                 with open(filename_out, 'a', encoding='utf-8') as appending:
#                     new_file = csv.writer(appending, delimiter=',')
#                     new_file.writerow(lines)
#             else:       
#                 with open(filename_out, 'w', encoding='utf-8') as new_file:
#                     new_file = csv.writer(new_file, delimiter=',')
#                     new_file.writerows(lines)
#         else:
#             pass

# read_csv('test.txt', 4, filename_out='csv_exercises3.csv')




# 5. Add a parameter cols to the function read_csv. cols should be a list of ints that
# specify the index of the columns that should be included.
# For instance, : read_csv(filename=“test.csv”, n_lines=10, filename_out=“out.csv”,
# cols=[0, 2,3]) should only write the first, third and fourth column (remember that we
# use zero-index in Python!)

def read_csv(file, cols, n_lines=None, filename_out=None):
    lines = []
    col_lines = []


    with open(file, 'r', encoding='utf-8') as csv_file:
        myfile = csv.reader(csv_file, delimiter=' ')
        for count, line in enumerate(myfile):
            if n_lines==None:
                 pass        
            elif n_lines>=count+1:
                 lines.append(line) 
            else:
                pass
        
        for col in cols:
            col_lines.append(lines[col])

        if filename_out != None:
            if os.path.isfile(filename_out):
                with open(filename_out, 'a', encoding='utf-8') as appending:
                    new_file = csv.writer(appending, delimiter=',')
                    new_file.writerow(col_lines)
            else:       
                with open(filename_out, 'w', encoding='utf-8') as new_file:
                    new_file = csv.writer(new_file, delimiter=',')
                    new_file.writerows(col_lines)
        else:
            pass

print(read_csv('test.txt', [1, 3, 5], 8, filename_out='csv_exercises3.csv'))


# 6. Experiment with transforming the values of each row. For instance, try adding a
# column with integers in your CSV and write each integer squared (i.e i*i) to the out
# CSV. Also try printing the total sum of that integer row.



# 7. Add a column “Date” to your CSV and fill it with values.
# Try writing that date as three separate columns “Year”, “Month” and “Day” in the out
# csv