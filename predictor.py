trn_time, tst_time = 0, 0
users = []
user_edits, user_solus = {}, {}
user_frstedit, user_lastedit = {}, {}

from scipy.cluster import vq
from matplotlib import pyplot as plt
import cPickle as pickle
def load(dataset):
    global trn_time, tst_time
    global users
    global user_edits, user_solus
    global user_frstedit, user_lastedit, user_edit_freq
    pkl_file = open('data_%s.pkl' % dataset, 'rb')
    (trn_time, tst_time) = pickle.load(pkl_file)
    users = pickle.load(pkl_file)
    (user_edits, user_solus) = pickle.load(pkl_file)
    (user_frstedit, user_lastedit) = pickle.load(pkl_file)
    user_edit_freq = pickle.load(pkl_file)
    pkl_file.close()

def edits_num(u, t, p):
    if p < 1:
        return len(user_edits[u][(t,p)])
    else:
        return len(sum([user_edits[u][m] for m in range(t-p,t)], []))

def artis_num(u, t, p):
    if p < 1:
        return len(set(user_edits[u][(t,p)]))
    else:
        return len(set(sum([user_edits[u][m] for m in range(t-p,t)], [])))

import math
import numpy

periods = [2**j for j in range(-4,3)] + [12,36,106]
def features(u, t):
    vector = []
    vector += [float(edits_num(u, t, p)) for p in periods]
    vector += [numpy.reciprocal(numpy.mean(user_edit_freq[u]))]
    #vector += [float(artis_num(u, t, p)) for p in periods]
    #vector += [math.log1p(user_lastedit[(u,t)]-user_frstedit[(u,t)])]
    return vector

def my_features(u, t):
    vector = []
    #vector += [float(edits_num(u, t, p)) for p in periods]
    vector += [math.log1p(user_lastedit[(u,t)]-user_frstedit[(u,t)])]
    vector += [math.log1p(numpy.reciprocal(numpy.mean(user_edit_freq[u])))] 
    #vector += [float(artis_num(u, t, p)) for p in periods]
    return vector

def my_represent(us, t):
    return [my_features(u, t) for u in us]

def represent(us, t):
    return [features(u, t) for u in us]

def label(us, t):
    if t == trn_time:  # training
        return [math.log1p(edits_num(u, t+5, 5)) for u in us]
    elif t == tst_time:  # testing
        return [math.log1p(user_solus[u]) for u in us]
    return -1  # error

def tst_la():
    tst_users = [u for u in users if edits_num(u, tst_time, 12) > 0]
    return label(tst_users, tst_time)

import matplotlib.pyplot as plt
def plot_tst_la():
    editnum = []
    for u in users:
        editnum.append(math.log1p(user_lastedit[(u,trn_time)]-user_frstedit[(u,trn_time)]))
    #plt.plot(editnum)
    #plt.xlabel('users')
    #plt.ylabel('Difference between first and last edit')
    plt.scatter(users, editnum, plt.xlabel('users'),plt.ylabel('difference of last and first edit (log scale)'))
    
    plt.show()
    

import numpy as np
from sklearn import linear_model
#from scikits.learn import svm
#from sklearn import neighbors
from sklearn.neighbors import KNeighborsRegressor
import cv2
    

def learn():
    trn_users = [u for u in users if edits_num(u, trn_time, 12) > 0]
    data = np.array(represent(trn_users, trn_time), dtype=np.float32)
    targets = np.array(label(trn_users, trn_time), dtype=np.float32)
    # model = linear_model.LinearRegression()
    # model = linear_model.SGDRegressor()
    # model = svm.SVR(kernel='linear', C=1)
    # model = svm.SVR(kernel='rbf', C=1e3)
    model = KNeighborsRegressor(n_neighbors=120)
    model.fit(data, targets)
    #model = cv2.GBTrees()
    #model.train(data, cv2.CV_ROW_SAMPLE, targets, params={'weak_count':1000})  # 'subsample_portion':0.8, 'shrinkage':0.0
    return model



def get_features():
    trn_users = [u for u in users if edits_num(u, trn_time, 12) > 0]
    #data = np.array(represent(trn_users, trn_time), dtype=np.float32)
    data = np.vstack(my_represent(trn_users, trn_time))
    #for u in data[:,1]:
    #    print u
    plt.scatter(data[:,0],data[:,1]),plt.xlabel('difference of last and first edit'),plt.ylabel('edit frequency')
    plt.show()

    return
    

def drift():
    trn_avg_la = sum([math.log1p(edits_num(u, trn_time, 5)) for u in users])/len(users)
    tst_avg_la = sum([math.log1p(edits_num(u, tst_time, 5)) for u in users])/len(users)
    
    return tst_avg_la - trn_avg_la

def estimate(model=None):
    # all 0s benchmark
    # return [math.log1p(0) for u in us]
    # all 1s benchmark
    # return [math.log1p(1) for u in us]
    # optimized constant value benchmark
    # return [math.log1p(1.750998229) for u in us]
    # most recent 5 months benchmark
    # return [math.log1p(edits_num(u, tst_time, 5)) for u in us]
    # supervised learning
    tst_users = [u for u in users if edits_num(u, tst_time, 12) > 0]
    data = np.array(represent(tst_users, tst_time), dtype=np.float32)
    forecasts = model.predict(data)  # for scikits.learn models
    #forecasts = [model.predict(sample) for sample in data]
    d = drift()
    return [max(y+d, 0) for y in forecasts]

def printsolus():
    outfile = open("user_solutions.csv", 'w')
    
    for u in users:
        outfile.write(str(u)+','+str(user_solus[u])+'\n')

    outfile.close()
