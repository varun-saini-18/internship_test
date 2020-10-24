# Importing all important Python Modules
import csv
import re

# Initialising two empty lists
thislist = []
another_list = []

# To read the given input file and separate out the rows containing
# USA as the country.
with open('C:\\Python Course\\input\\main.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            x = re.search("^USA", row[8])
            if x:
                thislist.append(row)

# To Create a new file in Output folder containing USA as the country
with open('C:\\Python Course\\output\\filteredCountry.csv', mode='w') as filtered_file:
    file_writer = csv.writer(filtered_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['SKU','DESCRIPTION','YEAR','CAPACITY','URL','PRICE','SELLER INFORMATION','OFFER DESCRIPTION','COUNTRY'])
    for x in thislist:
        file_writer.writerow(x)
        another_list.append(x)

# Initialising various empty dictionaries for mapping of values
# We have two variables for every value of SKU ie. value1[SKU] and value2[SKU]
# value1 will contain the minimum value of price and value2 will contain second minimum
# vale of SKU.
value1 = {}
value2 = {}
count = {}
check = {}

# Initialising the count of every unique element present in SKU with 0
for x in another_list:
    count[x[0]]=0
    check[x[0]]=0

for x in another_list:
    y = x[0]

    # Converting the string value of price to float
    z=''
    for l in x[5]:
        if l=='$' or l==',' or l=='?':
            continue
        else:
            z = z+l
    z=float(z)
    
    if count[y]==0:
        value1[y]=z
    elif count[y]==1:
        if value1[y]>z:
            value2[y]=value1[y]
            value1[y]=z
        else:
            value2[y]=z
    else:
        if value2[y]<z:
            continue
        elif value1[y]<z:
            value2[y]=z
        else:
            value2[y]=value1[y]
            value1[y]=z
    count[y]+=1

# To create a new file in output folder having th minimum and second minimum value of price
with open('C:\\Python Course\\output\\lowestPrice.csv', mode='w') as filtered_file:
    file_writer = csv.writer(filtered_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['SKU','FIRST_MINIMUM_PRICE','SECOND_MINIMUM_PRICE'])
    for x in another_list:
        if check[x[0]]==0:
            check[x[0]]+=1
            if count[x[0]]==1:
                file_writer.writerow([x[0],value1[x[0]],'-'])
            elif count[x[0]]>=2:
                file_writer.writerow([x[0],value1[x[0]],value2[x[0]]])
