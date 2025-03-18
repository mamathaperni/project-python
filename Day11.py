#File Handling
# file must be .txt file
# Method 1: Using write mode 'w'
with open('myfile.txt', 'w') as file:
    file.write("Hello World!\n")
    file.write("This is a new text file.")
# the file is created using AI we can see in the files section 
 # syntax:
# open("myfilename",mode)
# filename-myfile.txt,myfile.json,...
# mode-read(r),write(w),append(a)....


#to write or to open the file it starts with "with"
with open("myfile.txt",'r')as f:
    print(f.read())

with open("myfile.txt",'a')as f:
    f.write("\nthis is the my first file ")

with open("myfile.txt",'r')as f:
    print(f.read())

# Method 1: Using csv module (recommended)
import csv

# Create and write to CSV file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Name', 'Age'])
    
    # Write data rows
    writer.writerow(['John', 25])
    writer.writerow(['Alice', 30])

# # Read and display the CSV file
# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


 #   To handle CSV FILES WE CAN USE PANDAS
import pandas as pd
#to acess files

pd.read_csv("data.csv.csv")