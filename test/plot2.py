
infile1 = open('final_outputs_1.csv')
infile2 = open('user_solutions.csv')
outfile = open('new_solutions.csv','w')

for line in infile1:
    attr = line.strip().split(',')
    userid = int(attr[0])
    
    for line1 in infile2:
        attr1 = line1.strip().split(',')
        if(int(userid) == int(attr1[0])):
            print userid
            outfile.write(str(userid)+','+str(attr1[1])+'\n')


outfile.close()
infile2.close()            
infile1.close()
