import os
import numpy as np
import pickle as pk

file = open('I:/babijon.txt', 'r')
matrix = np.arange(600*600)
matrix = matrix.reshape(600,600)
for i in range(600):
    temp = file.readline()
    temp = temp.split(' ')
    print(temp)
    for j in range(600):
       matrix[i,j] = int(temp[j])
        
        

print(matrix)
pk.dump(matrix, open('qubos1.pickle', 'wb'))