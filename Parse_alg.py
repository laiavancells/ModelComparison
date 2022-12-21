import pandas as pd
import os
from typing import List, Tuple
from urllib.parse import urlparse

# change for your path
file_path = r'/Users/laiavancells/Desktop/Tredmill study'

# file name from the folder
file_name = 'tred02.txt'

# Change this number to correspond with the subject 
# IMPORTANT TO CHANGE FOR EACH SUBJECT
ind_labels_keep = 2

# change the directory to the directory containing files
os.chdir(file_path)

# read in data from the file
with open(file_name, 'r') as f:
    data_raw = f.read()

MA_vals = [1, 1, 2, 4, 3, 3, 2, 2, 2, 3, 3, 3, 2, 4, 1]
mass_vals = [1, 63, 71, 116, 63.2, 89.1, 75.4, 68.8, 61.3, 73.6, 77, 70.7, 80.2, 152, 97.8]
MA_val = MA_vals[ind_labels_keep]
mass_val = mass_vals[ind_labels_keep]

# line from the parse data in excel corresponding to the subject
parse_vals = [30, 175, 176, 215, 219, 250, 251, 279, 280, 340, 344, 
              369, 380, 395, 397, 457, 461, 494, 497, 523, 528, 582, 585, 620, 621, 
              654, 655, 722, 727, 754, 757, 777, 786, 842, 845, 883, 885, 910, 914, 1098]

# copy from excel file
incline_vals = [0, 10, 10, 10, 0, 0, 0, 20, 20, 20, 5, 5, 5, 25, 25, 25, 15, 15, 15, 0]

parse_labels = ['Warmup', 'Slow', 'Medium', 'Fast', 'Slow', 'Medium', 'Fast', 'Slow', 'Medium', 'Fast', 'Slow', 'Medium', 'Fast', 'Slow', 
                'Medium', 'Fast', 'Slow', 'Medium', 'Fast', 'Cooldown']

inds_labels = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 2, 3, 4, 5],  # sub 1
    [1, 2, 3, 4, 5],  # sub 2
    [1, 2, 3, 4, 5],  # sub 3
    [1, 4, 3, 2, 5],  # sub 4
    [1, 4, 3, 2, 5],  # sub 5
    [1, 4, 3, 2, 5],  # sub 6
    [1, 2, 3, 4, 5],  # sub 7
    [1, 2, 3, 4, 5],  # sub 8
    [1, 2, 3, 4, 5],  # sub 9
    [1, 4, 3, 2, 5],  # sub 10
    [1, 4, 3, 2, 5],  # sub 11
    [1, 4, 3, 2, 5],  # sub 12
    [1, 2, 3, 4, 5],  # sub 13
    [1, 4, 3, 2, 5],  # sub 14
    [1, 2, 3, 4, 5]   # sub 15
]

incline_vals = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 10, 10, 10, 0, 0, 0, 20, 20, 20, 5, 5, 5, 25, 25, 25, 15, 15, 15, 0],
    [0, 10, 10, 10, 5, 5, 5, 15, 15, 15, 0, 0, 0, 20, 20, 20, 25, 25, 25, 0],
    [0, 5, 5, 5, 10, 10, 10, 20, 20, 20, 25, 25, 25, 15, 15, 15, 0, 0, 0, 0],
    [0, 15, 15, 15, 0, 0, 0, 5, 5, 5, 10, 10, 10, 25, 25, 25, 20, 20, 20, 0],
    [0, 10, 10, 10, 5, 5, 5, 15, 15, 15, 25, 25, 25, 20, 20, 20, 0, 0, 0, 0],
    [0, 0, 0, 0, 10, 10, 10, 20, 20, 20, 5, 5, 5, 15, 15, 15, 25, 25, 25, 0],
    [0, 0, 0, 0, 5, 5, 5, 15, 15, 15, 10, 10, 10, 25, 25, 25, 20, 20, 20, 0],
    [0, 10, 10, 10, 0, 0, 0, 15, 15, 15, 5, 5, 5, 25, 25, 25, 20, 20, 20, 0],
    [0, 25, 25, 25, 0, 0, 0, 20, 20, 20, 5, 5, 5, 15, 15, 15, 10, 10, 10, 0],
    [0, 20, 20, 20, 25, 25, 25, 15, 15, 15, 0, 0, 0, 5, 5, 5, 10, 10, 10, 0],
    [0, 5, 5, 5, 0, 0, 0, 20, 20, 20, 25, 25, 25, 10, 10, 10, 15, 15, 15, 0],
    [0, 0, 0, 0, 20, 20, 20, 10, 10, 10, 25, 25, 25, 15, 15, 15, 5, 5, 5, 0],
    [0, 0, 0, 0, 20, 20, 20, 10, 10, 10, 15, 15, 15, 25, 25, 25, 5, 5, 5, 0],
    [0, 25, 25, 25, 20, 20, 20, 10, 10, 10, 15, 15, 15, 0, 0, 0, 5, 5, 5, 0]
]

