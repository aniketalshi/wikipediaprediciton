dataset = 'moredata'
import sys
if len(sys.argv) > 1:
    dataset = sys.argv[1]

import predictor
predictor.load(dataset)
model = predictor.learn()
tst_lp = predictor.estimate(model)
tst_la = predictor.tst_la()
#predictor.plot_tst_la()
predictor.get_features()
#predictor.printsolus()

import math
def rmsle(lp, la):
    n = len(lp)
    sle = sum([math.pow(lp[i]-la[i], 2) for i in range(n)])
    return math.sqrt(sle/n)

print 'RMSLE =', rmsle(tst_lp, tst_la)
