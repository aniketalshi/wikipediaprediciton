from random import random

#lines = [line for line in open("moredata.tsv") if random() >= .5]

out_file = open('training_new.tsv', 'w')
out_file.write('user_id\tarticle_id\trevision_id\tnamespace\ttimestamp\tmd5\treverted\treverted_user_id\treverted_revision_id\tdelta\tcur_size\n')

oldfile = open('training_new111.tsv')
for line in oldfile:
    if (random() >= .7):
        out_file.write(line)

out_file.close()
oldfile.close()
