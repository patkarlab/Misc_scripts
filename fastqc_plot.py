#!/usr/bin/env python

import os
import math
import pylab as plt
import numpy as np
import pandas as pd
import matplotlib.patches as patches
import sys
from Bio import SeqIO
import gzip

testfile = sys.argv[1]		# Input is file in fastq.gz format
outfile = sys.argv[2]		# 

def plot_fastq_qualities(filename, ax=None, limit=10000):

	fastq_parser = SeqIO.parse(gzip.open(filename, "rt"), "fastq")
	res=[]
	c=0
	for record in fastq_parser:
		score=record.letter_annotations["phred_quality"]
		res.append(score)
		c+=1
		if c>limit:
			break
	df = pd.DataFrame(res)
	l = len(df.T)+1

	if ax==None:
		f,ax=plt.subplots(figsize=(10,10))
	rect = patches.Rectangle((0,0),l,20,linewidth=0,facecolor='r',alpha=.4)
	ax.add_patch(rect)
	rect = patches.Rectangle((0,20),l,8,linewidth=0,facecolor='yellow',alpha=.4)
	ax.add_patch(rect)
	rect = patches.Rectangle((0,28),l,12,linewidth=0,facecolor='g',alpha=.4)
	ax.add_patch(rect)
	df.mean().plot(ax=ax,c='black')
	boxprops = dict(linestyle='-', linewidth=1, color='black')
	df.plot(kind='box', ax=ax, grid=False, showfliers=False,
			color=dict(boxes='black',whiskers='black')  )
	ax.set_xticks(np.arange(0, l, 10))
	ax.set_xticklabels(np.arange(0, l, 10), fontsize = 20)

	#ax.set_yticks((0, 35))
	#ax.set_yticklabels((0, 35, 10), fontsize = 20)

	ax.set_xlabel('position(bp)', fontsize = 20)
	ax.set_ylabel('base quality dist.', fontsize = 20)

	ax.set_xlim((0,l))
	ax.set_ylim((15,50))
	#ax.set_title('per base sequence quality')	
	#plt.show()

	plt.xticks(fontsize=20, rotation = 15)
	plt.yticks(fontsize=20)
	plt.tight_layout()
	plt.savefig(outfile, format = 'png', dpi = 1000, transparent=True, bbox_inches='tight',pad_inches = 0)
	return

plot_fastq_qualities(testfile, limit=100000) # yields this plot:
