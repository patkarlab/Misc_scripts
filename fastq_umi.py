#!/usr/bin/env python
import gzip

R1_file = "/home/pipelines/Consensus_pipeline_with_espresso/sequences/24MPR26-NV2-AMLMRD_S10_R1_001.fastq.gz"
R2_file = "/home/pipelines/Consensus_pipeline_with_espresso/sequences/24MPR26-NV2-AMLMRD_S10_R2_001.fastq.gz"
output = "R1.fastq"
outfile = open (output,'w')
with gzip.open( R1_file , "rt") as r1_fastq:
	for lines_r1 in r1_fastq:
		print (lines_r1.strip(), file=outfile)

outfile.close()		
