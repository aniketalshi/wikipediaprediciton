import numpy as np
import matplotlib.pyplot as plt

dataset = 'training_new'
import sys
if len(sys.argv) > 1:
    dataset = sys.argv[1]

import predictor
predictor.load(dataset)
model = predictor.learn()
tst_lp = predictor.estimate(model)



import math

out_file = open('my_outputs.csv', 'w')
out_file.write('user,solution\n')  # header
for i in range(len(predictor.users)):
    u = predictor.users[i]
    p = math.expm1(tst_lp[i])
    out_file.write('%d,%f\n' % (u, p))
out_file.close()
