import numpy as np
import matplotlib.pyplot as plt

first_file = open("final_outputs_1.csv")
second_file = open("final_outputs_3.csv")

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
plt.plot(userid1, edits1, c='b', label='prediction', linewidth=2.0)
plt.plot(userid2, edits2, c='g', label='data', linewidth=2.0)
plt.ylabel("user edits in next 5 months log scale")
plt.xlabel("users")
plt.axis('tight')
plt.legend()
plt.yscale('log')
plt.show()