vels = [0.8, 0.8, 1.2, 1.6, 0.8, 1.2, 1.6, 0.8, 1.2, 1.6, 0.8, 1.2, 1.6, 0.8, 1.2, 1.6, 0.8, 1.2, 1.6, 0.8]

data_ind_temp = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 4, 3, 2, 5],
    [1, 4, 3, 2, 5],
    [1, 4, 3, 2, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 4, 3, 2, 5],
    [1, 4, 3, 2, 5],
    [1, 4, 3, 2, 5],
    [1, 2, 3, 4, 5],
    [1, 4, 3, 2, 5],
    [1, 2, 3, 4, 5]
]

data_ind_temp = inds_labels[ind_labels_keep + 2, :]

data_label_correct = ['Time', 'Heel', 'Midfoot', 'Forefoot', 'Total']
data_labels = [data_label_correct[i] for i in data_ind_temp]

for j, label in enumerate(data_labels):
    data_proc['raw'][label] = data_raw['data'][:, j]

moment, data_proc['raw']['T_F'], data_proc['raw']['T_F_norm'] = moment_loadsol(MA_val, [data_proc['raw']['Heel'], data_proc['raw']['Midfoot'], data_proc['raw']['Forefoot']], mass_val)


data_temp = data_proc['parsed_steps']
b = list(data_temp.keys())

P_vals_temp = parse_vals

for j in range(len(b)):  # exclude first 20 steps and last 20 steps (getting on and off the treadmill)
    data_temp_2 = data_temp[b[j]]

    for k in range(4, 38, 2):
        inds_pre = [P_vals_temp[k - 1], P_vals_temp[k]]
        inc_label = 'incline_' + str(incline_vals[ind_labels_keep][k // 2])
        if data_temp_2['time_point'] > inds_pre[0] and data_temp_2['time_point'] < inds_pre[1]:
            # temp_color = rand(1,3)
            data_proc['sorted_steps'][inc_label][parse_labels[k // 2]][b[j]] = data_temp_2
            speed_temp = parse_labels[k // 2]
            data_proc['sorted_steps'][inc_label][parse_labels[k // 2]][b[j]]['speed'] = vels[k // 2]
            data_proc['sorted_steps'][inc_label][parse_labels[k // 2]][b[j]]['incline'] = incline_vals[ind_labels_keep][k // 2]
            data_proc['sorted_steps'][inc_label][parse_labels[k // 2]][b[j]]['peak_AT_force_norm'] = max(data_temp_2['AT_Force_norm'])

import matplotlib.pyplot as plt

data_temp = data_proc['sorted_steps']

data_temp = {k: data_temp[k] for k in sorted(data_temp)}
b = list(data_temp.keys())
n = 1
fig, axs = plt.subplots(3, 6)
for j in range(len(b)):

    data_temp_2 = data_temp[b[j]]
    c = list(data_temp_2.keys())

    for k in range(len(c)):

        ax = axs[k // 6, k % 6]
        ax.hold(True)
        color_plot = np.random.rand(3, 1)
        data_temp_3 = data_temp_2[c[k]]
        n = n + 1
        d = list(data_temp_3.keys())
        for ii in range(len(d)):
            data_temp_4 = data_temp_3[d[ii]]
            ax.plot(data_temp_4['Time_norm'], data_temp_4['AT_Force_norm'], color=color_plot)
            ax.set_ylim([-.5, 8])
            ax.set_ylabel('Normalized AT Force')
            ax.set_title(f'{file_name} {data_temp_4["incline"]}% incline at {data_temp_4["speed"]} m/s') 
            