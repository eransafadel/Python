# OS2 Python Programming 2019b
#
# File:ex1.py
# ==============================================================================
# Writen by: Eran Safadel, Batya Pollack
#
# Run: ex1.py using Python interpreter
#%%--------------------------------------------------------------------------%%#



# ----------------import-------------------------
import os
import re

# ---------------get_table_name--------------------------

"""function that get cuurent line and return the manipulatin line"""
def get_values(current_line):
    my_line = current_line.partition(' VALUES ')[2]
    my_line = my_line.replace('),', '\n')
    my_line = my_line.replace(');', ' ')
    my_line = my_line.replace(')', ' ')
    my_line = my_line.replace('(', ' ')
    return my_line



# ----------------instert_in_curr_line------------------------
"""check if "INSERT INTO" containes in line"""
def instert_in_curr_line(current_line):
    return 'INSERT INTO' in current_line or False



# ---------------get_values----------------------------------------------------
""" function that get line and search if is a table name """
def get_table_name(line):
    match = re.search('`([0-9_a-zA-Z]+)`', line)
    if match:
        return match.group(1)
    else:
        print(line)
# --------------get_columns----------------------------------------------------
""" function that get line and return the column in line """
def get_columns(line):
    line1 = line.partition(' VALUES ')[2]
    match = re.search('INSERT INTO `.*` VALUES ()', line)
    if match:
        return list(map(lambda x: x.replace('`', '').strip(),
                        line1.group(1).split(',')))
# ----------------remove_csv-------------------------------------------------
""" function that remove the empty tables """
def remove_csv():
        for t in table_list:
            if table_list[t] == 0:
                os.remove(t + ".csv")
# ---------------read_next_column--------------------------------------------
"""function that get line and read te next column"""
def read_next_column(current_line):
    is_in = re.search('\s\s`([0-9_a-zA-Z]+)`', current_line)
    if is_in:
        return is_in.group(1)
    return " "
# ----------------main-----------------------------
""" the main function """
def main():
    with open("demo.sql", 'rb') as func:
        found = False
        for my_line in func.readlines():#read the lines from file
            my_line = my_line.decode("utf-8")
            if 'CREATE TABLE' in my_line:
                found = True#the table is true

                table = get_table_name(my_line)#get table name
                table_list[table] = 0
                open(table + '.csv', 'w')
            else:
                if found:  # insert into table if exist
                    with open(table + '.csv', 'a') as csvfiles:

                        if not instert_in_curr_line(my_line):#if we in CREATE TABLE and not in insert into
                            res_of_line = read_next_column(my_line)
                            if res_of_line != ' ':
                                csvfiles.write(res_of_line + ",")

                        else:#if we found insert into
                            csvfiles.write("\n")
                            val = get_values(my_line)
                            csvfiles.write(val)
                            table_list[table] += 1

table_list = {}
if __name__ == '__main__':
    main()
    remove_csv()
