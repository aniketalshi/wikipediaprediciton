from random import random

new_file = open("final_outputs_1", "w")
new_file.write("user, solutions\n")

old_file = open("final_outputs.csv")

for line in old_file:
    attr = line.strip().split(',')
    if(attr[1] != 0 and random() >= .8):
        new_file.write(line)

old_file.close()
new_file.close()
    
    
