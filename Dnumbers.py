# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:10:56 2023

@author: noraj
"""

import openpyxl
import os
import random

### Renaming number array

#get list of ordered numbers
numbers_ordered = list(range(1, 176))
#turn n umbers into strings
numbers_str = [str(num) for num in numbers_ordered]
#add 0 before single digits
for i in range(9):
    numbers_str[i] = "00" + numbers_str[i]
for i in range(9,99):
    numbers_str[i] = "0" + numbers_str[i]
#Shuffle numbers
random.shuffle(numbers_str)
print(numbers_str)
number_counter = 0

### Policy number variable that will be added to the html file
policynum = "var policynumber = 'test';"


### Excel file that contains the d values
excel = "Dnumbers.xlsx"
wb_obj = openpyxl.load_workbook(excel)
#Sheet 
sheetDnumbers = wb_obj["Dnumbers"]
row_Dnumber = 1

### Excel file for final lists
excel2 = "List.xlsx"
wb_obj2 = openpyxl.load_workbook(excel2)
#Sheet 
sheet_v1 = wb_obj2["v1"]
sheet_v2 = wb_obj2["v2"]
sheet_v3 = wb_obj2["v3"]
sheet_v4 = wb_obj2["v4"]
sheet_v5 = wb_obj2["v5"]
sheet_all = wb_obj2["all"]

row_List = 2




###### v1 ######

#2d

#find files in folder
folder_path = "v1/2d/"
dirs = os.listdir(folder_path)

#Create new folder
newpath = "v1/2d/new" 
if not os.path.exists(newpath):
    os.makedirs(newpath)
    
#List excel iterators to save d values
col_count = 2
row_count = 2

#Access files one by one
for file in dirs:
    if file.endswith(".html"):
        file_name = file
        #Open file for reading
        template2d = open(folder_path + file, "r")
        content = template2d.read()
        
        #Filename
        f_name = file_name[:-5]
        print(f_name)
        
        #Name the new file
        htmlName = numbers_str[number_counter] + "_v1_2d_4Fre5hBTC.html"
        
        #Add policy number to html
        content_split = content.split("</script>")
        content = content_split[0] + "\n" + policynum + "\n" + "</script>" + content_split[1]
        
        #Count instances of d values
        instance_count = content.count("getRandomIntDec(300, 500)")
        #Loop through instances
        for inst in range(instance_count):
            d_temp = sheetDnumbers['A' + str(row_Dnumber)].value
            row_Dnumber += 1
            content_temp = content.replace("getRandomIntDec(300, 500)", d_temp, 1)
            content = content_temp
            #Add d values to excel
            sheet_v1.cell(row=row_count, column=col_count).value = d_temp
            col_count += 1
            #wb_obj2.save("List.xlsx")
        
        #Save name in excel
        sheet_v1['A' + str(row_count)] = htmlName
        wb_obj2.save("List.xlsx")
        col_count = 2
        row_count += 1
            
        #Create new html file and place it in the new folder 
        number_counter += 1
        path = "v1\\2d\\new\\" + htmlName
        newHtml = open(path, "w")
        newHtml.write(content)
        newHtml.close()
        
        

       
            
            
        
        
        
        
        
        
        
        







#3d
#5d





###### v2 ######

#2d
#3d
#5d

###### v3 ######

#2d
#3d
#5d

###### v4 ######
#2d
#3d
#5d

###### v5 ######
#2d
#3d
#5d

