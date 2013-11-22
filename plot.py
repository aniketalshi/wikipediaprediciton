import numpy as np
import matplotlib.pyplot as plt

first_file = open("final_outputs.csv")
second_file = open("final.csv")

userid1 = []
edits1 = []
userid2 = []
edits2 = []

for line in first_file:
    attr = line.strip().split(',')
    userid1.append(attr[0])
    edits1.append(attr[1])

for line in second_file:
    attr = line.strip().split(',')
    userid2.append(attr[0])
    edits2.append(attr[1])

#plt.plot(userid, edits, c='g')
#plt.subplot(1, 1, )
#plt.plot(userid, edits, color='purple', lw=2, marker='s')
plt.plot(userid1, edits1, c='k', label='prediction')
plt.plot(userid1, edits1, c='g', label='data')

plt.axis('tight')
plt.legend()
#plt.xscale('log')
plt.show()

