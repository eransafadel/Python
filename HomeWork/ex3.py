
#ex5
#submit: Batya pollack & Eran safadel
#In this program we will print the focus of 30 cities in the US cities
#-------------------import-------------------------------------------
import re
#--------------------------------------------------------------------
Names_of_cities = []
file1 = open("largest_cities.txt", "r")
next(file1)
#----------------loop on file 1------------------------------------
for line in file1:
    temp_Names_of_cities = re.search(r"[A-Z][a-z]+([\s][A-Z][a-z]+){0,2}", line)
    city = temp_Names_of_cities.group(0)
    Names_of_cities.append(city)

file2 = open("us_postal_codes.csv", "r")
next(file2)
result_dict = {i: -1 for i in Names_of_cities}
#-----------loop on file 2-----------------------------------------
for line in file2:
    city = line.split(',')[1]
    if city in result_dict and result_dict[city] is -1:
        result = re.search(r"[0-9]+", line)
        result_dict[city] = result.group()
#----------print--------------------------------------------------
for (key, val) in result_dict.items():
    print(key, val)

#-------close files-------------------------------------------------
file1.close()
file2.close()
