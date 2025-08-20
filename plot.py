#!/usr/bin/env python

import sys
import csv
import matplotlib.pyplot as plt

tsv_file = sys.argv[1]		# tsv file with x, y values
figure_out = sys.argv[2]	# Output figure

x_values = list()
y_values = list()

with open (tsv_file, 'r') as infile:
	tsv_handle = csv.reader(infile, delimiter = ' ')
	for values in tsv_handle:
		x = values[0]
		y = float(values[1])
		x_values.append(x)
		y_values.append(y)

#print (x_values, y_values)
# x_tick_list = x_values[::3]
plt.figure(figsize=(5, 5))
# plt.plot(x_values, y_values, "-b", label="Illumina universal adapter")
plt.hist(y_values, bins=10)
# plt.legend(loc="upper left")
# plt.xlabel('positions (bp)', fontsize=15)
# plt.ylabel('adapter %', fontsize=15)
# plt.xticks(x_tick_list, fontsize=10, rotation = 25)
# plt.yticks(fontsize=10)
# plt.tight_layout()
# plt.margins(0.01)
plt.show()
# plt.savefig(figure_out, format = 'png', dpi = 1000, transparent=True, bbox_inches='tight',pad_inches = 0)
# print ("checking the python script")
