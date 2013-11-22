from random import random

new_file = open("final_outputs_3.csv", "w")
#new_file.write("user, solutions\n")

old_file = open("final_outputs_2.csv")

for line in old_file:
    if random() > .5:
        new_file.write(line)
    else:
        attr = line.strip().split(',')
        user = float(attr[0])
        num = float(attr[1])
        if random() > .5:
            num += num*random()
        else:
            num -= num*random()
        print num
        new_file.write('%d,%f\n' % (user, num))

old_file.close()
new_file.close()
    
    
