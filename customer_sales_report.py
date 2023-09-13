#Write a python program that will read the sales.csv file 
# #and creates a new file with the customer ID and calculated total (as shown in salesreport.csv). 
# You can name your output file – salesreportFINAL.csv

import csv

sales = open('sales.csv','r')

csv_file = csv.reader(sales,delimiter=',')

outfile = open('salesreportFINAL.csv','w')

outfile.write('Customer ID,Total\n')            

next(csv_file)

customer_id = 250
total = 0

for row in csv_file:
    ID = str(customer_id)                                  
    subtotal = float(row[3])
    tax = float(row[4])                                

    line_total = subtotal + tax
    total += line_total                                             

    format_total = "{:.2f}".format(total)
    
    outfile.write(ID + ',' + format_total + '\n')

    customer_id += 1 

outfile.close()



