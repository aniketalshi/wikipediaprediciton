import sys
dataset = "moredata"
if dataset == 'training_new':
    tst_time = 116
elif dataset == 'moredata':
    tst_time = 116-5
elif dataset == 'validation':
    tst_time = 84
else:
    sys.exit("ERROR: The dataset is invalid.")
trn_time = tst_time-5

from editlog import parse_timestamp
active_editors = set()
data_file = open('data/%s.tsv' % dataset)
data_file.readline()  # header
for line in data_file:
    attr = line.strip().split('\t')
    user = int(attr[0])
    if user in active_editors:
        continue
    timestamp = parse_timestamp(attr[4])
    if (timestamp >= tst_time-12) and (timestamp < tst_time):  # last1y
        active_editors.add(user)
data_file.close()
users = sorted(active_editors)

from collections import defaultdict
user_edits = {}
user_solus = {}
user_frstedit = {}
user_lastedit = {}
for user in users:
    user_edits[user] = defaultdict(list)
    user_solus[user] = 0
    for deadline in [trn_time, tst_time]:
        user_frstedit[(user,deadline)] = deadline
        user_lastedit[(user,deadline)] = 0
        
user_edit_freq = {}
user_last_edit = {}
for user in users:
    user_edit_freq[user] = []
    user_last_edit[user] = 0.0

data_file = open('data/%s.tsv' % dataset)
data_file.readline()  # header
for line in data_file:
    #print line
    attr = line.strip().split('\t')
    user = int(attr[0])
    if user not in users:
        continue
    article = int(attr[1])
    # revision = int(attr[2])
    # namespace = int(attr[3])
    timestamp = parse_timestamp(attr[4])
    if (timestamp >= tst_time) and (timestamp < tst_time+5):  # next5m
        user_solus[user] += 1
        continue
    m = int(timestamp)
    user_edits[user][m].append(article)
    # print user_edits[user][m]
    
    for deadline in [trn_time, tst_time]:
        for fraction in [2**j for j in range(-4,0)]:
            if (timestamp >= deadline-fraction) and (timestamp < deadline):
                user_edits[user][(deadline,fraction)].append(article)

    
                
    for deadline in [trn_time, tst_time]:
        if timestamp < deadline and timestamp < user_frstedit[(user,deadline)]:
            user_frstedit[(user,deadline)] = timestamp
        if timestamp < deadline and timestamp > user_lastedit[(user,deadline)]:
            user_lastedit[(user,deadline)] = timestamp


    user_edit_freq[user].append(timestamp - user_last_edit[user])
    user_last_edit[user] = timestamp
            
data_file.close()

import math
import numpy
out_file = open('akshay.csv', 'w')
out_file.write('user,edit frequency\n')  # header
for user in users:
    #print user, numpy.mean(user_edit_freq[user])    
    out_file.write(str(user)+','+ str(numpy.reciprocal(numpy.mean(user_edit_freq[user])))+'\n')
out_file.close()



if dataset == 'validation':
    solu_file = open('data/validation_solutions.csv')
    solu_file.readline()  # header
    for line in solu_file:
        (user_str, solu_str) = line.strip().split(',')
        user = int(user_str)
        solu = int(solu_str)
        if user not in users:
            continue
        user_solus[user] = solu
    solu_file.close()

import cPickle as pickle
pkl_file = open('data_%s.pkl' % dataset, 'wb')
pickle.dump((trn_time, tst_time), pkl_file, -1)
pickle.dump(users, pkl_file, -1)
pickle.dump((user_edits, user_solus), pkl_file, -1)
pickle.dump((user_frstedit, user_lastedit), pkl_file, -1)
pickle.dump(user_edit_freq, pkl_file, -1)
pkl_file.close()
